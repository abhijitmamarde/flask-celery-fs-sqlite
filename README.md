# flask-celery-filesystem
Example of using Celery with Filesystem Broker

## Instructions
1. pip install -r requirements.txt in your virtual environment
2. Launch flask on one terminal
  ```
  python wsgi_app.py 
  ```
3. Launch celery on another terminal
```
celery worker -A wsgi_app.celery --loglevel=info --pool=solo
```

## Task Execution Example
![Task](https://quantmill.s3.eu-west-2.amazonaws.com/github/task-flask-celery.PNG)

## Terminals
![Terminal](https://quantmill.s3.eu-west-2.amazonaws.com/github/cmder-flask-celery.PNG)
