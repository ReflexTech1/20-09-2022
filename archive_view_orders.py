from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
import os
from datetime import datetime

root = Tk()
root.attributes('-fullscreen', True)
root.title("School Shoes")
root.config(bg="skyblue3")

OrderNo = StringVar()
Quantity = IntVar()

dateTimeObj = datetime.now()

timestampStr = dateTimeObj.strftime("%d-%b-%Y")

l1 = Label(root, text="Orders Archived", width=120, anchor=CENTER, font=["Bodoni MT", 30, "bold"], background="tomato", relief="raised").pack(side='top', ipady=10)

def orders():
    tree.delete(*tree.get_children())
    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM MyShoe_Archive")
        for row in mycursor:
            tree.insert('', 'end', values=row[2:6])


frame = Frame(root)
frame.pack()

# Treeview
style = ttk.Style()
style.configure("Treeview.Heading", font=("Calibri", 17, 'bold'), foreground='black')

# Modify the font of the body
style.configure("Treeview", bd=2, font=('Calibri', 14))

# Modify OnClick
style.map('Treeview', background=[('selected', 'firebrick')])

tree = ttk.Treeview(frame, columns=(1, 2, 3, 4), height=45, show="headings")
tree.pack(side='left')

tree.heading(1, text="OrderNo")
tree.heading(2, text="Style/Description")
tree.heading(3, text="Delivery Date")
tree.heading(4, text="Quantity")

tree.column(1, width=190)
tree.column(2, width=430)
tree.column(3, width=230)
tree.column(4, width=230)

Scrollbar
scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
scroll.pack(side='right', fill='y')
tree.configure(yscrollcommand=scroll.set)

# Style of Buttons
style = Style()
style.configure('E.TButton', font=('Arial Narrow', 14, 'bold',
                                   'underline'), foreground='firebrick2', background='skyblue3')
style.configure('N.TButton', font=('Arial Narrow', 14, 'bold',
                                   'underline'), foreground='blue2', background='skyblue3')

#to add order search input box
#def tkinter10():
    #ret3 = os.system('python order_search.py')
    #if ret3:
        #orders()


def tkinter11():
    ret4 = os.system('python archive_view_production.py')
    if ret4:
        orders()


def tkinter12():
    ret4 = os.system('python archive_planning_search.py')
    if ret4:
        orders()


def tkinter13():
    ret4 = os.system('python excel_export_orders.py')
    if ret4:
        orders()


def close_screen(e):
    	command=root.destroy()
root.bind('<Escape>', lambda e: close_screen(e))

# Buttons
btn = Button(root, text='Exit', style='E.TButton', command=root.destroy).pack(side='right')

#btn3 = Button(root, text='Search Orders', style='N.TButton', command=tkinter10).pack(side='left')
btn4 = Button(root, text='View Production', style='N.TButton', command=tkinter11).pack(side='left')
btn5 = Button(root, text='View Planning', style='N.TButton', command=tkinter12).pack(side='left')
btn6 = Button(root, text='Export', style='N.TButton', command=tkinter13).pack(side='right')

orders()

root.mainloop()
