from celery import Celery
from celery.schedules import crontab



app = Celery('tasks',broker='redis://localhost:6379/4')


@app.on_after_configure.connect
def setup_periodic_tasks(sender,**kwargs):
    sender.add_periodic_task(
        crontab(),get.s
    )


@app.task
def get():
    print('执行了一次')