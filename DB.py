import mysql.connector

# Connect to the MySQL server running in XAMPP
conn = mysql.connector.connect(
    host="localhost",
    user="root",         # default user for XAMPP
    password="",         # default password is empty
    database="hamdani"    # replace with your DB name
)

cursor = conn.cursor()

# cursor# Example: Insert data into table
# query = "INSERT INTO users (name, email) VALUES (%s, %s)"
# values = ("Alice", "alice@example.com")
# cursor.execute(query, values)
#
# conn.commit()
#
# print("Data inserted successfully!")
cursor.execute("select * from studentinfo")
result = cursor.fetchall()
for row in result:
    print(row)
# Always close the connection
cursor.close()
conn.close()
