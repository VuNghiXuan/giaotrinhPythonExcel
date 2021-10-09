import xlwings as xw

# Đặt tên biến app = App Excel
app = xw.App()

# Đặt biến path_full làm tên đường dẫn đầy đủ
path_full = 'D:\\MyBook_PyExcel\\xlwings\\read_Datas\\movies.xls'
"Đường dẫn thay bằng '\\' để tránh lỗi (mình đã giải thích bài trên)";

# Đặt biến wb (bảng tính Excell), mở bằng đoạn code sau
wb = app.books.open(path_full)

# In ra Terminal tên bảng tính, và đường dẫn đầy đủ file
print(f'Tên bảng tính là:{wb.name}\nĐường dẫn file:{wb.fullname}')

# Thoát khỏi ứng dụng
app.quit()