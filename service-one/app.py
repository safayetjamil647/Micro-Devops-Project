import requests
import logging
import os
from flask import Flask
from elasticapm.contrib.flask import ElasticAPM
import elasticapm
logging.basicConfig(level=logging.DEBUG,
                   format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                   datefmt='%Y-%m-%d %H:%M:%S',
                   handlers=[logging.StreamHandler()])

logger = logging.getLogger()
server_url = 'http://localhost:8201'
service_name = 'Service One'
environment = 'production'

app = Flask(__name__)
apm = ElasticAPM(app, server_url=server_url, service_name=service_name, environment=environment)

@app.before_request
def apm_log():
    elasticapm.label(platform = 'Service One',
                     application = 'Service One')

@app.route('/')
def hello_geek():
    return 'hello from service one'

@app.route('/todo/')
def todo_request():
    return requests.get('https://jsonplaceholder.typicode.com/todos/1').content
@app.route('/get-request/')
def get_request():
    return requests.get('http://172.17.0.4:5000/service-two').content

@app.route('/hello-world/')
def helloWorld():
	return "Hello World"

app.run()
