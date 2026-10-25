from extensions import db

class transaction_data(db.Model):
    t_id = db.Column(db.Integer,primary_key=True)
    t_customer_name = db.Column(db.String(50))
    t_amount = db.Column(db.Integer)

