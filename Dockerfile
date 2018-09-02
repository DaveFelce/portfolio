FROM python:3.5

# Nginx section
ENV NGINX_VERSION 1.11.10-1~jessie

RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \
    && echo "deb http://nginx.org/packages/mainline/debian/ stretch nginx" >> /etc/apt/sources.list \
    && apt-get update \
    && apt-get install --no-install-recommends --no-install-suggests -y \
                        ca-certificates \
                        nginx \
                        nginx-module-xslt \
                        nginx-module-geoip \
                        nginx-module-image-filter \
                        nginx-module-njs \
                        gettext-base \
                        curl \
                        supervisor \
    && rm -rf /var/lib/apt/lists/*

RUN rm -f /etc/nginx/conf.d/default.conf
COPY ./configs/nginx/conf.d/default.conf /etc/nginx/conf.d/

# Django section
ENV PYTHONBUFFERED 1
ENV APPLICATION_ROOT /webapp/
RUN ls -la /
RUN mkdir -p $APPLICATION_ROOT
WORKDIR $APPLICATION_ROOT
COPY requirements.txt $APPLICATION_ROOT
RUN pip install -r requirements.txt

# Add site
ADD . $APPLICATION_ROOT
RUN chown -R www-data $APPLICATION_ROOT

COPY ./configs/supervisor/supervisord.conf /etc/supervisor/conf.d/
RUN chown www-data db.sqlite3
RUN chown -R www-data media
RUN mkdir /shared
RUN chmod 777 /shared

# Expose ports for nginx
EXPOSE 8082 443

# Run
CMD [ "/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf" ]
