#!/usr/bin/env python

'''
@author: puneet.reddy@gmail.com
@created: 2020-10-23
@blurb: A simple csv reader with the option to show if some rows are failing
    to import correctly.
    Returns a list of lists where each inner list corresponds to a csv row.
    Throws an AttributeError in case of failure.
TODO: Add sparseness tollerance
TODO: Process/clean footer rows
TODO: Guess data types for the differentcolumns
'''

def read_csv(filename, options=None, **kwargs):
    if not options:
        options = {
            'line_terminator': '\n',
            'delimiter': ',',
            'quote_char': '"',
            'header': 1
        }
    terminator, delimiter, quote_char, header = options.values()
    for key, val in kwargs.items():
        if key in options:
            options[key] = val
    with open(filename, 'r', encoding='utf-8') as fp:
        data = fp.read() 
    _rows = data.split(terminator)
    header_row = _rows[:header]
    rows = []
    separator_sequence = f'{quote_char}{delimiter}{quote_char}'
    validation_dict = {}
    for row in _rows[header:]:
        row.strip(quote_char)
        cells = row.split(separator_sequence)
        cell_count = len(cells)
        if cell_count in validation_dict:
            validation_dict[cell_count] += 1
        else:
            validation_dict[cell_count] = 1
        rows.append(cells)
    return header_row, rows, validation_dict
