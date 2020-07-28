#!/usr/bin/env python

import re

def Main():
    line = 'I think I understand regular expressions'
    match_result = re.match('think', line, re.M|re.I)
    if match_result:
        print('Match found: '+match_result.group())
    else:
        print('No match was found')

    search_result = re.search('think', line, re.M|re.I)
    if search_result:
        print('Search found:'+search_result.group())
    else:
        print('Nothing found in search')

if __name__ == '__main__':
    Main()