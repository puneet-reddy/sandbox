
import flask
from flask import request, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)


@app.route('/')
def test_page():
    args = {}
    args = build_args(args, 'id')
    args = build_args(args, 'name')
    args = build_args(args, 'email')
    print(args)
    res = User.query.filter_by(**args).all()
    print(res)
    return make_response(jsonify([e.as_dict() for e in res]), 200)

def build_args(args, key=None):
    val = request.args.get(key)
    if val:
        args.update({str(key): val})
    return args


db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'filter_test'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    u1 = User(name='test1', email='test@test.com')
    u2 = User(name='test2', email='test@test.com')
    u3 = User(name='test3', email='test@testing.com')
    u4 = User(name='test3', email='test@test.com')
    db.session.add(u1)
    db.session.add(u2)
    db.session.add(u3)
    db.session.add(u4)
    db.session.commit()
    app.run(debug=True)
