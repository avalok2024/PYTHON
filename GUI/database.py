from tkinter import *
# from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title("Database")
root.geometry("300x200")

# Database


# creating a database to connect
conn = sqlite3.connect("address.db")

f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=30)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

#create a label

f_name_label = Label(root, text="First name ").grid(row=0, column=0)
l_name_label = Label(root, text="Last name ").grid(row=1, column=0)
address_label = Label(root, text="Full Address").grid(row=2, column=0)
city_label = Label(root, text="City").grid(row=3, column=0)
state_label = Label(root, text="State").grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode").grid(row=5, column=0)

# submit button

def submit():

    conn = sqlite3.connect("address_book.db")

    c = conn.cursor()
    c.execute("INSERT INFO address VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)"
             {
                "f_name" : f_name.get(),
                "l_name" : l_name.get(),
                "address" : address.get(),
                "city" : city.get(),
                "state" : state.get(),
                "zipcode" : zipcode.get()
             })



    # commit changes
    conn.commit()

    # close connection
    conn.close()

    # clear the boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


# create a button

submit_button = Button(root, text="Add in Database", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)






# creating the cursor
'''
c = conn.cursor()
c.execute(""" CREATE TABLE addresses(
         first_name text,
         last_name text,
         address text,
         city text,
         state text, 
         zipcode integer)""")
'''
# create commit
conn.commit()

# create the close connection
conn.close()



root.mainloop()
