import tkinter as tk
from tkinter import ttk


class MyCanvas(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.canvas = tk.Canvas(parent, width=1024, height=768, cursor='arrow')
        self.canvas.pack()

        self.canvas.create_rectangle(100, 100, 200, 200, fill='orange')

        self.canvas.create_rectangle((600, 100), (700, 200), fill='#FF8800')

        self.canvas.create_oval((350, 250), (450, 350), fill='blue')
        
        self.canvas.create_line((100, 400), (400, 500),
                (700, 400), (100, 400), width=5, fill='red')

        self.canvas.create_polygon((400, 150), (350, 300), (450, 300), 
                fill='blue', smooth=True)
        
        # Place text or image
        self.canvas.create_text((400, 600), text='Smile!',
                fill='cyan', font='TkDefaultFont 64')



            


class Application(tk.Tk):
    """Application root windows"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set title
        self.title("Python Vim Emulator")

        # Set Canvas
        self.canvas = MyCanvas(self)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
