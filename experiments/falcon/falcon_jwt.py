#/usr/bin/env python3

import os
import falcon
import bjoern
import jwt
import json
from datetime import (datetime, timedelta)

SECRET = os.getenv('JWT_SECRET', 'some_secret')

class JWTDemo:
    def on_get(self, req, res):
        now = datetime.utcnow()
        delta = timedelta(days=0, seconds=600)
        data = 'Sample payload data for demo'
        payload = {
            'exp': now + delta,
            'iat': now,
            'sub': data
        }
        res.status = falcon.HTTP_200
        res.body = jwt.encode(payload, SECRET, algorithm='HS256')

class JWTDecoder:
    def on_post(self, req, res):
        payload = json.load(req.bounded_stream)
        data = jwt.decode(payload, SECRET)
        res.status = falcon.HTTP_200
        res.body = json.dumps(data.get('sub'))

class JWTEncoder:
    def on_post(self, req, res):
        now = datetime.utcnow()
        exp = now + timedelta(days=0, seconds=600)
        data = json.load(req.bounded_stream)
        payload = {'exp': exp, 'iat': now, 'sub': data}
        res.status = falcon.HTTP_200
        res.body = jwt.encode(payload, SECRET, algorithm='HS256')
            

app = falcon.API()
app.req_options.auto_parse_form_urlencoded = True
demo = JWTDemo()
app.add_route('/', demo)
app.add_route('/decode', JWTDecoder())
app.add_route('/encode', JWTEncoder())

if __name__ == '__main__':
    host, port = 'localhost', 5000
    print(f'Starting service on {host}:{port}')
    bjoern.run(app, host, port)

        
