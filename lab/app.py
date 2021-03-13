from flask import Flask, render_template
from datetime import date
import requests

app = Flask(__name__)

data = {
    "firstName": "Coach",
    "lastName": "Alyssa",
    "hobbies": ["running", "skydiving", "bowling"],
    "age": 300,
    "children": [
        {
            "firstName": "Alice",
            "age": 2
        },
        {
            "firstName": "Bob",
            "age": 4
        }
    ]
}

print(data["firstName"])
print(data['children'[2]])
print(data.firstName)

       
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
