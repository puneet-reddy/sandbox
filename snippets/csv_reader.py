#!/usr/bin/env python

'''
@author: puneet.reddy@gmail.com
@created: 2020-10-23
@blurb: A simple csv reader with the option to show if some rows are failing
    to import correctly.
    Returns a list of lists where each inner list corresponds to a csv row.
    Throws an AttributeError in case of failure.
TODO: Figure out how to deal with only a few quoted fields.(Use regex maybe?)
TODO: Add sparseness tollerance
TODO: Process/clean footer rows
TODO: Guess data types for the differentcolumns
'''

class CSVReader:
    def __init__(self, filename, options=None, **kwargs):
        self.filename = filename
        defaults = {
            'terminator': '\n',
            'delimiter': ',',
            'quote_char': '"',
            'header': 1
        }
        options = options or defaults
        options = {**defaults, **options}
        for key, val in kwargs.items():
            if key in options:
                options[key] = val
        self.__dict__ = {**self.__dict__, **options}
    
    def read_csv(self):
        with open(self.filename, 'r', encoding='utf-8') as fp:
            data = fp.read()
        _rows = data.split(self.terminator)
        header_row = _rows[self.header - 1]
        rows = []
        bad_rows = []
        sep = f'{self.quote_char}{self.delimiter}{self.quote_char}'
        header_row = header_row.strip(self.quote_char)
        header_row = header_row.split(sep)
        expected = len(header_row)
        for idx, row in enumerate(_rows[self.header:]):
            row.strip(self.quote_char)
            cells = row.split(sep)
            cell_count = len(cells)
            if cell_count == expected:
                rows.append(cells)
            else:
                bad_rows.append(idx+1)
        return header_row, rows, bad_rows
        

if __name__ == '__main__':
    reader = CSVReader('/home/puneet/Downloads/sample.csv')
    head, data, bad_rows = reader.read_csv()
    print(f"Headers: {head}")
    print(f"Processed {len(data)} rows - Rows:{bad_rows} had bad data")
    
    
