FROM ubuntu:22.04

ENV DEBIAN_FRONTEND noninteractive

ADD https://bootstrap.pypa.io/get-pip.py /tmp/get-pip.py
ADD . /opt/fastapi-openai

RUN set -e \
      && ln -sf bash /bin/sh \
      && ln -s python3 /usr/bin/python

RUN set -e \
      && apt-get -y update \
      && apt-get -y dist-upgrade \
      && apt-get -y install --no-install-recommends --no-install-suggests \
        ca-certificates curl locales python3-dev python3-distutils \
      && apt-get -y autoremove \
      && apt-get clean \
      && rm -rf /var/lib/apt/lists/*

RUN set -e \
      && locale-gen en_US.UTF-8 \
      && update-locale

RUN set -e \
      && /usr/bin/python3 /tmp/get-pip.py install -U --no-cache-dir pip \
      && /usr/local/bin/pip install -U --no-cache-dir \
        -r /opt/fastapi-openai/requirements.txt

EXPOSE 8000

WORKDIR /opt/fastapi-openai

ENTRYPOINT ["/usr/local/bin/uvicorn"]
CMD ["app.main:app", "--host=0.0.0.0", "--port=8000", "--reload"]
