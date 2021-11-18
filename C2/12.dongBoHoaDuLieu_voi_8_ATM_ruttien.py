import time
import threading

class TaiKhoan:
    def __init__(self, name, soDu):
        self.name = name
        self.soDu = soDu

# Viết hàm chương trình rút tiền
def ruttien(taikhoan, soTienRut):
    soDu = taikhoan.soDu
    if soDu> 0:
        if soTienRut > soDu: #Số tiền rút > số dư tài khoản
            print(f"Số tiền rút chỉ là: {soDu} (đồng)")
            soDu  -= soDu
            taikhoan.soDu = soDu
            print(f"Cập nhật số dư hiện nay là: {soDu} (đồng)")
        elif soTienRut > 10: # Số tiền rút > 10 triệu cho phép
            soTienRut = 10
            print(f'Số tiền tối đa rút là: {soTienRut}')
            soDu  -= soTienRut
            taikhoan.soDu = soDu
            print(f"Cập nhật số dư hiện nay là: {soDu} (đồng)")

        else:
            soDu  -= soTienRut
            taikhoan.soDu = soDu
            print(f"Cập nhật số dư hiện nay là: {soDu} (đồng)")
    else:
        print(f"Tài khoản đã hết tiền!!!")

taikhoan = TaiKhoan("VuNghiXuan", 55)
print(f'Tên tài khoản: {taikhoan.name}. Số dư: {taikhoan.soDu}')

print("Các giao dịch rút tiền")
timeBegin = time.time()
"Phân luồng cho các ATM hoạt động";
for i_ATM in range (8):
    print(f'Rút lần thứ {i_ATM+1}:')
    ruttien(taikhoan, 12)
print(f'Tổng thời gian thực hiện {time.time()-timeBegin}')



