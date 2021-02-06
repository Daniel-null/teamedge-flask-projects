from flask import Flask, render_template, request, json, jsonify, current_app as app
from datetime import date
import os
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return 0

@app.route('/Daniel', methods=['GET'])
def me_json():
	me_info = os.path.join(app.static_folder, 'data', 'me.json')
	with open(me_info, 'r') as json_data:
		json_info = json.load(json_data)
		return jsonify(json_info)

@app.route('/Kendric', methods=['GET'])
def kendric_json():
	me_info = os.path.join(app.static_folder, 'data', 'kendric.json')
	with open(me_info, 'r') as json_data:
		json_info = json.load(json_data)
		return jsonify(json_info)

@app.route('/Mohamed', methods=['GET'])
def Mohamed_json():
	me_info = os.path.join(app.static_folder, 'data', 'Mohamed.json')
	with open(me_info, 'r') as json_data:
		json_info = json.load(json_data)
		return jsonify(json_info)

@app.route('/Master', methods=['GET'])
def master_json():
	me_info = os.path.join(app.static_folder, 'data', 'master.json')
	with open(me_info, 'r') as json_data:
		json_info = json.load(json_data)
		return jsonify(json_info)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')