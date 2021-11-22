import xlwings as xw

"Đoạn comment lại"
# path_input = 'D:\\MyBook_PyExcel\\xlwings\\read_Datas\\1.BangDiem.xlsx'

# # Mở workbook để xem trước dữ liệu
# xw.Book(path_input)
"----------"

# Sau khi wb được mở comment 2 dòng trên và thực hiện code sau 
wb = xw.books.active

# Kiểm tra file có tên sheet là "test", nếu không thì tạo sheets("test")
"Đoạn code trong vòng for này giúp bạn không bị lỗi khi chạy code nhiều lần với tên sheet 'test' đã tạo trước đó"
# Kiểm tra file có tên sheet là "test", nếu không thì tạo sheets("test")
"Đoạn code trong vòng for này giúp bạn không bị lỗi khi chạy code nhiều lần với tên sheet 'test' đã tạo trước đó"
sheetNames = ""
for sh in wb.sheets:
    # Nếu tên sheet không phải là "test"
    if sh.name != "test": 
        sheetNames += sh.name
    else: 
        # Nếu tên sheet là "test"           
        sheetNames += sh.name
        print("Đã tồn tại sheet có tên: 'test'")
        break  

# Kiểm tra sự tồn tại sheet test
if "test" not in sheetNames:
    sh_test = wb.sheets.add("test") #Tạo sheet("test") mới 
else: sh_test = wb.sheets("test") # Gán tên sheet("test") 
 
list_1D = [1,2,3]
datas = ['Nguyễn Văn A', 'Nguyễn Văn B']

# Cách 1: Ghi dữ liệu trên 1 dòng
sh_test.range("A1").value = list_1D
sh_test.range("A2").value = list_1D

# Cách 2: Ghi dữ liệu trên 1 dòng
sh_test.range("A3").value = datas

# Cách 3: Ghi theo vùng dữ liệu (range: nhiều cells) 
sh_test.range("E1").options(ndim=1).value = sh_test.range('A1:C3').value
