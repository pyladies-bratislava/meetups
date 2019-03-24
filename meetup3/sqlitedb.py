import sqlite3

# Connect to the database
connection = sqlite3.connect('chinook.db')

cursor = connection.cursor()
sql = "SELECT COUNT(*) FROM artists;"
cursor.execute(sql)
result = cursor.fetchone()
print(result)
connection.close()
