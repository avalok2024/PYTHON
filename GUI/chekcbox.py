from tkinter import *

root = Tk()
root.title("checkbox")

def show():
    my_label = Label(root, text=var.get()).pack()

var = IntVar()

c = Checkbutton(root, text="I am checking the box!", variable=var)
c.pack()

my_button = Button(root, text="click here!", command=show).pack()
root.mainloop()
