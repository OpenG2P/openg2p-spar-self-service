FROM bitnami/python:3.10.13-debian-11-r24

ARG container_user=openg2p
ARG container_user_group=openg2p
ARG container_user_uid=1001
ARG container_user_gid=1001

RUN groupadd -g ${container_user_gid} ${container_user_group} \
  && useradd -mN -u ${container_user_uid} -G ${container_user_group} -s /bin/bash ${container_user}

RUN install_packages gettext libpq-dev \
  && apt-get clean && rm -rf /var/lib/apt/lists /var/cache/apt/archives

WORKDIR /app

ADD openg2p-spar-mapper-interface-lib /app/openg2p-spar-mapper-interface-lib
ADD openg2p-spar-self-service-api /app/openg2p-spar-self-service-api
ADD openg2p-spar-g2pconnect-mapper-connector-lib /app/openg2p-spar-g2pconnect-mapper-connector-lib
ADD db_scripts /app/db_scripts
ADD main.py /app/main.py

RUN python3 -m pip install git+https://github.com/openg2p/openg2p-fastapi-common@1.1\#subdirectory=openg2p-fastapi-common  # to_be_removed_on_tag
RUN python3 -m pip install git+https://github.com/openg2p/openg2p-fastapi-common@1.1\#subdirectory=openg2p-fastapi-auth  # to_be_removed_on_tag
RUN python3 -m pip install git+https://github.com/openg2p/openg2p-g2pconnect-common-lib@1.1\#subdirectory=openg2p-g2pconnect-common-lib # to_be_removed_on_tag
RUN python3 -m pip install git+https://github.com/openg2p/openg2p-g2pconnect-common-lib@1.1\#subdirectory=openg2p-g2pconnect-mapper-lib # to_be_removed_on_tag
RUN python3 -m pip install \
  /app/openg2p-spar-mapper-interface-lib \
  /app/openg2p-spar-self-service-api \
  /app/openg2p-spar-g2pconnect-mapper-connector-lib

USER ${container_user}

ENV SPAR_SELFSERVICE_NO_OF_WORKERS=1
ENV SPAR_SELFSERVICE_HOST=0.0.0.0
ENV SPAR_SELFSERVICE_PORT=8000
ENV SPAR_SELFSERVICE_WORKER_TYPE=gunicorn

CMD python3 main.py migrate; \
    gunicorn "main:app" --workers ${SPAR_SELFSERVICE_NO_OF_WORKERS} --worker-class uvicorn.workers.UvicornWorker --bind ${SPAR_SELFSERVICE_HOST}:${SPAR_SELFSERVICE_PORT}
