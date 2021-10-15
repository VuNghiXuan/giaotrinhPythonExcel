import xlwings as xw

wb = xw.books.active
sh = wb.sheets["DS_xeploai"]

rng = sh.range('F1:F5') 
valueErr = rng.options(empty='NA').value # cho phép lấy giá trị Lỗi

numErr = 0
for err in range(len(valueErr)):
    if valueErr[err] == 'NA':
        numErr += 1
        print("Giá trị lỗi ô:", rng[err].address)

print('Tổng các ô có lỗi là:', numErr)
