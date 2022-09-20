from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
import os

# Tkinter Create and Layout
root = Tk()
# root.state('zoomed') # Windowed view
root.attributes('-fullscreen', True)  # To make Full screen
root.title("Stock Movement")
root.config(bg="skyblue2")


# Information from Database
def stock_movement():
    tree.delete(*tree.get_children())
    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        mycursor = conn.cursor()
        mycursor.execute(
            "SELECT ItemCode,Quantity,ReceiveDate FROM StockRecord")
        for row in mycursor:
            tree.insert('', 'end', values=row[0:6])


frame = Frame(root)
frame.pack()

# Treeview and Configuration
style = ttk.Style()
style.configure("Treeview.Heading", font=("Arial Narrow", 18,
                                          'bold', 'underline'), foreground='black')  # 'antiquewhite4')

tree = ttk.Treeview(frame, columns=(0, 1, 2), height=32, show="headings")
tree.pack(side='left')

tree.heading(0, text="Description")
tree.heading(1, text="Quantity")
tree.heading(2, text="Date received")

tree.column(0, width=200)
tree.column(1, width=200)
tree.column(2, width=200)

# Scrollbar Layout and Configuration
scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
scroll.pack(side='right', fill='y')

tree.configure(yscrollcommand=scroll.set)

# Button Style Configuration
style = Style()
style.configure('E.TButton', font=('Century Gothic', 14, 'bold',
                                   'underline'), foreground='firebrick3', background='black')
style.configure('I/S.TButton', font=('Century Gothic', 12, 'bold',
                                     'underline'), foreground='dodgerblue4', background='black')

# Program to Open on Button Click


def tkinter1():
    ret = os.system('python stock_move_search.py')
    if ret:
        # record updated, reload data
        stock_movement()


def tkinter2():
    ret = os.system('python excel_export_stock_move.py')
    if ret:
        # record updated, reload data
        stock_movement()


# Buttons
''' Button 1'''
btn1 = Button(root, text="Search Item", style='I/S.TButton',
              command=tkinter1).pack(side='left')

''' Button 2'''
btn1 = Button(root, text="Export", style='I/S.TButton',
              command=tkinter2).pack(side='left')

''' Button Exit'''
btn = Button(root, text='Exit', style='E.TButton',
             command=root.destroy).pack(side='right')

stock_movement()

root.mainloop()
