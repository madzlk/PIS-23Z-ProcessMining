FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

COPY ./main.py /app/main.py

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app/backend

EXPOSE 8080

CMD ["bash", "-c", "uvicorn main:app --host 0.0.0.0 --port 8080 --reload"]
