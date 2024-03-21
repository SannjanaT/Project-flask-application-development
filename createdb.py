import sqlite3

conn = sqlite3.connect('users.db')
print("Opened database successfully")

conn.execute("CREATE TABLE users (first_name TEXT, last_name TEXT, email_address TEXT, password TEXT)")
print("Table successfully created")

conn.close()
