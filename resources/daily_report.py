from flask import Blueprint, Response, request
from database.models import Report

reports = Blueprint('reports', __name__)

@app.route('/reports')
def get_reports():
    reports = Report.objects().to_json()
    return Response(reports, mimetype="application/json", status=200)

@app.route('/reports', methods=['POST'])
def add_report():
    body = request.get_json()
    report = Report(**body).save()
    id = report.id
    return {'id': str(id)}, 200

@app.route('/reports/<id>', methods=['PUT'])
def update_report(id):
    body = request.get_json()
    Report.objects.get(id=id).update(**body)
    return '', 200

@app.route('/reports/<id>', methods=['DELETE'])
def delete_report(id):
    report = Report.objects.get(id=id).delete()
    return '', 200

@app.route('/reports/<id>')
def get_report(id):
    report = Report.objects.get(id=id).to_json()
    return Response(report, mimetype="application/json", status=200)
 
