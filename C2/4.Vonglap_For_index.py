# Nhập vào các danh sách học sinh Lớp Python_Excel gồm có 4 tổ 
colors = ["red", "green", "blue", "yellow", "white", "black"]
""" 
list colors màu trên có các chỉ số index lần lượt là:
    + Giá trị "red" -->index= 0
    + Giá trị "green" -->index= 1
    + Giá trị "blue" -->index= 2
    + Giá trị "yellow" -->index= 3
    + Giá trị "white" -->index= 4
    + Giá trị "black" -->index= 5
"""
# In ra giá trị màu xem có đúng theo chỉ số index trên không?
for i_color in range(len(colors)):
    print(f"Màu '{colors[i_color]}', có index là: {i_color}")  

