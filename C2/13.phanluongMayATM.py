import time
import threading

class TaiKhoan:
    def __init__(self, name, soDu):
        self.name = name
        self.soDu = soDu

# Viết hàm chương trình rút tiền
def ruttien(taikhoan, soTienRut):
    # name_Thread = threading.getNam()
    soDu = taikhoan.soDu
    while soDu>0:        
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
    
    print(f"Tài khoản đã hết tiền!!!")

taikhoan = TaiKhoan("VuNghiXuan", 105)
print(f'Tên tài khoản: {taikhoan.name}. Số dư: {taikhoan.soDu}')

print("Các giao dịch rút tiền")
timeBegin = time.time()

"Phân luồng cho các ATM hoạt động";
try:   
    # Thiết lập luồng cho 3 máy ATM
    atm_1 = threading.Thread(target = ruttien, args= (taikhoan, 10))
    atm_2 = threading.Thread(target = ruttien, args= (taikhoan, 10))
    atm_3 = threading.Thread(target = ruttien, args= (taikhoan, 10))   
    
    # Bắt đầu chạy luồng
    atm_1.start()    
    atm_2.start()    
    atm_3.start()    
except: 
    print("Có lỗi xảy ra giữa các luồng!!!")
print(f'Tổng thời gian thực hiện {time.time()-timeBegin}')



