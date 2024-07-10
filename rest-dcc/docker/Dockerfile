FROM debian:bookworm-slim AS base

ARG PERL_TEST_OPTION="--notest"
ARG MARIADB_ROOT_PASSWORD=changeme
ARG MARIADB_DATABASE=dcc_docdb
ARG MARIADB_USER=docdbrw
ARG MARIADB_PASSWORD
ARG MARIADB_USER2=docdbro
ARG MARIADB_PASSWORD2
ARG FQDN

ENV DOCDB_BASE=/usr1/www
ENV DOCDB_CGI_DIR=${DOCDB_BASE}/cgi-bin
ENV DOCDB_HTML_DIR=${DOCDB_BASE}/html
ENV DEBIAN_FRONTEND=noninteractive
ENV PERL5LIB=/usr1/www/cgi-bin/private/DocDB

ENV MARIADB_ROOT_PASSWORD=${MARIADB_ROOT_PASSWORD}
ENV MARIADB_DATABASE=${MARIADB_DATABASE}
ENV MARIADB_USER=${MARIADB_USER}
ENV MARIADB_PASSWORD=${MARIADB_PASSWORD}
ENV MARIADB_USER2=${MARIADB_USER2}
ENV MARIADB_PASSWORD2=${MARIADB_PASSWORD2}
ENV FQDN=${FQDN}

SHELL ["/bin/bash", "-l", "-c"]

RUN apt update && apt upgrade -y &&\
    apt install -y supervisor build-essential \
                   nginx vim curl wget


# TODO: installs should come from a requirements.txt

RUN mkdir -p /opt/rest-dcc &&\
    cd /opt &&\
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh &&\
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda3 &&\
    /opt/miniconda3/bin/conda init &&\
    eval "$(/opt/miniconda3/bin/conda shell.bash hook)" &&\
    /opt/miniconda3/bin/conda create --name dcc conda-forge::sqlalchemy conda-forge::sqlacodegen conda-forge::fastapi conda-forge:mariadb conda-forge::mysqlclient conda-forge::uvicorn


COPY tables.py /opt/rest-dcc
COPY main.py /opt/rest-dcc

COPY ${FQDN}.crt /etc/nginx/certs/${FQDN}.crt
COPY ${FQDN}.key /etc/nginx/certs/${FQDN}.key
COPY docker/nginx-default /etc/nginx/sites-enabled/default
RUN sed -i "s/FQDN/${FQDN}/g" /etc/nginx/sites-enabled/default

COPY docker/supervisord.conf /etc/supervisord.conf
CMD [ "/usr/bin/supervisord" ]
