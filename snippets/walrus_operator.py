#!/usr/bin/env python

'''
Using the walrus operator in one of the few places where it's actually
useful.
'''
from coroutine_wrapper import coroutine

@coroutine
def printer():
    while line := (yield):
        print(line,)

if __name__ == '__main__':
    import sys
    if sys.version_info.major < 3:
        print("Need python >= 3.8 to run this test.")
        sys.exit(0)
    elif sys.version_info.major == 3 and sys.version_info.minor <= 8:
        print("Need python >= 3.8 to run this test.")
        sys.exit(0)
    p = printer()
    p.send('Testing 123')
    