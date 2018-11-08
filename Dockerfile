 FROM python:3.6
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /zad
 WORKDIR /zad
 ADD requirements.txt /zad/
 RUN pip install -r requirements.txt
 ADD . /zad/

 WORKDIR /zad/zad
