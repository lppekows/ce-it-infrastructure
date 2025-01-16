FROM debian:bookworm-slim as base

ARG FQDN

ENV FQDN=${FQDN} 

SHELL ["/bin/bash", "-l", "-c"]

RUN apt update && apt upgrade -y &&\
    apt install -y python3 python3-venv libaugeas0 cron


RUN python3 -m venv /opt/certbot/  &&\
    /opt/certbot/bin/pip install --upgrade pip

RUN /opt/certbot/bin/pip install certbot certbot-apache

#RUN certbot certonly --apache

# https://stackoverflow.com/questions/37458287/how-to-run-a-cron-job-inside-a-docker-container
RUN echo "0 0,12 * * * root /opt/certbot/bin/python -c 'import random; import time; time.sleep(random.random() * 3600)' && sudo certbot renew -q" > /etc/cron.d/certbot
RUN chmod 0644 /etc/cron.d/certbot
# RUN crontab /etc/cron.d/certbot

RUN touch /var/log/cron.log
CMD cron && tail -f /var/log/cron.log

