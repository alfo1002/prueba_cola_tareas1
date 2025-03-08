redis:

sudo service redis-server start

systemctl status redis-server
sudo nano /etc/redis/redis.conf
*******************
# Require a password to access Redis
requirepass mi_contraseña

# Specify the user that can access Redis with the password
masterauth mi_contraseña
*******************

redis-cli
AUTH 123456789

django:

pip install celery redis

pip install celery redis django-celery-beat django-celery-results

pip install flower

comandos:
=========

celery -A prueba_cola_tareas1 beat --loglevel=info

celery -A prueba_cola_tareas1 flower
http://0.0.0.0:5555

celery -A prueba_cola_tareas1 worker --loglevel=info --pool=solo
