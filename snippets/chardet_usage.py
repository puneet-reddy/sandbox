#!/usr/bin/env python

'''
Guessing the encoding of a file with chardet
'''

from chardet.universaldetector import UniversalDetector

test_file = r'C:\Users\css112720\Desktop\aruba\automation\data\sfdc_20200826\report1598425558894_lmd.csv'

with open(test_file, 'rb') as fp:
    try:
        ud = UniversalDetector()
        for line in fp.readlines():
            ud.feed(line)
            if ud.done: break
    except Exception as err:
        print(str(err))
        raise err
    finally:
        if ud:
            ud.close()

print(ud.result)