import xlwings as xw
from xlwings import constants


def set_validation_list(rng, validation_list):
    if validation_list is None:
        validation_list = [' ']
        print('validation_list là giá trị None')
    if not isinstance(validation_list, list):
        raise TypeError('Biến validation_list không phải là list?')
    
    # VBA cung cấp các tham số cho Validation nnư sau:
    dv_type = constants.DVType.xlValidateList
    dv_alertstyle = constants.DVAlertStyle.xlValidAlertStop
    dv_operator = constants.FormatConditionOperator.xlEqual
    rng.api.Validation.Delete() #Xóa Validation chạy code trước đó
    rng.api.Validation.Add(dv_type, dv_alertstyle, dv_operator, ';'.join(validation_list))

wb = xw.books.active
sh = wb.sheets["DS_xeploai"]
rngGetData = sh.range('B2:B13')
rng_droplist = sh.range('F1')

# Lọc lấy giá trị duy nhất
value = rngGetData.value
unique_value = list(set(rngGetData.value)) # Hàm set: cho giá trị duy nhất
set_validation_list(rng_droplist, unique_value) # cho value vào cũng được