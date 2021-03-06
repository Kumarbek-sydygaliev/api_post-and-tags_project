import os
from celery import Celery
from django.conf import settings


if not ("DJANGO_SETTINGS_MODULE" in os.environ):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_example.settings')

app = Celery('first_api')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.task_always_eager = False

@app.task(bind = True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
