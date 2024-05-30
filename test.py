import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="devry123",
  database="pokedex"
)


cursor = mydb.cursor()

cursor.execute("SELECT P_Name from pokemon where P_Name = 'Charizard'")

name = cursor.fetchone()

for i in name:
    print(i)