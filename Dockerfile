FROM python:3.11.13-alpine3.22

ARG container_user=openg2p
ARG container_user_group=openg2p
ARG container_user_uid=1001
ARG container_user_gid=1001

RUN apk add --no-cache --virtual .build-deps gcc libc-dev linux-headers make
RUN apk add --no-cache bash git gettext libpq-dev postgresql16-client

RUN addgroup -g ${container_user_gid} ${container_user_group} \
  && adduser -D -u ${container_user_uid} -G ${container_user_group} -s /bin/bash ${container_user}

WORKDIR /app

ADD openg2p-spar-mapper-interface-lib /app/openg2p-spar-mapper-interface-lib
ADD openg2p-spar-self-service-api /app/openg2p-spar-self-service-api
ADD openg2p-spar-g2pconnect-mapper-connector-lib /app/openg2p-spar-g2pconnect-mapper-connector-lib
ADD db_scripts /app/db_scripts
ADD main.py /app/main.py

RUN pip install git+https://github.com/openg2p/openg2p-fastapi-common@1.1\#subdirectory=openg2p-fastapi-common  # to_be_removed_on_tag
RUN pip install git+https://github.com/openg2p/openg2p-fastapi-common@1.1\#subdirectory=openg2p-fastapi-auth  # to_be_removed_on_tag
RUN pip install git+https://github.com/openg2p/openg2p-g2pconnect-common-lib@1.1\#subdirectory=openg2p-g2pconnect-common-lib # to_be_removed_on_tag
RUN pip install git+https://github.com/openg2p/openg2p-g2pconnect-common-lib@1.1\#subdirectory=openg2p-g2pconnect-mapper-lib # to_be_removed_on_tag
RUN pip install \
  -e /app/openg2p-spar-mapper-interface-lib \
  -e /app/openg2p-spar-self-service-api \
  -e /app/openg2p-spar-g2pconnect-mapper-connector-lib

RUN apk del --no-network .build-deps

USER ${container_user}

ENV PYTHONUNBUFFERED=1
ENV SPAR_SELFSERVICE_NO_OF_WORKERS=1
ENV SPAR_SELFSERVICE_HOST=0.0.0.0
ENV SPAR_SELFSERVICE_PORT=8000
ENV SPAR_SELFSERVICE_WORKER_TYPE=gunicorn

CMD python3 main.py migrate; \
    gunicorn "main:app" --workers ${SPAR_SELFSERVICE_NO_OF_WORKERS} --worker-class uvicorn.workers.UvicornWorker --bind ${SPAR_SELFSERVICE_HOST}:${SPAR_SELFSERVICE_PORT}
