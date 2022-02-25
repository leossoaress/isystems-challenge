FROM python:3.8

WORKDIR /app

COPY ./app ./app
COPY run.py run.py
COPY requirements.txt requirements.txt

RUN apt-get update
RUN pip install -r requirements.txt

CMD ["python3", "run.py"]