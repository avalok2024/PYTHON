from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Frames")

frame = LabelFrame(root, text="This is frame...", padx=50, pady=50)
frame.grid(padx=10, pady=10)

b1 = Button(frame, text="Don't Click")
b1.grid(row=0, column=1)

b2 = Button(frame, text="Click Here!")
b2.grid(row=1, column=2)


root.mainloop()
