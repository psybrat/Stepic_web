#!/bin/sh
sudo rm /etc/nginx/sites-available/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo rm -r /etc/gunicorn.d/*
sudo ln -sf /home/box/web/etc/wsgi_hello.conf /etc/gunicorn.d/wsgi_hello.conf
sudo ln -sf /home/box/web/etc/wsgi_django.conf /etc/gunicorn.d/wsgi_django.conf
sudo /etc/init.d/gunicorn restart
