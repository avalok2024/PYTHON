from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learning the new windows segment")


def open():
    top = Toplevel
    top.title("This is new file")
    my_img = ImageTk.PhotoImage(Image.open("D:/PYTHON/GUI/Image Viewer/avenger6.png"))
    mylabel = Label(top, image=my_img).pack()

bt = Button(root, text="Open", command=open)
# mylable = Label(top,text="hello there!").pack()


root.mainloop()
