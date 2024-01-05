from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Marvel Avengers")
root.iconbitmap("logo.ico")

my_img1 = ImageTk.PhotoImage(Image.open("avenger1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("avenger2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("avenger3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("avenger4.png"))
my_img5 = ImageTk.PhotoImage(Image.open("avenger5.png"))
my_img6 = ImageTk.PhotoImage(Image.open("avenger6.png"))

img_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6]

my_label = Label(image=my_img1)
my_label.grid(row=0, columnspan=3, column=0)

status = Label(root, text=f"Image 1 of {len(img_list)}", bd=1, relief=SUNKEN, anchor=E)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=img_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda : forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda : back(image_number - 1))

    my_label.grid(row=0, columnspan=3, column=0)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    status = Label(root, text=f"Image {image_number} of {len(img_list)}", bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, columnspan=3, column=0, sticky=W+E)

    if image_number == 6:
        button_forward = Button(root, text=">>", state=DISABLED)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=img_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda : forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda : back(image_number - 1))

    my_label.grid(row=0, columnspan=3, column=0)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

    # Update status bar
    status = Label(root, text=f"Image {image_number} of {len(img_list)}", bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, columnspan=3, column=0, sticky=W+E)

    if image_number == 1:
        button_forward = Button(root, text=">>", state=DISABLED)



button_back = Button(root, text="<<",command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_forward.grid(row=1, column=2, pady=20)
button_exit.grid(row=1, column=1)
button_back.grid(row=1, column=0)
status.grid(row=2, columnspan=3, column=0, sticky=W+E)

root.mainloop()
