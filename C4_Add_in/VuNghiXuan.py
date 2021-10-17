import xlwings as xw

def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[0]
    in_str = "" 
    idx = 0
    while idx<10:
        in_str += "oO!Oo"
        sheet.range(idx+1, idx+1).value = in_str
        idx += 1
    
@xw.func
def hello(name):
    return f"Hello {name}!"

if __name__ == "__main__":
    xw.Book("VuNghiXuan.xlsm").set_mock_caller()
    main()
