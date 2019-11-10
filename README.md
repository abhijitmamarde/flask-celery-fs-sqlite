# flask-celery-fs-sqlite
Example of using Celery with Filesystem Broker and SQLite3 to store back-end results

## Instructions
1. pip install -r requirements.txt in your virtual environment
2. If using a windows os
  ```
   pip install pywin32==223 
  ``` 
3. Launch flask on one terminal
  ```
  python wsgi_app.py 
  ```
4. Launch celery on another terminal
```
celery worker -A wsgi_app.celery --loglevel=info --pool=solo
```

## Task Submission
![Task Submission](https://quantmill.s3.eu-west-2.amazonaws.com/github/celery-sqlite.png)

## Database Results
![Celery Results](https://quantmill.s3.eu-west-2.amazonaws.com/github/celery-results.PNG)


