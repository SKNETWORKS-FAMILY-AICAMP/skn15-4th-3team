# chat/rag.py
import os
from operator import itemgetter
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_postgres import PGVector

# --- 환경 변수 불러오기 ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-api-key")
PG_CONN = os.getenv("PG_CONN", "postgresql+psycopg2://user:pass@host:5432/dbname")

# --- LLM & Embeddings ---
llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)
embed = OpenAIEmbeddings(api_key=OPENAI_API_KEY)

# --- Retriever 세팅 ---
def get_retriever():
    vs = PGVector(
        embeddings=embed,
        collection_name="insurance_docs",  # 실제 collection 이름으로 교체
        connection=PG_CONN,
        use_jsonb=True,
    )
    return vs.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 4, "fetch_k": 20, "lambda_mult": 0.8},
    )

# --- Prompt ---
prompt = ChatPromptTemplate.from_template(
    """
    당신은 보험 전문가 챗봇입니다.

    [질문]: {question}
    [컨텍스트]: {context}

    - 한국어로 친절하게 설명
    - 마크다운 형식 사용
    - 출처는 반드시 (출처: 파일명, p.페이지) 형식으로 표시
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
def rag_answer(question: str) -> str:
    retriever = get_retriever()
    rag_chain = (
        {
            "question": itemgetter("question"),
            "context": itemgetter("question") | retriever | format_docs,
        }
        | prompt
        | llm
        | StrOutputParser()
    )
    return rag_chain.invoke({"question": question})
