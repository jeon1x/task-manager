FROM python:3.12.7-slim
WORKDIR /app
COPY . .
CMD ["python", "task_app.py"]