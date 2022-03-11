import requests
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return 'hello from service one'

@app.route('/todo')
def todo_request():
    return requests.get('https://jsonplaceholder.typicode.com/todos/1').content
@app.route('/get-request')
def get_request():
    return requests.get('http://172.17.0.4:5000/service-two').content

if __name__ == "__main__":
    app.run(debug=True)