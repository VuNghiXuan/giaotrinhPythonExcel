class hocsinh():

    # Khởi tạo 1 đối là học sinh
    def __init__(self, ten, toan, ly, hoa):        
        self.ten = str(ten)
        self.toan = float(toan)
        self.ly = float(ly)
        self.hoa = float(hoa)

    # Phương thức tính điểm trung bình
    def diem_TB(self):
        self.avrg_score = round((self.toan +self.ly + self.hoa)/3,3)
        return self.avrg_score

    # Thuộc tính (Chiều cao, cân nặng)
    def ketqua(self):
        if self.avrg_score > 5:
            return "Đậu"
        else: return "Rớt"

hs = [hocsinh("Bắc Kiều Phong", 9, 10, 10),
      hocsinh("Nam Mộ Dung", 5, 6, 7),
      hocsinh("Nam Đế", 4, 5, 1),
      hocsinh("Bắc Cái", 10, 0, 1)]

for i_hs in range(len(hs)):
    print(f'{i_hs+1}. Tên học sinh: {hs[i_hs].ten}. Điểm toán: {hs[i_hs].toan}, lý: {hs[i_hs].ly}, hóa: {hs[i_hs].hoa}') 
    print(f'Điểm trung bình là: {hs[i_hs].diem_TB()}. Kết quả: {hs[i_hs].ketqua()}')

