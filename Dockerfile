FROM alpine

LABEL author="Gabriel Martins Andrade <gabrielandrade21@hotmail.com>" \
      version="1.0"

ADD ./main.py /root/main.py

RUN apk update --no-cache && \
    apk upgrade --no-cache && \
    apk add --no-cache python3 python3-dev && \
    adduser -S worker && \
    mkdir -p /worker/apps/ && \
    mv /root/main.py /worker/apps/main.py && \
    chown -R worker. /worker/apps/ && \
    pip3 install --upgrade pip && \
    pip3 install requests

USER worker
ENTRYPOINT [ "/worker/apps/main.py" ]