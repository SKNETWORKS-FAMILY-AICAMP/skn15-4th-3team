
# <img width="50" height="50" alt="logo" src="https://github.com/user-attachments/assets/59ca02dd-bc0e-4019-869a-1f7aa44a0e80" />운전자 보험 약관 RAG 챗봇!


# 팀 소개


| 이준원    | 권도원    | 기현택       | 유의정     | 이소정  | 한승희    |
|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|
|[@none-jun](https://github.com/none-jun)|[@dowonk120](https://github.com/dowonk120)|[@mathplanet](https://github.com/mathplanet)|[@ryu0ej](https://github.com/Rr-EJ)|[@leesojunghub](https://github.com/leesojunghub)|[@seunghee-han](https://github.com/seunghee-han)|
| Project Manager | Backend Engineer | Frontend Engineer | Backend Engineer | DevOps Engineer | DevOps Engineer |


</div>
<br/>
<br/>
<br/>

# 프로젝트 기간
2025년 9월 15일 ~ 9월 16일 (2일)
<br/>
<br/>
<br/>	

# 프로젝트 개요

## 기술 스택

| 항목    | 내용     |
| ---------- | ---------- |
| Language    | <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white"> <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> |
| Development    |<img src="https://img.shields.io/badge/Visual Studio Code-61DAFB?style=for-the-badge&logo=VisualStudioCode&logoColor=white"> |
| Deployment   | <img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white">   <img src="https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white">  <img src="https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=Gunicorn&logoColor=white"> <img src="https://img.shields.io/badge/amazonaws-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white"> |
| Embedding    | <img src="https://img.shields.io/badge/OpenAIEmbedding-181717?style=for-the-badge&logo=openai&logoColor=white">     |
| LLM Model    | <img src="https://img.shields.io/badge/chatgpt_4o-3776AB?style=for-the-badge&logo=openai&logoColor=white">      |
| Collaboration Tool    | <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"> <img src="https://img.shields.io/badge/Discord-02569B?style=for-the-badge&logo=Discord&logoColor=white">     |
|Framework|<img src="https://img.shields.io/badge/langchain-1C3C3C?style=for-the-badge&logo=openai&logoColor=white">  <img src="https://img.shields.io/badge/RAG-FFCA28?style=for-the-badge&logo=rag&logoColor=white"> <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">|
| Vector DB    |<img src="https://img.shields.io/badge/pgvector-00599C?style=for-the-badge&logo=pgvector&logoColor=white"> <img src="https://img.shields.io/badge/psycopg2-3776AB?style=for-the-badge&logo=psycopg2&logoColor=white"> <img src="https://img.shields.io/badge/FAISS-E34F26?style=for-the-badge&logo=faiss&logoColor=white">   |
| API    | <img src="https://img.shields.io/badge/OpenAI API-181717?style=for-the-badge&logo=openai&logoColor=white">    |
|Database | <img src="https://img.shields.io/badge/PostgreSQL-0769AD?style=for-the-badge&logo=postgresql&logoColor=white">  |




## 🗂️ 디렉토리 구조
```
Project
├── 📂insurance_chatbot/
│   ├── 📂chat/
│   │   ├── 📂migrations/
│   │   │   ├── 📂__pycache__/
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── rag.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── 📂insurance_chatbot/
│   │   ├── 📂__pycache__/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── 📂static/
│   │   ├── 📂css/
│   │   │   └── style.css
│   │   ├── 📂images/
│   │   │   └── logo.png
│   │   └── 📂js/
│   │   │   └── script.js
│   ├── 📂templates/chat
│   │   ├── login.html
│   │   ├── rag_view.html
│   │   └── singup.html
│   ├── db.sqlite3
│   └── manage.py
├── .gitignore
├── Dockerfile
├── docker-compose.yml
└── requirements.txt

```

## 🗂️ Requirements

| 구분              | 패키지                        | 버전/조건              | 설명                                   |
|-------------------|-------------------------------|------------------------|----------------------------------------|
| **Django & DB**   | Django                        | >=5.2,<6.0             | 웹 프레임워크                          |
|                   | psycopg2-binary               | >=2.9                  | PostgreSQL 연동 드라이버               |
| **REST API & 서버** | djangorestframework           | 최신                   | REST API 구축                          |
|                   | gunicorn                      | 최신                   | WSGI 서버                              |
|                   | whitenoise                    | 최신                   | 정적 파일 서빙                         |
| **AI / RAG**      | transformers                  | >=4.42.0               | 사전학습 모델 (HuggingFace)            |
|                   | torch                         | >=2.3.0                | 딥러닝 프레임워크 (PyTorch)            |
|                   | langchain                     | >=0.2.0                | RAG 파이프라인 구성 라이브러리         |
|                   | langchain-community           | >=0.2.0                | LangChain 커뮤니티 패키지              |
|                   | openai                        | >=1.35.0               | OpenAI API 연동                        |
|                   | tiktoken                      | 최신                   | 토큰화 라이브러리                      |
| **Vector DB**     | pgvector                      | 최신                   | PostgreSQL 벡터 확장                   |
| **Utils**         | python-dotenv                 | 최신                   | 환경변수(.env) 관리                    |
|                   | requests                      | 최신                   | HTTP 요청                              |
|                   | pandas                        | 최신                   | 데이터 처리                            |
|                   | numpy                         | 최신                   | 수치 계산                              |





## 🛠️ 아키텍쳐

RAG 파이프라인

<img width="850" height="701" alt="Image" src="https://github.com/user-attachments/assets/e7645226-f5a0-40ba-a927-7c080657d392" />

AWS

<img width="850" height="541" alt="Image" src="https://github.com/user-attachments/assets/8fda180f-b26c-4fc4-873d-6912fa8e1ced" />


## ⚙️ 주요 기능

### 💬 채팅 시스템

 * 간편 질문 : 나이, 성별, 차종, 운전 경력을 간단하게 입력 -> 빠른 보험 추천
   
 * 상세 질문 : 구체적 상황 질의 -> 약관 기반 답변 제공
   
 * 이력 관리 : 질문과 답변이 저장 -> 이전 대화 열람
   
### 📊 저장소 및 LLM

 * PDF 청킹 : 보험 약관 문서를 청크 단위로 분할

 * 임베딩 생성 : PostgreSQL(pgvector)에 저장

 * LLM 모델 답변 : 사용자의 질문을 LLM이 Prompt를 통해 답변

 * 외부 문서 : PDF 업로드 기능 지원

### 🔐 사용자 인증

 * 회원가입 : 문자,숫자,기호 기반 회원가입

 * 로그인 : 아이디/패스워드 기반 로그인

 * 세션 관리 : 로그인 상태 유지 및 로그아웃 기능

### ✅ 세션 관리

 * 세션 생성 : 간편/상세 채팅 세션 생성

 * 세션 관리 : 질문 내용에 따른 세션명 자동 설정

 * 세션 저장 : 세션 별로 대화 저장




## 🔄 동작 과정

### 0단계 : RAG 파이프라인

1. PDF 약관 문서 수집
2. 문서 전처리 (텍스트 추출 -> 불필요한 공백/특수문자 제거)
3. 문서 분할(청킹)
4. 임베딩 생성 (텍스트 -> 벡터 변환)
5. 벡터 DB에 저장 (PostgreSQL + pgvector) + 메타데이터 (보험사, 문서명)

### 1단계 : 사용자 질문 처리

1. 사용자가 웹 UI에 질문 입력
2. 입력 텍스트 전처리 및 벡터화
3. 벡터DB에서 관련 청크 검색 (앙상블 리트리버 적용)
4. 검색된 문맥(Context)을 LLM Prompt에 삽입

### 2단계 : 답변 생성

1. LLM이 컨텍스트 기반 답변 생성
2. 응답 후처리
3. DB에 저장

### 3단계 : 웹 서비스

1. 프론트엔드(UI)
   * 질문 입력창, 답변 출력 영역
   * 최근 대화 목록 (사이드바)
   * 간편 질문 / 상세 질문
2. 백엔드(Django)
   * 질문 처리 & RAG 호출
   * 사용자별 대화 기록 관리
   * 회원가입 / 로그인 가능
3. DB연동
   * PostgreSQL -> 약관 데이터 검색용, 유저 정보, 대화 기록 저장
4. 배포
   * Docker + docker-compose
   * Nginx + Gunicorn (웹 서버)
   * AWS EC2 (Ubuntu 24.04)




## 💻 구현 화면


* 메인화면
  
<img width="1900" height="1004" alt="Image" src="https://github.com/user-attachments/assets/f81634e8-36b6-4ca9-a7e8-a9188d3c810a" />

* 질문 답변(상세)

<img width="1900" height="1005" alt="Image" src="https://github.com/user-attachments/assets/4d72a7a8-e4d3-4e3c-a2cf-c5305fe931a0" />

* 정보 추천(간편)

<img width="1903" height="997" alt="Image" src="https://github.com/user-attachments/assets/29126778-b1c3-4e27-8860-e265e5452863" />













# 회고록

* 권도원 :

* 기현택 : 
  
* 유의정 : 
  
* 이소정 : 
  
* 이준원 :
  
* 한승희 : 


