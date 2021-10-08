import xlwings as xw

# Đặt đường dẫn đầy đủ tên file là
# path_full = "D:\MyBook_PyExcel\xlwings\read_Datas\movies.xls"

# Cách 2: thêm ký tự r và gán trực tiếp phương thức Book
excel_movies = xw.Book(r"D:\MyBook_PyExcel\xlwings\read_Datas\movies.xls")

print(excel_movies.name)