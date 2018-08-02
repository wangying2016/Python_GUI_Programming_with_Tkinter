import tkinter as tk
from tkinter import ttk


class View(tk.Frame):
    """Litter module"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        my_boolean_var = tk.BooleanVar()
        my_checkbutton = ttk.Checkbutton(
                parent,
                text="Check to make this option True",
                variable=my_boolean_var)
        my_checkbutton.pack()


class MyApplication(tk.Tk):
    """Basic Main Application"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        View(self).pack()


if __name__ == '__main__':
    app = MyApplication()
    app.mainloop()
