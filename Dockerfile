# 1. Eng avval bizga toza va yengil Python 3.10 kompyuteri (muhiti) kerak
FROM python:3.12.3-slim

# 2. Docker qutisi ichida o'zimiz ishlaydigan papka ochamiz (nomi /app bo'ladi)
WORKDIR /app


COPY requirements.txt .

# 4. Quti ichida turib, o'sha kutubxonalarni o'rnatamiz
RUN pip install --no-cache-dir -r requirements.txt

# 5. Endi o'zimizning kodimiz (main.py) va ML modelimizni (bank_marketing.pkl) qutiga o'tkazamiz
COPY . .

# 6. Quti ishga tushganda FastAPI qanday komanda bilan yonishini aytamiz
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]