# Exercise 8 - Merge the Pdf Solution in Python | Python Tutorial - Day #82

# https://www.youtube.com/watch?v=qKKGemhBRVM&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=82

from PyPDF2 import PdfWriter
import os

merger = PdfWriter()

files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write("merger-pdf.pdf")    
merger.close()