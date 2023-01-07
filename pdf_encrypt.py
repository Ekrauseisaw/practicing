from PyPDF2 import PdfReader, PdfWriter
from getpass import getpass

pdf_writer = PdfWriter()
pdf = PdfReader("di.pdf")

for page in range(len(pdf.pages)):
    pdf_writer.add_page(pdf.pages[page])

password = getpass(prompt="Enter password: ")
pdf_writer.encrypt(password)

with open("protected.pdf", "wb") as file:
    pdf_writer.write(file)