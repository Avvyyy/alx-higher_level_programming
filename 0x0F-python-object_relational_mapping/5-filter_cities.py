#!/usr/bin/python3

"""List all cities of a state"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()
    state_name = sys.argv[4]
    
    # Use parameterized queries to prevent SQL injection
    cur.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id;", (state_name,))
    
    cities = cur.fetchall()
    
    # Check if any cities were found
    if cities:
        city_names = [city[0] for city in cities]
        print(', '.join(city_names))
    else:
        print()

    cur.close()
    db.close()
