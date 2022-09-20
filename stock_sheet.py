from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
import os


# Tkinter Create and Layout
root = Tk()
# root.state('zoomed') # Windowed view
root.attributes('-fullscreen', True)  # To make Full screen
root.title("Inventory Balance")
root.config(bg="skyblue2")

l1 = Label(root, text="Inventory List", width=120, anchor=CENTER, font=["Bodoni MT", 30, "bold"], background="skyblue3", relief="raised").pack(side='top', ipady=10)


# Information from Database
def stock_sheet():
    tree.delete(*tree.get_children())
    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM StockSheet")
        for row in mycursor:
            tree.insert('', 'end', values=row[0:6])


frame = Frame(root)
frame.pack()

# Treeview and Configuration
style = ttk.Style()
# Modify the font of the body
style.configure("Treeview", bd=1, font=('Calibri', 11))
# Modify the font of the heading
style.configure("Treeview.Heading", font=("Calibri", 18, 'bold'), foreground='black')  # 'antiquewhite4')

tree = ttk.Treeview(frame, columns=(0, 1, 2, 3, 4, 5),
                    height=45, show="headings")
tree.pack(side='left')

tree.heading(0, text="Item Code")
tree.heading(1, text="Description")
tree.heading(2, text="Category")
tree.heading(3, text="Unit")
tree.heading(4, text="Quantity")
tree.heading(5, text="Last Received")

tree.column(0, width=150)
tree.column(1, width=400)
tree.column(2, width=200)
tree.column(3, width=200)
tree.column(4, width=200)
tree.column(5, width=200)

# Scrollbar Layout and Configuration
scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
scroll.pack(side='right', fill='y')

tree.configure(yscrollcommand=scroll.set)

# Button Style Configuration
style = Style()
style.configure('E.TButton', font=('Century Gothic', 12, 'bold',
                                   'underline'), foreground='firebrick3', background='black')
style.configure('I/S.TButton', font=('Century Gothic', 12, 'bold',
                                     'underline'), foreground='dodgerblue4', background='black')


# Program to Open on Button Click
def tkinter1():
    ret = os.system('python stock_receive.py')
    if ret:
        # record updated, reload data
        stock_sheet()


def tkinter2():
    ret = os.system('python stock_search.py')
    if ret:
        stock_sheet()


def tkinter3():
    ret = os.system('python stock_movement.py')
    if ret:
        stock_sheet()


def tkinter4():
    ret = os.system('python excel_export_req.py')
    if ret:
        stock_sheet()


def require1():
    ret = os.system('python excel_export_lu_req.py')
    if ret:
        stock_sheet()


def require2():
    ret = os.system('python excel_export_hop_req.py')
    if ret:
        stock_sheet()


def require3():
    ret = os.system('python excel_export_tba_req.py')
    if ret:
        stock_sheet()


def require4():
    ret = os.system('python excel_export_slip_req.py')
    if ret:
        stock_sheet()


def tkinter5():
    ret = os.system('python bill.py')
    if ret:
        stock_sheet()


# Buttons
''' Button Exit'''
btn = Button(root, text='Exit', style='E.TButton', command=root.destroy).pack(side='right')

''' Button 1'''
btn1 = Button(root, text="Search Stock", style='I/S.TButton', command=tkinter2).pack(side='left')

''' Button 2'''
btn2 = Button(root, text="Issue/Receive", style='I/S.TButton', command=tkinter1).pack(side='left')

''' Button 3'''
btn3 = Button(root, text="View Movement", style='I/S.TButton', command=tkinter3).pack(side='left')

''' Button 4'''
# btn4 = Button(root, text="Export", style='I/S.TButton', command=tkinter4).pack(side='right')
# Export
mb4 =  Menubutton (root, text="Export", style='I/S.TButton')
mb4.menu  =  Menu ( mb4, tearoff = 0, activebackground="red", fg="ghost white", bg="chartreuse4", font=["Calibri", 14])
mb4["menu"]  =  mb4.menu
mb4.menu.add_command (label = "Lace Up", command = require1)
mb4.menu.add_command (label = "Idler", command = require2)
mb4.menu.add_command (label = "T-Bar", command = require3)
mb4.menu.add_command (label = "Slippers", command = require4)
mb4.pack(side='right')

''' Button 5'''
btn5 = Button(root, text="Costing", style='I/S.TButton', command=tkinter5).pack(side='right')

stock_sheet()

root.mainloop()
