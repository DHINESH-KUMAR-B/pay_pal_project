from extensions import db

class sales_data(db.Model):
    s_id = db.Column(db.Integer, primary_key=True)

    t_id = db.Column(
        db.Integer,
        db.ForeignKey("transaction_data.t_id"),
        nullable=False
    )

    s_product = db.Column(db.String(50))
    s_qty = db.Column(db.Integer)
    s_net = db.Column(db.Integer)

    transaction = db.relationship(
        "transaction_data",
        back_populates="sales"
    )