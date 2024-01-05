from tkinter import *
from tkinter import filedialog
from tkinter import 
root = Tk()
root.title("open a file dialog")

root.filename = filedialog.askopenfile(
    initialdir="D:/PYTHON/GUI/Image Viewer", title="Select a File", filetypes=(("png files", "*.png"), ("All files", "*.*"))
    )

myLabel = Label(root, text=root.filename).pack()
my_image =

root.mainloop()
