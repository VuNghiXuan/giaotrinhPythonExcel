import xlwings as xw

"Khai báo đường dẫn cụ thể file input và output";

# Đường dẫn file input (file "movies.xls" chứa trong thư mục "read_Datas")
path_input = 'D:\\MyBook_PyExcel\\xlwings\\read_Datas\\movies.xls'

# Đường dẫn file output, file lưu (file "C3_save_movies.xls" chứa trong thư mục "read_Datas")
path_output = 'D:\\MyBook_PyExcel\\xlwings\\save_Datas\\C3_save_movies.xls'

# Đặt tên biến app = App Excel
app = xw.App()

# Mở đọc file input (movies.xls)
wb = app.books.open(path_input)

# Lưu file output (C3_save_movies.xls)
wb.save(path_output)

# In ra thông tin file output
print(f'Tên bảng tính là: {wb.name}\nĐường dẫn file: "{wb.fullname}"')

# Đóng workbook
wb.close()

# Thoát khỏi 1 ứng dụng Excel hiện hành. 
app.quit() 

# Thoát khỏi các ứng dụng Excel.
# for app in xw.apps:
#     app.quit
