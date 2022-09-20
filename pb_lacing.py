from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
import os
from datetime import datetime

root = Tk()
root.attributes('-fullscreen', True)
root.title("Pre-Boys Handlacing")
root.config(bg="skyblue3")

dateTimeObj = datetime.now()

timestampStr = dateTimeObj.strftime("%d-%b-%Y")

l1 = Label(root, text=r"Pre-Boy's Handlacing", width=120, anchor=CENTER, font=["Bodoni MT", 21, "bold"], background="skyblue3", relief="raised").pack(side='top', ipady=10)

def pb_lacing():
    tree.delete(*tree.get_children())
    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        mycursor = conn.cursor()
        mycursor.execute(
            "SELECT DatePB,Order3,SupplierPB,Size9,Size10,Size11,Size12,Size13,Size1,Sent,Received FROM HandlacingPB")
        for row in mycursor:
            tree.insert('', 'end', values=row[0:11])


frame = Frame(root)
frame.pack()

# Treeview
style = ttk.Style()
style.configure("Treeview.Heading", font=(
    "Arial Narrow", 16, 'bold'), foreground='antiquewhite4')

tree = ttk.Treeview(frame, columns=(0, 1, 2, 3, 4, 5, 6, 7,
                                    8, 9, 10), height=30, show="headings")
tree.pack(side='top', padx=10, pady=10)

tree.heading(0, text="Date")
tree.heading(1, text="Order No")
tree.heading(2, text="Supplier")
tree.heading(3, text="Size 9")
tree.heading(4, text="Size 10")
tree.heading(5, text="Size 11")
tree.heading(6, text="Size 12")
tree.heading(7, text="Size 13")
tree.heading(8, text="Size 1")
tree.heading(9, text="Sent")
tree.heading(10, text="Received")

tree.column(0, width=110)
tree.column(1, width=110)
tree.column(2, width=110)
tree.column(3, width=110)
tree.column(4, width=110)
tree.column(5, width=110)
tree.column(6, width=110)
tree.column(7, width=110)
tree.column(8, width=110)
tree.column(9, width=110)
tree.column(10, width=110)

# Scrollbar
# scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
# scroll.pack(side='right', fill='y')

# tree.configure(yscrollcommand=scroll.set)

# Style of Buttons
style = Style()
style.configure('E.TButton', font=('Arial Narrow', 14, 'bold'), foreground='firebrick2', background='black')
style.configure('N.TButton', font=('Arial Narrow', 14, 'bold'), foreground='blue2', background='black')


def tkinter():
    ret = os.system('python pb_send.py')
    if ret:
        pb_lacing()


def tkinter2():
    ret2 = os.system('python pb_search.py')
    if ret2:
        pb_lacing()


def tkinter3():
    ret3 = os.system('python pb_receive.py')
    if ret3:
        pb_lacing()


# Buttons
btn = Button(root, text='Exit', style='E.TButton', command=root.destroy).pack(side='right')

btn1 = Button(root, text='Send', style='N.TButton', command=tkinter).pack(side='left')
btn2 = Button(root, text='Receive', style='N.TButton', command=tkinter3).pack(side='left')
btn3 = Button(root, text='Search', style='N.TButton', command=tkinter2).pack(side='left')

pb_lacing()

root.mainloop()
