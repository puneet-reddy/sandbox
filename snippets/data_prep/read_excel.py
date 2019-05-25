#!/usr/bin/env python

import xlrd

filename = 'yourexcel.xlsx'

wb = xlrd.open_workbook(filename)

ws = wb.sheet_by_name('Sheet1')

dataset = []

for r in xrange(ws.nrows):
    col = []
    for c in range(ws.ncols):
        col.append(ws.cell(r, c).value)
    dataset.append(col)

