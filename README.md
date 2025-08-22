# skn15-3rd-3team

# 1. 팀 소개

| 기현택     | 권도원     | 유의정     | 이소정     | 이준원     | 한승희    |
| ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
|[@mathplanet](https://github.com/mathplanet)|[@dowonk120](https://github.com/dowonk120)|[@ryu0ej](https://github.com/Rr-EJ)|[@leesojunghub](https://github.com/leesojunghub)|[@none-jun](https://github.com/none-jun)|[@seunghee-han](https://github.com/seunghee-han)|
| | | | | | |

</div>
<br/>
<br/>
<br/>

# 2. 프로젝트 기간
2025년 8월 22일 ~ 2025년 8월 25일 (2일)
<br/>
<br/>
<br/>	

# 3. 프로젝트 개요

## 📕 프로젝트명
운전자 보험 RAG 챗봇

## ✅ 프로젝트 배경 및 목적
운전자 보험 약관은 복잡하고 이해하기 어려워 가입자들이 궁금증을 해소하기 어렵습니다. 
RAG 챗봇은 방대한 약관 문서에서 필요한 정보를 정확하게 찾아내어 사용자 질문에 대한 신뢰성 있는 답변을 제공하는 것을 목표로 합니다.

## 🖐️ 프로젝트 소개
###🛠️ 주요 기능 및 기술 스택

LLM 모델: GPT-4o-mini를 활용하여 복잡한 질문을 이해하고 자연스러운 답변을 생성합니다.

문서 수집: DB손해보험, 현대해상, 한화손해보험, 삼성화재, 메리츠 화재의 운전자 보험 약관 PDF 파일을 데이터로 사용합니다.

RAG(Retrieval-Augmented Generation): 사용자 질문과 관련된 문서를 벡터 데이터베이스에서 검색하여 LLM에 제공함으로써 답변의 정확성과 신뢰성을 높입니다.

벡터 데이터베이스: PGVector를 사용하여 PostgreSQL에 문서의 임베딩 벡터를 저장하고 효율적으로 검색합니다.

LangChain: RAG 체인 구축을 위한 프레임워크로, 문서 로드, 청크 분할, 벡터화, 검색 및 LLM과의 연동 과정을 간소화합니다.

###💡 프로젝트 흐름

데이터 전처리: 각 보험사별 PDF 약관을 PyPDFLoader로 로드하고, RecursiveCharacterTextSplitter로 문서를 청크 단위로 분할합니다.

임베딩 및 저장: 분할된 문서 청크를 OpenAIEmbeddings를 사용해 벡터로 변환하고, 각 보험사별로 다른 collection_name을 지정하여 PGVector에 저장합니다.

다중 검색: EnsembleRetriever를 활용해 여러 보험사의 컬렉션에서 동시에 문서를 검색하고, 가장 관련성 높은 문서를 찾아냅니다.

질의응답: 검색된 문서를 LLM의 컨텍스트로 전달하여, 사용자의 질문에 대한 답변을 생성하고 출처를 함께 제공합니다.

## ❤️ 기대효과
가입자 만족도 및 신뢰도 향상: 복잡한 보험 약관을 사용자가 직접 찾아보지 않아도, 필요한 정보를 쉽고 빠르게 얻을 수 있습니다. 정확한 출처까지 함께 제공되므로 답변의 신뢰도가 높아져 고객 만족도가 크게 향상 할 수 있다

콜센터 업무 효율 증대: 단순 반복적인 문의(예: "보험료 납부 기한은 언제인가요?", "특약 해지 시 불이익이 있나요?")에 대한 응대를 챗봇이 대신함으로써, 콜센터 직원들이 더 복잡하고 전문적인 상담에 집중할 수 있게 되어 업무 효율이 증대할 수 있다

정보 비대칭성 완화: 보험사는 방대한 정보를 제공하지만, 사용자는 이를 모두 파악하기 어렵습니다. 챗봇은 이 정보 비대칭성을 해소하여 소비자들이 더 현명하게 보험 상품을 선택하고 관리할 수 있도록 도움될 수 있다

확장성 및 유지보수 용이: 새로운 보험 상품이 출시되거나 약관이 개정될 경우, 해당 문서만 벡터 데이터베이스에 추가하면 챗봇이 즉시 새로운 정보를 바탕으로 답변할 수 있어 유지보수가 간편하다

## 👤 대상 사용자


# 4. 기술 스택
### ✔️ Environment
<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Visual Studio Code-61DAFB?style=for-the-badge&logo=VisualStudioCode&logoColor=white">
<img src="https://img.shields.io/badge/streamlit-7952B3?style=for-the-badge&logo=streamlit&logoColor=white">
<img src="https://img.shields.io/badge/PostgreSQL-0769AD?style=for-the-badge&logo=postgresql&logoColor=white">
<img src="https://img.shields.io/badge/OpenAI-181717?style=for-the-badge&logo=openai&logoColor=white">
<img src="https://img.shields.io/badge/langchain-1C3C3C?style=for-the-badge&logo=openai&logoColor=white">

### ✔️ Communication
<img src="https://img.shields.io/badge/Discord-02569B?style=for-the-badge&logo=Discord&logoColor=white">
<img src="https://img.shields.io/badge/Notion-F7DF1E?style=for-the-badge&logo=notion&logoColor=black">
<br/>
<br/>


# 5. 수행결과



# 6. 한 줄 회고

