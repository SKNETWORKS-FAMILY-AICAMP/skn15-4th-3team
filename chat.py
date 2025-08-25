# !! 사용시 openai key, db 계정 변경 필요!!

import os
import json
from typing import List
from operator import itemgetter

import streamlit as st
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.embeddings import CacheBackedEmbeddings
from langchain.storage import LocalFileStore
from langchain_community.vectorstores import FAISS
from langchain.retrievers import EnsembleRetriever
from langchain_postgres import PGVector
from langchain_core.messages import HumanMessage
import re

def render_answer(md: str) -> str:
    """
    - '<br>' 표기를 실제 줄바꿈으로 보이게 처리
    - 표 셀에서도 줄바꿈이 보이도록 HTML <br/> 로 치환
    - 불필요한 과도한 빈줄 정리
    """
    # 1) 다양한 형태의 <br> 태그를 통일
    s = re.sub(r'<\s*br\s*/?\s*>', '<br/>', md, flags=re.I)

    # 2) 연속 3줄 이상 빈줄 -> 2줄로 축소(과한 공백 방지)
    s = re.sub(r'\n{3,}', '\n\n', s)

    return s

# =====================
# 🎨 Custom CSS for a beautiful UI
# =====================
st.markdown(
    """
<style>
/* =====================
   전체 페이지
===================== */
body {
    font-family: 'Inter', 'Segoe UI', sans-serif;
    background-color: #f7f8fa;
    color: #111827;
}

/* =====================
   메인 컨테이너
===================== */
.main .block-container {
    padding: 2rem 2.5rem;
    max-width: 900px;
    margin: auto;
}

/* =====================
   사이드바
===================== */
[data-testid="stSidebar"] {
    background-color: #ffffff;
    border-right: 1px solid #e5e7eb;
    padding: 2rem 1rem;
    min-width: 220px;
}

[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #111827;
    font-weight: 600;
}

/* 사이드바 버튼 */
[data-testid="stSidebar"] .stButton > button {
    width: 100%;
    text-align: left;
    padding: 12px 16px;
    border-radius: 10px;
    border: none;
    font-size: 0.95rem;
    color: #111827;
    background-color: #f3f4f6;
    margin-bottom: 0.5rem;
    font-weight: 500;
    transition: all 0.2s ease;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}
[data-testid="stSidebar"] .stButton > button:hover {
    background-color: #e5e7eb;
}
[data-testid="stSidebar"] .stButton[data-selected="true"] > button {
    background-color: #2563eb;
    color: #ffffff;
    font-weight: 600;
}

/* 새 채팅 버튼 강조 */
.stButton:nth-child(1) button {
    background-color: #2563eb;
    color: #ffffff !important;
    font-weight: 600;
}
.stButton:nth-child(1) button:hover {
    background-color: #1e40af !important;
}

/* =====================
   사이드바 닫혔을 때 전체 확장
===================== */
/* 1. 최상위 컨테이너에서 닫힌 사이드바 숨기기 */
[data-testid="stAppViewContainer"] > [data-testid="stSidebar"][aria-expanded="false"] {
    display: none !important;
    width: 0 !important;
    padding: 0 !important;
    margin: 0 !important;
}

/* 2. 사이드바 다음 .main 영역 너비 100% */
[data-testid="stAppViewContainer"] > [data-testid="stSidebar"][aria-expanded="false"] + .main {
    width: 100% !important;
    margin: 0 !important;
}

/* 3. .block-container 내부 콘텐츠 가득 채우기 */
[data-testid="stAppViewContainer"] > [data-testid="stSidebar"][aria-expanded="false"] + .main .block-container {
    max-width: none !important;
    width: calc(100% - 4rem) !important;
    margin: auto !important;
}

/* =====================
   채팅 메시지 카드
===================== */
[data-testid="stChatMessage"] {
    border-radius: 16px;
    padding: 1rem 1.2rem;
    margin-bottom: 1rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    max-width: 100%;
    line-height: 1;
    font-size: 0.95rem;
    word-wrap: break-word;
    white-space: pre-wrap;
}

/* 사용자 메시지 (오른쪽) */
.st-emotion-cache-1c0t8v9 {
    background-color: #2563eb !important;
    color: #ffffff !important;
    border-top-left-radius: 0 !important;
    margin-left: auto;
}

/* 어시스턴트 메시지 (왼쪽) */
.st-emotion-cache-x7gh8c {
    background-color: #f3f4f6 !important;
    color: #111827 !important;
    border-top-right-radius: 0 !important;
    margin-right: auto;
}

/* =====================
   입력창
===================== */
[data-testid="stTextInput"] > div > div > input {
    border-radius: 999px;
    border: 1px solid #d1d5db;
    padding: 14px 20px;
    font-size: 0.95rem;
    transition: all 0.2s ease;
    background-color: #ffffff;
    width: calc(100% - 40px);
}
[data-testid="stTextInput"] > div > div > input:focus {
    border-color: #2563eb;
    box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.2);
}

/* =====================
   제목
===================== */
h1 {
    color: #111827;
    font-weight: 700;
    font-size: 2rem;
    margin-bottom: 1rem;
}

/* =====================
   파일 업로드
===================== */
.stFileUpload {
    border-radius: 14px;
    border: 1px dashed #d1d5db;
    padding: 1rem;
    background-color: #ffffff;
}

/* =====================
   구분선
===================== */
hr {
    border: none;
    border-top: 1px solid #e5e7eb;
    margin: 1.5rem 0;
}

/* =====================
   모바일/반응형
===================== */
@media (max-width: 768px) {
    .main .block-container {
        padding: 1rem 1rem;
    }
    [data-testid="stSidebar"] {
        min-width: 180px;
        padding: 1rem 0.5rem;
    }
    [data-testid="stChatMessage"] {
        max-width: 90%;
    }
}
</style>
""",
    unsafe_allow_html=True,
)


