import threading
import time

class MyThread(threading.Thread): #Kế thừa model threading, class Thread
    # Khởi tạo theo phương thức ghi đè
    def __init__(self, name, counter, delay):
        # Thực hiện ghi đè lên contructer (cấu trúc) của model threading, class Thread
        threading.Thread.__init__(self)
        self.name = name
        self.counter = counter
        self.delay = delay

    # run là Phương thức có sẵn khi star nó sẽ khởi động chạy
    def run(self):
        print(f'Bắt đầu chạy {self.name}')
        # Lay lock de dong bo hoa cac thread
        threadLock = threading.Lock()
        threadLock.acquire()

        while self.counter:
            time.sleep(self.delay)
            print(f'{self.name} {time.ctime()}')
            self.counter -=1
        
        # Giai phong lock cho thread ke tiep
        threadLock.release()
        print(f'Kết thúc {self.name} {time.ctime()}')
try:
    threads =[]
    th1= MyThread("Thread1", 5, 1)
    th2= MyThread("Thread2", 5, 2)
    th1.start()
    th2.start()
    
    # Sử dụng phương thức join để chờ các Thread thực hiện xong xuất kết quả cùng 1 lúc
    threads.append(th1)
    threads.append(th2)
    for thr in threads:
        thr.join() #Thêm join để đợi kết quả các thread cùng hoàn thành
    print("Hoàn thành các Threads", time.ctime())
    

except:
    print('Lỗi')
