#!/usr/bin/python3
"""
  script that takes in an argument and displays all values in the states
   table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
import sys

def main():
  """
    Function to display the values in a table
     where name matches an argument
  """
  
  username = sys.argv[1]
  password = sys.argv[2]
  db_name = sys.argv[3]
  state_name = sys.argv[4]

  db = MySQLdb.connect(
       host="localhost",
       port=3306,
       user=username,
       passwd=password,
       db=db_name
   )

  cursor = db.cursor() 

  cursor.execute(
              "SELECT * FROM states WHERE name=%s ORDER BY id ASC", (state_name,)
  )

  results = cursor.fetchall()
  for row in results:
    print(row)

  cursor.close()
  db.close()

if __name__ == "__main__":
  main()
