#!/usr/bin/env python

'''
Client side script for a socket based python chat program
'''

import socket
import threading
import sys

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def read_data(soc):
    while True:
        data = soc.recv(1024)
        print(data.decode())

def write_data(soc):
    while True:
        data = input('->')
        soc.send(data.encode())


def run():
    '''Runs the chat client'''
    read_thread = threading.Thread(target=read_data, args=(SERVER,))
    write_thread = threading.Thread(target=write_data, args=(SERVER,))
    read_thread.start()
    write_thread.start()
    read_thread.join()
    write_thread.join()

    SERVER.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Correct usage: python {} host port".format(__file__))
        sys.exit(0)

    host = str(sys.argv[1])
    port = int(sys.argv[2])
    SERVER.connect((host, port))
    run()
