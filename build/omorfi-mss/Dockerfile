FROM cscmss/omorfi

MAINTAINER Olli Tourunen <tourunen@csc.fi>

RUN dnf install -y python3-flask nss_wrapper gettext && dnf clean all

EXPOSE 5000

ENV PYTHONPATH=/usr/local/lib/python3.5/site-packages

COPY src/python/app.py /app.py
COPY src/bash/start.sh /start.sh
COPY src/templates/passwd.template /passwd.template

ENTRYPOINT bash /start.sh
