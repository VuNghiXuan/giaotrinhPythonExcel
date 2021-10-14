import xlwings as xw

"Đoạn comment lại"
# path_input = 'D:\\MyBook_PyExcel\\xlwings\\read_Datas\\1.BangDiem.xlsx'

# # Mở workbook để xem trước dữ liệu
# xw.Book(path_input)
"----------"

# Sau khi wb được mở comment 2 dòng trên và thực hiện code sau 
wb = xw.books.active
sh1 = wb.sheets('DS_xeploai')
rng1 = sh1.range('A1:E5')

# Kiểm tra file có tên sheet là "test", nếu không thì tạo sheets("test")
"Đoạn code trong vòng for này giúp bạn ko bị lỗi khi chạy code nhiều lần với tên sheet 'test' đã tạo trước đó"
for sh in wb.sheets:
    if sh.name == "test": 
        sh_test = sh.name
        print("Đã tồn tại sheet có tên: 'test'")
        break
    else:
        # Tạo 1 bảng tính có tên là "test"
        sh_test = wb.sheets.add("test")

# Ghi dữ liệu theo chiều gốc của bảng tính
sh_test.range("A1").value = rng1.value

# Đổi chiều dòng thành cột và ngược lại
sh_test.range("A8").options(transpose=True).value = rng1.value
