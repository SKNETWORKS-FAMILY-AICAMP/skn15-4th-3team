# Python 3.12 slim 이미지 사용
FROM python:3.12-slim

# 작업 디렉토리 설정
WORKDIR /app

# 기본 패키지 설치 (psycopg2, torch 빌드에 필요)
RUN apt-get update && apt-get install -y \
    nginx \
    gcc \
    g++ \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# requirements.txt 복사 및 설치
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# 소스코드 복사
COPY . .

# Django 실행 (개발용) — 운영에서는 gunicorn + nginx 권장
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
