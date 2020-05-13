from app_setup import db

class Subject(db.Model):
    __tablename__="Subject"
    id = db.Column('id', db.Integer, primary_key=True)
    first_name = db.Column('first_name', db.String(30), nullable=False)
    last_name = db.Column('last_name', db.String(30),nullable=False)
    images = db.relationship("Image", backref="subject", lazy='dynamic')
    def __init__(self, first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name

        def __repr__(self):
            return f'Subject {self.id}'

        