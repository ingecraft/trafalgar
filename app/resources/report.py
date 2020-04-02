from flask import Blueprint, Response, request
from database.models import Report
from flask_restful import Resource

reports = Blueprint('reports', __name__)

class ReportsApi(Resource):
    def get(self):
        reports = Report.objects().to_json()
        return Response(reports, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        report = Report(**body).save()
        id = report.id
        return {'id': str(id)}, 200

class ReportApi(Resource):
    def put(self, id):
        body = request.get_json()
        Report.objects.get(id=id).update(**body)
        return '', 200

    def delete(self, id):
        report = Report.objects.get(id=id).delete()
        return '', 200

    def get(self, id):
        reports = Report.objects.get(id=id).to_json()
        return Response(reports, mimetype="application/json", status=200)

