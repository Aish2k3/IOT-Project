FROM python:alpine
WORKDIR /app


COPY . /app/
COPY requirements.txt /app/

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "main.py"]