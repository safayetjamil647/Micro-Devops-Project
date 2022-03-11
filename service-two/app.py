import requests
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return 'hello from service two'
@app.route('/todo')
def todo_request():
    return requests.get('https://jsonplaceholder.typicode.com/todos/1').content
@app.route('/service-two')
def service_request():
    return 'welcome request from service two'

if __name__ == "__main__":
    app.run(debug=True)