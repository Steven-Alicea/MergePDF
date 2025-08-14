import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from src.helpers.pdf_functions import merge_append, merge_duplex, load_pdf_file, save_and_open_pdf



class MergeFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pdf1 = None
        self.pdf2 = None
        
        # Widgets
        self.label_frame_pdf1 = ttk.LabelFrame(self, text='PDF 1')
        self.label_frame_pdf2 = ttk.LabelFrame(self, text='PDF 2')
        self.label_frame_merge_mode = ttk.LabelFrame(self, text='Merge Mode', padding=(10, 5))

        self.label_file1_path = ttk.Label(self.label_frame_pdf1)
        self.label_file2_path = ttk.Label(self.label_frame_pdf2)

        self.mode = tk.IntVar()
        self.radiobutton_mode_append = ttk.Radiobutton(self.label_frame_merge_mode, text='Append', takefocus=False, variable=self.mode, value=1, command=lambda: self.enable_buttons())
        self.radiobutton_mode_duplex = ttk.Radiobutton(self.label_frame_merge_mode, text='Duplex', takefocus=False, variable=self.mode, value=2, command=lambda: self.enable_buttons())

        self.button_select_file_1 = ttk.Button(self.label_frame_pdf1, text='Select File', takefocus=False, command=lambda: self.select_file(1))
        self.button_select_file_2 = ttk.Button(self.label_frame_pdf2, text='Select File', takefocus=False, command=lambda: self.select_file(2))
        self.button_merge = ttk.Button(self, text='Merge', takefocus=False, state='disabled', command=lambda: self.merge_pdfs())

        self.create_layout()

    def create_layout(self):
        self.columnconfigure((0, 1, 2), weight=1, uniform='a')
        self.rowconfigure((0, 1, 2), weight=1, uniform='a')

        # row 0
        self.label_frame_pdf1.grid(row=0, column=0, columnspan=3, padx=20, sticky='ew')
        self.label_file1_path.pack(side='left')
        self.button_select_file_1.pack(side='right')

        # row 1
        self.label_frame_pdf2.grid(row=1, column=0, columnspan=3, padx=20, pady=10, sticky='ew')
        self.label_file2_path.pack(side='left')
        self.button_select_file_2.pack(side='right')

        # row 2
        self.label_frame_merge_mode.grid(row=2, column=0, padx=20, sticky='w')
        self.radiobutton_mode_append.grid(row=0, column=0, padx=(0,5))
        self.radiobutton_mode_duplex.grid(row=0, column=1, padx=(5,0))
        self.button_merge.grid(row=2, column=2, padx=20, sticky='e')


    def enable_buttons(self):
        if str(self.label_file1_path.cget("text")).endswith(".pdf") and str(self.label_file2_path.cget("text")).endswith(".pdf") and (self.mode.get() == 1 or self.mode.get() == 2):
            self.button_merge.config(state='normal')

    def disable_buttons(self):
        if not str(self.label_file1_path.cget("text")).endswith(".pdf") or not str(self.label_file2_path.cget("text")).endswith(".pdf") or self.mode.get() == 1 or self.mode.get() == 2:
            self.button_merge.config(state='disabled')

    def select_file(self, button):
        path = filedialog.askopenfilename(initialdir=os.path.expanduser("~"),
                                          title='Open',
                                          filetypes=(('pdf files', '*.pdf'),))
        if button == 1: 
            if path:
                self.label_file1_path.config(text=path.split('/')[-1])
                self.pdf1 = load_pdf_file(path)
                self.enable_buttons()
            else:
                self.label_file1_path.config(text="")
                self.pdf1 = None
                self.disable_buttons()
        elif button == 2:
            if path:
                self.label_file2_path.config(text=path.split('/')[-1])
                self.pdf2 = load_pdf_file(path)
                self.enable_buttons()
            else:
                self.label_file2_path.config(text="")
                self.pdf2 = None
                self.disable_buttons()

    def merge_pdfs(self):
        if self.mode.get() == 1:
            pdf_output = merge_append(self.pdf1, self.pdf2)
        elif self.mode.get() == 2:
            if self.pdf1.get_num_pages() >= self.pdf2.get_num_pages() + 2:
                messagebox.showerror(title='Error', message='PDF 1 has 2 or more pages than PDF 2.\n\nPlease select another PDF.')
                return
            elif self.pdf1.get_num_pages() < self.pdf2.get_num_pages():
                messagebox.showerror(title='Error', message='PDF 1 has less pages than PDF 2.\n\nPlease select another PDF.')
                return
            pdf_output = merge_duplex(self.pdf1, self.pdf2)
        save_and_open_pdf(pdf_output)
