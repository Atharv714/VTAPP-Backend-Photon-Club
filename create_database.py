# create_database.py

import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('event_database.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Drop the existing participants table (if it exists)
cursor.execute('DROP TABLE IF EXISTS participants')

# Create a new participants table with the updated schema
cursor.execute('''
    CREATE TABLE IF NOT EXISTS participants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        contact_number TEXT,
        event TEXT,
        payment_amount INTEGER,
        screenshot_path TEXT,
        registration_number TEXT
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
