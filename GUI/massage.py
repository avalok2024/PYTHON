from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("message box")

def popup():
     response = messagebox.askyesno("This is my popup!", "Hello World!")
     # Label(root, text=response).pack()
     if response == 1:
        Label(root, text="You clicked on Yes!").pack()
     else:
        Label(root, text="You clicked on no!").pack()


Button(root, text="click here", command=popup).pack()

root.mainloop()
