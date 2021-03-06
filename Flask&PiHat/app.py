from flask import Flask, render_template, redirect, url_for, request, json, jsonify, current_app as app
import requests
import sys
import sqlite3 

app = Flask(__name__)

from sense_hat import SenseHat   #import the SenseHat object from the sense_hat library
from time import sleep
#from sense_emu import SenseHat

sense = SenseHat()

@app.route('/')
def info():
    return render_template('login.html')

#@app.route('/name')
#def name():
#   if len(name) == 0:
#      return redirect(url_for('login'))
   
@app.route('/send', methods=['POST', 'GET'])
def sent():
   if request.method == 'POST':
      name = request.form['nm']
      messege = request.form['mn']
      conn = sqlite3.connect('./static/data/info.db')
      curs = conn.cursor()
      curs.execute("INSERT INTO names (name, messege) VALUES((?),(?))", (name,messege))
      conn.commit ()

      conn.close()
      return redirect(url_for('success',name = name))
   else:
      return render_template('login.html')

@app.route('/all')
def all():
   conn = sqlite3.connect('./static/data/info.db')
   curs = conn.cursor()
   messeges = []
   rows = curs.execute("SELECT * FROM names")
   for row in rows:
      messege = ({'name': row[0], 'messege':row[1]})
      messeges.append(messege)
   
   return render_template('all.html', messeges = messeges)


@app.route('/success/<name>')
def success(name):
   sense.show_message(name)
   
   return 'welcome %s' % name + '  message recieved :P'

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      return render_template('login.html')


#@app.route('/login')
#def login():
   #if request.method == 'POST':
    #user = request.form['nm']
    #name = ''
    #return render_template('login.html', name = name)
   #else:
    #user = request.args.get('nm')
    #return redirect(url_for('success',name = user))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')