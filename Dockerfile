FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir flet
EXPOSE 8080
CMD ["flet", "run", "--web", "--port", "8080", "main.py"]
