from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
import os
from datetime import datetime

root = Tk()
#root.state('zoomed')
root.attributes('-fullscreen', True)
root.title("School Shoes")
root.config(bg="skyblue3")


dateTimeObj = datetime.now()

timestampStr = dateTimeObj.strftime("%d-%b-%Y")

l1 = Label(root, text="Filter By Date / Style", width=80, anchor=CENTER, font=["Bodoni MT", 30, "bold"], background="skyblue3", relief="raised").pack(side='top', ipadx= 20, ipady=10)

#Bind keys
def close_screen(e):
	command=root.destroy()
root.bind('<Escape>', lambda e: close_screen(e))

with sqlite3.connect('Reflex Footwear.sql3') as conn:
    cursor = conn.cursor()
    my_data = cursor.execute("SELECT DISTINCT Style FROM MyShoe")
    my_list = [r for r, in my_data]
    options = StringVar()

with sqlite3.connect('Reflex Footwear.sql3') as conn:
    cursor = conn.cursor()
    my_data1 = cursor.execute("SELECT DISTINCT DeliveryDate FROM MyShoe")
    my_list1 = [r for r, in my_data1]
    options1 = StringVar()

def del_date():
    dates1 = options1.get()
    tree.delete(*tree.get_children())
    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        mycursor = conn.cursor()
        mycursor.execute("SELECT Factory,OrderNo,Style,DeliveryDate,Quantity,Balances FROM MyShoe WHERE DeliveryDate=?", (dates1,))
        for row in mycursor:
            tree.insert('', 'end', values=row[1:6])


def orders():
    desc = options.get()
    dates1 = options1.get()
    tree.delete(*tree.get_children())
    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        mycursor = conn.cursor()
        mycursor.execute("SELECT Factory,OrderNo,Style,DeliveryDate,Quantity,Balances FROM MyShoe WHERE Style=? AND DeliveryDate=?", (desc, dates1))
        for row in mycursor:
            tree.insert('', 'end', values=row[1:6])


def styles():
    desc = options.get()
    tree.delete(*tree.get_children())
    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        mycursor = conn.cursor()
        mycursor.execute("SELECT Factory,OrderNo,Style,DeliveryDate,Quantity,Balances FROM MyShoe WHERE Style=?", (desc,))
        for row in mycursor:
            tree.insert('', 'end', values=row[1:6])


frame = Frame(root)
frame.pack()

# Treeview
style = ttk.Style()
style.configure("Treeview.Heading", font=("Calibri", 15, 'bold'), foreground='black')

tree = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5), height=29, show="headings")
tree.pack(side='right')

#tree.heading(0, text="Factory")
tree.heading(1, text="Order No.")
tree.heading(2, text="Style/Description")
tree.heading(3, text="Delivery Date")
tree.heading(4, text="Order Qty")
tree.heading(5, text="Balance")

#tree.column(0, width=80)
tree.column(1, width=130)
tree.column(2, width=240)
tree.column(3, width=140)
tree.column(4, width=120)
tree.column(5, width=120)

# Scrollbar
# scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
# scroll.pack(side='right', fill='y')

# tree.configure(yscrollcommand=scroll.set)

# Style of Buttons
style = Style()
style.configure('E.TButton', font=('Arial Narrow', 14, 'bold', 'underline'), foreground='firebrick2', background='skyblue3')
style.configure('N.TButton', font=('Arial Narrow', 14, 'bold', 'underline'), foreground='blue2', background='skyblue3')


def tkinter6():
    ret6 = os.system('python excel_export_date_orders_admin.py')
    if ret6:
        orders()

#label_1 = Label(root, text="Style:", width=8, background="skyblue3", foreground="", font=("Calibri", 15, "bold")).pack(side="left")
option_1 = OptionMenu(root, options, *my_list).pack(side="left", padx=10)
options.set("Style")
btn2 = Button(root, text='Style', style='N.TButton', command=styles).pack(side='left', padx=10)

#label_2 = Label(root, text="Delivery Date:", width=14, background="skyblue3", foreground="", font=("Calibri", 15, "bold")).pack(side="left")
option_2 = OptionMenu(root, options1, *my_list1).pack(side="left", padx=10)
options1.set("Delivery Date")
btn2 = Button(root, text='Date', style='N.TButton', command=del_date).pack(side='left', padx=10)

btn7 = Button(root, text='Style/Date', style='N.TButton', width=14, command=orders).pack(side='left', padx=20)

btn = Button(root, text='Close (Esc)', width=14, style='E.TButton', command=root.destroy).pack(side='right', padx=10)


orders()

root.mainloop()
