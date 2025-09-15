
# <img width="50" height="50" alt="logo" src="https://github.com/user-attachments/assets/59ca02dd-bc0e-4019-869a-1f7aa44a0e80" />운전자 보험 약관 RAG 챗봇!


# 팀 소개


| 이준원    | 권도원    | 기현택       | 유의정     | 이소정  | 한승희    |
|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|
|[@none-jun](https://github.com/none-jun)|[@dowonk120](https://github.com/dowonk120)|[@mathplanet](https://github.com/mathplanet)|[@ryu0ej](https://github.com/Rr-EJ)|[@leesojunghub](https://github.com/leesojunghub)|[@seunghee-han](https://github.com/seunghee-han)|
| Project Manager | Backend Engineer | Frontend Engineer | AI Engineer | DevOps Engineer | Cloud Infrastructure Engineer |


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
| Development    | <img src="https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white"> <img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white">  <img src="https://img.shields.io/badge/Visual Studio Code-61DAFB?style=for-the-badge&logo=VisualStudioCode&logoColor=white"> <img src="https://img.shields.io/badge/amazonaws-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white"> |
| Embedding    | <img src="https://img.shields.io/badge/OpenAIEmbedding-181717?style=for-the-badge&logo=openai&logoColor=white">     |
| LLM Model    | <img src="https://img.shields.io/badge/chatgpt_4.1-3776AB?style=for-the-badge&logo=openai&logoColor=white">      |
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

## 🛠️ 아키텍쳐

RAG 파이프라인

<img width="850" height="701" alt="Image" src="https://github.com/user-attachments/assets/e7645226-f5a0-40ba-a927-7c080657d392" />

AWS

<img width="850" height="541" alt="Image" src="https://github.com/user-attachments/assets/8fda180f-b26c-4fc4-873d-6912fa8e1ced" />


## ⚙️ 주요 기능

### 💬 채팅 시스템

 * 간편 질문 : 나이, 성별, 차종, 운전 경력을 간단하게 입력하여 빠른 운전자 보험을 추천 받음
   
 * 상세 질문 : 자세한 질문을 통하여 상황에 알맞은 답변을 받을 수 있음
   
 * 이력 관리 : 질문과 답변이 저장되어 이전 대화 열람 가능
   
### 📊 저장소 맟 LLM

 * PDF 청킹 : 보험 약관 문서를 청크 단위로 분할

 * 임베딩 생성 : 청크를 벡터로 변환하여 DB에 저장

 * LLM 모델 답변 : 사용자의 질문을 LLM이 Prompt를 통해 답변

 * 외부 문서 : PDF 업로드를 통한 추가 가능

### 🔐 사용자 인증

 * 회원가입

 * 로그인

 * 세션 관리

 

### ✅ 세션 관리

 * 세션 생성

 * 세션 관리

 * 세션 저장




## 🔄 동작 과정






## 💻 구현 화면
















# 회고록

* 권도원 :

* 기현택 : 
  
* 유의정 : 
  
* 이소정 : 
  
* 이준원 :
  
* 한승희 : 


