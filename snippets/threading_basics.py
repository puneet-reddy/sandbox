#!/usr/bin/env python

from threading import Thread, Lock
import time

t_lock = Lock()

def timer(name, delay, repeat):
    print('Timer: ', name, ' started')
    t_lock.acquire()
    print(name, ' has acquired the lock')
    while repeat > 0:
        time.sleep(delay)
        print(name, ' : ', str(time.ctime(time.time())))
        repeat -= 1
    print(name, ' is releasing the lock')
    t_lock.release()
    print('Timer: ', name, ' is completed')

def Main():
    t1 = Thread(target=timer, args=("timer1", 1, 5))
    t2 = Thread(target=timer, args=('timer2', 2, 5))
    t1.start()
    t2.start()

    print("Main completed")

if __name__ == '__main__':
    Main()