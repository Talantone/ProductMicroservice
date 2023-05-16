FROM postgres
ENV POSTGRES_USER root
ENV POSTGRES_PASSWORD qwerty
ENV POSTGRES_DB product_db
COPY product_db.sql /docker-entrypoint-initdb.d/