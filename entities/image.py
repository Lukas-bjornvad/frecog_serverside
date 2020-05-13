from app_setup import db

class Image(db.model):
    id = db.column(db.Integer, primary_key=True)
    path = db.column(db.String(255), nullable=False)