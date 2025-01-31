FROM bitnami/python:3.10.13-debian-11-r24

ARG container_user=openg2p
ARG container_user_group=openg2p
ARG container_user_uid=1001
ARG container_user_gid=1001

RUN groupadd -g ${container_user_gid} ${container_user_group} \
  && useradd -mN -u ${container_user_uid} -G ${container_user_group} -s /bin/bash ${container_user}

WORKDIR /app

RUN install_packages nginx libpq-dev wkhtmltopdf \
  && apt-get clean && rm -rf /var/lib/apt/lists /var/cache/apt/archives

RUN python3 -m pip install git+https://github.com/openg2p/openg2p-fastapi-common@develop#subdirectory=openg2p-fastapi-common

RUN chown -R ${container_user}:${container_user_group} /app
USER ${container_user}

ADD --chown=${container_user}:${container_user_group} . /app/src
ADD --chown=${container_user}:${container_user_group} main.py /app

RUN python3 -m pip install -e ./src

ENTRYPOINT [ "bash" ]
CMD ["-c" , "nginx -g 'daemon off;' &; exec python3 main.py run"]
