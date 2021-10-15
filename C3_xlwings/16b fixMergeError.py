import xlwings as xw
from xlwings import constants

# Nhập hàm từ thư viện xlwings, chứa trong folder
from xlwings.constants import DeleteShiftDirection

# Kích hoạt wb 
wb = xw.books.active
sh = wb.sheets["DS_xeploai"]
rngCells = sh.range('C1:E1')

# Bước 1: Lưu dữ liệu vào 1 cái biến có giá trị 3 ô 
valueCells = ', '.join(rngCells.value)

# Nước 2: Xóa dữ liệu để merge không có thông báo
rngCells.clear()

# Bước 3: Thực hiện trộn ô merge
rngCells.merge() # Trộn 2 hay nhiều ô thành 1

# Bước 4: Dán lại dữ liệu
rngCells.value = valueCells
rngCells.color = (255,255,0) # Cho màu vàng ô
rngCells.api.Font.Bold = True
rngCells.api.HorizontalAlignment = constants.HAlign.xlHAlignCenter # Canh giữa