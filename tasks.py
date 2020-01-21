from celery import Celery
from analyzer import *

# celery instance
app = Celery('tasks', broker='redis://localhost:6379/0')


@app.task
def analyse(file):
    packet_analysis(file)
