import os
from celery.schedules import crontab  # Importa crontab aquí
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prueba_cola_tareas1.settings')

app = Celery('prueba_cola_tareas1')
app.config_from_object('django.conf:settings', namespace='CELERY')


""" # Configuración de tareas periódicas (Beat Schedule)
app.conf.beat_schedule = {
    'task-every-30-min': {
        'task': 'facturacion.tasks.scheduled_task',  # Asegúrate de que la ruta sea correcta
        'schedule': crontab(minute='*/1'),  # Ejecutar cada 1 minutos
        'args': ()  # Si tu tarea requiere argumentos, los defines aquí
    },
    # Puedes agregar más tareas programadas aquí
} """

app.autodiscover_tasks()