# Exercise 8 - Merge the PDF | Python Tutorial - Day #76

# https://www.youtube.com/watch?v=uUbvJ7ZEhPE&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=77

from PyPDF2 import PdfFileReader, PdfFileWriter
import os
merger = PdfFileWriter()
files = os.listdir('Day_76/clutter')

for file in files:
    merger.append(fileobj=f'Day76/clutter/{file}')

merger.write('Day_76/clutter/merger.pdf')    
merger.close()