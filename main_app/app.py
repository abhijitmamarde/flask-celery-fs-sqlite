from flask import Flask
from main_app.blueprints.pages.views import page
from celery import Celery
from main_app.celery_task_registry import CELERY_TASK_LIST
import os


# Extensions
from main_app.extensions import db

def make_celery(app=None):
    """
    Make Celery App
    :param app: flask app instance
    :return: celery
    """

    broker_url = os.getenv('CELERY_BROKER_URL', 'filesystem://')
    broker_dir = os.getenv('CELERY_BROKER_FOLDER', './broker')

    for f in ['out', 'processed']:
        if not os.path.exists(os.path.join(broker_dir, f)):
            os.makedirs(os.path.join(broker_dir, f))

    celery = Celery(app.import_name,
                    broker=broker_url,
                    backend=f"db+{app.config['SQL_ALCHEMY_DATABASE_URI']}")

    celery.conf.update({
        'broker_url': broker_url,
        'broker_transport_options': {
            'data_folder_in': os.path.join(broker_dir, 'out'),
            'data_folder_out': os.path.join(broker_dir, 'out'),
            'data_folder_processed': os.path.join(broker_dir, 'processed')
        },
        'timezone': 'utc',
        'imports': CELERY_TASK_LIST,
        'result_persistent': False,
        'task_serializer': 'json',
        'result_serializer': 'json',
        'accept_content': ['json']})

    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask

    return celery


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    if settings_override:
        app.config.update(settings_override)

    app.register_blueprint(page)

    return app


def extensions(app):
    """
    Register 0 or more extensions (mutates app instance passed in)
    :param app: flask app
    :return: None
    """
    db.init_app(app)

    return None

flask_app = create_app()
celery_app = make_celery(flask_app)
