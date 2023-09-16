#!/usr/bin/python3
"""
Program to retrieve states from a MySQL database
"""

import MySQLdb
import sys

def main():
    """
    Main function to retrieve and print states from the database.
    """
    # Check if all required command-line arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Execute the SQL query to retrieve the list of states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all the results and print them
        results = cursor.fetchall()
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
    finally:
        # Close the database connection
        if 'db' in locals() and db is not None:
            cursor.close()
            db.close()

if __name__ == "__main__":
    main()

