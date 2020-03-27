from flask import Flask, request, Response
from database.db import initialize_db
from resources.report import reports

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/trafalgar'
}

initialize_db(app)
app.register_blueprint(reports)
   
app.run()

