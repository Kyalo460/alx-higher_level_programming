#!/usr/bin/python3
"""matches the argument."""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         database=sys.argv[3])

    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC",
        [sys.argv[4]])
    for row in cur.fetchall():
        print(row)
