FROM python:3.9-slim

WORKDIR /app

COPY requisitos.txt .

RUN pip install -r requisitos.txt

COPY . .

CMD ["python", "app.py"]
