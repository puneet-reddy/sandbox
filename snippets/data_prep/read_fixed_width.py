#!/usr/bin/env python

import string
import struct

datafile = 'yourdata.data'

mask = '9s14s5s'

data = []
with open(datafile, 'r') as f:
    for line in f:
        fields = struct.Struct(mask).unpack_from(line)
        data.append(fields)


