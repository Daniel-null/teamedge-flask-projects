from flask_apscheduler import APScheduler
from flask import Flask, render_template, request, redirect, url_for, request, json, jsonify, current_app as app
from datetime import date
from sense_hat import SenseHat
from time import sleep
import requests
import sys
import sqlite3 


sense = SenseHat()

app = Flask(__name__)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()




#today = str(date.today())
@app.route('/')
def info():
    return redirect(url_for('all'))

@app.route('/all', methods=(['GET', 'POST']))
def all():
    if request.method == 'POST':
        #code to store task and date in a variable
        task = request.form['task']
        date = request.form['date']

        #code to display message on sensehat
        sense.show_message('The task is ' + task + 'and is due ' + date)

        return redirect(url_for('data', task = task, date = date))
    else:
        #code to get data from  database
        conn = sqlite3.connect('./static/data/task.db')
        curs = conn.cursor()
        tasks = []
        rows = curs.execute("SELECT * FROM task")
        for row in rows:
            task = ({'id': row[0], 'task': row[1], 'date':row[2]})
            tasks.append(task)

        return render_template('form.html', tasks = tasks)



@app.route('/data/<task>/<date>', methods = ['POST', 'GET'])
def data(task, date):
    #database and storing task
    conn = sqlite3.connect('./static/data/task.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO task (task, date) VALUES((?),(?))", (task, date))
    conn.commit ()
    #closes connection to database
    conn.close()

    #database pulling row id
    conn = sqlite3.connect('./static/data/task.db')
    curs = conn.cursor()     
    row_id = []
    rows = curs.execute("SELECT ROWID FROM task")
    for row in rows:
        row_idd = {'id': row[0]}
        row_id.append(row_idd)
    print(row_id[-1]['id'])
    idb = str(row_id[-1]['id'])

    print(task)
    print(date)

    scheduler.add_job(id=idb, func='test' , trigger='date', run_date=date, args=task)

    return redirect(url_for('all'))






@app.route('/reminder/edit/<id>', methods=(['GET', 'POST']))
def edit(id):
    #code to get task
    if(scheduler.get_job(id)):
        scheduler.get_job(id)
        return redirect(url_for('all'))
    else:
        return redirect(url_for('all'))


@app.route('/reminder/delete/<id>')
def delete(id):
    if(scheduler.get_job(id)):
        scheduler.remove_job(id)
        return redirect(url_for('all'))
    else:
        return redirect(url_for('all'))

    #code to delete task

@app.route('/reminder/done/<id>', methods=(['GET', 'POST']))
def add(id):
    print(id)

    conn = sqlite3.connect('./static/data/task.db')
    curs = conn.cursor()
    tasks = []
    rows = curs.execute("SELECT * FROM task WHERE rowid=%s"%id)
    for row in rows:
        task = ({'task': row[1], 'date':row[2]})
        tasks.append(task)
    print(tasks)
        
    scheduler.add_job(id=id, func='test' , trigger='date', run_date=tasks['date'], args=[tasks['task']])
    #code to add task
    return render_template('form.html')

def test():
    print(hello)
    return 0


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')