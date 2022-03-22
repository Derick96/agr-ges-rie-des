FROM quay.io/basisai/python-alpine-grpcio
# set work directory
RUN apk add gcc g++ linux-headers
RUN apk add --update alpine-sdk
RUN apk add postgresql-dev
WORKDIR /usr/src/app

RUN apk add --update py3-pip
RUN apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev && \
    apk add --no-cache --update python3 && \
    pip3 install --upgrade pip setuptools
RUN pip3 install pendulum service_identity

# set environment variables
ENV PYTHON_PIP_VERSION=20.1
ENV PYTHONDONTWRITEBYTECODE 1
ENV GRPC_PYTHON_DISABLE_LIBC_COMPATIBILITY=1
ENV PYTHONUNBUFFERED 1


# install dependencies
COPY ./requirements.txt /usr/src/app
RUN pip3 install -r requirements.txt

# copy project
COPY . /usr/src/app

EXPOSE 8001

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]