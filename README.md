# flask-celery-fs-sqlite
Example of using Celery with Filesystem Broker and SQLite3 to store back-end results

## Instructions
1. pip install -r requirements.txt in your virtual environment
2. Launch flask on one terminal
  ```
  python wsgi_app.py 
  ```
3. Launch celery on another terminal
```
celery --app wsgi_app.celery worker --loglevel=info --pool=solo
```

## Task Submission
![Task Submission](https://quantmill.s3.eu-west-2.amazonaws.com/github/celery-sqlite.png)

## Database Results
![Celery Results](https://quantmill.s3.eu-west-2.amazonaws.com/github/celery-results.PNG)


