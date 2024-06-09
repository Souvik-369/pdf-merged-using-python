import PyPDF2
import sys
import os # is used for interacting with the operating system.
merge = PyPDF2.PdfMerger()
pdf_files_to_merge = ["one.pdf","two.pdf"]
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        #print(file)
       
        merge.append(file)

merge.write("Hello Souvik!mergedDoc is BTC402.pdf")# you can change the name 
merge.close()
# date 21-02-2024