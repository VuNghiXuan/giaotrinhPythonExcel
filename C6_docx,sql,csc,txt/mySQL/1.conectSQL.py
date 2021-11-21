import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Vu05291922"
)

# Tạo database
mycursor =  mydb.cursor()
"Tạo DataBase mới";
# createDB.execute("CREATE DATABASE myDataFromPython")

"Show tất cả database"
# mycursor.execute("SHOW DATABASES")
# for cursor in mycursor:
#   print(cursor)

"Đặt biến 1 DB"
db_Python = 'myDataFromPython'
print(db_Python)


