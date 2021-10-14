import xlwings as xw

# Nhập hàm từ thư viện xlwings, chứa trong folder
from xlwings.constants import DeleteShiftDirection

# Kích hoạt wb 
wb = xw.books.active
sh = wb.sheets["DS_xeploai"]

# Bỏ in đậm ô A1
sh.range('A1').api.Font.Bold = False

# In đậm dòng 1
sh.range('1:1').api.Font.Bold = True

"Tương tự bạn thực hiện tìm hiểu"

sh.range('B:B').api.Font.Bold = True #In đậm 1 cột
sh.range('B:B').api.Font.Italic = True #In nghiêng 1 cột
sh.range('B:B').api.Font.Underline = True #In nghiêng 1 cột
sh.range('B:B').api.Font.Name = "Tahoma" #Thay kiểu chữ
sh.range('B:B').api.Font.Size = 15 #Thay kiểu chữ
sh.range('B:B').api.Font.ColorIndex = 5 #Thay màu chữ
sh.range('B:B').api.Font.ColorIndex = 5 #Thay màu chữ
sh.range('B:B').api.WrapText = True # Tự động xuống dòng

"Một số thuộc tính không cần thực qua API"
sh.range('B:B').color = (255,255,0) # Thay màu nền
sh.range('B:B').autofit() # Tự động dãn cột vừa chữ
