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

list_2D = [[4,5],
           [6,7],
           [8,9]]

# Ghi dữ liệu list 2D
sh_test.range("A2").value = list_2D
