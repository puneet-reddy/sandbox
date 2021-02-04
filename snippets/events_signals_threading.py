#!/usr/bin/env python

'''
This demonstrates how to use python events to catch a SIGTERM event and cause
a thread to exit gracefully, allowing it time to do a cleanup.
This is better than simply instatiating it as a daemon thread.
NOTE: This will only work on a *NIX OS 
'''

import random
import signal
import threading
import time

exit_event = threading.Event()

def bg_thread():
    for i in range(1, 30):
        print(f'{i} of 30 iterations...')
        time.sleep(random.random()) #Pretend to do some work

        if exit_event.is_set():
            break
        
    print(f'{i} iterations completed before exiting.')

def signal_handler(signum, frame):
    exit_event.set()

signal.signal(signal.SIGINT | signal.CTRL_C_EVENT, signal_handler)
th = threading.Thread(target=bg_thread)
th.start()
th.join()