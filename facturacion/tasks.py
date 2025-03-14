from celery import shared_task
from prueba_cola_tareas1.celery import app
import time
from rest_framework.response import Response

""" @shared_task
def scheduled_task():
    print("Tarea Programada ejecutada a la hora programada!") """
     
@app.task
def add(n):
    time.sleep(10)
    print("Sumando................................")
    return 5