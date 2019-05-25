#!/usr/bin/env python

from datetime import (datetime, timedelta)
from flask import (Flask)
import json
import jwt

from require_jwt import authorize

app = Flask(__name__)


@app.route('/')
@authorize
def test():
    print(user_data)
    return user_data.get('sub')

@app.route('/token')
def get_token():
    sample = {'name': 'someone', 'id': 1}
    delta = timedelta(days=0, seconds=600)
    payload = {
        'exp': datetime.utcnow()+delta,
        'iat': datetime.utcnow(),
        'sub': json.dumps(sample)
    }
    return jwt.encode(payload, 'my_precious_development', algorithm='HS256')

if __name__ == '__main__':
    app.run(debug=True)