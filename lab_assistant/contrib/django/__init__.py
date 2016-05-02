from django.conf import settings
from lab_assistant import conf


storage_backend = getattr(settings, 'LABORATORY_BACKEND', None)
if storage_backend:
    conf.storage = storage_backend
