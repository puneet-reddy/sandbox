#!/usr/bin/env python

'''
A simple example of using pdfkit
It needs wkhtmltopdf to be installed and on the system path
If you get a IOError: 'Command Failed', it usually means that pdfkit couldn't 
understand some input
'''

import pdfkit

#wkhtmltopdf options
options = {
    'page-size': 'A4',
    'margin-top': '0.0in',
    'margin-right': '0.0in',
    'margin-bottom': '0.0in',
    'margin-left': '0.0in',
    'encoding': "UTF-8",
    'custom-header' : [
        ('Accept-Encoding', 'gzip')
    ],
    'cookie': [
        ('cookie-name1', 'cookie-value1'),
        ('cookie-name2', 'cookie-value2'),
    ],
    'no-outline': None
}

pdfkit.from_string("This is a pdfkit test...", "out.pdf", options=options)
pdfkit.from_url("https://www.google.com", "google.pdf")
#pdfkit.from_file("somehtmlfile.html", "pdf_outpt.pdf")

