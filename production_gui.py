from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
import os
from datetime import datetime
import customtkinter
from PIL import Image, ImageTk
import tkinter.messagebox

root = Tk()
root.state('zoomed') # Windowed view
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (width,height))
root.title("Manufacturing")
root.config(bg="lightblue2")

dateTimeObj = datetime.now()

l1 = Label(root, text="LogSheet Tracker", width=120, anchor=CENTER, font=["Bodoni MT", 30, "bold"], background="grey80", relief="raised").pack(side='top', ipady=10)
# l1 = customtkinter.CTkLabel(root, text="LogSheet Tracker", text_font=("Bodoni MT", -30), bg="grey80").pack(side='top', ipady=10)


def production():
    tree.delete(*tree.get_children())
    tree.tag_configure("evenrow",background='white')
    # tree.tag_configure("oddrow",background='grey80')
    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        mycursor = conn.cursor()
        mycursor.execute("SELECT Order2,Style,Deldate,Orderqty,Clicking,Closing,Finishing,Despatch,Warehouse,ToShip FROM Production")
        for row in mycursor:
                tree.insert('', 'end',values=row[0:12])

def DblClick(event):
    curItem = tree.focus()
    order = tree.item(curItem)['values'][0]
    desc = 0
    root2 = Tk()
    root2.state('zoomed') # Windowed view
    root2.title("Production Breakdown")
    root2.config(bg="skyblue2")
    style2 = ttk.Style()
    l_logsheet = Label(root2, text="Log Sheet", width=120, anchor=CENTER, font=["Bodoni MT", 30, "bold"], background="grey80", relief="raised").pack(side='top', ipady=10)

    def close_screen(e):
    	command=root2.destroy()
    root2.bind('<Escape>', lambda e: close_screen(e))

    def logsheet():
        tree2.delete(*tree2.get_children())
        with sqlite3.connect('Log Sheets.sql3') as conn:
            mycursor2 = conn.cursor()
            mycursor2.execute("SELECT Barcode,OrderNo,Style,Delivery,Size2,Size3,Size4,Size5,Qty,Ticket FROM '{}'".format(order))
            for row in mycursor2:
                    tree2.insert('', 'end',values=row[0:9])

    frame2 = Frame(root2)
    frame2.pack()
    style2 = ttk.Style()
    style2.configure("Treeview", bd=2, font=('Calibri', 12))
    style2.map('Treeview', background=[('selected', 'firebrick')])

    style2.configure("Treeview2.Heading", font=( "Calibri", 15, 'bold'), background='silver', foreground='black')
    tree2 = ttk.Treeview(frame2, columns=(0, 1, 2, 3, 4, 5), height=44, show="headings")
    tree2.pack(side='left')

    tree2.heading(0, text="Barcode")
    tree2.heading(1, text="Order No.")
    tree2.heading(2, text="Style/Description")
    tree2.heading(3, text="Delivery Date")
    tree2.heading(4, text="Size")
    tree2.heading(5, text="Quantity")

    tree2.column(0, width=160)
    tree2.column(1, width=160)
    tree2.column(2, width=230)
    tree2.column(3, width=160)
    tree2.column(4, width=160)
    tree2.column(5, width=160)

    scroll2 = ttk.Scrollbar(frame2, orient="vertical", command=tree2.yview)
    scroll2.pack(side='right', fill='y')

    tree2.configure(yscrollcommand=scroll2.set)

    logsheet()
    root2.mainloop()

#Bind keys
root.bind("<Double-1>", DblClick)


def close_screen(e):
	command=root.destroy()
root.bind('<Escape>', lambda e: close_screen(e))

frame = Frame(root)
frame.pack()

# Treeview and Configuration
style = ttk.Style()
# Modify the font of the body
style.configure("Treeview", bd=2, font=('Calibri', 12))

# Modify OnClick
style.map('Treeview', background=[('selected', 'firebrick')])

# Modify the font of the heading and select columns
style.configure("Treeview.Heading", font=( "Calibri", 15, 'bold'), background='silver' ,foreground='black')
tree = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), height=30, show="headings")
tree.pack(side='left')

tree.heading(1, text="Order No.", anchor=N)
tree.heading(2, text="Style/Description")
tree.heading(3, text="Delivery Date")
tree.heading(4, text="Order Qty")
tree.heading(5, text="To Click")
tree.heading(6, text="In Closing")
tree.heading(7, text="In Finishing")
tree.heading(8, text="In Despatch")
tree.heading(9, text="In Warehouse")
tree.heading(10, text="To Ship")

tree.column(1, width=140)
tree.column(2, width=210)
tree.column(3, width=140)
tree.column(4, width=140)
tree.column(5, width=140)
tree.column(6, width=140)
tree.column(7, width=140)
tree.column(8, width=140)
tree.column(9, width=140)
tree.column(10, width=140)

scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
scroll.pack(side='right', fill='y')

tree.configure(yscrollcommand=scroll.set)


style = Style()
style.configure('R.TButton', font=('Calibri', 14, 'bold', 'underline'), foreground='dodgerblue4', background='grey80') # To Be Removed

def tkinter1():
    ret = os.system('python update_clicking.py')
    if ret:
        production()


def tkinter2():
    ret = os.system('python update_closing.py')
    if ret:
        production()


def tkinter3():
    ret = os.system('python update_despatch.py')
    if ret:
        production()


def tkinter4():
    ret = os.system('python update_warehouse.py')
    if ret:
        production()


def tkinter5():
    ret = os.system('python update_shipped.py')
    if ret:
        production()


def tkinter6():
    ret = os.system('python excel_export_prod_1.py')
    if ret:
        production()


def tkinter7():
    ret = os.system('python production_breakdown.py')
    if ret:
        production()


def tkinter8():
    ret = os.system('python archive_order.py')
    if ret:
        production()


btn = customtkinter.CTkButton(root, text="Close (Esc)", border_width=3, text_font=('Calibri', -15, 'bold'), fg_color='red', command=root.destroy).pack(side='right')

mb =  Menubutton (root, text = "Scores", style='R.TButton' )
mb.pack(side='left')
mb.menu  =  Menu ( mb, tearoff = 0, activebackground="red", fg="ghost white", bg="chartreuse4", font=["Calibri", 14])
mb["menu"]  =  mb.menu

mb.menu.add_command (label = "Clicking", command = tkinter1)
mb.menu.add_command (label = "Closing", command = tkinter2)
mb.menu.add_command (label = "Despatch", command = tkinter3)
mb.menu.add_command (label = "Warehouse", command = tkinter4)
mb.menu.add_command (label = "Shipped", command = tkinter5)
mb.pack()
btn5 = customtkinter.CTkButton(root, text="Export", border_width=3, text_font=('Calibri', -15, 'bold'), fg_color='green', command=tkinter6).pack(side='right')
btn6 = customtkinter.CTkButton(root, text="View Scores", border_width=3, text_font=('Calibri', -15, 'bold'), fg_color='green', command=tkinter7).pack(side='left')
btn7 = customtkinter.CTkButton(root, text="Archive", border_width=3, text_font=('Calibri', -15, 'bold'), fg_color='green', command=tkinter8).pack(side='left')

production()

root.mainloop()
