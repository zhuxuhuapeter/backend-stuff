
import sys
import mariadb
# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="123456",
        host="127.0.0.1",
        port=3306,
        database="northwind"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()
cur.execute(
    "SELECT FirstName FROM employees")
   
    # Print Result-set
for (FirstName) in cur:
    print(f"First Name: {FirstName}")