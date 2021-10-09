import xlwings as xw

# Khởi tạo App cho phép hiện ra màn hình
app = xw.App(visible = True) 

"""
Ghi chú:
    + visible=True: Nghĩa là cho phép hiện bảng tính mới vừa tạo
    + add_book = False": Nghĩa là không tạo thêm 01 bảng tính mới nữa
    + add_book: Không khai báo mặt định là False
"""

# In ra phiên bản app
print("Bản Excel là: ", app.version)



