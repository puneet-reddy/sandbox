#!/usr/bin/env python

'''
Read a large file in chunks of 1000 lines
'''

import os
import sys

if len(sys.argv) < 2:
    print("Error: Need to pass a filename.")
    print("Usage: $python {} <somefilename>".format(__file__))
    sys.exit(1)

filename = sys.argv[1]

if not os.path.isfile(filename):
    print("Error: The given filename is not a file!", file=sys.stderr)
    sys.exit(1)

with open(filename, 'rb') as bigfile:
    chunksize = 1000 #Lines
    readable = ''

    while bigfile:
        start = bigfile.tell()
        print("starting at :", start)
        file_block = ''
        for _ in range(start, start + chunksize):
            line = bigfile.next()
            file_block = file_block + line
            print('file_block', type(file_block), file_block)
        readable = readable + file_block

        stop = bigfile.tell()
        print('readable', type(readable), readable)
        print('reading bytes from {} to {}'.format(start, stop))

        #To pause between reading blocks
        input("Press any key to continue...")