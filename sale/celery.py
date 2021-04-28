from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab
from kombu import Queue, Exchange

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sale.settings')

app = Celery('sale')
app.conf.task_queues = (
    Queue('default', Exchange('default'), routing_key='default', delivery_mode=1),
)

app.conf.beat_schedule = {
    # 'pull_all_data_fox_manager': {
    #     'task': 'core.tasks.pull_all_data_fox_manager',
    #     'schedule': crontab(hour=5, minute=0)
    # },
}

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
