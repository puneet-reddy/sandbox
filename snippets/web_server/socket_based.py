#!/usr/bin/env python

import socket

HOST, PORT = '', 8889

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

print('Serving HTTP on port {}'.format(PORT))
while True:
    client_connection, client_address = listen_socket.accept()
    print("Connection from:", client_address)
    request = client_connection.recv(1024)
    print(request)

    #There can be no preceeding spaces and the blank line is required for http
    http_response=b"""
HTTP/1.1 200 OK

Hello from a simple socket based web server written in python!
    """
    client_connection.sendall(http_response)
    client_connection.close()