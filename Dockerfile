FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Shell form so $PORT is expanded at runtime.
CMD uvicorn main:app --host 0.0.0.0 --port $PORT
