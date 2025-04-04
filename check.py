import sqlite3

conn = sqlite3.connect('database.db')  # Connect to the database
c = conn.cursor()

# Check if the 'questions' table exists
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = c.fetchall()
print(tables)  # This should include 'questions'

conn.close()
