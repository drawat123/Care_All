import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="dr",
  password="Abcd@1234",
  database="CareAll",
  use_pure=True
)