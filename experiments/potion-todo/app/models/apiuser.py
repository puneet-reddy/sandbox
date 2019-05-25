from app.extensions import db


class ApiUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    is_admin = db.Column(db.Boolean(), default=False)
    is_editor = db.Column(db.Boolean(), default=False)

    @property
    def is_authenticated(self):
        return True
