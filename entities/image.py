from app_setup import db

class Image(db.model):
    __tablename__="Image"
    id = db.column(db.Integer, primary_key=True)
    path = db.column(db.String(255), nullable=False)

    subject_id = db.Column(db.Integer, db.Foreignkey('subject.id'), nullable=False)
    subject = db.relationship('Subject')

    def __init__(self, path, subject):
        self.path = path
        self.subject = subject

        def __repr__(self):
            return f'<Image {self.id}>'





    id_subject = db.Column(db.Integer, db.Foreignkey('id_subject.id'), nullable=False)
    category = db.relationship('Subject', backref=db.backref('Image'),)