FROM python:3.9-slim

# تثبيت الملحقات الضرورية للنظام
RUN apt-get update && apt-get install -y \
    libgstreamer1.0-dev \
    libgstreamer-plugins-base1.0-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir flet

# أمر التشغيل المعدل لبيئة الريندر
CMD ["flet", "run", "--web", "--port", "8080", "main.py"]

