# Nhập vào các danh sách học sinh Lớp Python_Excel gồm có 4 tổ 
To_1 = ["An", "Cường", "Đào", "Thịnh"]
To_2 = ["Thúy", "Mận", "Khang"]
To_3 = ["Phú", "Loan", "Duyên", "Thái"]
To_4 = ["Hạnh", "Hồng", "Nhật", "Nguyệt", "Cang"]

# Giả sử có thêm 1 bạn vào tổ 3; Ta sử dụng phương thức append() để nới rộng list như sau:
To_3.append("Dần")

# Cách sắp xếp các tổ thành danh sách lớp
lop_pyExcel = To_1 + To_2 + To_3 + To_4

# In ra danh sách Lớp Python_Excel
print(f"Danh sách lớp lop_pyExcel: {lop_pyExcel}. Có tổng cộng: {len(lop_pyExcel)} (người) ")

# In ra Tên người thứ 2 trong tổ 3
print("Tên người đầu tiên trong tổ 1 là:", To_1[0])

# In ra Tên người thứ 2 trong tổ 3
print("Tên người thứ 2 trong tổ 3 là:", To_3[1])

# In ra Tên người cuối cùng trong tổ 2
print("Tên người cuối cùng trong tổ 2 là:", To_2[-1])

# In ra Người từ thứ 1 đến người thứ 3 trong tổ 4
print("Người từ thứ 1 --> thứ 3 trong tổ 4 là:", To_2[0:4])
