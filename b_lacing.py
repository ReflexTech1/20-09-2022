from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
import os
from datetime import datetime

# Tkinter Create
root = Tk()
root.attributes('-fullscreen', True)
root.title("Boys Handlacing")
root.config(bg="skyblue3")

OrderNo = StringVar()
Quantity = IntVar()

dateTimeObj = datetime.now()

timestampStr = dateTimeObj.strftime("%d-%b-%Y")

l1 = Label(root, text=r"Boy's Handlacing", width=120, anchor=CENTER, font=["Bodoni MT", 21, "bold"], background="skyblue3", relief="raised").pack(side='top', ipady=10)

def b_lacing():
    tree.delete(*tree.get_children())
    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        mycursor = conn.cursor()
        mycursor.execute(
            "SELECT DateB,Order3,SupplierB,Size2,Size3,Size4,Size5,Sent,Received FROM HandlacingB")
        for row in mycursor:
            tree.insert('', 'end', values=row[0:9])


frame = Frame(root)
frame.pack()

# Treeview
style = ttk.Style()
style.configure("Treeview.Heading", font=(
    "Arial Narrow", 16, 'bold'), foreground='antiquewhite4')

tree = ttk.Treeview(frame, columns=(0, 1, 2, 3, 4, 5, 6,
                                    7, 8), height=30, show="headings")
tree.pack(side='top', padx=10, pady=10)

tree.heading(0, text="Date")
tree.heading(1, text="Order No")
tree.heading(2, text="Supplier")
tree.heading(3, text="Size 2")
tree.heading(4, text="Size 3")
tree.heading(5, text="Size 4")
tree.heading(6, text="Size 5")
tree.heading(7, text="Sent")
tree.heading(8, text="Received")

tree.column(1, width=130)
tree.column(2, width=130)
tree.column(3, width=130)
tree.column(4, width=130)
tree.column(5, width=130)
tree.column(6, width=130)
tree.column(7, width=130)
tree.column(8, width=130)

# Scrollbar
# scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
# scroll.pack(side='right', fill='y')

# tree.configure(yscrollcommand=scroll.set)

# Style of Buttons
style = Style()
style.configure('E.TButton', font=('Arial Narrow', 14, 'bold'),
                foreground='firebrick2', background='black')
style.configure('N.TButton', font=('Arial Narrow', 14, 'bold'),
                foreground='blue2', background='black')


# Program to open with Button Click
def tkinter():
    ret = os.system('python b_send.py')
    if ret:
        b_lacing()


def tkinter2():
    ret2 = os.system('python b_search.py')
    if ret2:
        b_lacing()


def tkinter3():
    ret3 = os.system('python b_receive.py')
    if ret3:
        b_lacing()


# Buttons
btn = Button(root, text='Exit', style='E.TButton',
             command=root.destroy).pack(side='right')

btn1 = Button(root, text='Send', style='N.TButton',
              command=tkinter).pack(side='left')
btn2 = Button(root, text='Receive', style='N.TButton',
              command=tkinter3).pack(side='left')
btn3 = Button(root, text='Search', style='N.TButton',
              command=tkinter2).pack(side='left')

b_lacing()

root.mainloop()
