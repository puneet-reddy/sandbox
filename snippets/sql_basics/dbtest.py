#!/usr/bin/env python

import sqlite3


def Main():
    try:
        con = sqlite3.connect('test.db')
        cur = con.cursor()
        cur.execute("CREATE TABLE Pets(Id INT, Name TEXT, Price INT)")
        pets = (
            (1, 'Cat', 200),
            (2, 'Dog', 300),
            (3, 'Rat', 20),
            (4, 'Elephant', 2000),
            (5, 'Naga', 400)
        )
        cur.executemany("insert into Pets values (?, ?, ?)", pets)
        con.commit()
        cur.execute('select * from pets')
        data = cur.fetchall()
        for row in data:
            print(row)
    except sqlite3.Error as err:
        print("Exception caught: ", str(err))
        if con:
            print("Error! Rolling back")
            con.rollback()
    finally:
        if con:
            con.close()


if __name__ == '__main__':
    Main()
