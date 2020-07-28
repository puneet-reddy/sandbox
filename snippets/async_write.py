#!/usr/bin/env python

import threading
import time

class AsyncWrite(threading.Thread):
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out
    
    def run(self):
        with open(self.out, 'a') as f:
            f.write(self.text+'\n')
        time.sleep(2)
        print("finished background file write to ", self.out)

def Main():
    message = input("Enter a string to store:")
    background = AsyncWrite(message, 'out.txt')
    background.start()
    print("The program can continue while another thread runs")
    background.join()
    print('waited untill thread was complete')

if __name__ == '__main__':
    Main()