# Write a script that demonstrates a try/except/else statement.
# For example, you can revisit the course module about database interactions
# and include a try/except/else statement based on what to do whether or not
# the database connection can be established.


#The sqlite3 module was written by Gerhard Häring. It provides an SQL interface compliant with the DB-API 2.0 specification described by PEP 249, and requires SQLite 3.7.15 or newer.

import sqlite3

def connect_to_database(dbCarmenAI):
    try:
        # Try to establish a database connection
        conn = sqlite3.connect(dbCarmenAI)
    except sqlite3.Error as e:
        # This block will execute if an exception is raised when trying to connect
        print("An error occurred while connecting to the database:", e)
    else:
        # This block will execute if no exceptions were raised
        print("Connected to the database CarmenAI successfully.")
        # Perform database operations here
        # ...
        # Close the database connection at the end
        conn.close()

# Replace 'example.db' with the actual database name
connect_to_database('example.db')
