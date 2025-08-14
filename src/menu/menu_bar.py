import sys
import tkinter as tk
from tkinter import messagebox
from src.helpers.resource import resource_path
from src.frames.edit_frame import EditFrame
from src.frames.merge_frame import MergeFrame



def show_license():
    license = resource_path("LICENSE.txt")
    with open(license, 'r') as file:
        text = file.read()
    messagebox.showinfo("License", text)

def show_about():
    date = "August 13, 2025"
    developer = "Steven M. Alicea"
    email = "Steven.M.Alicea@gmail.com"
    messagebox.showinfo("About MergePDF", "MergePDF 0.1\n\n"
                                 f"Built on {date}\n\n"
                                 f"Developer: {developer}\n\n"
                                 f"E-mail: {email}")

class MenuBar(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)

        file_menu = tk.Menu(self, tearoff=False)
        self.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='Edit PDF', command=lambda: parent.change_frame(EditFrame))
        file_menu.add_command(label='Merge PDF', command=lambda: parent.change_frame(MergeFrame))
        file_menu.add_command(label='Exit', command=sys.exit)

        help_menu= tk.Menu(self, tearoff=0)
        self.add_cascade(label="About", menu=help_menu)
        help_menu.add_command(label='About MergePDF', command=show_about)
        help_menu.add_command(label='License', command=show_license)
        