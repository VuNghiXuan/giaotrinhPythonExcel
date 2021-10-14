import xlwings as xw

# Nhập hàm từ thư viện xlwings, chứa trong folder
from xlwings.constants import DeleteShiftDirection

# Kích hoạt wb 
wb = xw.books.active
sh = wb.sheets["DS_xeploai"]

# Xóa 1 dòng số 2
sh.range('2:2').api.Delete(DeleteShiftDirection.xlShiftUp)

# Xóa 1 cột F (cột tổng)
sh.range('F:F').api.Delete(DeleteShiftDirection.xlShiftUp)