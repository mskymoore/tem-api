from celery import shared_task
from celery.signals import worker_ready

@shared_task
def do_data_update():
   pass 


@worker_ready.connect
def update_data(sender=None, conf=None, **kwargs):
    do_data_update()