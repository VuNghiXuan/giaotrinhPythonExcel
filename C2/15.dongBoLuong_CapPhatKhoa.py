import time
import threading

class TaiKhoan:
    def __init__(self, name, soDu):
        self.name = name
        self.soDu = soDu
        # self.counter = counter #Biến đếm

# Viết hàm chương trình rút tiền
def ruttien(taikhoan, lock, soTienRut):
    
    # đồng bộ dữ liệu giữa các luồng
    lock.acquire() 
    # Cập nhật số dư tại thời điểm cho luồng mới
    soDu = taikhoan.soDu    
    print(str(threading.current_thread().getName()))
    count = 0
    while count < 10:
        # time.sleep(1)
        if soTienRut > soDu: #Số tiền rút > số dư tài khoản
            print(f"Số tiền rút chỉ là: {soDu} (đồng)")
            soTienRut = soDu
            soDu  -= soDu
            taikhoan.soDu = soDu
            count +=1

            print(f"Lần rút {count}: Số tiền rút: {soTienRut} (đồng). Tài khoản đã hết tiền!!!")
        elif soTienRut > 10: # Số tiền rút > 10 triệu cho phép
            soTienRut = 10
            print(f'Số tiền tối đa rút là: {soTienRut}')
            soDu  -= soTienRut
            taikhoan.soDu = soDu
            count +=1

            print(f"Lần rút {count}: Số tiền rút: {soTienRut} (đồng). Cập nhật số dư hiện nay là: {soDu} (đồng)")
        else:
            soDu  -= soTienRut
            taikhoan.soDu = soDu
            count +=1
            print(f"Lần rút {count}: Số tiền rút: {soTienRut} (đồng). Cập nhật số dư hiện nay là: {soDu} (đồng)")     
        
    "Gỡ bỏ khóa luồng hiện tại";
    lock.release()
    
def main():
    "Cấp phát khóa cho luồng và đồng bộ dữ liệu các luồng";
    lock = threading.Lock() #cấp khóa

    taikhoan = TaiKhoan("VuNghiXuan", 105)
    print(f'Tên tài khoản: {taikhoan.name}. Số dư: {taikhoan.soDu}')

    print("Các giao dịch rút tiền")
    timeBegin = time.time()

    "Phân luồng cho các ATM hoạt động";
    try:   
       
        # Máy 1
        atm_1 = threading.Thread(target = ruttien, args= (taikhoan, lock, 3))
        atm_1.setName("ATM 1")
       
        # Máy 2
        atm_2 = threading.Thread(target = ruttien, args= (taikhoan, lock, 5))
        atm_2.setName("ATM 2")
        
        # Máy 3
        atm_3 = threading.Thread(target = ruttien, args= (taikhoan, lock, 12))  
        atm_3.setName("ATM 3")        

        # Bắt đầu chạy luồng
        atm_1.start()    
        atm_2.start()    
        atm_3.start()    
    except: 
        print("Có lỗi xảy ra giữa các luồng!!!")

    "Dùng join tham gia chờ luồng";
    # Thiết bị ATM gồm 3 máy
    thietbi_ATM = []
    thietbi_ATM.append(atm_1)
    thietbi_ATM.append(atm_2)
    thietbi_ATM.append(atm_3)
    for may in thietbi_ATM:
        may.join()

    print(f'Tổng thời gian thực hiện {time.time()-timeBegin}')

if __name__ == "__main__":
    main()


