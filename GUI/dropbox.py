from tkinter import *

root = Tk()
root.title("Drop Box")
root.geometry("500x500")

# Drop box
def show():
    my_label = Label(root, text=clicked.get()).pack()


option = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Saturday",
    "Sunday"
]

clicked = StringVar()
clicked.set(option[0])

drop = OptionMenu(root, clicked, *option).pack()
drop_button = Button(root, text="Show", command=show).pack()

root.mainloop()
