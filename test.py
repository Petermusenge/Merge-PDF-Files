# How to use the code to merge two PDF files

from PyPDF2 import PdfFileMerger

def merge_pdfs(file1, file2, output_file):
    merger = PdfFileMerger()
    merger.append(file1)
    merger.append(file2)
    merger.write(output_file)

if __name__ == "__main__":
    merge_pdfs("file1.pdf", "file2.pdf", "merged.pdf")