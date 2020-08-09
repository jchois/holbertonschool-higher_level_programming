#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM states\
                 JOIN cities ON states.id=cities.state_id\
                 WHERE states.name = %s ORDER BY cities.id ASC", (argv[4], ))
    rows = cur.fetchall()
    print(", ".join([row[1] for row in rows]))
    cur.close()
    db.close()
