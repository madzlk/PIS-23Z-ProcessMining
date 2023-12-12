FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app/backend

WORKDIR /app/backend

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8080

CMD ["bash", "-c", "uvicorn main:app --host 0.0.0.0 --port 8080 --reload"]
