from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learning the new windows segment")


def open():
    global my_img
    top = Toplevel()
    top.title("This is a new file")
    my_img = ImageTk.PhotoImage(Image.open("D:/PYTHON/GUI/Image Viewer/avenger6.png"))
    mylabel = Label(top, image=my_img).pack()
    btn = Button(top, text="Close", command=top.destroy).pack()


bt = Button(root, text="Open", command=open).pack()
# mylable = Label(top,text="hello there!").pack()


root.mainloop()
