from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
import os

# Tkinter Create and Layout
root = Tk()
# root.state('zoomed') # Windowed view
root.attributes('-fullscreen', True)  # To make Full screen
root.title("Production Balance")
root.config(bg="skyblue2")

l1 = Label(root, text="Production Balances", width=120, anchor=CENTER, font=["Bodoni MT", 30, "bold"], background="grey80", relief="raised").pack(side='top', ipady=10)


def close_screen(e):
    command=root.destroy()
root.bind('<Escape>', lambda e: close_screen(e))

Departm = StringVar()
departm = ("Department","Department","Clicking", "Closing", "Despatch", "Warehouse", "To Ship", "Shipped")

with sqlite3.connect('Reflex Footwear.sql3') as conn:
    cursor = conn.cursor()
    my_data1 = cursor.execute("SELECT DISTINCT DelDate FROM Production_Balances ORDER BY DelDate ASC")
    my_list1 = [r for r, in my_data1]
    options1 = StringVar()


def del_date():
    dates1 = options1.get()
    tree.delete(*tree.get_children())
    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        mycursor = conn.cursor()
        mycursor.execute("SELECT Order2,Style,Deldate,Orderqty,Clicking,Closing,Finishing,Despatch,Warehouse,ToShip,Shipped FROM Production_Balances WHERE DelDate=?", (dates1,))
        for row in mycursor:
            tree.insert('', 'end', values=row[0:10])


def department():
    dates1 = options1.get()
    dep = Departm.get()
    clicking = 'Clicking'
    closing = 'Closing'
    desp = 'Despatch'
    ware = 'Warehouse'
    toship = 'To Ship'
    ship = 'Shipped'
    tree.delete(*tree.get_children())
    if dep == clicking:
        with sqlite3.connect('Reflex Footwear.sql3') as conn:
            mycursor = conn.cursor()
            mycursor.execute("SELECT Planned,Order2,Style,DelDate,Orderqty,Clicking FROM Production_Balances ORDER BY DelDate ASC")
            for row in mycursor:
                tree.insert("",END, values=(row[1], row[2], row[3], row[4], row[5]))
    elif dep == closing:
        with sqlite3.connect('Reflex Footwear.sql3') as conn:
            mycursor = conn.cursor()
            mycursor.execute("SELECT Planned,Order2,Style,DelDate,Orderqty,Closing FROM Production_Balances ORDER BY DelDate ASC")
            for row in mycursor:
                tree.insert("",END, values=(row[1], row[2], row[3], row[4], "", row[5]))
    elif dep == desp:
        with sqlite3.connect('Reflex Footwear.sql3') as conn:
            mycursor = conn.cursor()
            mycursor.execute("SELECT Planned,Order2,Style,DelDate,Orderqty,Despatch FROM Production_Balances ORDER BY DelDate ASC")
            for row in mycursor:
                tree.insert("",END, values=(row[1], row[2], row[3], row[4], "", "", row[5]))
    elif dep == ware:
        with sqlite3.connect('Reflex Footwear.sql3') as conn:
            mycursor = conn.cursor()
            mycursor.execute("SELECT Planned,Order2,Style,DelDate,Orderqty,Warehouse FROM Production_Balances ORDER BY DelDate ASC")
            for row in mycursor:
                tree.insert("",END, values=(row[1], row[2], row[3],row[4], "", "", "", row[5]))
    elif dep == toship:
        with sqlite3.connect('Reflex Footwear.sql3') as conn:
            mycursor = conn.cursor()
            mycursor.execute("SELECT Planned,Order2,Style,DelDate,Orderqty,ToShip FROM Production_Balances ORDER BY DelDate ASC")
            for row in mycursor:
                tree.insert("",END, values=(row[1], row[2], row[3], row[4], "", "", "", "", row[5]))
    elif dep == ship:
        with sqlite3.connect('Reflex Footwear.sql3') as conn:
            mycursor = conn.cursor()
            mycursor.execute("SELECT Planned,Order2,Style,DelDate,Orderqty,Shipped FROM Production_Balances ORDER BY DelDate ASC")
            for row in mycursor:
                tree.insert("",END, values=(row[1], row[2], row[3], row[4], "", "", "", "", "", row[5]))
    else:
       with sqlite3.connect('Reflex Footwear.sql3') as conn:
           mycursor = conn.cursor()
           mycursor.execute("SELECT Planned,Order2,Style,DelDate,Orderqty,Clicking,Closing,Despatch,Warehouse,ToShip,Shipped FROM Production_Balances ORDER BY DelDate ASC")
           for row in mycursor:
               tree.insert('', 'end', values=row[1:11])

# Information from Database
def reflex_prod():
    tree.delete(*tree.get_children())
    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        mycursor = conn.cursor()
        mycursor.execute("SELECT Order2,Style,Deldate,Orderqty,Clicking,Closing,Despatch,Warehouse,ToShip,Shipped FROM Production_Balances ORDER BY DelDate ASC")
        for row in mycursor:
            tree.insert('', 'end', values=row[0:10])


frame = Frame(root)
frame.pack()

# Treeview and Configuration
style = ttk.Style()
# Modify the font of the body
style.configure("Treeview", highlightthickness=0, bd=1, font=('Calibri', 11))
# Modify the font of the heading
style.configure("Treeview.Heading", font=( "Calibri", 15, 'bold'), foreground='black')

tree = ttk.Treeview(frame, columns=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
                    height=24, show="headings")
tree.pack(side='left')

tree.heading(0, text="OrderNo")
tree.heading(1, text="Style / Description")
tree.heading(2, text="Delivery Date")
tree.heading(3, text="Quantity")
tree.heading(4, text="Clicking")
tree.heading(5, text="Closing")
tree.heading(6, text="Despatch")
tree.heading(7, text="Warehouse")
tree.heading(8, text="To Ship")
tree.heading(9, text="Shipped")

tree.column(0, width=150)
tree.column(1, width=170)
tree.column(2, width=150)
tree.column(3, width=150)
tree.column(4, width=150)
tree.column(5, width=150)
tree.column(6, width=150)
tree.column(7, width=150)
tree.column(8, width=150)
tree.column(9, width=150)


# Scrollbar Layout and Configuration
scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
scroll.pack(side='right', fill='y')

tree.configure(yscrollcommand=scroll.set)

# Button Style Configuration
style = Style()
style.configure('E.TButton', font=('Century Gothic', 12, 'bold',
                                   'underline'), foreground='firebrick3', background='grey80')
style.configure('I/S.TButton', font=('Century Gothic', 12, 'bold',
                                     'underline'), foreground='dodgerblue4', background='grey80')

def tkinter1():
    ret = os.system(r'python excel_export_bal_admin.py')
    if ret:
        exit()


# Buttons
option_1 = OptionMenu(root, Departm, *departm).pack(side="left", padx=10)
Departm.set("Department")
btn2 = Button(root, text='Department', style='I/S.TButton', command=department).pack(side='left', padx=10)

option_2 = OptionMenu(root, options1, *my_list1).pack(side="left", padx=10)
options1.set("Delivery Date")
btn2 = Button(root, text='Date', style='I/S.TButton', command=del_date).pack(side='left', padx=10)

btn = Button(root, text='Exit', style='E.TButton', command=root.destroy).pack(side='right')

btn1 = Button(root, text='Export', style='I/S.TButton', command=tkinter1).pack(side='right')


reflex_prod()

root.mainloop()
