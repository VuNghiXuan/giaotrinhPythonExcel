import xlwings as xw

wb = xw.books.active
sh = wb.sheets["DS_xeploai"]

# sh.range("3:3").insert() # Chèn 1 dòng
sh.range("3:7").insert() # Chèn nhiều dòng
# sh.range("F:F").insert() # Chèn 1 cột
sh.range("F:G").insert() # Chèn nhiều cột

