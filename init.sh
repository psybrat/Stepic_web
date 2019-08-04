sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/wsgi.conf /etc/gunicorn.d/wsgi-test
sudo /etc/init.d/gunicorn restart