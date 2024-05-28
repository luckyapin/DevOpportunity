from celery import Celery
import requests
celery = Celery('tasks', broker='redis://localhost:6379')

@celery.task
def upload_vacancy():
    return None
