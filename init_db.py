import pandas as pd

from datetime import datetime, timedelta
from database.models import Report

from mongoengine import *

def get_today_string():
    today = date.today()
    return "{:04d}-{:02d}-{:02d}".format(today.year, today.month, today.day)

class DataGetter():
    def __init__(self, date):
        self.ecdc_base_url = "https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-"
        self.ecdc_date_format = "{:04d}-{:02d}-{:02d}".format(today.year, today.month, today.day)
        self.ecdc_file_extension = ".xlsx"
        self.ecdc_url = self.ecdc_base_url + self.ecdc_date_format + self.ecdc_file_extension
        
    def all_ecdc_data(self):
       self.all_ecdc_data = pd.read_excel(self.ecdc_url).values.tolist()
    
    def init_db(self):
        connect('trafalgar')
        for row in self.all_ecdc_data:
            date = row[0]
            country = str(row[6])
            geo_id = str(row[7])
            cases = row[4]
            deaths = row[5]
            report = Report(date=date, country=country, geo_id=geo_id, \
                    cases=cases, deaths=deaths)
            report.save()
        
        print("Database initialized")

        
if __name__=="__main__":
    today = datetime.today() - timedelta(days=1)
    dg = DataGetter(today)
    dg.all_ecdc_data()
    dg.init_db()
