from celery import Celery

app = Celery('tasks', broker='amqp://localhost', backend='rpc://localhost')

@app.task
def add(x, y):
    return x + y