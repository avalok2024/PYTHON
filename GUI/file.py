from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("open a file dialog")

root.filename = filedialog.askopenfile(initialdir="D:/PYTHON/GUI/Image Viewer", title="Select a File", filetypes=(("png files", "*.png"), ("All files", "*.*")))
my_label = Label(root, text=root.filename).pack()
my_image = ImageTk.PhotoImage(Image.open(root.filename))
my_image_label = Label(image=my_image).pack()

def open():
      global my_image
      root.filename = filedialog.askopenfile(initialdir="D:/PYTHON/GUI/Image Viewer", title="Select a File", filetypes=(("png files", "*.png"), ("All files", "*.*")))
      my_label = Label(root, text=root.filename).pack()
      my_image = ImageTk.PhotoImage(Image.open(root.filename))
      my_image_label = Label(image=my_image).pack()

my_btn = Button(root, text="clcik here", command=open).pack()

root.mainloop()
