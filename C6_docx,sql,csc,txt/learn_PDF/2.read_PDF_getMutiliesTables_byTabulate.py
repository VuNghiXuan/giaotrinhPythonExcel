import tabula as tb

pdf_path = "1768_6_DMBDTX.pdf"
out_file = "D:\ThanhVu\\code\python\\PyDPF\\DinhMuc_DuyTu_TT44\\Table"
#reads table from pdf file
df = tb.read_pdf(pdf_path, pages='all') #pages='1'
for ipage in range(len(df)):
    df[ipage].to_excel(out_file+f'{ipage}.xlsx')
    # print(df[ipage])
# print(df[0])

