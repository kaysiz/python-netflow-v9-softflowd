from celery import Celery

# celery instance
app = Celery('tasks', broker='redis://localhost:6379/0')


@app.task
def add(x, y):
    return x + y
