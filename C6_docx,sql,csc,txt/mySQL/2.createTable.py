import mysql.connector

#  Thêm tham số database = 'taora_database_moi'
objConectSQl = mysql.connector.connect(user = 'root', host = 'localhost', password= 'Vu05291922', database = 'taora_database_moi')

myCursor = objConectSQl.cursor()

myCursor.execute("create table DS_NhanVien (id int (20) not null primary key," 
        + "name varchar(255),"
        + "address varchar(255))") 

objConectSQl.close() # Đóng kết nối