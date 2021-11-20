import xlwings as xw

# Tìm vùng có chứa dữ liệu
def tim_DongCuoi_CotCuoi(sh):
    lr_table = sh.cells.last_cell.row    
    lc_table = sh.cells.last_cell.column   
    lr_data = sh.range('C'+ str(lr_table)).end('up').row  
    lc_data = sh.range(5, lc_table).end('left').column   
    table_datas = sh.range((5,1), (lr_data,lc_data))   
    return table_datas

# Đọc file Excel
def readExcel(file_Input):    
    """Đoạn này tránh lỗi file chưa tắt"""
    try: 
        excel = xw.Book(file_Input)
    except:
        print("File này đang được mở")
    return excel    

# Bảng tổng hợp chấm công
def tonghop_Cong(excel):
    # Khai báo các biến cần thiết
    tieude = ['STT','Họ và tên','ID','Vị trí'] #Tiêu đề cố định
    soSheet = len(excel.sheets) 
    soPtu_Dong = len(tieude)+soSheet
    
    data_TongHop = []   
    check_Id = [] # Thêm id duy nhất vào list    
    # Bắt đầu lấy dữ liệu
    demSoNgayDaChamCong = 1 # tương ứng số ngày chấm công
    for sh in excel.sheets:       
        if sh.name != 'Tong':
            tieude.append('Ngày '+ sh.name) # Thêm ngày công vào tiêu đề             

            dataOfSheet = tim_DongCuoi_CotCuoi(sh)# Tìm địa chỉ bảng dữ liệu
            dataOfSheet = dataOfSheet.value # Lấy giá trị trong bảng
            
            # Lọc qua từng dòng dữ liệu
            for i_row in range(len(dataOfSheet)):
                ten = dataOfSheet[i_row][1]
                id = dataOfSheet[i_row][2]
                # if id != None and ten != None:
                # Tạo list có chứa phần tử rỗng = ptử tieu de + so sheet cần lấy dữ liệu
                list_row = [0 for i in range(soPtu_Dong)]
                # list_row[-1] = 0

                if id not in check_Id: # Check id chưa có
                    check_Id.append(id) #Thêm id vào
                    list_row[0:4] = dataOfSheet[i_row][0:4] # dữ liệu cho tiêu đề cố định
                    list_row[3+demSoNgayDaChamCong] = dataOfSheet[i_row][-1] # dữ liệu cho ngày chấm công
                    data_TongHop.append(list_row)
                    # Thay đổi số thứ tự
                    data_TongHop[i_row][0] = i_row+1
                    #Số công
                    
                    data_TongHop[i_row][-1] = dataOfSheet[i_row][-1]
                else: 
                    # id trong check_Id
                    viTriThayThe = check_Id.index(id)
                    data_TongHop[viTriThayThe][3+demSoNgayDaChamCong] = dataOfSheet[i_row][-1]
                    #Cộng dồn ngày công 
                    print(data_TongHop[viTriThayThe][-1], dataOfSheet[i_row][-1])                   
                    
                    data_TongHop[viTriThayThe][-1] += dataOfSheet[i_row][-1]
            demSoNgayDaChamCong += 1
    # Thêm tiêu đề Tổng cộng
    tieude.append('Tổng cộng')
    data_TongHop.insert(0, tieude)
    return data_TongHop

def main():
    excel = readExcel("ChamCong.xlsx")
    out_data = tonghop_Cong(excel)
    excel.sheets('Tong').range('A3').value = out_data
    
    

            # print(dataOfSheet.address)
if __name__=='__main__':
    main()