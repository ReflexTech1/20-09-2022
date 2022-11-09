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

l1 = Label(root, text="Filter By Date / Department / Order No", width=80, anchor=CENTER, font=["Bodoni MT", 30, "bold"], background="skyblue3", relief="raised").pack(side='top', ipadx= 20, ipady=10)

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

with sqlite3.connect('Reflex Footwear.sql3') as conn2:
    cursor2 = conn2.cursor()
    my_data = cursor2.execute("SELECT DISTINCT Order2 FROM ProductionBreakdown")
    my_list = [r for r, in my_data]
    options = StringVar()

def del_date():
	dates1 = options1.get()
	order = options.get()
	dep = Departm.get()
	clicking = 'Clicking'
	closing = 'Closing'
	desp = 'Despatch'
	ware = 'Warehouse'
	ship = 'Shipped'
	tree.delete(*tree.get_children())
	if dep == clicking:
		with sqlite3.connect('Reflex Footwear.sql3') as conn:
			mycursor = conn.cursor()
			mycursor.execute("SELECT Factory,Date,Order2,SUM(Clicking) AS Clicking FROM ProductionBreakdown WHERE Date=? GROUP BY Order2", (dates1,))
			for row in mycursor:
				tree.insert("",END, values=(row[1], row[2], row[3]))
	elif dep == closing:
		with sqlite3.connect('Reflex Footwear.sql3') as conn:
			mycursor = conn.cursor()
			mycursor.execute("SELECT Factory,Date,Order2,SUM(Closing) AS Closing FROM ProductionBreakdown WHERE Date=? GROUP BY Order2", (dates1,))
			for row in mycursor:
				tree.insert("",END, values=(row[1], row[2], "", row[3]))
	elif dep == desp:
		with sqlite3.connect('Reflex Footwear.sql3') as conn:
			mycursor = conn.cursor()
			mycursor.execute("SELECT Factory,Date,Order2,SUM(Despatch) AS Despatch FROM ProductionBreakdown WHERE Date=? GROUP BY Order2", (dates1,))
			for row in mycursor:
				tree.insert("",END, values=(row[1], row[2], "", "", row[3]))
	elif dep == ware:
		with sqlite3.connect('Reflex Footwear.sql3') as conn:
			mycursor = conn.cursor()
			mycursor.execute("SELECT Factory,Date,Order2,SUM(Warehouse) AS Warehouse FROM ProductionBreakdown WHERE Date=? GROUP BY Order2", (dates1,))
			for row in mycursor:
				tree.insert("",END, values=(row[1], row[2], "", "", "", row[3]))
	elif dep == ship:
		with sqlite3.connect('Reflex Footwear.sql3') as conn:
			mycursor = conn.cursor()
			mycursor.execute("SELECT Factory,Date,Order2,SUM(Shipped) AS Shipped FROM ProductionBreakdown WHERE Date=? GROUP BY Order2", (dates1,))
			for row in mycursor:
				tree.insert("",END, values=(row[1], row[2], "", "", "", "", row[3]))
	else:
		with sqlite3.connect('Reflex Footwear.sql3') as conn:
			mycursor = conn.cursor()
			mycursor.execute("SELECT Factory,Date,Order2,SUM(Clicking) AS Clicking,SUM(Closing) AS Closing,SUM(Despatch) AS Despatch,SUM(Warehouse) AS Warehouse,SUM(Shipped) AS Shipped FROM ProductionBreakdown WHERE Date=? GROUP BY Order2", (dates1,))
			for row in mycursor:
				tree.insert('', 'end', values=row[1:8])


def per_order():
	order = options.get()
	dep = Departm.get()
	dates1 = options1.get()
	tree.delete(*tree.get_children())
	with sqlite3.connect('Reflex Footwear.sql3') as conn:
		mycursor = conn.cursor()
		mycursor.execute("SELECT Factory,Date,Order2,SUM(Clicking),SUM(Closing),SUM(Despatch),SUM(Warehouse),SUM(Shipped) FROM ProductionBreakdown WHERE Order2='{}'".format(order))
		for row in mycursor:
			tree.insert('', 'end', values=row[1:8])


