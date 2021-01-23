from flask import Flask, render_template, current_app as app

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('rainbow.html')

@app.route('/rainbow')
def rainbow():
    saves=['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    usages=['http://0.0.0.0:5000/red', 'http://0.0.0.0:5000/orange', 'http://0.0.0.0:5000/yellow', 'http://0.0.0.0:5000/green', 'http://0.0.0.0:5000/blue', 'http://0.0.0.0:5000/purple']
    return render_template('rainbow.html', saves=saves, usages=usages)

@app.route('/red')
def red():
    return render_template('rainbow.html', color='red', css='color:red;')

@app.route('/orange')
def orange():
    return render_template('rainbow.html', color='orange', css='color:orange')

@app.route('/yellow')
def yellow():
    return render_template('rainbow.html', color='yellow', css='color:yellow')

@app.route('/green')
def green():
    return render_template('rainbow.html', color='green', css='color:green')

@app.route('/blue')
def blue():
    return render_template('rainbow.html', color='blue', css='color:blue')

@app.route('/purple')
def purple():
    return render_template('rainbow.html', color='purple', css='purple')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')