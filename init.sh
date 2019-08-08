#!/bin/sh
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/wsgi_hello.conf /etc/gunicorn.d/wsgi-test
sudo ln -sf /home/box/web/etc/wsgi_django.conf /etc/gunicorn.d/wsgi-django
sudo /etc/init.d/gunicorn restart
