FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY ./ ./
COPY wait_for_postgres.sh ./
RUN chmod +x wait_for_postgres.sh
RUN pip3 install -r requirements.txt
RUN apt-get update
RUN apt-get -y install postgresql-client
