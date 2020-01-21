from celery import Celery

# celery instance
app = Celery()


@app.task
def add(x, y):
    return x + y
