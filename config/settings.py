# DEV settings.py
import os
from pathlib import Path

DEBUG = True

# Secret key
SECRET_KEY = os.urandom(24)

# Database Path
DB_PATH = os.path.join(Path(__file__).parent.parent, 'database.sqlite3')

# Celery config
CELERY_RESULT_BACKEND = f"db+sqlite:///{DB_PATH}"
# CELERY_BROKER_URL = 'redis://localhost:6379'
