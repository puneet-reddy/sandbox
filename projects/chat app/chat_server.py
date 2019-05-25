#!/usr/bin/env python

'''
Server side script for a socket based python chat program
'''

import socket
import select
import sys
import threading

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

CONNECTIONS = []

def client_thread(conn, addr):
    # Sends a message to the client whose user object is conn
    conn.send(b"Welcome to the chat room!")

    while True:
        try:
            message = conn.recv(1024)
            if message:
                print(message.decode())
                broadcast(message, conn)
            else:
                remove(conn)
        except:
            continue

def broadcast(message, source):
    '''
    Send a message to all the clients.
    '''
    for client in CONNECTIONS:
        try:
            if client == source:
                pass
            client.send(message)
        except:
            client.close()
            remove(client)

def remove(connection):
    '''Remove a connection from the global list of connection'''
    if connection in CONNECTIONS:
        CONNECTIONS.remove(connection)

def run():
    '''Starts the server to keep listening for client connections'''
    while True:
        print('.',)
        conn, addr = SERVER.accept()
        CONNECTIONS.append(conn)

        print(addr[0], ' connected')
        threading._start_new_thread(client_thread, (conn, addr))

    conn.close()
    SERVER.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Correct usage: python {} host port'.format(__file__))
        sys.exit(0)

    host = str(sys.argv[1])
    port = int(sys.argv[2])
    SERVER.bind((host, port))
    SERVER.listen(100) #Listens for up to 100 connections
    run()
