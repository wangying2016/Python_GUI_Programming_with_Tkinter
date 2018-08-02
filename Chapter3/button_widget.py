import tkinter as tk
from tkinter import ttk


class View(tk.Frame):
    """Litter module"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.tvar = tk.StringVar()
        self.tvar.set('Begin')
        my_button = ttk.Button(
                parent,
                textvariable=self.tvar,
                command=self.swaptext)
        my_button.pack()

    def swaptext(self):
        if self.tvar.get() == 'Hi':
           self.tvar.set("There")
        else:
            self.tvar.set('Hi')

        
class MyApplication(tk.Tk):
    """Basic Main Application"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        View(self).pack()


if __name__ == '__main__':
    app = MyApplication()
    app.mainloop()
