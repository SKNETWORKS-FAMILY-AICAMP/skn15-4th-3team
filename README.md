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
운전자 보험 RAG 챗봇

## ✅ 프로젝트 배경 및 목적
운전자 보험 약관은 복잡하고 이해하기 어려워 가입자들이 궁금증을 해소하기 어렵습니다. 
RAG 챗봇은 방대한 약관 문서에서 필요한 정보를 정확하게 찾아내어 사용자 질문에 대한 신뢰성 있는 답변을 제공하는 것을 목표로 합니다.

## 🖐️ 프로젝트 소개

<img width="967" height="359" alt="Image" src="https://github.com/user-attachments/assets/45202a26-0fa5-40c7-973f-9baea4bf5f85" />

(보험신보. 2020.04.27)

보험사의 약관은 해가 거듭할수록 두꺼워지고 복잡해져갔습니다. 보험에 가입하려는 사람에게 약관은 가벼운 마음으로 불 수 없는 사실상 그냥 넘기게 되는 그런 문서가 되어 가고 있습니다.

<img width="863" height="405" alt="Image" src="https://github.com/user-attachments/assets/e3743b6c-fcb2-4616-acdb-6b26408f689a" />

(nate뉴스. 2025.02.13)

100p뿐만 아니라 몇몇 보험은 500p가 넘어가는 방대한 양을 가지고 있어 고객들은 약관을 꼼꼼히 살피기란 불가능에 가깝습니다.

이에 따라, 보험의 방대한 약관을 임베딩을 통해 벡터 DB에 저장하고 이를 RAG를 이용해 챗봇으로 질문을 한다면, 고객들은 쉽게 약관의 정보를 검색하고 이용할 수 있게 될 것입니다.


## 🛠️ 주요 기능 및 기술 스택

LLM 모델: GPT-4o-mini를 활용하여 복잡한 질문을 이해하고 자연스러운 답변을 생성합니다.

문서 수집: DB손해보험, 현대해상, 한화손해보험, 삼성화재, 메리츠 화재의 운전자 보험 약관 PDF 파일을 데이터로 사용합니다.

RAG(Retrieval-Augmented Generation): 사용자 질문과 관련된 문서를 벡터 데이터베이스에서 검색하여 LLM에 제공함으로써 답변의 정확성과 신뢰성을 높입니다.

벡터 데이터베이스: PGVector를 사용하여 PostgreSQL에 문서의 임베딩 벡터를 저장하고 효율적으로 검색합니다.

LangChain: RAG 체인 구축을 위한 프레임워크로, 문서 로드, 청크 분할, 벡터화, 검색 및 LLM과의 연동 과정을 간소화합니다.

## 💡 프로젝트 흐름

|데이터 전처리|임베딩 및 저장|다중 검색|질의응답|
|-----|-----|-----|-----|
|각 보험사별 PDF 약관을 PyPDFLoader로 로드하고, RecursiveCharacterTextSplitter로 문서를 청크 단위로 분할합니다.|분할된 문서 청크를 OpenAIEmbeddings를 사용해 벡터로 변환하고, 각 보험사별로 다른 collection_name을 지정하여 PGVector에 저장합니다.|EnsembleRetriever를 활용해 여러 보험사의 컬렉션에서 동시에 문서를 검색하고, 가장 관련성 높은 문서를 찾아냅니다.|검색된 문서를 LLM의 컨텍스트로 전달하여, 사용자의 질문에 대한 답변을 생성하고 출처를 함께 제공합니다.|

## ❤️ 기대효과

|가입자 만족도 및 신뢰도 향상|콜센터 업무 효율 증대|정보 비대칭성 완화|확장성 및 유지보수 용이|
|-----|-----|-----|-----|
| 필요한 정보를 쉽고 빠르게 얻을 수 있습니다. 정확한 출처까지 함께 제공되므로 답변의 신뢰도가 높아져 고객 만족도가 크게 향상 할 수 있습니다.|다양한 상황에 대한 응대를 챗봇이 대신함으로써, 콜센터 직원들이 더 복잡하고 전문적인 상담에 집중할 수 있게 되어 업무 효율이 증대할 수 있습니다.|보험사는 방대한 정보를 제공하지만, 사용자는 이를 모두 파악하기 어렵습니다. 챗봇은 이 정보 비대칭성을 해소합니다.|새로운 보험 상품이 출시되거나 약관이 개정될 경우, 해당 문서만 벡터 데이터베이스에 추가하면 챗봇이 즉시 새로운 정보를 바탕으로 답변할 수 있어 유지보수가 간편합니다.|


## 👤 대상 사용자

보험회사의 약관은 양이 매우 많고 원하는 정보를 빠르게 찾기 어렵습니다. 따라서 보험회사의 운전자보험 약관을 학습한 LAG 기반 챗봇을 통해 사용자는 보다 빠르고 편리하게 정보를 얻을 수 있게 될 것 입니다.

나아가 사용자의 상황에 맞게 다양한 보험상품을 추천 받게 되면서, 사용자는 보험 상품의 가입에 있어서 큰 도움을 받을 수 있게 될 것입니다.


# 4. 기술 스택

| 항목    | 내용     |
| ---------- | ---------- |
| Language    | <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/langchain-1C3C3C?style=for-the-badge&logo=openai&logoColor=white"> <img src="https://img.shields.io/badge/RAG-FFCA28?style=for-the-badge&logo=rag&logoColor=white">    |
| Development    |<img src="https://img.shields.io/badge/streamlit-7952B3?style=for-the-badge&logo=streamlit&logoColor=white"> <img src="https://img.shields.io/badge/Visual Studio Code-61DAFB?style=for-the-badge&logo=VisualStudioCode&logoColor=white">    |
| Embedding    |      |
| LLM Model    | <img src="https://img.shields.io/badge/chatgpt_4o_mini-3776AB?style=for-the-badge&logo=openai&logoColor=white">      |
| Collaboration Tool    | <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"> <img src="https://img.shields.io/badge/Discord-02569B?style=for-the-badge&logo=Discord&logoColor=white">     |
| Vector DB    |<img src="https://img.shields.io/badge/pgvector-00599C?style=for-the-badge&logo=pgvector&logoColor=white"> <img src="https://img.shields.io/badge/psycopg2-3776AB?style=for-the-badge&logo=psycopg2&logoColor=white"> <img src="https://img.shields.io/badge/PostgreSQL-0769AD?style=for-the-badge&logo=postgresql&logoColor=white">    |
| API    | <img src="https://img.shields.io/badge/OpenAI API-181717?style=for-the-badge&logo=openai&logoColor=white">    |












<br/>
<br/>


# 5. 수행결과

## Vector DB
| Collection    | Embedding     |
| ---------- | ---------- |
| <img width="600" height="300" alt="Image" src="https://github.com/user-attachments/assets/b77924a7-8c06-46e1-897d-e2baa56e0c69" /> | <img width="600" height="300" alt="Image" src="https://github.com/user-attachments/assets/6dc37fde-1434-450c-847e-9f1b7b1146cb" />  |


# 6. 한 줄 회고

