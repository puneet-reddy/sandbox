#!/usr/bin/env python

import json
import logging
import uuid
import bjoern

import falcon
import requests

class StorageEngine(object):
    def get_things(self, marker, limit):
        #TODO: What does marker do again???
        return [{'id': str(uuid.uuid4()), 'color': 'green'}]

    def add_thing(self, thing):
        thing['id'] = str(uuid.uuid4())
        return thing

class StorageError(Exception):

    @staticmethod
    def handle(ex, req, resp, params):
        description = ('Sorry, could\'nt write your thing to the '
                        'database. It worked on my machine!')

        raise falcon.HTTPError(falcon.HTTP_725, 'Database Error', description)

class SinkAdapter(object):
    engines = {
    'ddg': 'https://duckduckgo.com',
    'gog': 'https://www.google.com'
    }

    def __call__(self, req, resp, engine):
        url = self.engines[engine]
        params = {'q': req.get_param('q', True)}
        result = requests.get(url, params=params)

        resp.status = str(result.status_code) + ' ' + result.reason
        resp.content_type = result.headers['content-type']
        resp.body = result.text

class AuthMiddleware(object):

    def process_request(self, req, resp):
        token = req.get_header('Authorization')
        account_id = req.get_header('Account-ID')

        challenges = ['Token type="Fernet"']

        if token is None:
            description = ('Please provide an auth token '
                            'as part of the request.')
            raise falcon.HTTPUnauthorized(
                'Auth token required',
                description,
                challenges,
                href='http://docs.example.com/auth')

    def _token_is_valid(self, token, account_id):
        return True #TODO: Suuuure it's valid alright...

class RequireJson(object):

    def process_request(self, req, resp):
        if not req.client_accepts_json:
            raise falcon.HTTPNotAcceptable(
                'This API only supports responses encoded as JSON.',
                href='http://docs.examples.com/api/json'
            )

        if req.method in ('POST', 'PUT'):
            if 'application/json' not in req.content_type:
                raise falcon.HTTPUnsupportedMediaType(
                    'This API only supports requests encoded as JSON.',
                    href='http://docs.examples.com/api/json'
                )

class JSONTranslator(object):

    def process_request(self, req, resp):
        if req.content_length in (None, 0):
            return

        body = req.stream.read()
        if not body:
            raise falcon.HTTPBadRequest(
                'Empty request body',
                'A valid JSON document is required')

        try:
            req.context['doc'] = json.loads(body.decode('utf-8'))
        except (ValueError, UnicodeDecodeError):
            raise falcon.HTTPError(
                falcon.HTTP_753,
                'Malformed JSON',
                'Could not decode the request body. The JSON was incorrect '
                'or not encoded as UTF-8.'
            )

    def process_response(self, req, resp, resource, req_succeeded):
        if 'result' not in resp.context:
            return

        resp.body = json.dumps(resp.context['result'])

def max_body(limit):

    def hook(req, resp, resource, params):
        length = req.content_length
        if length is not None and length > limit:
            msg = ('The size of the request is too large. The body must not '
                'exceed ' + str(limit) + ' bytes in length.')

            raise falcon.HTTPRequestEntityTooLarge(
                'Reuqest body is too large', msg
            )
    return hook

class ThingResource(object):

    def __init__(self, db):
        self.db = db
        self.logger = logging.getLogger('thingsapp.' + __name__)

    def on_get(self, req, resp, user_id):
        marker = req.get_param('marker') or ''
        limit = req.get_param_as_int('limit') or 50

        try:
            result = self.db.get_things(marker, limit)
        except Exception as ex:
            self.logger.error(ex)

            description = (
                'Aliens have attacked our base! We will be back as soon '
                'as we fight them off. We appreciate your patience.'
            )

            raise falcon.HTTPServiceUnavailable(
                'Service Outage', description, 30
            )

        resp.context['result'] = result
        resp.set_header('Powered-By', 'Falcon')
        resp.status = falcon.HTTP_200

    @falcon.before(max_body(64 * 1024))
    def on_post(self, req, resp, user_id):
        try:
            doc = req.context['doc']
        except KeyError:
            raise falcon.HTTPBadRequest(
                'Missing thing',
                'A thing you asked for could not be found in our pseudo db.'
            )

        proper_thing = self.db.add_thing(doc)
        resp.status = falcon.HTTP_201
        resp.location = '/{}/things/{}'.format(user_id, proper_thing['id'])

app = falcon.API(
    middleware=[
        AuthMiddleware(),
        RequireJson(),
        JSONTranslator()
    ]
)

db = StorageEngine()
things = ThingResource(db)
app.add_route('/{user_id}/things', things)

app.add_error_handler(StorageError, StorageError.handle)

sink = SinkAdapter()
app.add_sink(sink, r'/search/(?P<engine>ddg|gog)\Z')

if __name__ == '__main__':
    bjoern.run(app, 'localhost', 8080)