def department():
	dep = Departm.get()
	clicking = 'Clicking'
	closing = 'Closing'
	desp = 'Despatch'
	ware = 'Warehouse'
	ship = 'Shipped'
	if dep == clicking:
		tree.delete(*tree.get_children())
		with sqlite3.connect('Reflex Footwear.sql3') as conn:
			mycursor = conn.cursor()
			mycursor.execute("SELECT Factory,Date,Order2,Clicking FROM ProductionBreakdown")
			for row in mycursor:
				tree.insert("",END, values=(row[1], row[2], row[3]))
	elif dep == closing:
		tree.delete(*tree.get_children())
		with sqlite3.connect('Reflex Footwear.sql3') as conn:
			mycursor = conn.cursor()
			mycursor.execute("SELECT Factory,Date,Order2,Closing FROM ProductionBreakdown")
			for row in mycursor:
				tree.insert("",END, values=(row[1], row[2], "", row[3]))
	elif dep == desp:
		tree.delete(*tree.get_children())
		with sqlite3.connect('Reflex Footwear.sql3') as conn:
			mycursor = conn.cursor()
			mycursor.execute("SELECT Factory,Date,Order2,Despatch FROM ProductionBreakdown")
			for row in mycursor:
				tree.insert("",END, values=(row[1], row[2], "", "", row[3]))
	elif dep == ware:
		tree.delete(*tree.get_children())
		with sqlite3.connect('Reflex Footwear.sql3') as conn:
			mycursor = conn.cursor()
			mycursor.execute("SELECT Factory,Date,Order2,Warehouse FROM ProductionBreakdown")
			for row in mycursor:
				tree.insert("",END, values=(row[1], row[2], "", "", "", row[3]))
	else:
		tree.delete(*tree.get_children())
		with sqlite3.connect('Reflex Footwear.sql3') as conn:
			mycursor = conn.cursor()
			mycursor.execute("SELECT Factory,Date,Order2,Shipped FROM ProductionBreakdown")
			for row in mycursor:
				tree.insert("",END, values=(row[1], row[2], "", "", "", "", row[3]))


frame = Frame(root)
frame.pack()

# Treeview
style = ttk.Style()
style.configure("Treeview.Heading", font=("Calibri", 15, 'bold'), foreground='black')

tree = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5, 6, 7), height=29, show="headings")
tree.pack(side='left')

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
scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
scroll.pack(side='right', fill='y')

tree.configure(yscrollcommand=scroll.set)

# Style of Buttons
style = Style()
style.configure('E.TButton', font=('Arial Narrow', 14, 'bold', 'underline'), foreground='firebrick2', background='skyblue3')
style.configure('N.TButton', font=('Arial Narrow', 14, 'bold', 'underline'), foreground='blue2', background='skyblue3')


def tkinter_ex1():
    ret1 = os.system('python excel_export_order_admin.py')
    if ret1:
        exit()


def tkinter_ex2():
    ret2 = os.system('python excel_export_dep_admin.py')
    if ret2:
        exit()


def tkinter_ex3():
    ret6 = os.system('python excel_export_date_admin.py')
    if ret6:
        exit()


def tkinter_ex4():
    ret3 = os.system('python excel_export_bal_admin.py')
    if ret3:
        exit()


option_1 = OptionMenu(root, Departm, *departm).pack(side="left", padx=10)
Departm.set("Department")
btn2 = Button(root, text='Department', style='N.TButton', command=department).pack(side='left', padx=10)

option_2 = OptionMenu(root, options1, *my_list1).pack(side="left", padx=10)
options1.set("Production Date")
btn2 = Button(root, text='Date', style='N.TButton', command=del_date).pack(side='left', padx=10)

option_2 = OptionMenu(root, options, *my_list).pack(side="left", padx=10)
options.set("Order No.")
btn2 = Button(root, text='OrderNo', style='N.TButton', command=per_order).pack(side='left', padx=10)

btn = Button(root, text='Close (Esc)', style='N.TButton', command=root.destroy).pack(side='right', padx=10)

mb =  Menubutton ( root, text = "Export", style='N.TButton' )
mb.pack(side='right')
mb.menu  =  Menu ( mb, tearoff = 0, activebackground="red", fg="ghost white", bg="chartreuse4", font=["Calibri", 14])
mb["menu"]  =  mb.menu

mb.menu.add_command (label = "By Order No", command = tkinter_ex1)
mb.menu.add_command (label = "By Department", command = tkinter_ex2)
mb.menu.add_command (label = "By Date", command = tkinter_ex3)
mb.menu.add_command (label = "Export All", command = tkinter_ex4)

mb.pack()


root.mainloop()
