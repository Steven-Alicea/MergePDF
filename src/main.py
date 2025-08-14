import tkinter as tk
from tkinter import ttk
from src.helpers.resource import resource_path
from src.menu.menu_bar import MenuBar
from src.frames.option_frame import OptionFrame



class App(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        icon = tk.PhotoImage(file=resource_path("icon.png"))
        self.iconphoto(False, icon)
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')

        # widgets
        self.menubar = MenuBar(self)
        self.config(menu=self.menubar)

        self.title = ttk.Label(self, text='MergePDF', font=('Segoe UI', 20, 'bold'))
        self.label_version = ttk.Label(self, text='Version: 0.1')

        self.option_frame = OptionFrame(self)
        self.workspace_frame = ttk.Frame(self)
        
        self.create_layout()

    def create_layout(self):
        self.title.pack(side='top')
        self.option_frame.pack()
        self.label_version.pack(side='bottom', anchor='s')

    def change_frame(self, frame_class):
        new_frame = frame_class(self)
        self.workspace_frame.destroy()
        self.workspace_frame = new_frame
        self.workspace_frame.pack(fill='both', padx=10, pady=10)


def main():
    app = App('MergePDF', (640,480))
    app.mainloop()


if __name__ == '__main__':
    main()
