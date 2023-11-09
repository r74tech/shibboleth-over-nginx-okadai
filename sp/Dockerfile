FROM pennlabs/shibboleth-sp-nginx:latest

ENV APP_HOME=/usr/src/sp

RUN groupadd -r shibd && useradd -r -g shibd shibd

RUN mkdir -p $APP_HOME 

WORKDIR $APP_HOME 

COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf

# 必要な証明書をコピー
COPY ./certs/devgenec.okayama-u.ac.jp.pem /etc/nginx/cert.pem
COPY ./certs/devgenec.okayama-u.ac.jp-key.pem /etc/nginx/key.pem

COPY ./shibboleth/server-cert.pem /etc/shibboleth/cert/server.crt
COPY ./shibboleth/server-key.pem /etc/shibboleth/cert/server.key

RUN chown shibd:shibd /etc/shibboleth/cert/server.crt
RUN chown shibd:shibd /etc/shibboleth/cert/server.key

RUN chmod 440 /etc/shibboleth/cert/server.crt
RUN chmod 440 /etc/shibboleth/cert/server.key

COPY ./shibboleth/ /etc/shibboleth/