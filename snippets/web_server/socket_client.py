#!/usr/bin/env python

'''
A simple client to connect to a socket
'''

import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(('localhost', 8888))

soc.sendall(b'test')
data = soc.recv(1024)
print(data.decode())
