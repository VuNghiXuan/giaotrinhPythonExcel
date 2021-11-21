import mysql.connector 

"""1. Kết nối với MySQL bằng Trình kết nối / Python"""
# Hàm connect()tạo tạo kết nối đến máy chủ MySQL và trả về một MySQLConnection đối tượng.
objConectSQl = mysql.connector.connect(user = 'root', password = 'Vu05291922', host = 'localhost') # host='127.0.0.1' tương đương 'localhost'

"""2. Kết nối class cusor bằng phương thức con trỏ (): chúng được ràng buộc với kết nối trong toàn bộ thời gian tồn tại và tất cả các lệnh được thực thi trong ngữ cảnh của phiên cơ sở dữ liệu được bao bọc bởi kết nối. """
myCursor = objConectSQl.cursor()

# # Thực thi lệnh bằng execute(), hiển thị liệt kê toàn bộ MySQL
# myCursor.execute('SHOW DATABASES')
# for cursor in myCursor:
#     print(cursor)
"""3. Tạo 1 DataBase mới"""
myCursor.execute('CREATE DATABASE TaoRa_DataBase_Moi') # TaoRa_DataBase_Moi: là tên data mới
objConectSQl.close() # Đóng kết nối
