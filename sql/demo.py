import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Emmanuel111*"
)

cursor = conn.cursor()

cursor.execute("USE test")
cursor.execute("SELECT * FROM users")
row = cursor.fetchall()

print(row)

