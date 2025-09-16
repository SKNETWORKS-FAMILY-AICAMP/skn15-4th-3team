# chat/rag.py
import os
from operator import itemgetter
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_postgres import PGVector

from dotenv import load_dotenv

load_dotenv()

# --- 환경 변수 불러오기 ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PG_CONN = os.getenv("PG_CONN")

# --- LLM & Embeddings ---
llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)
embed = OpenAIEmbeddings(api_key=OPENAI_API_KEY)

# --- Retriever 세팅 ---
def get_retriever():
    vs = PGVector(
        embeddings=embed,
        collection_name="insurance_all",  # 실제 collection 이름으로 교체
        connection=PG_CONN,
        use_jsonb=True,
    )
    return vs.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 4, "fetch_k": 20, "lambda_mult": 0.8},
    )

retriever = get_retriever()  # 모듈 로딩 시 한 번만

# --- Prompt ---
prompt = ChatPromptTemplate.from_template(
    """
    당신은 운전자 보험을 전문적으로 설명해주는 챗봇입니다.  
    사용자의 질문에 대해 아래 지침을 꼭 지켜 답변하세요.

    [질문]: {question}
    [컨텍스트]: {context}
    [첨부 파일 내용]: {file_content}

    지시사항:
    - 한국어로 이해하기 쉽게 설명합니다.  
    - 불필요한 인사말은 줄이고, 핵심 정보 위주로 정리합니다.  
    - **주요 보장 항목과 차이점**을 명확하게 설명합니다.  
    - 여러 회사를 비교할 때는 마크다운 표를 사용합니다.  
    - 표에는 '추천도' 열을 추가하고, ◯ / △ / ✕ / — 기호만 사용합니다.  
    - 추천도 사용 시, 표 바로 아래줄에 범례를 반드시 추가하시오: ◯ 추천 / △ 보통 / ✕ 없음 / — 미확인
    - 답변 마지막에는 사용자가 추가로 궁금한 점을 질문하도록 유도합니다.  
    - 반드시 사용한 정보의 출처를 (출처: 파일명, p.페이지) 형식으로 표시합니다.
    - 파일이 첨부된 경우 첨부된 파일의 내용을 참고하여 대답합니다.
    """
)


# --- 문서 포맷 함수 ---
def format_docs(docs):
    lines = []
    for d in docs:
        src = d.metadata.get("source", "")
        page = d.metadata.get("page", "?")
        lines.append(f"{d.page_content}\n(출처: {os.path.basename(src)}, p.{page})")
    return "---".join(lines)


# --- 최종 RAG 실행 함수 ---
def rag_answer(question: str, file_path: str = None) -> str:
    """
    파일 내용과 검색된 문서를 기반으로 질문에 답변하는 RAG 함수
    """
    # 🐛 해결: file_content를 빈 문자열로 먼저 초기화합니다.
    file_content = ''
    
    # 파일이 존재할 경우에만 내용을 읽어옵니다.
    if file_path and os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                file_content = f.read()
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
            # 파일 읽기 실패 시에도 계속 진행하도록 file_content는 ''로 유지됩니다.

    # 1. 검색 (Retrieve)
    docs = retriever.get_relevant_documents(question)
    context = format_docs(docs)
    
    # 2. 프롬프트 생성 (Prompt)
    chat_input = prompt.format(
        question=question, 
        context=context, 
        file_content=file_content
    )
    
    # 3. LLM 호출하여 답변 생성 (Generate)
    answer = llm.invoke(chat_input)
    
    return answer.content.strip()
