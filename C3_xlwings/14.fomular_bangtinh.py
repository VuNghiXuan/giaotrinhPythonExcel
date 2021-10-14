import xlwings as xw

"Đoạn comment lại"
# path_input = 'D:\\MyBook_PyExcel\\xlwings\\read_Datas\\1.BangDiem.xlsx'

# # Mở workbook để xem trước dữ liệu
# xw.Book(path_input)
"----------"

# Sau khi wb được mở comment 2 dòng trên và thực hiện code sau 
wb = xw.books.active
sh = wb.sheets["DS_xeploai"]

# Ghi vào cột F, G tiêu đề cột
sh.range("F1").value = ['Tổng', 'Điểm TB'] 

# Điền công thức tính tổng Ô F2
sh.range("F2").value = "=sum(C2:E2)"

# Điền công thức tính Trung bình ô G2
sh.range("G2").value = "=average(C2:E2)"

# Sao chép công thức Ô F2:G2 cho các dòng bên dưới
func_rng = sh.range("F2:G2").formula
sh.range("F2:G5").formula = func_rng
