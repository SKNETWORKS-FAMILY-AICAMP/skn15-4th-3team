# 운전자 보험 약관 RAG 챗봇



# 팀 소개
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

# 기술 스택

| 항목    | 내용     |
| ---------- | ---------- |
| Language    | <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">  <img src="https://img.shields.io/badge/sql-4479A1?style=for-the-badge&logo=sql&logoColor=white"> |
| Development    | <img src="https://img.shields.io/badge/Visual Studio Code-61DAFB?style=for-the-badge&logo=VisualStudioCode&logoColor=white"> |
| Embedding    | <img src="https://img.shields.io/badge/OpenAIEmbedding-181717?style=for-the-badge&logo=openai&logoColor=white">     |
| LLM Model    | <img src="https://img.shields.io/badge/chatgpt_4.1-3776AB?style=for-the-badge&logo=openai&logoColor=white">      |
| Collaboration Tool    | <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"> <img src="https://img.shields.io/badge/Discord-02569B?style=for-the-badge&logo=Discord&logoColor=white">     |
|Framework|<img src="https://img.shields.io/badge/langchain-1C3C3C?style=for-the-badge&logo=openai&logoColor=white">  <img src="https://img.shields.io/badge/RAG-FFCA28?style=for-the-badge&logo=rag&logoColor=white"> <img src="https://img.shields.io/badge/streamlit-7952B3?style=for-the-badge&logo=streamlit&logoColor=white">|
| Vector DB    |<img src="https://img.shields.io/badge/pgvector-00599C?style=for-the-badge&logo=pgvector&logoColor=white"> <img src="https://img.shields.io/badge/psycopg2-3776AB?style=for-the-badge&logo=psycopg2&logoColor=white"> <img src="https://img.shields.io/badge/PostgreSQL-0769AD?style=for-the-badge&logo=postgresql&logoColor=white"> <img src="https://img.shields.io/badge/FAISS-E34F26?style=for-the-badge&logo=faiss&logoColor=white">   |
| API    | <img src="https://img.shields.io/badge/OpenAI API-181717?style=for-the-badge&logo=openai&logoColor=white">    |
|Evaulation|<img src="https://img.shields.io/badge/Ragas-F7DF1E?style=for-the-badge&logo=ragas&logoColor=white"> |


# 프로젝트 기간
2025년 8월 22일, 2025년 8월 25일 (2일)
<br/>
<br/>
<br/>	

# 프로젝트 개요

## 📕 프로젝트 발단

보험 약관이 너무 복잡하고 소비자가 이해하기 어렵다는 사회적 지적이 늘고 있습니다.  
<img width="500" height="250" alt="Image" src="https://github.com/user-attachments/assets/45202a26-0fa5-40c7-973f-9baea4bf5f85" /><img width="500" height="250" alt="Image" src="https://github.com/user-attachments/assets/e3743b6c-fcb2-4616-acdb-6b26408f689a" />
(보험신보. 2020.04.27)(nate뉴스. 2025.02.13)


보험사의 약관은 매년 더 복잡해지고 길어지며, 가입자들에게는 쉽고 가볍게 읽기 어려운 문서가 되어가고 있습니다. 이 프로젝트는 바로 그 문제에서 출발했습니다.

보험 약관은 때로는 300페이지, 심지어 500페이지를 넘어가기도 합니다. 이렇게 방대한 문서를 고객이 처음부터 끝까지 살펴보는 것은 현실적으로 어렵습니다.

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

### 약관 예시
<img width="900" height="600" alt="Image" src="https://github.com/user-attachments/assets/33de0f2c-6dc9-4e1a-8ce0-f60fd56ad948" />

-현대해상-

### 약관의 문제점

* 소비자에게 매우 불리한 방대한 내용
  * 빼곡한 글자와 어려운 용어 난무
  * 500 페이지가 넘는 엄청난 양
* 잦은 개정 및 강제성
  * 일정한 주기마다 잦은 개정으로 소비자가 정확한 내용 접근 어려움
  * 동의를 해야 가입 가능한 강제성
  * '약관에 다 있었다'라는 마법의 문장으로 보험회사가 유리하게 해석 가능

## ✅ 프로젝트 배경 및 목적

운전자 보험 약관은 내용이 너무 복잡해 고객이 원하는 정보를 직접 찾아내기 어렵습니다. 

이 프로젝트의 RAG 챗봇은 방대한 약관 속에서 핵심 정보를 추출하여, 사용자가 궁금한 내용을 신뢰성 있게 확인할 수 있도록 돕습니다.

## ❤️ 기대효과

* 가입자 만족도 및 신뢰도 향상
  *  필요한 정보를 쉽고 빠르게 얻을 수 있습니다. 정확한 출처까지 함께 제공되므로 답변의 신뢰도가 높아져 고객 만족도가 크게 향상 할 수 있습니다.
* 정보 비대칭성 완화
  *  보험사는 방대한 정보를 제공하지만, 사용자는 이를 모두 파악하기 어렵습니다. 챗봇은 이 정보 비대칭성을 해소합니다.
* 확장성 및 유지보수 용이
  *  새로운 보험 상품이 출시되거나 약관이 개정될 경우, 해당 문서만 벡터 데이터베이스에 추가하면 챗봇이 즉시 새로운 정보를 바탕으로 답변할 수 있어 유지보수가 간편합니다.
