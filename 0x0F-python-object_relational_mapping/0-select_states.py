#!/user/bin/python3
"""Module that lists all states fomr mySQL database"""
import sys
import mySQLdb

def list_states(username, password, database):
    # Connect to the mySQL server
    db = mySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Execute the SQL query to fetch all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the the rows from the query result
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the database connection
    db.close()

    # Example usage
    if __name__ == '__main__':
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        list_states(username, password, database) 
