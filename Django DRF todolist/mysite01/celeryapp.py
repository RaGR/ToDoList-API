import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite01.settings')

app = Celery('mysite01')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()