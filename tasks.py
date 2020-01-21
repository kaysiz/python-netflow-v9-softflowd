from celery import Celery

# celery instance
app = Celery('tasks', backend='amqp', broker='amqp://admin')


@app.task
def add(x, y):
    return x + y


@app.task
def analyse_json(file):