# =====================
# ⚙️ App Config
# =====================
st.set_page_config(page_title="운전자 보험 챗봇 서비스", layout="wide")
st.title("운전자 보험 챗봇 서비스")

# --- Environment ---
# change
OPENAI_API_KEY = "your_key"
if not OPENAI_API_KEY:
    st.warning(
        "⚠️ OPENAI_API_KEY 환경변수가 설정되어 있지 않습니다. .env 또는 시스템 환경변수를 확인하세요."
    )

connection_string = os.getenv(
    "PG_CONN",
    # change
    "postgresql+psycopg2://",
)


# =====================
# 🔧 Engine (커넥션 풀 캐시로 Too many clients 방지)
# =====================
@st.cache_resource(show_spinner=False)
def get_engine(conn_str: str) -> Engine:
    """커넥션 풀이 적용된 데이터베이스 엔진을 생성합니다."""
    return create_engine(
        conn_str,
        pool_size=5,
        max_overflow=0,
        pool_pre_ping=True,
        pool_recycle=1800,
    )


# =====================
# 세션 관리
# =====================
def generate_title(message):
    """LLM을 사용하여 메시지의 제목을 생성합니다."""
    prompt = f"이 메시지를 5~10자 이내로 간단히 제목화 해줘:\n\n{message}"
    response = ChatOpenAI(model="gpt-4.1-2025-04-14", api_key=OPENAI_API_KEY).invoke(
        [HumanMessage(content=prompt)]
    )
    return response.content.strip()


# 초기 세션 상태 설정
if "conversations" not in st.session_state:
    st.session_state["conversations"] = [
        {"title": "대화 내용이 기록됩니다", "messages": []}
    ]

if "current_chat" not in st.session_state:
    st.session_state["current_chat"] = 0

if "dev_mode" not in st.session_state:
    st.session_state["dev_mode"] = False


# =====================
# 💬 Sidebar
# =====================
with st.sidebar:
    st.subheader("✨ 시작하기")

    # '새 채팅' 버튼
    if st.button("➕ 새 채팅"):
        st.session_state["conversations"].append(
            {"title": "대화 내용이 기록됩니다", "messages": []}
        )
        st.session_state["current_chat"] = len(st.session_state["conversations"]) - 1
        st.rerun()

    st.markdown("---")
    st.subheader("💬 채팅 기록")

    # 채팅 기록 버튼
    for i, session in enumerate(st.session_state["conversations"]):
        button_label = session["title"]
        is_selected = i == st.session_state["current_chat"]

        # Streamlit 버튼에 data-selected 속성을 추가하여 CSS로 스타일링
        button_container = st.container()
        if button_container.button(button_label, key=f"chat_{i}"):
            st.session_state["current_chat"] = i
            st.rerun()

        # 선택된 버튼에 CSS 클래스를 추가하는 스크립트 (다소 불안정할 수 있음)
        if is_selected:
            st.markdown(
                f"""
                <script>
                    const button = window.parent.document.querySelector('[data-testid="stSidebar"] button[key="chat_{i}"]');
                    if (button) {{
                        button.parentElement.setAttribute('data-selected', 'true');
                    }}
                </script>
            """,
                unsafe_allow_html=True,
            )

    st.markdown("---")
    st.subheader("📤 개인 파일 업로드")
    uploads = st.file_uploader(
        "PDF 또는 TXT 업로드", type=["pdf", "txt"], accept_multiple_files=True
    )

    st.markdown("---")
    st.session_state["dev_mode"] = st.checkbox(
        "개발자 모드", value=st.session_state["dev_mode"]
    )

