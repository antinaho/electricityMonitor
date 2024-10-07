FROM python:3.12

WORKDIR /app

COPY ./images/requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

CMD python main.py