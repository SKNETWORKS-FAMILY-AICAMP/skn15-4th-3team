# skn15-3rd-3team

# 1. 팀 소개
<div align="center">
<img width="320" height="320" alt="Image" src="https://github.com/user-attachments/assets/34eb158f-413f-4f38-b1e4-6440ea6ae851" />


| 기현택     | 권도원     | 유의정     | 이소정     | 이준원     | 한승희    |
|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|
|[@mathplanet](https://github.com/mathplanet)|[@dowonk120](https://github.com/dowonk120)|[@ryu0ej](https://github.com/Rr-EJ)|[@leesojunghub](https://github.com/leesojunghub)|[@none-jun](https://github.com/none-jun)|[@seunghee-han](https://github.com/seunghee-han)|
| Project Manager | Prompt Engineer | Frontend Engineer | Dataset Manager | Evaluation Specialist | Prompt Engineer |

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
운전자 보험 약관 RAG 챗봇

## ✅ 프로젝트 배경 및 목적
운전자 보험 약관은 너무 복잡해 고객이 원하는 정보를 직접 찾아내기 어렵습니다. 이 프로젝트의 RAG 챗봇은 방대한 약관 속에서 핵심 정보를 추출하여, 사용자가 궁금한 내용을 신뢰성 있게 확인할 수 있도록 돕습니다.

## 🖐️ 프로젝트 소개

<img width="967" height="359" alt="Image" src="https://github.com/user-attachments/assets/45202a26-0fa5-40c7-973f-9baea4bf5f85" />

(보험신보. 2020.04.27)

보험사의 약관은 매년 더 복잡해지고 길어지며, 가입자들에게는 쉽고 가볍게 읽기 어려운 문서가 되어가고 있습니다. 이 프로젝트는 바로 그 문제에서 출발했습니다.

<img width="863" height="405" alt="Image" src="https://github.com/user-attachments/assets/e3743b6c-fcb2-4616-acdb-6b26408f689a" />

(nate뉴스. 2025.02.13)

보험 약관은 때로는 100페이지, 심지어 500페이지를 넘어가기도 합니다. 이렇게 방대한 문서를 고객이 처음부터 끝까지 살펴보는 것은 현실적으로 어렵습니다.

그래서 본 프로젝트에서는 약관을 벡터 DB에 임베딩하고, RAG 기반 챗봇을 활용해 고객이 궁금한 부분을 손쉽게 질문하고 답변받을 수 있도록 구현했습니다.

|약관문서|페이지 수|
|-----|-----|
|DB운전자보험|900|
|KB_Direct_LngtrmDriver(24755)_202508|634|
|meritzfire|639|
|무배당 삼성화재 다이렉트 국방가족안심 운전자보험|331|
|무배당 삼성화재 다이렉트 운전자보험(2504.23)|323|
|무배당 삼성화재 운전자보험 안전운전 파트너 플러스(2504.8) 1종(연만기, 납입면제형)|528|
|무배당 삼성화재 운전자보험 안전운전 파트너 플러스(2504.8) 2종(연만기, 일반형)|522|
|한화 다이렉트 3400운전자보험 무배당|209|
|한화 시그니처 여성 운전자상해보험 무배당2504|430|
|한화 운전자상해보험 무배당 2504|544|
|현대해상약관|544|
|AXA운전자보험|192|



## ❤️ 기대효과

|가입자 만족도 및 신뢰도 향상|콜센터 업무 효율 증대|정보 비대칭성 완화|확장성 및 유지보수 용이|
|-----|-----|-----|-----|
| 필요한 정보를 쉽고 빠르게 얻을 수 있습니다. 정확한 출처까지 함께 제공되므로 답변의 신뢰도가 높아져 고객 만족도가 크게 향상 할 수 있습니다.|다양한 상황에 대한 응대를 챗봇이 대신함으로써, 콜센터 직원들이 더 복잡하고 전문적인 상담에 집중할 수 있게 되어 업무 효율이 증대할 수 있습니다.|보험사는 방대한 정보를 제공하지만, 사용자는 이를 모두 파악하기 어렵습니다. 챗봇은 이 정보 비대칭성을 해소합니다.|새로운 보험 상품이 출시되거나 약관이 개정될 경우, 해당 문서만 벡터 데이터베이스에 추가하면 챗봇이 즉시 새로운 정보를 바탕으로 답변할 수 있어 유지보수가 간편합니다.|


## 👤 대상 사용자

보험 약관은 방대한 분량과 복잡한 구조로 인해 원하는 정보를 찾기 어렵습니다. 따라서 운전자보험 약관을 손쉽게 확인하고 싶은 일반 가입자, 그리고 보험 상품 가입을 고려하는 사용자들이 주요 대상입니다. 이들은 RAG 기반 챗봇을 통해 필요한 정보를 빠르게 얻고, 개인 상황에 맞는 상품 추천까지 받을 수 있습니다.

## 🛠️ 주요 기능 및 기술 스택

|LLM 모델|RAG(Retrieval-Augmented Generation)|벡터 데이터베이스|LangChain|
|-----|-----|-----|-----|
|GPT-4o-mini를 활용|사용자 질문과 관련된 문서를 벡터 데이터베이스에서 검색하여 LLM에 제공함으로써 답변의 정확성과 신뢰성을 높입니다.|PGVector를 사용하여 PostgreSQL에 문서의 임베딩 벡터를 저장하고 효율적으로 검색합니다.|RAG 체인 구축을 위한 프레임워크로, 문서 로드, 청크 분할, 벡터화, 검색 및 LLM과의 연동 과정을 간소화합니다.|


## 💡 프로젝트 흐름

|데이터 전처리|임베딩 및 저장|다중 검색|질의응답|
|-----|-----|-----|-----|
|PDF -> PyPDFLoader로 로드 -> RecursiveCharacterTextSplitter 문서 청크| OpenAIEmbeddings를 사용 -> 벡터로 변환 -> 보험사별 collection_name을 지정 -> PGVector에 저장 | EnsembleRetriever를 활용 -> 동시에 문서를 검색 -> 가장 관련성 높은 문서|LLM의 컨텍스트로 전달 -> 답변을 생성 -> 출처를 제공 |

## Vector DB
| Collection    | Embedding     |
| ---------- | ---------- |
| <img width="600" height="300" alt="Image" src="https://github.com/user-attachments/assets/b77924a7-8c06-46e1-897d-e2baa56e0c69" /> | <img width="600" height="300" alt="Image" src="https://github.com/user-attachments/assets/6dc37fde-1434-450c-847e-9f1b7b1146cb" />  |



# 4. 기술 스택

| 항목    | 내용     |
| ---------- | ---------- |
| Language    | <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">|
| Development    |<img src="https://img.shields.io/badge/streamlit-7952B3?style=for-the-badge&logo=streamlit&logoColor=white"> <img src="https://img.shields.io/badge/Visual Studio Code-61DAFB?style=for-the-badge&logo=VisualStudioCode&logoColor=white"> <img src="https://img.shields.io/badge/langchain-1C3C3C?style=for-the-badge&logo=openai&logoColor=white"> <img src="https://img.shields.io/badge/RAG-FFCA28?style=for-the-badge&logo=rag&logoColor=white">|
| Embedding    | <img src="https://img.shields.io/badge/OpenAIEmbedding-181717?style=for-the-badge&logo=openai&logoColor=white">     |
| LLM Model    | <img src="https://img.shields.io/badge/chatgpt_4o_mini-3776AB?style=for-the-badge&logo=openai&logoColor=white">      |
| Collaboration Tool    | <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"> <img src="https://img.shields.io/badge/Discord-02569B?style=for-the-badge&logo=Discord&logoColor=white">     |
| Vector DB    |<img src="https://img.shields.io/badge/pgvector-00599C?style=for-the-badge&logo=pgvector&logoColor=white"> <img src="https://img.shields.io/badge/psycopg2-3776AB?style=for-the-badge&logo=psycopg2&logoColor=white"> <img src="https://img.shields.io/badge/PostgreSQL-0769AD?style=for-the-badge&logo=postgresql&logoColor=white">    |
| API    | <img src="https://img.shields.io/badge/OpenAI API-181717?style=for-the-badge&logo=openai&logoColor=white">    |












<br/>
<br/>


# 5. 수행결과




# 6. 한 줄 회고

| 기현택     | 권도원     | 유의정     |
|:----------:|:----------:|:----------:|
||||

| 이소정     | 이준원     | 한승희    |
|:----------:|:----------:|:----------:|
||||
