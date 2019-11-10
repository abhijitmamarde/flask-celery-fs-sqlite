from flask import current_app as app
from flask import (Blueprint,
                   render_template,
                   request,
                   jsonify)

import sqlite3
import pandas as pd

page = Blueprint('pages', __name__, template_folder='templates')


@page.route("/")
def index():
    """
    Index / Main page
    :return: html
    """

    return render_template('index.html')


@page.route("/_execute_task", methods=['POST'])
def _execute_task():
    """
    Invoke this function from an Ajax Call
    :return: json
    """
    from main_app.blueprints.pages.tasks import my_task

    if request.method == 'POST':
        # Invoke celery task
        task = my_task.delay()

    return jsonify({'taskID': task.id}), 201


@page.route("/celery-results")
def celery_results():
    try:
        conn = sqlite3.connect(app.config['DB_PATH'], detect_types=sqlite3.PARSE_DECLTYPES)

        celery_results_df = pd.read_sql_query('Select * from celery_taskmeta', conn)

        conn.close()

        return render_template('celery-results.html',
                               celery_results=celery_results_df.to_html(classes=["table"],
                                                                        index=False,
                                                                        table_id='celery-results-table'))

    except Exception as err:

        return render_template('celery-results.html',
                               celery_results=None)
