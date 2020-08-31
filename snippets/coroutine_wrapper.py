#!/usr/bin/env python

'''
Simple decorator to prime a coroutine
'''

def coroutine(func):
    def start(*args, **kwargs):
        wrapped = func(*args, **kwargs)
        next(wrapped)
        return wrapped
    return start

if __name__ == '__main__':
    @coroutine
    def printer():
        while True:
            value = (yield)
            print(value)

    @coroutine
    def upcaser():
        while True:
            value = (yield)
            yield value.upper()
    
    p = printer()
    u = upcaser()
    p.send(u.send('Testing 123'))