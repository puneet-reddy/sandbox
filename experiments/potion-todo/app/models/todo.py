from app.extensions import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=True)
    active = db.Column(db.Integer)

    

