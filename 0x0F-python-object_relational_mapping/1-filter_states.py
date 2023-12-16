#!/usr/bin/python3
"""a script that lists all states with a name starting with N."""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         database=sys.argv[3])

    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
