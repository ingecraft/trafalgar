import pandas as pd

from datetime import date
from database.models import Report

def get_today_string():
    today = date.today()
    return "{:04d}-{:02d}-{:02d}".format(today.year, today.month, today.day)

class DataGetter():
    def __init__(self, date):
        self.ecdc_base_url = "https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-"
        self.ecdc_date_format = "{:04d}-{:02d}-{:02d}".format(today.year, today.month, today.day)
        self.ecdc_file_extension = ".xlsx"
        self.ecdc_url = self.ecdc_base_url + self.ecdc_date_format + self.ecdc_file_extension
        
    def ecdc_data(self):
        return pd.read_excel(self.ecdc_url).values.tolist()

if __name__=="__main__":
    today = date.today()
    dg = DataGetter(today)
    ecdc_data = dg.ecdc_data()
