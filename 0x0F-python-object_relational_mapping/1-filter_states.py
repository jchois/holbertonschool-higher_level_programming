#!/usr/bin/python3
"""
script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    database = argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=passwd, db=database)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        if state[1][0] is 'N':
            print(state)
    cur.close()
    db.close()
