from celery import Celery
from celery.schedules import crontab
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

app = Celery('api')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
