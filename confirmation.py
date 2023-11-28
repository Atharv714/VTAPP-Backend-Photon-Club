import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('event_database.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a SELECT query to fetch data
cursor.execute('SELECT * FROM participants')

# Fetch all rows from the result set
rows = cursor.fetchall()

# Print the data
for row in rows:
    print(row)

# Close the connection
conn.close()

