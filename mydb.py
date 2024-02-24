import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Local@123",
)

cursor = database.cursor()

cursor.execute("CREATE DATABASE crm_")

print("All Done!")