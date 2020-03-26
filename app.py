from flask import Flask, request, Response
from database.db import initialize_db
from database.models import DailyEntry

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/trafalgar'
}

initialize_db(app)

@app.route('/daily-entries')
def get_daily_entries():
    entries = DailyEntry.objects().to_json()
    return Response(entries, mimetype="application/json", status=200)

@app.route('/daily-entries', methods=['POST'])
def add_daily_entry():
    body = request.get_json()
    entry = DailyEntry(**body).save()
    id = entry.id
    return {'id': str(id)}, 200

@app.route('/daily_entries/<id>', methods=['PUT'])
def update_movie(id):
    body = request.get_json()
    DailyEntry.objects.get(id=id).update(**body)
    return '', 200

@app.route('/daily_entries/<id>', methods=['DELETE'])
def delete_entry(id):
    entry = Entry.objects.get(id=id).delete()
    return '', 200

@app.route('/daily_entries/<id>')
def get_daily_entry(id):
    entry = DailyEntry.objects.get(id=id).to_json()
    return Response(entry, mimetype="application/json", status=200)
    
app.run()

