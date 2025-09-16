import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
PG_CONN = os.getenv("PG_CONN", "")

# 전역 객체는 바로 만들지 말고, 필요할 때 1회만 생성
_llm = None
_embed = None
_retriever = None

def _init_llm():
    """OpenAI Chat 모델 지연 초기화"""
    global _llm
    if _llm is None:
        from langchain_openai import ChatOpenAI
        _llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)
    return _llm

def _init_embed():
    """임베딩 지연 초기화"""
    global _embed
    if _embed is None:
        from langchain_openai import OpenAIEmbeddings
        _embed = OpenAIEmbeddings(api_key=OPENAI_API_KEY)
    return _embed

def _init_retriever():
    """PGVector retriever 지연 초기화(모듈 로딩 시 DB 접속 금지)"""
    global _retriever
    if _retriever is None:
        from langchain_postgres import PGVector

        # DB 타임아웃이 없으면 붙여서 워커가 길게 매달리지 않게 함
        conn = PG_CONN or ""
        if conn and "connect_timeout" not in conn:
            sep = "&" if "?" in conn else "?"
            conn = f"{conn}{sep}connect_timeout=3"

        vs = PGVector(
            embeddings=_init_embed(),
            collection_name="insurance_all",
            connection=conn,
            use_jsonb=True,
        )
        _retriever = vs.as_retriever(
            search_type="mmr",
            search_kwargs={"k": 4, "fetch_k": 20, "lambda_mult": 0.8},
        )
    return _retriever

prompt = ChatPromptTemplate.from_template(
    """
    당신은 운전자 보험을 전문적으로 설명해주는 챗봇입니다.

    [질문]: {question}
    [컨텍스트]: {context}
    [첨부 파일 내용]: {file_content}

    지시사항:
    - 한국어로 이해하기 쉽게 설명합니다.
    - 불필요한 인사말은 줄이고, 핵심 위주로 정리합니다.
    - **주요 보장 항목과 차이점**을 명확히 설명합니다.
    - 회사명을 말해야할때는 보험사명을 정확히 말해줍니다.
    - 보험상품을 말해야할때는 상품명을 정확히 말해줍니다.
    - 여러 회사를 비교할 땐 마크다운 표를 사용합니다.
    - 표에는 '추천도' 열(◯ / △ / ✕ / —)을 추가합니다.
    - 범례: ◯ 추천 / △ 보통 / ✕ 없음 / — 미확인
    - 답변 끝에 추가 질문을 유도합니다.
    - 파일이 첨부되면 그 내용을 참고합니다.
    """
)

def _format_docs(docs):
    lines = []
    for d in docs or []:
        src = d.metadata.get("source", "")
        page = d.metadata.get("page", "?")
        lines.append(f"{d.page_content}\n(출처: {os.path.basename(src)}, p.{page})")
    return "---".join(lines)

def _read_text_file_if_exists(file_path: str) -> str:
    if not file_path:
        return ""
    if not os.path.exists(file_path):
        return ""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return ""

def rag_answer(question: str, file_path: str | None = None) -> str:
    """
    파일 내용(+벡터 검색 컨텍스트)을 이용해 질문에 답하는 RAG 함수.
    - 무거운 초기화는 여기서 최초 1회만 수행됨.
    """
    file_content = _read_text_file_if_exists(file_path)

    context = ""
    try:
        retriever = _init_retriever()
        # langchain retriever는 get_relevant_documents가 표준
        docs = retriever.get_relevant_documents(question)
        context = _format_docs(docs)
    except Exception as e:
        # 검색 실패해도 LLM만으로 답변하도록 계속 진행
        context = f"(주의: 검색 실패로 문서 컨텍스트를 불러오지 못했습니다: {e})"

    # ChatPromptTemplate은 messages로 포맷하는 게 안전
    messages = prompt.format_messages(
        question=question, context=context, file_content=file_content
    )

    llm = _init_llm()
    resp = llm.invoke(messages)
    return resp.content.strip()
