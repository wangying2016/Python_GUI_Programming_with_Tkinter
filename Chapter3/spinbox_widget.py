import tkinter as tk
from tkinter import ttk


class View(tk.Frame):
    """Litter module"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.my_double_var = tk.DoubleVar()
        my_spinbox = tk.Spinbox(
                parent,
                from_=0.5,
                to=52.0,
                increment=.01,
                textvariable=self.my_double_var)
        my_spinbox.pack()


class MyApplication(tk.Tk):
    """Basic Main Application"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        View(self).pack()


if __name__ == '__main__':
    app = MyApplication()
    app.mainloop()
