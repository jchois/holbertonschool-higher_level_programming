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
    cur.execute("SELECT cities.id, cities.name, states.name FROM states\
                 JOIN cities ON states.id=cities.state_id\
                 WHERE states.name = %s ORDER BY id ASC", (argv[4], ))
    rows = cur.fetchall()
    new_list = []
    for row in rows:
        new_list.append(row[0])
    print(", ".join(new_list))
    cur.close()
    db.close()
