from flask import Flask, render_template, current_app as app

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to Daniels Rainbow project<h1>'

@app.route('/red')
def red():
    return render_template('red.html')

@app.route('/orange')
def orange():
    return render_template('orange.html')

@app.route('/yellow')
def yellow():
    return render_template('yellow.html')

@app.route('/green')
def green():
    return render_template('green.html')

@app.route('/blue')
def blue():
    return render_template('blue.html')

@app.route('/purple')
def purple():
    return render_template('purple.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
