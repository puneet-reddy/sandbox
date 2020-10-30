#!/usr/bin/env python

'''
@author: Puneet Reddy
@created: 2020-10-26
@blurb: A quick test to see how well bcpy works from importing csv data
    to a sql table.
'''

import bcpy


sql_config = {
    'server': 'awslabapse1w003.ad.csscorp.com',
    'database': 'Alcatel',
    'username': 'sa',
    'password': 'Slash!23'
}

sql_table_name = 'bcpy_open_date'
csv_file_path = r'C:\Users\css112720\Desktop\aruba\automation\data\report1603438156112_opn\sample.csv'
flat_file = bcpy.FlatFile(qualifier='', path=csv_file_path)
sql_table = bcpy.SqlTable(sql_config, table=sql_table_name)
flat_file.to_sql(sql_table)