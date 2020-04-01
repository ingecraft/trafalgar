import os

from flask import Flask, request, Response
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'username': os.environ.get("MONGODB_USERNAME", ""),
    'password': os.environ.get("MONGODB_PASSWORD", ""),
    'host': os.environ.get("MONGODB_HOSTNAME", "localhost"),
    'db': os.environ.get("MONGODB_DATABASE", "trafalgar"),
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

