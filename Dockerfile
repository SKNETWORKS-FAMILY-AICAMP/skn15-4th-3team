# Python 런타임
FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 앱 루트
WORKDIR /app

# 빌드 도구 (psycopg2 빌드 등)
RUN apt-get update && apt-get install -y \
    libpq-dev build-essential \
    && rm -rf /var/lib/apt/lists/*

# 파이썬 의존성
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 복사
COPY . .

# 비루트 유저 & 권한
RUN useradd -m appuser && \
    mkdir -p /app/insurance_chatbot/staticfiles && \
    chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

# 정적파일 수집 후 gunicorn 실행
# manage.py는 /app/insurance_chatbot/manage.py 에 있으므로 절대경로 유지
CMD sh -c "python insurance_chatbot/manage.py collectstatic --noinput && \
           gunicorn insurance_chatbot.wsgi:application \
           --bind 0.0.0.0:8000 --workers 1 --threads 2 --timeout 60 \
           --access-logfile - --error-logfile -"
