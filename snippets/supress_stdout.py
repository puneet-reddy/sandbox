#!/usr/bin/env python

'''
A simple script to supress the output of a given bit of code.
Works on both windows and linux.
To use it, just wrap the code you want supressed in a context like below
with supress_stdout():
    print("You won't see this")
'''

from contextlib import contextmanager
import sys
import os

@contextmanager
def supress_stdout():
    with open(os.devnull, 'w') as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout


if __name__ == '__main__':
    print("Unsupressed print.")
    with supress_stdout():
        print("Supressed print.")