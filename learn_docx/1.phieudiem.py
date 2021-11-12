from docx import Document

# Gán cái Document 
doc = Document()
# Add tiêu đề đầu tiên là 
doc.add_heading('Phiếu thông báo điểm', 0)

doc.save('phieudiem.docx')