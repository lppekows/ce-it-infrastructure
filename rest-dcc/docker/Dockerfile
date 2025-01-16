FROM nginx:1.27.3

ARG PERL_TEST_OPTION="--notest"
ARG MARIADB_ROOT_PASSWORD=changeme
ARG MARIADB_DATABASE=dcc_docdb
ARG MARIADB_USER=docdbrw
ARG MARIADB_PASSWORD
ARG MARIADB_USER2=docdbro
ARG MARIADB_PASSWORD2
ARG FQDN

ENV DEBIAN_FRONTEND=noninteractive

ENV MARIADB_ROOT_PASSWORD=${MARIADB_ROOT_PASSWORD}
ENV MARIADB_DATABASE=${MARIADB_DATABASE}
ENV MARIADB_USER=${MARIADB_USER}
ENV MARIADB_PASSWORD=${MARIADB_PASSWORD}
ENV MARIADB_USER2=${MARIADB_USER2}
ENV MARIADB_PASSWORD2=${MARIADB_PASSWORD2}
ENV FQDN=${FQDN}

RUN apt update && apt upgrade -y && \
    apt install -y build-essential wget less vim

COPY ../RESTServer.py /root
COPY nginx.conf /etc/nginx

RUN mkdir /opt/restdcc && \
    cd /opt/restdcc && \
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/restdcc/miniconda3 && \
    eval "$(/opt/restdcc/miniconda3/bin/conda shell.bash hook)" && \
    conda create --name dcc conda-forge:mariadb conda-forge::mysqlclient conda-forge::mysql-client=8.4.2
