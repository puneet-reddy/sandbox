#!/usr/bin/env python

'''
Attempting to set up a really simple CGI server which should work in
a windows environment
'''

from http.server import HTTPServer, CGIHTTPRequestHandler

class Handler(CGIHTTPRequestHandler):
    cgi_directories = ['/cgi-bin']

def Main():
    host = '127.0.0.1'
    port = 8080
    httpd = HTTPServer((host, port), Handler)
    print("Running CGI server at: ", host, port)
    httpd.serve_forever()

if __name__ == '__main__':
    Main()