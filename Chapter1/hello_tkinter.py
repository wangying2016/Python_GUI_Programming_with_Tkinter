'''Hello World application for Tkinter'''
from tkinter import *
from tkinter.ttk import *

root = Tk()
label = Label(root, text="Hello World")
button = Button(root, text="Click This")
entry = Entry(root, text="input text")
label.pack()
entry.pack()
button.pack()
root.mainloop()
