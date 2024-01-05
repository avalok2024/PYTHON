from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("message box")

def popup():
    messagebox.showinfo("This is my popup!", "Hello World!")

Button(root, text="click here", command=popup).pack()

root.mainloop()
