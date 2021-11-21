from docx import Document
from docx.shared import Inches
# Gán cái Document 
doc = Document()
# Add tiêu đề đầu tiên là 
doc.add_heading('Phiếu báo điểm', 0)
# Lưu file word 
doc.save('phieudiem.docx')