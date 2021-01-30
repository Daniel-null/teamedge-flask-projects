from flask import Flask, render_template, request, json, jsonify, current_app as app
from datetime import date
import os
import requests

app = Flask(__name__)

@app.route('/')
def holidays():
    response = requests.get('https://date.nager.at/api/v2/PublicHolidays/2020/us')
    data = response.json()
#    return jsonify(data)
    return render_template('holidays.html', data=data)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
