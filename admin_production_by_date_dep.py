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

# mycursor.execute("SELECT Factory,Planned,Order2,Style,Deldate,Orderqty,Clicking,Closing,Finishing,Despatch,Warehouse,ToShip,Shipped FROM Production_Balances")
dateTimeObj = datetime.now()

timestampStr = dateTimeObj.strftime("%d-%b-%Y")

l1 = Label(root, text="Filter By Date / Department", width=80, anchor=CENTER, font=["Bodoni MT", 30, "bold"], background="skyblue3", relief="raised").pack(side='top', ipadx= 20, ipady=10)

#Bind keys
def close_screen(e):
	command=root.destroy()
root.bind('<Escape>', lambda e: close_screen(e))

Departm = StringVar()
departm = ("Department","Clicking", "Closing", "Despatch", "Warehouse", "Shipped")

with sqlite3.connect('Reflex Footwear.sql3') as conn:
    cursor = conn.cursor()
    my_data1 = cursor.execute("SELECT DISTINCT Date FROM ProductionBreakdown")
    my_list1 = [r for r, in my_data1]
    options1 = StringVar()

def del_date():
    dates1 = options1.get()
    tree.delete(*tree.get_children())
    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        mycursor = conn.cursor()
        mycursor.execute("SELECT Factory,Date,Order2,Clicking,Closing,Despatch,Warehouse,Shipped FROM ProductionBreakdown WHERE Date=?", (dates1,))
        for row in mycursor:
            tree.insert('', 'end', values=row[1:8])

''' To be added upon verification
def orders():
    dep = Departm.get()
    dates1 = options1.get()
    tree.delete(*tree.get_children())
    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        mycursor = conn.cursor()
        mycursor.execute("SELECT Factory,Date,Order2,Clicking,Closing,Despatch,Warehouse,Shipped FROM ProductionBreakdown")
		# mycursor.execute("SELECT Factory,Date,Order2,Clicking,Closing,Despatch,Warehouse,Shipped FROM ProductionBreakdown WHERE '{}'=? AND Date=?".format(dep), (dates1,))
        for row in mycursor:
            tree.insert('', 'end', values=row[1:8])
'''

def department():
	dep = Departm.get()
	clicking = 'Clicking'
	closing = 'Closing'
	desp = 'Despatch'
	ware = 'Warehouse'
	if dep == closing:
		tree.delete(*tree.get_children())
		with sqlite3.connect('Reflex Footwear.sql3') as conn:
			mycursor = conn.cursor()
			mycursor.execute("SELECT Factory,Date,Order2,Closing FROM ProductionBreakdown")
			for row in mycursor:
				tree.insert('', 'end', values=row[1:8])
	elif dep == clicking:
		tree.delete(*tree.get_children())
		with sqlite3.connect('Reflex Footwear.sql3') as conn:
			mycursor = conn.cursor()
			mycursor.execute("SELECT Factory,Date,Order2,Clicking FROM ProductionBreakdown")
			for row in mycursor:
				tree.insert('', 'end', values=row[1:8])
	elif dep == desp:
		tree.delete(*tree.get_children())
		with sqlite3.connect('Reflex Footwear.sql3') as conn:
			mycursor = conn.cursor()
			mycursor.execute("SELECT Factory,Date,Order2,Despatch FROM ProductionBreakdown")
			for row in mycursor:
				tree.insert('', 'end', values=row[1:8])
	else:
		tree.delete(*tree.get_children())
		with sqlite3.connect('Reflex Footwear.sql3') as conn:
			mycursor = conn.cursor()
			mycursor.execute("SELECT Factory,Date,Order2,Warehouse FROM ProductionBreakdown")
			for row in mycursor:
				tree.insert('', 'end', values=row[1:8])


frame = Frame(root)
frame.pack()

# Treeview
style = ttk.Style()
style.configure("Treeview.Heading", font=("Calibri", 15, 'bold'), foreground='black')

tree = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5, 6, 7), height=29, show="headings")
tree.pack(side='right')

#tree.heading(0, text="Factory")
tree.heading(1, text="Production Date")
tree.heading(2, text="Order No")
tree.heading(3, text="Clicking Qty")
tree.heading(4, text="Closing Qty")
tree.heading(5, text="Despatch Qty")
tree.heading(6, text="Warehouse Qty")
tree.heading(7, text="Shipped Qty")

#tree.column(0, width=80)
tree.column(1, width=150)
tree.column(2, width=240)
tree.column(3, width=150)
tree.column(4, width=150)
tree.column(5, width=150)
tree.column(6, width=150)
tree.column(7, width=150)

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

option_1 = OptionMenu(root, Departm, *departm).pack(side="left", padx=10)
Departm.set("Department")
btn2 = Button(root, text='Department', style='N.TButton', command=department).pack(side='left', padx=10)

option_2 = OptionMenu(root, options1, *my_list1).pack(side="left", padx=10)
options1.set("Production Date")
btn2 = Button(root, text='Date', style='N.TButton', command=del_date).pack(side='left', padx=10)

#btn7 = Button(root, text='Departmet/Date', style='N.TButton', width=14, command=orders).pack(side='left', padx=20)
btn1 = Button(root, text='Close (Esc)', width=14, style='E.TButton', command=tkinter6).pack(side='right', padx=10)
btn = Button(root, text='Export', style='N.TButton', command=root.destroy).pack(side='right', padx=10)

# orders()

root.mainloop()
