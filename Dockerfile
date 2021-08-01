FROM python:3.7

WORKDIR /app

ADD . /app

RUN cd /app && \

    pip install -r requirements.txt

CMD python3 sax.py

