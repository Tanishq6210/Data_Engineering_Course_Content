import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "admin",
    database = "day_39_widow_functions"
)

print("Connection established!")

cursor = connection.cursor()

query = """
    update employees set salary = %s where employee_id = %s
"""

cursor.execute(query, (10000, 1))

connection.commit()

print("Value updated!")
cursor.close()
connection.close()