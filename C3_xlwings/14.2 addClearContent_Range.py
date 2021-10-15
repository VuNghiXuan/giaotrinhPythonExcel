import xlwings as xw

wb = xw.books.active
sh = wb.sheets["DS_xeploai"]

"Cách thêm nội dung";
sh.range('A1').value = "Thêm nội dung ô A1"
sh.range('A2').value = "Thêm nội dung ô A2"

# Nối nội dung ô A1 và ô A2 thành chuỗi mới
sh.range('A3').value = sh.range('A1').value + " " + sh.range('A2').value
sh.range('A4').value = "=Concatenate(A1,char(32),A2)" # char(32): khoảng trắng
sh.range('A5').value = "=Concatenate(A1,char(10),A2)" # char(10): Xuống dòng
# ô A3, A4 cùng kết quả >>> "Thêm nội dung ô A1 Thêm nội dung ô A2"

"Xóa nội dung";
sh.range('A4').clear() #Xóa nội dung ô A4
