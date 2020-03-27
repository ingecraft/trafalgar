from .report import ReportApi, ReportsApi

def initialize_routes(api):
    api.add_resource(ReportsApi, '/reports')
    api.add_resource(ReportApi, '/reports/<api>')
