FROM python:3.12-alpine
WORKDIR /app
COPY . . 
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["uvicorn", "app.app:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]