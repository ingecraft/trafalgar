from .db import db

class DailyEntry(db.Document):
        date = db.DateTimeField(required=True)
        country = db.StringField(required=True)
        geo_id = db.StringField(required=True)
        cases = db.IntegerField(required=True)
        deaths = db.IntegerField(required=True)


