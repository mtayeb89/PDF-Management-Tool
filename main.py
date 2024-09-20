# Required libraries: PyPDF2 and tkinter
# Install PyPDF2: pip install PyPDF2

import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2
import os

# Create the main application window
root = tk.Tk()
root.title("PDF Management Tool")
root.geometry("400x400")

# Function to merge multiple PDF files
def merge_pdfs():
    files = filedialog.askopenfilenames(title="Select PDFs to Merge", filetypes=[("PDF files", "*.pdf")])
    if files:
        output_file = filedialog.asksaveasfilename(defaultextension=".pdf", title="Save Merged PDF", filetypes=[("PDF files", "*.pdf")])
        if output_file:
            try:
                merger = PyPDF2.PdfMerger()
                for pdf in files:
                    merger.append(pdf)
                merger.write(output_file)
                merger.close()
                messagebox.showinfo("Success", "PDFs Merged Successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Error while merging PDFs: {e}")

# Function to split a PDF into individual pages
def split_pdf():
    file = filedialog.askopenfilename(title="Select PDF to Split", filetypes=[("PDF files", "*.pdf")])
    if file:
        output_folder = filedialog.askdirectory(title="Select Folder to Save Split PDFs")
        if output_folder:
            try:
                with open(file, 'rb') as pdf_file:
                    pdf_reader = PyPDF2.PdfReader(pdf_file)
                    total_pages = len(pdf_reader.pages)
                    for page_num in range(total_pages):
                        pdf_writer = PyPDF2.PdfWriter()
                        pdf_writer.add_page(pdf_reader.pages[page_num])
                        output_pdf = os.path.join(output_folder, f"page_{page_num + 1}.pdf")
                        with open(output_pdf, 'wb') as output_file:
                            pdf_writer.write(output_file)
                    messagebox.showinfo("Success", f"PDF Split into {total_pages} pages")
            except Exception as e:
                messagebox.showerror("Error", f"Error while splitting PDF: {e}")

# Function to extract text from a PDF
def extract_text():
    file = filedialog.askopenfilename(title="Select PDF to Extract Text", filetypes=[("PDF files", "*.pdf")])
    if file:
        try:
            with open(file, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
                # Display the extracted text in a new window
                text_window = tk.Toplevel(root)
                text_window.title("Extracted Text")
                text_area = tk.Text(text_window, wrap='word', height=20, width=60)
                text_area.pack(expand=1, fill='both')
                text_area.insert(tk.END, text)
        except Exception as e:
            messagebox.showerror("Error", f"Error while extracting text: {e}")

# GUI Components
tk.Label(root, text="PDF Management Tool", font=("Arial", 16)).pack(pady=10)

merge_button = tk.Button(root, text="Merge PDFs", command=merge_pdfs, width=20)
merge_button.pack(pady=10)

split_button = tk.Button(root, text="Split PDF", command=split_pdf, width=20)
split_button.pack(pady=10)

extract_button = tk.Button(root, text="Extract Text from PDF", command=extract_text, width=20)
extract_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
