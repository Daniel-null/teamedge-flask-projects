from flask_apscheduler import APScheduler
from flask import Flask, render_template, request
from datetime import date
#today = str(date.today())

@app.route('/all', methods=(['GET', 'POST']))
def all():
    return 0

@app.route('/reminder/edit/<id>', methods=(['GET', 'POST']))
def edit(id):
    #code to edit task
    return 0

@app.route('/reminder/delete/<id>')
def delete(id):
    scheduler.remove_job(id)
    #code to delete task
    return 0

@app.route('/reminder/done/<id>')
def add(id, task):

    scheduler.add_job(id=id, func='function %s' %id , trigger='date', run_date='place holder', args=[task])
    #code to add task
    return 0

if __name__ == "__main__":
    app = Flask(__name__)
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()

