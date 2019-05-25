#!/usr/bin/env python

def app(environ, start_response):
    """
    A barebones WSGI appliction.
    WIthout using Flask, Django, Pyramid or anything else!
    """
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]
    start_response(status, response_headers)
    return [b'Hello from a barebones WSGI application!\n']