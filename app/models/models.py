from app import db

class Postcode(db.Model):
    __tablename__ = 'postcodes'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(6))
    address = db.Column(db.String(128))
    town = db.Column(db.String(128))
    province = db.Column(db.String(128))
    county = db.Column(db.String(128))
