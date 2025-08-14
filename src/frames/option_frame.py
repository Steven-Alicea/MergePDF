from tkinter import ttk
from src.frames.edit_frame import EditFrame
from src.frames.merge_frame import MergeFrame

class OptionFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Widgets
        self.label_frame_menu = ttk.LabelFrame(self, text='Options', padding=(10, 5))

        self.button_edit = ttk.Button(self.label_frame_menu, text='Edit PDF', takefocus=False, command=lambda: parent.change_frame(EditFrame))
        self.button_merge = ttk.Button(self.label_frame_menu, text='Merge PDF', takefocus=False, command=lambda: parent.change_frame(MergeFrame))

        self.create_layout()

    def create_layout(self):
        self.label_frame_menu.pack(expand=True, fill='x', padx=20, pady=10)
        self.button_edit.pack(side='left', padx=5)
        self.button_merge.pack(side='left', padx=5)
