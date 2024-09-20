# PDF-Management-Tool
a Python PDF Management Tool with a Tkinter GUI. This tool provides a graphical interface to merge, split, and extract text from PDF files using PyPDF2 and tkinter.

Description

This is a Python-based PDF management tool with a graphical user interface (GUI) built using Tkinter. The tool allows users to:

    Merge multiple PDF files into one.
    Split a single PDF file into multiple PDFs, each containing a single page.
    Extract text from a PDF file and display it in a text window.

This tool is useful for beginners working in the IT department of an academy or any professional environment requiring basic PDF operations.
Features

    Merge PDFs: Select multiple PDF files, merge them into a single file, and save the merged PDF.
    Split PDF: Split a PDF file into individual pages, with each page saved as a separate PDF file.
    Extract Text: Extract and display the text from a PDF file.

Requirements

    Python 3.x
    PyPDF2: A Python library to work with PDF files.
    Tkinter: A built-in library in Python for creating GUIs.

To install the required package:

bash

pip install PyPDF2

How to Run

    Clone the repository or download the Python file.
    Make sure you have the required libraries installed using the pip command above.
    Run the Python script:

    bash

    python pdf_tool.py

Usage
Merge PDFs

    Click the Merge PDFs button.
    Select multiple PDF files you wish to merge.
    Specify the name and location for the merged output PDF.
    A success message will confirm the merging.

Split PDF

    Click the Split PDF button.
    Choose the PDF file you wish to split.
    Select a folder where the split PDFs (one per page) will be saved.
    A success message will show the number of pages that have been split.

Extract Text from PDF

    Click the Extract Text from PDF button.
    Select the PDF file to extract text from.
    The text will be displayed in a new window.

File Structure

plaintext

📁 PDF Management Tool
   ├── pdf_tool.py     # Main Python script with Tkinter GUI
   └── README.md       # Documentation (this file)

Future Enhancements

    Add Watermark: The ability to add a watermark to PDFs.
    Encrypt PDFs: Implement password protection for PDF files.
    PDF Compression: Add functionality to compress PDFs.

Contributing

Contributions are welcome! Please feel free to submit a Pull Request on GitHub or suggest features by opening an issue.
License

This project is licensed under the MIT License.
