from extensions import db

class bussiness_data(db.Model):
    b_id = db.Column(db.Integer,primary_key=True)
    b_name = db.Column(db.String(50))
    b_type = db.Column(db.String(50))
    b_service = db.Column(db.String(50))
    b_location = db.Column(db.String(100))
