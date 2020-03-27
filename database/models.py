from .db import db

class DailyEntry(db.Document):
    date = db.DateTimeField(required=True)
    country = db.StringField(required=True)
    geo_id = db.StringField(required=True)
    country_code = db.StringField(required=True)
    cases = db.IntField(required=True)
    deaths = db.IntField(required=True) 
        
