import tkinter as tk
from tkinter import ttk


class View(tk.Frame):
    """Litter module"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        my_string_var = tk.StringVar()
        combobox = ttk.Combobox(
                parent,
                textvariable=my_string_var,
                values=["Option 1", "Option 2", "Option 3"])
        combobox.pack()


class MyApplication(tk.Tk):
    """Basic Main Application"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        View(self).pack()


if __name__ == '__main__':
    app = MyApplication()
    app.mainloop()
