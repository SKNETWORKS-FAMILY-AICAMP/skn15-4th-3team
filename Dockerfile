# Python 공식 이미지 기반
FROM python:3.11-slim

# 컨테이너 안 작업 경로
WORKDIR /app

# 필수 패키지 (Postgres 쓰려면 libpq-dev 필요)
RUN apt-get update && apt-get install -y build-essential libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# Django와 gunicorn 설치
RUN pip install --no-cache-dir django gunicorn

# 프로젝트 코드 복사 (지금은 비어있어도 됨)
COPY . /app

# 서버 실행 명령
CMD ["gunicorn", "insurance_chatbot.wsgi:application", "-b", "0.0.0.0:8000"]