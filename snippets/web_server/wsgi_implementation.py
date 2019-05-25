#!/usr/bin/env python

'''
Implementing the WSGI using python's standard libraries only
'''

import socket
import sys
from io import StringIO

class WSGIServer(object):

    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 1

    def __init__(self, server_address):
        # Create a listening socket
        self.listen_socket = listen_socket = socket.socket(
            self.address_family,
            self.socket_type
        )
        # Allow to reuse the same address
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Bind
        listen_socket.bind(server_address)
        # Activate
        listen_socket.listen(self.request_queue_size)
        # Get server host name and port
        host, port = self.listen_socket.getsockname()[:2]
        self.server_name = socket.getfqdn(host)
        self.server_port = port
        # Return headers set by the web framework/ web app
        self.headers_set = []

    def set_app(self, application):
        self.application = application

    def server_forever(self):
        listen_socket = self.listen_socket
        while True:
            # New client connection
            self.client_connection, client_address = listen_socket.accept()
            # Handle one request and close the connection then keep looping
            self.handle_one_request()

    def handle_one_request(self):
        self.request_data = request_data = self.client_connection.recv(1024)
        # Print formatted request data 'like in curl -v'
        print(''.join(
            '< {line}\n'.format(line=line)
            for line in request_data.splitlines()
        ))
        self.parse_request(request_data)

        # Construct environment dictionary using request data
        env = self.get_environ()

        # Call the application callable to get a result
        # This result becomes the HTTP response body
        result = self.application(env, self.start_response)

        # Construct a response and send it back to the clinet
        self.finish_response(result)

    def parse_request(self, text):
        request_line = text.splitlines()[0]
        request_line = request_line.rstrip(b'\r\n')
        # Break down the request line to get the components
        (self.request_method, 
        self.path, 
        self.request_version) = request_line.split()

    def get_environ(self):
        return {
            # Required WSGI variables
            'wsgi.version': (1, 0),
            'wsgi.url_scheme': 'http',
            'wsgi.input': StringIO(str(self.request_data, 'utf-8')),
            'wsgi.errors': sys.stderr,
            'wsgi.multithread': False,
            'wsgi.multiprocess': False,
            'wsgi.run_once': False,
            # Required CGI variables
            'REQUEST_METHOD': self.request_method,
            'PATH_INFO': str(self.path, 'utf-8'),
            'SERVER_NAME': self.server_name,
            'SERVER_PORT': str(self.server_port)
        }
        
    def start_response(self, status, response_headers, exc_info=None):
        # Add the necessary server headers
        server_headers = [
            ('Date', 'Tue, 29 Jan 2019 10:22:11 GMT'),
            ('Server', 'WSGIServer 0.2'),
        ]
        self.headers_set = [status, response_headers + server_headers]
        # TODO: As per the WSGI spec, the start_response must return a 'write'
        # callable. Using self.finish_response instead for now.
        return self.finish_response

    def finish_response(self, result):
        #TODO: Error handling
        try:
            status, response_headers = self.headers_set
            response = 'HTTP/1.1 {status}\r\n'.format(status=status)
            for header in response_headers:
                response += '{0}: {1}\r\n'.format(*header)
            response += '\r\n'
            for data in result:
                response += str(data, 'utf-8')
            print(''.join('> {line}\n'.format(line=line) for line in response.splitlines()))
            self.client_connection.sendall(bytes(response, 'utf-8'))
        finally:
            self.client_connection.close()

SERVER_ADDRESS = (HOST, PORT) = '', 8889

def make_server(server_address, application):
    '''A server factory!'''
    server = WSGIServer(server_address)
    server.set_app(application)
    return server

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Provide a WSGI application object as module:callable')
    app_path = sys.argv[1]
    module, application  = app_path.split(':')
    module = __import__(module)
    application = getattr(module, application)
    httpd = make_server(SERVER_ADDRESS, application)
    print('WSGIServer: Serving HTTP on port {port} ...\n'.format(port=PORT))
    httpd.server_forever()