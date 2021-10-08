import xlwings as xw

# Đặt đường dẫn đầy đủ tên file là
# path_full = "D:\MyBook_PyExcel\xlwings\read_Datas\movies.xls"

# Cách 1: Thêm "\" vào trở thành "\\"
path_full = "D:\\MyBook_PyExcel\\xlwings\\read_Datas\\movies.xls"

# Mở file bằng phương thức xw.Book từ đg dẫn path_full và đặt tên biến là excel_movies
# excel_movies = xw.Book(r'D:\MyBook_PyExcel\xlwings\read_Datas\movies.xls')
excel_movies = xw.Book(path_full)

print(excel_movies.name)