FROM python:3.10.4-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /store

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY /goods/fixtures/initial_data.json /main/app/fixtures/initial_data.json
   

   

   
