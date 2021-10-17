import xlwings as xw

def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[0]
    list_RowsCols = [[15,21.56,32.98, 4.658],
                     ['Xuân', 'Lan', 'Thu', 'Cúc'],
                     ['Mặn', "chằn", "cả", "hai"]]   
    sheet.range('A1').value = list_RowsCols
        
    
@xw.func
def hello(name):
    return f"Hello {name}!"

if __name__ == "__main__":
    # set_mock_caller() dễ dàng chuyển qua lại gọi hàm giữa Python và Excel
    # Mã nguồn khuyến cáo file Excel và mã Python cùng folder.
    xw.Book("VuNghiXuan.xlsm").set_mock_caller()
    main()
