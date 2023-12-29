import sqlite3
conn = sqlite3.connect("database.db")
print("Opened database successfully")
conn.execute("CREATE TABLE STUDENTS(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, address TEXT, pin TEXT)")
print("Database created successfully")
conn.close()