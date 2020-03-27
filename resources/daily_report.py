@app.route('/daily-reports')
def get_daily_reports():
    reports = DailyReport.objects().to_json()
    return Response(reports, mimetype="application/json", status=200)

@app.route('/daily-reports', methods=['POST'])
def add_daily_report():
    body = request.get_json()
    report = DailyReport(**body).save()
    id = report.id
    return {'id': str(id)}, 200

@app.route('/daily_reports/<id>', methods=['PUT'])
def update_report(id):
    body = request.get_json()
    DailyReport.objects.get(id=id).update(**body)
    return '', 200

@app.route('/daily_reports/<id>', methods=['DELETE'])
def delete_report(id):
    report = Report.objects.get(id=id).delete()
    return '', 200

@app.route('/daily_reports/<id>')
def get_daily_report(id):
    report = DailyReport.objects.get(id=id).to_json()
    return Response(report, mimetype="application/json", status=200)
 
