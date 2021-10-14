import xlwings as xw

# path_input = 'D:\\MyBook_PyExcel\\xlwings\\read_Datas\\movies.xls'
# xw.Book(path_input)
wb = xw.books.active
sh1 = wb.sheets('1900s')
rng1 = sh1.range('A1:D5')

# sh_test = wb.sheets.add("test")
sh_test = wb.sheets("test")
sh_test.range("A1").value = rng1.value
sh_test.range("A7").options(transpose=True).value = rng1.value

print(sh1.name)