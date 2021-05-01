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
            task = ({'task': row[0], 'date':row[1]})
            tasks.append(task)

        return render_template('form.html', tasks = tasks)



@app.route('/data', methods = ['POST', 'GET'])
def data(task, date):
    #database and storing task
    conn = sqlite3.connect('./static/data/task.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO task (task, date) VALUES((?),(?))", (task, date))
    conn.commit ()
    #closes connection to database
    conn.close()   

    return redirect(url_for(''))






@app.route('/reminder/edit/<id>', methods=(['GET', 'POST']))
def edit(id):
    #code to get task
    if(scheduler.get_job(id)):
        scheduler.get_job(id)
        return render_template('form.html')
    else:
        return render_template('form.html')


@app.route('/reminder/delete/<id>')
def delete(id):
    scheduler.remove_job(id)
    #code to delete task
    return 0

@app.route('/reminder/done/<id>')
def add(id, task):

        
    scheduler.add_job(id=id, func='all' , trigger='date', run_date=date, args=[task])
    #code to add task
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


