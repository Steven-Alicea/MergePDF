import os
import platform
import tempfile
from datetime import datetime
from io import BytesIO
from pypdf import PdfReader, PdfWriter
from tkinter import filedialog


def load_pdf_file(pdf_file_path):
    return PdfReader(pdf_file_path)

def save_pdf_file(pdf_file, pdf_file_path):
        with open(pdf_file_path, 'wb') as file:
            pdf_file.write(file)
        pdf_file.close()

def save_temporary_pdf_file(pdf_file):
    temp_directory = tempfile.mkdtemp(prefix='MergePDF_', suffix='temp')
    with tempfile.NamedTemporaryFile(dir=temp_directory, mode='wb', suffix='.pdf', delete=False) as temp_pdf_file:
        pdf_file.write(temp_pdf_file)
        return temp_pdf_file.name

def copy_pdf(pdf_file):
    return PdfWriter(pdf_file)

def delete_pdf_file(pdf_file_path):
    os.remove(pdf_file_path)

# opens pdf in default os pdf reader
def open_pdf(filepath):
    system_name = platform.system()
    if system_name == 'Windows':
        os.startfile(filepath)
    elif system_name == 'Darwin':
        os.system(f"open '{filepath}'")
    elif system_name == 'Linux':
        os.system(f"xdg-open '{filepath}'")

def save_and_open_pdf(pdf):
    pdf_destination = filedialog.asksaveasfilename(initialdir=str(os.path.expanduser("~")),
                                                    initialfile=('MergePDF_' + datetime.now().strftime
                                                    ("%Y-%m-%d-%H%M%S")),
                                                    title='Save',
                                                    defaultextension='.pdf',
                                                    filetypes=(('pdf files', '*.pdf'),))
    if pdf_destination:
        save_pdf_file(pdf, pdf_destination)
        open_pdf(pdf_destination)

def get_pdf_file_counts(pdf_files):
    count = 0
    for _ in pdf_files:
        count += 1
    return count

def remove_page(pdf_file, page_number):
    pdf_output = PdfWriter()
    for page in range(len(pdf_file.pages)):
        if page != page_number - 1:
            pdf_output.add_page(pdf_file.pages[page])
    return pdf_output

def remove_pages(pdf_file, page_list):
    pdf_output = PdfWriter()
    for page in range(len(pdf_file.pages)):
        if page not in page_list:
            pdf_output.add_page(pdf_file.pages[page])
    return pdf_output

def reverse_pages(pdf_file):
    pdf_reversed_file = PdfWriter()
    page = pdf_file.get_num_pages() - 1
    while page >= 0:
        pdf_reversed_file.add_page(pdf_file.pages[page])
        page -= 1
    return pdf_reversed_file

def merge_append(pdf_file1, pdf_file2):
    pdf = PdfWriter(pdf_file1)
    pdf.append(pdf_file2)
    return pdf

def merge_duplex(pdf_file1, pdf_file2):
    pdf_merged_file = PdfWriter()
    if pdf_file1.get_num_pages() == pdf_file2.get_num_pages():
        for i in range(len(pdf_file1.pages)):
            pdf_merged_file.add_page(pdf_file1.pages[i])
            pdf_merged_file.add_page(pdf_file2.pages[i])
    elif pdf_file1.get_num_pages() == pdf_file2.get_num_pages() + 1:
        for i in range(len(pdf_file1.pages)):
            pdf_merged_file.add_page(pdf_file1.pages[i])
            if i == len(pdf_file2.pdf_file):
                break
            else:
                pdf_merged_file.add_page(pdf_file2.pages[i])
    return pdf_merged_file

def convert_writer_to_reader(pdf_file):
    pdf_buffer = BytesIO()
    pdf_file.write(pdf_buffer)
    pdf_buffer.seek(0)
    pdf_reader = PdfReader(pdf_buffer)
    return pdf_reader
