import os

from flask import Flask, request, Response
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'username': os.environ['MONGODB_USERNAME'],
    'password': os.environ['MONGODB_PASSWORD'],
    'hostname': os.environ['MONGODB_HOSTNAME'],
    'db': os.environ['MONGODB_DATABASE']
}

initialize_db(app)
   
initialize_routes(api)

@app.route('/')
def hello():
    return "Hello, World"

if __name__== "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    app.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)

