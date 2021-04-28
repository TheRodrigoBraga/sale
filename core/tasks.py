from celery import shared_task
from core import models


@shared_task(bind=True, quere='default')
def process_long_task(self, loop_number: int):
    for item in range(0, loop_number):
        print(f'index: {item}')
