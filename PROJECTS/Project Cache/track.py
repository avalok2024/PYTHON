# Pending!!!!!

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Attack!")

top = Toplevel()

survive = messagebox.askyesno("av attack", "Welcome to the av attack")
survive.pack()

a = 5
while a:
    for i in survive:
       print(i)


mylable = Label(top, text="hello there")

root.mainloop()
