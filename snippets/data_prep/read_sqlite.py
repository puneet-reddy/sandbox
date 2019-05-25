#!/usr/bin/env python

import sqlite3
import sys

if len(sys.argv) < 2:
    print("Error: Need to supply a sql script")
    print("Usage: {} table.db ./sql-dump.sql".format(sys.argv[0]))
    sys.exit(1)

script_path = sys.argv[1]

if len(sys.argv) == 3:
    db = sys.argv[2]
else:
    db = ':memory:'


resultset = None

try:
    con = sqlite3.connect(db)
    with con:
        cur = con.cursor()
        with open(script_path, 'rb') as f:
            cur.executescript(f.read())
        resultset = cur.fetchall()
        col_names = [cn[0] for cn in cur.description]
except sqlite3.Error as err:
    print("Error occurred: {}".format(err))