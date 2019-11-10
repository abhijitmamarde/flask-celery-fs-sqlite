# DEV settings.py
import os

DEBUG = True

# Secret key
SECRET_KEY = os.urandom(24)

# Celery config
# CELERY_RESULT_BACKEND = 'redis://localhost:6379'
# CELERY_BROKER_URL = 'redis://localhost:6379'
