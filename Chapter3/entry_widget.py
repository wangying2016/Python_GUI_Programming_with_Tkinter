import tkinter as tk
from tkinter import ttk


class View(tk.Frame):
    """Litter module"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.my_text_var = tk.StringVar()
        my_entry = ttk.Entry(parent, textvariable=self.my_text_var, show='*')
        my_entry.pack()


class MyApplication(tk.Tk):
    """Basic Main Application"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        View(self).pack()


if __name__ == '__main__':
    app = MyApplication()
    app.mainloop()
