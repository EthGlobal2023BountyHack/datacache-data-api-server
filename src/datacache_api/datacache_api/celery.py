import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "datacache_api.settings")
app = Celery("datacache_api")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()