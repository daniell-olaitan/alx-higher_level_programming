#!/usr/bin/python3
"""
script lists all 'states' from the db 'hbtn_0e_usa' that match the given arg
and safe from sql injection
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], database=argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states \
             WHERE name LIKE BINARY %s \
             ORDER BY id"
    cur.execute(query, (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
