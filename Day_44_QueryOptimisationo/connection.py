import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="day_39_widow_functions"
)

print("Connected successfully!")

cursor = connection.cursor()

cursor.execute("select * from employees;")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
connection.close()
