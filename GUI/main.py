from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learning the Python')
root.iconbitmap("C:/Users/user/OneDrive/Pictures/PHOTOS/3.jpg")

my_img = ImageTk.PhotoImage(Image.open("11.png"))
my_label = Label(root, image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()

root.mainloop()