# =====================
# 🧠 LLM/Embedding
# =====================
llm = ChatOpenAI(model="gpt-4.1-2025-04-14", api_key=OPENAI_API_KEY)
base_embed = OpenAIEmbeddings(api_key=OPENAI_API_KEY)
cache_dir = "./mycache/embedding"
os.makedirs(cache_dir, exist_ok=True)
embed_store = LocalFileStore(cache_dir)
cached_embedder = CacheBackedEmbeddings.from_bytes_store(
    underlying_embeddings=base_embed,
    document_embedding_cache=embed_store,
)


# =====================
# 🗂️ Helpers (DB)
# =====================
@st.cache_data(show_spinner=False)
def list_collections(conn_str: str) -> List[str]:
    """데이터베이스의 모든 컬렉션을 조회합니다."""
    try:
        engine = get_engine(conn_str)
        with engine.connect() as conn:
            rows = conn.execute(
                text("SELECT name FROM public.langchain_pg_collection ORDER BY name")
            )
            return [(r[0] or "").strip() for r in rows]
    except Exception as e:
        st.error(f"컬렉션 조회 실패: {e}")
        return []


@st.cache_resource(show_spinner=False)
def build_pg_retrievers(conn_str: str, collections: List[str]):
    """PGVector에서 검색기를 빌드합니다."""
    retrievers = []
    skipped = []
    engine = get_engine(conn_str)
    with engine.connect() as conn:
        existing = {
            (r[0] or "").strip(): r[1]
            for r in conn.execute(
                text("SELECT name, uuid FROM public.langchain_pg_collection")
            )
        }

    for raw_name in collections:
        cname = (raw_name or "").strip()
        if not cname or cname not in existing:
            skipped.append(raw_name)
            continue
        vs = PGVector(
            embeddings=base_embed,
            collection_name=cname,
            connection=conn_str,
            use_jsonb=True,
        )
        try:
            _ = vs.similarity_search("ping", k=1)
        except ValueError as e:
            if "Collection not found" in str(e):
                skipped.append(cname)
                continue
            else:
                raise
        retrievers.append(
            vs.as_retriever(
                search_type="mmr",
                search_kwargs={"k": 4, "fetch_k": 20, "lambda_mult": 0.8},
            )
        )
    if skipped:
        st.warning(
            f"다음 컬렉션은 건너뜀(존재/접근 문제): {', '.join([s for s in skipped if s])}"
        )
    return retrievers


# =====================
# 📄 Helpers (Uploads)
# =====================
@st.cache_resource(show_spinner="업로드 파일 임베딩 중…")
def build_upload_retriever(files, chunk_size=1000, chunk_overlap=80):
    """업로드된 파일에서 검색기를 빌드합니다."""
    from langchain_core.documents import Document

    save_dir = "./mycache/files"
    os.makedirs(save_dir, exist_ok=True)
    docs = []
    for f in files:
        name = f.name
        ext = name.split(".")[-1].lower()
        save_path = os.path.join(save_dir, name)
        bin_bytes = f.read()
        with open(save_path, "wb") as fp:
            fp.write(bin_bytes)
        if ext == "pdf":
            loader = PDFPlumberLoader(save_path)
            file_docs = loader.load()
        elif ext == "txt":
            text = bin_bytes.decode("utf-8")
            file_docs = [
                Document(page_content=text, metadata={"source": save_path, "page": 1})
            ]
        else:
            continue
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap
        )
        docs.extend(splitter.split_documents(file_docs))
    if not docs:
        return None
    vs = FAISS.from_documents(docs, cached_embedder)
    return vs.as_retriever()


# =====================
# 🔎 Retriever Assembly (DB + Uploads)
# =====================
all_retrievers = []
all_collections = list_collections(connection_string)
if all_collections:
    db_retrievers = build_pg_retrievers(connection_string, all_collections)
    all_retrievers.extend(db_retrievers)
else:
    st.info("DB에 컬렉션이 없습니다. 업로드만 사용합니다.")

upload_retriever = None
if "uploads" in locals() and uploads:
    upload_retriever = build_upload_retriever(uploads)
    if upload_retriever is not None:
        all_retrievers.append(upload_retriever)

final_retriever = None
if len(all_retrievers) == 1:
    final_retriever = all_retrievers[0]
elif len(all_retrievers) > 1:
    final_retriever = EnsembleRetriever(retrievers=all_retrievers)

