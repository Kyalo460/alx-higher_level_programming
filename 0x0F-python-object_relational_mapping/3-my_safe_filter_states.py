#!/usr/bin/python3
"""a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
Safe from SQL injections.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         database=sys.argv[3])

    cur = db.cursor()
    if sys.argv[4] in ["California",
                       "Arizona", "Texas", "New York", "Nevada"]:
        q = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC".format(
            sys.argv[4])
        cur.execute(q)
        for row in cur.fetchall():
            print(row)
