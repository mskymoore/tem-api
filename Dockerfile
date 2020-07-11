FROM python:3.8
ENV PYTHONUNBUFFERED=1
RUN mkdir /opt/tem-api
WORKDIR /opt/tem-api
COPY ./requirements.txt /opt/tem-api/requirements.txt
RUN pip install -r ./requirements.txt
