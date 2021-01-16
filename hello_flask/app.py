from flask import Flask, render_template, request, json, jsonify, current_app as app
from datetime import date
import os
import requests

app = Flask(__name__)

Json_info = ''
movies_path = os.path.join(app.static_folder, 'data', 'movies.json')
with open(movies_path, 'r') as raw_json:
	json_info = json.load(raw_json)

@app.route('/')
def index():
	name='daniel'
	h='sup'
	friends = ['joe', 'kathrin', 'akeena']
	return render_template('index.html', greeting=name,description=h, friends=friends)

@app.route('/api/v1/album', methods=['GET'])
def album_json():
	album_info = os.path.join(app.static_folder, 'data', 'project.json')
	with open(album_info, 'r') as json_data:
		json_info = json.load(json_data)
		return jsonify(json_info)

@app.route('/api/v2/movies')
def all_movies():
	return jsonify(json_info)

#@app.route('/api/v2/movies')
#def movies():
#	json_info = ''
#	movie_info = os.path.join(app.static_folder, 'data', 'movies.json')
#	with open(movie_info, 'r') as json_data:
#		json_info = json.load(json_data)
#		return jsonify(json_info)

@app.route('/api/v2/movies/search_titles', methods=['GET'])
def search_titles():
	results = []
	if 'title' in request.args:
		title = request.args['title']

		for movie in json_info:
			if title in movie['title']:
				results.append(movie)

	if len(results) < 1:
		return "No Results found"
	return render_template('msearch.html', results=results)

@app.route('/about')
def about():
	return '<h1>About</h1><p>some other content</p>'

@app.route('/nasa')
def nasa_image():
	today = str(date.today())
	response = requests.get('https://api.nasa.gov/planetary/apod?api_key=wjlnR0Xw9B5Sh3WEIJa9kmVd368hNMiUVIGahGPi&date='+today)
	data = response.json()
	return render_template('nasa.html',data=data)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