# =====================
# 🧩 RAG Chain
# =====================
prompt = ChatPromptTemplate.from_template(
    """당신은 여러 보험사의 상품을 비교 분석하여 사용자에게 가장 쉽고 친절하게 정보를 전달하는 보험 전문가 챗봇입니다.

다음 지시사항을 철저히 따라 사용자의 질문에 한국어로 답변하세요.

답변의 서식:
- 마크다운(Markdown)을 사용하여 답변을 구조화하세요.
- 주요 정보는 **볼드체**로 강조하세요.
- 여러 회사를 비교하는 경우, 반드시 마크다운 표를 활용하여 항목별로 정리하세요.
- 서류나 항목을 나열할 때는 체크리스트(- 또는 * 또는 숫자 목록)를 사용하세요.

답변의 내용:
- 전문 용어는 피하고, 누구나 이해할 수 있도록 쉽고 자세하게 설명하세요.
- 답변은 질문에 대한 직접적인 내용만을 포함하며, 불필요한 서론이나 결론은 제외하세요.
- 제시된 '컨텍스트' 내의 정보만 사용하세요. 컨텍스트에 없는 내용은 절대로 지어내지 마세요. 
- 컨텍스트에 없는 내용을 질문할 시, 모른다고 말하지말고 질문한 회사의 전화번호나 링크를 줘서 직접 내용을 탐색하도록 유도하세요.
- 사용자의 상황(사고 유형, 과실 비율, 연령 등)을 고려해서 답변해주세요.
- 비교할때는 차이점을 명확하게 구체적으로 설명하세요.
- 추천 시에는 그 이유(보장 범위, 특화 옵션, 지급 조건 등)를 구체적으로 설명하세요.

출처 표기:
- 답변에 사용된 모든 정보는 마지막에 출처(파일명/페이지)를 명확히 명시하세요.
- 출처는 항상 괄호(()) 안에 (출처: 파일명, 페이지 p.N) 형식으로 표시하세요.

마지막에는 항상 더 물어볼 내용이 있는지 물어보면서 대화를 더 길게하도록 유도해

[대화 기록]
{history}

[질문]
{question}

[컨텍스트]
{context}
"""
)


def format_docs(docs):
    lines = []
    for d in docs:
        src = d.metadata.get("source", "")
        page = d.metadata.get("page", "")
        import os as _os

        lines.append(
            f"{d.page_content}\n[출처: {_os.path.basename(src)}, 페이지 p.{page}]"
        )
    return "---".join(lines)


def get_history_text(chat):
    """대화 기록을 텍스트 형식으로 변환합니다."""
    return "\n".join([f"{m['role']}: {m['content']}" for m in chat["messages"]])


# =====================
# 💬 Chat UI
# =====================
current_chat = st.session_state["conversations"][st.session_state["current_chat"]]

# 기존 대화 먼저 출력
for m in current_chat["messages"]:
    st.chat_message(m["role"]).write(m["content"])

# 입력창을 맨 아래에 고정
user_q = st.chat_input("질문을 입력하세요…")

if user_q:
    # 사용자 메시지 추가
    current_chat["messages"].append({"role": "user", "content": user_q})
    if len(current_chat["messages"]) == 1:
        try:
            current_chat["title"] = generate_title(user_q)
        except Exception:
            current_chat["title"] = user_q[:20] + ("..." if len(user_q) > 20 else "")

    # 사용자 메시지 UI에 표시
    st.chat_message("user").write(user_q)

    # RAG 체인 호출
    if final_retriever is None:
        st.error("활성화된 데이터 소스가 없습니다. (DB에 컬렉션이 없고 업로드도 없음)")
    else:
        with st.chat_message("assistant"):
            with st.spinner("답변을 생성하는 중..."):
                history_text = get_history_text(current_chat)
                # rag_chain = (
                #     RunnablePassthrough.assign(
                #         context=final_retriever | format_docs,
                #         history=lambda x: history_text,
                #     )
                #     | prompt
                #     | llm
                #     | StrOutputParser()
                # )
                # answer = rag_chain.invoke({"question": user_q})
                rag_chain = (
                    {
                        "question": itemgetter("question"),
                        "history": lambda _: history_text,
                        "context": itemgetter("question") | final_retriever | format_docs,
                    }
                    | prompt
                    | llm
                    | StrOutputParser()
                )

                answer = rag_chain.invoke({"question": user_q})
                st.write(answer)


                # 어시스턴트 메시지 추가
                current_chat["messages"].append(
                    {"role": "assistant", "content": answer}
                )

st.markdown("---")

# =====================
# 🔍 Debug / Info (optional)
# =====================
if st.session_state["dev_mode"]:
    with st.expander("디버그/정보"):

        def _mask(cs: str | None) -> str:
            if not cs:
                return "(없음)"
            return f"{cs[:8]}*** (마스킹됨)"

        st.write(
            {
                "connection_string": _mask(connection_string),
                "collections": all_collections,
                "has_upload_retriever": upload_retriever is not None,
            }
        )
        st.info(
            "Tip: 이 앱은 조회용입니다. 색인은 별도 스크립트에서 수행하고, pre_delete_collection=True는 거기서만 사용하세요."
        )
