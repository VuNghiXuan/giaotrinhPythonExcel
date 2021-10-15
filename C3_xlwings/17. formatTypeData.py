import xlwings as xw
from datetime import datetime as dt

wb = xw.books.active
sh = wb.sheets["DS_xeploai"]


from datetime import datetime

# Cách ghi 1 list giá trị trong Python
list_day = [['19/08/2020'], ['30/12/2022'], ['30/5/2021'], ['30/11/2021']]

"Ghi định dạng kiểu ngày tháng vào bảng tính";
sh.range('A11').options(dates=dt.date).value = list_day

"Định dạng ngày tháng list Python";
to_day = datetime.strptime('15/10/2021', '%d/%m/%Y')

# So sánh các ô trng bảng tính và ngày hiện tại
for i_cell in range(len(list_day)):
    rng = sh.range(f'A{11 + i_cell}')
    covertRngTime = datetime.strptime(rng.value, '%d/%m/%Y')
    if  covertRngTime > to_day:
        # Đánh dầu ô có giá trị > ngày '14/10/2021' trong bảng tính
        rng.color = (255,0,0)