import time
import threading

def tongcacso(cacSo):
    tong= 0
    for so in range(cacSo):
        tong += so
    # print(f"Tổng các số là: {tong}")

def hieucacso(cacSo):
    hieu = 0
    for so in range(cacSo):
        hieu -= so
    # print(f"Hiệu các số là: {hieu}")

def tichcacso(cacSo):
    tich = 1
    for so in range(cacSo):
        if so !=0:
            tich *= so
    # print(f"Tích các số là: {tich}")

listso=10**5

"Thực thi code không qua Thread";
print('Thực thi code qua từng hàm:')
t = time.time()
tong = tongcacso(listso)
hieu = hieucacso(listso)
tich = tichcacso(listso)

print('Tổng thời gian thực hiện lần lượt: ', time.time() -t)

"Phân luồng cho code chạy bằng class Thread trong model Threading"
try:
    "Thực thi code qua Thread";
    print('Thực thi code bằng Thread:')
    time_Tread = time.time()
    tong_Thread = threading.Thread(target=tongcacso, args=(listso,))
    hieu_Thread = threading.Thread(target=hieucacso, args=(listso,))
    tich_Thread = threading.Thread(target=tichcacso, args=(listso,))    

    tong_Thread.start()
    hieu_Thread.start()
    tich_Thread.start()
   

    # print(f"Tổng các số là: {tong_Thread}")
    # print(f"Tích các số là: {tich_Thread}") 
    print('Thời gian thực hiện các Thread song song: ', time.time() - time_Tread)   
    # print("Hoàn thành các Threads", time.ctime())
    
except:
    print('Lỗi')