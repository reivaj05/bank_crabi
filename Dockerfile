FROM python:alpine

ADD . /bank_crabi
WORKDIR /bank_crabi

RUN apk -U add gcc g++ make bash git python-dev libxml2-dev libxslt-dev libffi-dev linux-headers postgresql-dev
RUN make
RUN apk del make libxml2-dev libffi-dev openssl-dev linux-headers

ENTRYPOINT ./scripts/start.sh