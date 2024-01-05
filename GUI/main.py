from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Frames")

MODES = [
    ("pepporonie", "pepporonie"),
    ("Mushroom", "Mushroom"),
    ("Cheese", "Cheese"),
    ("Onion", "Onion"),
]
pizza = StringVar()
pizza.set("pepporonie")


for text, modes in MODES:
    Radiobutton(root, text=text, variable=pizza, value=modes).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

# Radiobutton(root, text="option 1", variable=r, value=1, command=lambda : clicked(r.get())).pack()
# Radiobutton(root, text="option 2", variable=r, value=2, command=lambda : clicked(r.get())).pack()

myButton = Button(root, text="clicked me!", command=lambda : clicked(pizza.get()))
myButton.pack()

# myLabel = Label(root, text=pizza.get())
# myLabel.pack()

root.mainloop()
