FROM python:3.10-slim

WORKDIR /app

COPY . /app
COPY requeriments.txt .

RUN apt-get update \
    && apt-get install

EXPOSE 8000

RUN pip install -r requeriments.txt

CMD ["python", "-m", "uvicorn", "src.app:main_app", "--port=8000", "--host", "0.0.0.0", "--reload"]
