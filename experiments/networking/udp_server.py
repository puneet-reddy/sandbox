#!/usr/bin/env python

import socket

def Main():
    host = '127.0.0.1'
    port = 2000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print("Server started on: ", host, port)
    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print('Message from: ', str(addr))
        print('Data received: ', data)
        data = data.upper()
        print('Sending data: ', data)
        s.sendto(data.encode('utf-8'), addr)
    c.close()

if __name__ == '__main__':
    Main()