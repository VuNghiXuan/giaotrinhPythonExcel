import xlwings as xw

wb = xw.books.active
sh = wb.sheets["DS_xeploai"]

# sh.range("3:3").insert() # Chèn 1 dòng
sh.range("3:7").insert() # Chèn nhiều dòng
# sh.range("F:F").insert() # Chèn 1 cột
sh.range("F:G").insert() # Chèn nhiều cột


# "Định dạng so sánh ngày tháng qua đoạn code sau:";
# from datetime import datetime

# list_day = [['19/08/2020'], ['30/12/2022'], ['30/5/2021'], ['30/11/2021']]
# sh.range('A5').value =list_day

# to_day = datetime.strptime('14/10/2021', '%d/%m/%Y')

# for i_cell in range(len(list_day)):
#     rng = datetime.strptime(sh.range(f'A{5 + i_cell}').value, '%d/%m/%Y')
#     if rng > to_day:
#         sh.range(f'A{5 + i_cell}').color = (255,0,0)