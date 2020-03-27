from .report import ReportApi, ReportsApi

def initialize_routes(api):
    api.add_resource(ReportsApi, '/api/reports')
    api.add_resource(ReportApi, '/api//reports/<id>')
    
