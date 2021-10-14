import xlwings as xw
from xlwings import constants

# Nhập hàm từ thư viện xlwings, chứa trong folder
from xlwings.constants import DeleteShiftDirection

# Kích hoạt wb 
wb = xw.books.active
sh = wb.sheets["DS_xeploai"]

# Bỏ in đậm ô A1
sh.range('A1').api.Font.Bold = False

# In đậm dòng 1
sh.range('1:1').api.Font.Bold = True

"Tương tự bạn thực hiện tìm hiểu các đoạn code sau:";

sh.range('B:B').api.Font.Bold = True #In đậm 1 cột
sh.range('B:B').api.Font.Italic = True #In nghiêng 1 cột
sh.range('B:B').api.Font.Underline = True #In nghiêng 1 cột
sh.range('B:B').api.Font.Name = "Tahoma" #Thay kiểu chữ
sh.range('B:B').api.Font.Size = 15 #Thay kiểu chữ
sh.range('B:B').api.Font.ColorIndex = 5 #Thay màu chữ
sh.range('B:B').api.WrapText = True # Tự động xuống dòng

" Canh chỉnh lề theo chiều ngang"
sh.range('B:B').api.HorizontalAlignment = constants.HAlign.xlHAlignLeft # Canh trái
sh.range('B:B').api.HorizontalAlignment = constants.HAlign.xlHAlignCenter # Canh giữa
sh.range('B:B').api.HorizontalAlignment = constants.HAlign.xlHAlignRight # Canh trái

" Canh chỉnh lề theo chiều dọc"
sh.range('B:B').api.VerticalAlignment = constants.VAlign.xlVAlignTop # Canh trên
sh.range('B:B').api.VerticalAlignment = constants.VAlign.xlVAlignCenter # Canh giữa
sh.range('B:B').api.VerticalAlignment = constants.VAlign.xlVAlignBottom # Canh dưới

" Xoay chữ theo chiều"
sh.range('B1').api.Orientation = constants.Orientation.xlVertical # Xoay chiều dọc
sh.range('B2').api.Orientation = constants.Orientation.xlHorizontal # Xoay chiều ngang
sh.range('B3').api.Orientation = constants.Orientation.xlDownward # Xoay xuống dưới
sh.range('B4').api.Orientation = constants.Orientation.xlUpward # Xoay lên trên

"Một số thuộc tính không cần thực qua API";
sh.range('B:B').color = (255,255,0) # Thay màu nền
sh.range('B:B').autofit()  # Tự động dãn cột vừa chữ
sh.range('F1:G1').merge() # Trộn 2 hay nhiều ô thành 1
sh.range('F1:G1').unmerge() # Bỏ trộn ô