* 콜센터 업무 효율 증대
  *  다양한 상황에 대한 응대를 챗봇이 대신함으로써, 콜센터 직원들이 더 복잡하고 전문적인 상담에 집중할 수 있게 되어 업무 효율이 증대할 수 있습니다.


## 🛠️ 플로우 구조

<img width="1200" height="600" alt="Image" src="https://github.com/user-attachments/assets/efcbcc95-25f5-4b3d-9165-10e86ac5ed8a" />

<img width="1200" height="650" alt="Image" src="https://github.com/user-attachments/assets/9d7f1eaa-7249-417a-8ff9-375e1344fa8f" />

* 데이터 전처리
  * PDF -> PyPDFLoader로 로드 -> RecursiveCharacterTextSplitter 문서 청크
* 임베딩 및 저장
  * OpenAIEmbeddings를 사용 -> 벡터로 변환 -> 보험사별 collection_name을 지정 -> PGVector 사용 -> postgreSQL에 저장
* 다중 검색
  * EnsembleRetriever를 활용 -> 동시에 문서를 검색 -> 가장 관련성 높은 문서
* 질의응답
  * LLM의 컨텍스트로 전달 -> 답변을 생성 -> 출처를 제공


### Vector DB
| Collection    | Embedding     |
| ---------- | ---------- |
| <img width="600" height="300" alt="Image" src="https://github.com/user-attachments/assets/b77924a7-8c06-46e1-897d-e2baa56e0c69" /> | <img width="600" height="300" alt="Image" src="https://github.com/user-attachments/assets/6dc37fde-1434-450c-847e-9f1b7b1146cb" />  |

<br/>
<br/>

### Prompt

<img width="1058" height="877" alt="Image" src="https://github.com/user-attachments/assets/a0726b49-9072-4d6d-8eae-17097c40419e" />

* 신뢰성 확보 -> 근거 없는 답변을 금지하고, 자료 부재 시 보험사 공식 연락처·링크로 안내
  
* 개인 맞춤 기반 추천 서비스 -> 사용자 특성(사고·과실·연령) 기반으로 비교·추천 근거를 구체적으로 제시


### 성능 평가

* 1차 Prompt

|지표|수치|설명|
|-----|-----|-----|
|faithfulness|0.339|답변 충실도, 환각 방지|
|answer_relevancy|0.171|답변의 질문 관련성|
|nv_context_relevance|0.408|검색한 문서의 답변 관련성|


* 2차 Prompt

|지표|수치|설명|
|-----|-----|-----|
|faithfulness|0.392|답변 충실도, 환각 방지|
|answer_relevancy|0.497|답변의 질문 관련성|
|nv_context_relevance|0.392|검색한 문서의 답변 관련성|

* 최종 Prompt

|지표|수치|설명|
|-----|-----|-----|
|faithfulness|0.416|답변 충실도, 환각 방지|
|answer_relevancy|0.316|답변의 질문 관련성|
|nv_context_relevance|0.400|검색한 문서의 답변 관련성|




## Streamlit
<img width="1905" height="1016" alt="Image" src="https://github.com/user-attachments/assets/5d27a1e3-3913-404e-89df-0bd4c77684ed" />


### 연령별 예시

* 30대

<img width="1100" height="751" alt="Image" src="https://github.com/user-attachments/assets/6eb04024-738b-477f-8560-3dbe02202ddb" />

* 40대

<img width="1071" height="754" alt="Image" src="https://github.com/user-attachments/assets/e6fc8763-70fb-48e5-b9bd-517e85a40c45" />

* 특정 나이

<img width="1440" height="685" alt="image" src="https://github.com/user-attachments/assets/ae4ee676-574a-4c32-8931-929ef851a7ce" />


### 상황별 예시

* 횡단보도에서 무단횡단 보행자 사고
<img width="1094" height="803" alt="Image" src="https://github.com/user-attachments/assets/b91b9abb-6565-4110-8153-c555f8e3aaaf" />
<img width="1029" height="694" alt="Image" src="https://github.com/user-attachments/assets/4ec8e3d9-7886-46f4-b395-9343a9d57860" />
<img width="1071" height="871" alt="Image" src="https://github.com/user-attachments/assets/4e50635f-1a7c-4cb6-9067-5db611d23ab3" />


## 프로젝트 확장성

* 다양한 보험 상품으로의 적용 가능
  * 건강보험, 화재보험 등 다양한 약관을 반영하면 햇봇의 목적을 바로 바꿀 수 있게 됩니다.
* 판례 데이터 반영
  * 파인 튜닝(Fine-Tuning)을 통한 판례 기반의 추론 강화
  * 법적 기반을 통한 방향성 확보
  * 챗봇이 더욱 풍부한 역할 가능

# 회고록

* 권도원

* 기현택
  
* 유의정
  
* 이소정 : 이번 프로젝트에서는 데이터베이스부터 RAG 모델까지 직접 구현하며 문제를 해결하는 과정에서 많은 성장을 느낄 수 있었습니다. 또한 팀원들과 협력하며 서로의 아이디어를 보태 더 완성도 높은 결과를 만들어낼 수 있었습니다.
  
* 이준원
  
* 한승희


