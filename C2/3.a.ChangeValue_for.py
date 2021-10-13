# Nhập vào các danh sách học sinh Lớp Python_Excel gồm có 4 tổ 
hop = ["Bánh", "Kẹo", "Viết", "Cục tẩy"]

# Số phần tử trong list
num_index = len(hop)

# Dùng vòng lặp for thay thế giá trị trong list
for idx in range(num_index):
    if hop[idx] == "Kẹo":
        hop[idx] = "Kim cương"
        break # break: Nghĩa là, khi tìm thấy điều kiện thì dừng và thoát khỏi vòng lặp
print(hop)
