from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Frames")

r = IntVar()
r.set("2")

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

Radiobutton(root, text="option 1", variable=r, value=1, command=lambda : clicked(r.get())).pack()
Radiobutton(root, text="option 2", variable=r, value=2, command=lambda : clicked(r.get())).pack()

myButton = Button(root, text="clicked me!", command=lambda : clicked(r.get()))
myButton.pack()

myLabel = Label(root, text=r.get())
myLabel.pack()

root.mainloop()
