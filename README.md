# PDF File Merger

This is a Python script that utilizes the `PyPDF2` library to merge PDF files. The script defines two functions, `by_appending()` and `by_inserting()`, which demonstrate different ways to merge PDFs.

## Installation

Before running the script, you need to make sure that `PyPDF2` is installed. If you haven't installed it yet, you can do so using pip:

```bash
pip install PyPDF2
```

## Usage

The script contains two functions, each serving a different merging method:

### Merging PDFs by Appending

The `by_appending()` function appends two PDF files together and creates a new merged PDF file. It demonstrates two ways of providing the input PDF files:

1. By passing a file stream: Open the first PDF file as a binary read stream using `open()`, then use the `append()` method to add it to the merger object.
2. By providing the direct file path: Pass the file path of the second PDF file directly to the `append()` method.

After appending both PDF files, the merged content is written to a new PDF file called `mergedPdf.pdf`.

### Merging PDFs by Inserting

The `by_inserting()` function merges one PDF file into another at a specified page number. It also creates a new merged PDF file.

The process involves:

1. Create a PdfFileMerger object.
2. Append the first PDF file to the merger object using the `append()` method.
3. Use the `merge()` method to insert the second PDF file at the specified page number (0-indexed) in the first PDF.
4. Write the merged content to a new PDF file called `mergedPdf1.pdf`.

## Running the Script

To merge PDF files, execute the script, and it will automatically call both merging functions, creating the merged PDF files in the same directory where the script is located.

```bash
python merge_pdfs.py
```

Please ensure that you have the PDF files "samplePdf1.pdf" and "samplePdf2.pdf" present in the same directory as the script before running it.

## Note

This script is based on the `PyPDF2` library as of the knowledge cutoff date in September 2021. If there have been updates or changes to the library after this date, it is recommended to check the latest documentation for the library for any potential modifications.
