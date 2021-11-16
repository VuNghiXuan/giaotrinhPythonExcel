class hocsinh():
    # Thêm 1 biến để đếm số học sinh
    soluong =  0
    # Khởi tạo 1 đối là học sinh
    def __init__(self, ten, toan, ly, hoa):        
        self.ten = str(ten)
        self.toan = float(toan)
        self.ly = float(ly)
        self.hoa = float(hoa)
        # Cách tăng class cho biến đếm
        hocsinh.soluong +=  1
    
    # Phương thức tính điểm trung bình
    def diem_TB(self):
        self.avrg_score = round((self.toan + self.ly + self.hoa )/3,3)
        return self.avrg_score

    # Phương thức tính điểm trung bình
    def ketqua(self):
        if self.avrg_score > 5:
            return "Đậu"
        else: return "Rớt"

# Class kế thừa
class hocsinh_VungCao(hocsinh):
    def __init__(self, ten, toan, ly, hoa, diemcong):
        # Khởi tạo diemcong cho học sinh nghèo 
        self.diemcong = diemcong
        # Cah1 kế thừa thuộc tính lớp cha như name, toan, ly. Mục đích không định nghĩa lại
        super(hocsinh_VungCao, self).__init__(ten, toan, ly, hoa)
        "Chú ý hàm super nhận 2 tham số khai báo trên. còn sau __initt__ là các thuộc tính kế thừa lại lớp hoc sinh";
    
    # Tính lại điểm trung bình cho hoc sinh vùng cao
    def diem_TB(self):
        self.avrg_score = round((self.toan +self.ly + self.hoa)/3 + int(self.diemcong),3)
        return self.avrg_score

hs = [hocsinh("Bắc Kiều Phong", 9, 10, 10),
      hocsinh("Nam Mộ Dung", 5, 6, 7),
      hocsinh("Nam Đế", 4, 5, 1),
      hocsinh_VungCao("Bắc Cái", 10, 0, 1, 2)]

for i_hs in range(len(hs)):
    print(f'{hs[i_hs].ten}. Có điểm trung bình {hs[i_hs].diem_TB()}. Kết quả: {hs[i_hs].ketqua()}')
print(f'Tổng số học sinh là: {hs[3].soluong}')
