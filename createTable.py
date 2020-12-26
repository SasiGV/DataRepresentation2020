import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="datarepresentation"
)

cursor = db.cursor()
sql="CREATE TABLE Stock (id INT AUTO_INCREMENT PRIMARY KEY, category VARCHAR(50), name VARCHAR(255), quantity INT) "

cursor.execute(sql)


