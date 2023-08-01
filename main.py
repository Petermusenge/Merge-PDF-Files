from PyPDF2 import PdfFileMerger

# By appending in the end
def by_appending():
    merger = PdfFileMerger()
    # Either provide file stream
    f1 = open("samplePdf1.pdf", "rb")
    merger.append(f1)  # Append the first PDF file
    # Or direct file path
    merger.append("samplePdf2.pdf")  # Append the second PDF file

    merger.write("mergedPdf.pdf")  # Write the merged PDF to a file


# By inserting after a specified page no.
def by_inserting():
    merger = PdfFileMerger()
    merger.append("samplePdf1.pdf")  # Append the first PDF file
    merger.merge(0, "samplePdf2.pdf")  # Insert the second PDF file after page 0

    merger.write("mergedPdf1.pdf")  # Write the merged PDF to a file


if __name__ == "__main__":
    by_appending()  # Call the function to merge PDFs by appending
    by_inserting()  # Call the function to merge PDFs by inserting