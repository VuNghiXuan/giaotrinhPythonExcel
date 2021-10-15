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
 

# "Định dạng so sánh ngày tháng qua đoạn code sau:";
# from datetime import datetime

# list_day = [['19/08/2020'], ['30/12/2022'], ['30/5/2021'], ['30/11/2021']]
# sh.range('A5').value =list_day

# to_day = datetime.strptime('14/10/2021', '%d/%m/%Y')

# for i_cell in range(len(list_day)):
#     rng = datetime.strptime(sh.range(f'A{5 + i_cell}').value, '%d/%m/%Y')
#     if rng > to_day:
#         sh.range(f'A{5 + i_cell}').color = (255,0,0)