#!/usr/bin/env python

import csv

filename = 'yourcsv.csv'

data = []
header = None
try:
    with open(filename) as f:
        #csv.reader(f, dialect=csv.excel_tab) if it's a tsv
        reader = csv.reader(f)
        header = reader.next()
        data = [row for row in reader]
except csv.Error as e:
    msg = 'Error reading CSV file at line {}: {}'.format(reader.line_num, e)
    print(msg)

if header:
    print(header)
