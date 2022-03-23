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
service_name = 'Service Two'
environment = 'production'

app = Flask(__name__)
apm = ElasticAPM(app, server_url=server_url, service_name=service_name, environment=environment)

@app.before_request
def apm_log():
    elasticapm.label(platform = 'Service Two',
                     application = 'Service Two')

@app.route('/')
def hello_geek():
    return 'hello from service two'
@app.route('/todo')
def todo_request():
    return requests.get('https://jsonplaceholder.typicode.com/todos/1').content
@app.route('/service-two')
def service_request():
    return 'welcome request from service two'

app.run()