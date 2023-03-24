#!/usr/bin/python3
"""
script lists all 'states' from the db 'hbtn_0e_usa' that match the given arg
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], database=argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states \
             WHERE name LIKE BINARY '{}' \
             ORDER BY id".format(argv[4])
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
