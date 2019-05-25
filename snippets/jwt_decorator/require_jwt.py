#!/usr/bin/env python3

'''
@author: puneet.reddy@beyondanalysis.net
@created:
@blurb: Decorator to easily handler JWT validation.
'''

import os
import jwt

from flask import (request, make_response, jsonify)

JWT_SECRET = os.getenv('JWT_SECRET', 'my_precious_development')


def authorize(func):
    '''
    Decorator funciton to handle jwt validation.
    It also injects a `user_data` dict into the global namespace of the
    decorated function.
    '''
    def wrapper(*args, **kwargs):

        if not 'Authorization' in request.headers:
            return make_response(jsonify({
                'status': 'fail',
                'message': 'Authorization header missing'
            }), 401)

        try:
            token = request.headers.get(
                'Authorization').encode('utf-8', 'ignore').split()[1]
        except Exception as err:
            return make_response(jsonify({
                'status': 'fail',
                'message': 'Malformed token. Please log in again.',
                'error_msg': str(err)
            }), 401)

        try:
            user = jwt.decode(token, "my_precious_development")
        except jwt.ExpiredSignatureError:
            return make_response(jsonify({
                'status': 'fail',
                'message': 'Token expired. Please log in again.'
            }), 401)
        except jwt.DecodeError as err:
            print(token)
            return make_response(jsonify({
                'status': 'fail',
                'message': 'Unable to decode token. Please try again.',
                'error_msg': str(err)
            }), 401)
        except jwt.InvalidTokenError:
            return make_response(jsonify({
                'status': 'fail',
                'message': 'Invalid or malformed token. Please log in again.'
            }), 401)
        except:
            return make_response(jsonify({
                'status': 'fail',
                'message': 'Unknown error. Please try again later.'
            }), 500)

        # Add the user details to the wrapped function's globals
        sentinel = func.__globals__.get('user_data', 'some_sentinel_value')
        func.__globals__['user_data'] = user
        try:
            result = func(*args, **kwargs)
        finally:
            if sentinel == 'some_sentinel_value':
                del func.__globals__['user_data']
            else:
                func.__globals__['user_data'] = sentinel
        return result
    return wrapper
