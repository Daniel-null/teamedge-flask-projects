from flask import Flask, render_template
from datetime import date
import requests

app = Flask(__name__)

@app.route('/')
def index():
	name='daniel'
	h='sup'
	friends = ['joe', 'kathrin', 'akeena']
	return render_template('index.html', greeting=name,description=h, friends=friends)

@app.route('/about')
def about():
	return '<h1>About</h1><p>some other content</p>'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
