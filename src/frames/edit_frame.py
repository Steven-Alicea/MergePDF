import os
from tkinter import ttk, filedialog
from tkinter import messagebox
from src.helpers.pdf_functions import remove_pages, reverse_pages, load_pdf_file, save_and_open_pdf
from src.helpers.page_selection_functions import is_regex_sequence, get_page_deletion_list



class EditFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pdf = None

        # Widgets
        self.label_frame_pdf = ttk.LabelFrame(self, text='PDF')
        self.label_frame_delete_pages = ttk.LabelFrame(self, text='Delete Pages', padding=(10, 5))

        self.label_file_path = ttk.Label(self.label_frame_pdf)

        self.entry_pages = ttk.Entry(self.label_frame_delete_pages)

        self.button_select_file = ttk.Button(self.label_frame_pdf, text='Select File', takefocus=False, command=lambda: self.select_file())
        self.button_delete_pages = ttk.Button(self.label_frame_delete_pages, text='Delete Pages', takefocus=False, state='disabled', command=lambda: self.delete_pages())
        self.button_reverse_pages = ttk.Button(self, text='Reverse Pages', takefocus=False, state='disabled', command=lambda: self.reverse_pdf())

        self.create_layout()


    def create_layout(self):
        self.columnconfigure((0, 1, 2), weight=1, uniform='a')
        self.rowconfigure((0, 1, 2), weight=1, uniform='a')

        # row 0
        self.label_frame_pdf.grid(row=0, column=0, columnspan=3, padx=20, sticky='ew')
        self.label_file_path.pack(side='left')
        self.button_select_file.pack(side='right')

        # row 1
        self.label_frame_delete_pages.grid(row=1, column=0, padx=20, sticky='w')
        self.entry_pages.pack()
        self.button_delete_pages.pack()
        self.button_reverse_pages.grid(row=1, column=2, padx=20, sticky='e')

    def enable_buttons(self):
        if str(self.label_file_path.cget("text")).endswith(".pdf"):
            self.button_delete_pages.config(state='normal')
            self.button_reverse_pages.config(state='normal')

    def disable_buttons(self):
        self.button_delete_pages.config(state='disabled')
        self.button_reverse_pages.config(state='disabled')

    def select_file(self):
        path = filedialog.askopenfilename(initialdir=os.path.expanduser("~"),
                                          title='Open',
                                          filetypes=(('pdf files', '*.pdf'),))
        if path:
            self.label_file_path.config(text=path.split('/')[-1])
            self.pdf = load_pdf_file(path)
            self.enable_buttons()
        else:
            self.label_file_path.config(text="")
            self.pdf = None
            self.disable_buttons()

    def delete_pages(self):
        pages = self.entry_pages.get()
        if not is_regex_sequence(pages):
            messagebox.showerror(title='Error', message='Invalid page deletion input.')
            return
        pages = get_page_deletion_list(pages)
        for page in pages:
            if page >= self.pdf.get_num_pages():
                messagebox.showerror(title='Error', message='PDF file does not contain the page(s) you wish to delete.')
                return
        pdf_output = remove_pages(self.pdf, pages)
        save_and_open_pdf(pdf_output)

    def reverse_pdf(self):
        pdf_output = reverse_pages(self.pdf)
        save_and_open_pdf(pdf_output)
