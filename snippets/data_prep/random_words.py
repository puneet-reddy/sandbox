#!/usr/bin/env python

'''
Neat trick to get random words on Linux
'''

import random

with open('/usr/share/dict/words', 'rt') as f:
    words = f.readlines()

words = [w.rstrip() for w in words]

five_words = random.sample(words, 5)

print(five_words)