from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
import os
from datetime import datetime

root = Tk()
# root.state('zoomed') # Windowed view
root.attributes('-fullscreen', True)
root.title("Manufacturing")
root.config(bg="lightblue2")

l1 = Label(root, text="Archived Production Tracker", width=120, anchor=CENTER, font=["Bodoni MT", 30, "bold"], background="tomato", relief="raised").pack(side='top', ipady=10)


def production():
    tree.delete(*tree.get_children())
    tree.tag_configure("evenrow",background='white')
    # tree.tag_configure("oddrow",background='grey80')
    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        mycursor = conn.cursor()
        mycursor.execute("SELECT Date,Order2,Style,Cutting,Closing,Despatch,Shipped FROM ProdBreak_Archive")
        for row in mycursor:
                tree.insert('', 'end',values=row[0:9])#, tags=('evenrow'))

frame = Frame(root)
frame.pack()

# Treeview and Configuration
style = ttk.Style()
# Modify the font of the body
style.configure("Treeview", bd=2, font=('Calibri', 14))

# Modify OnClick
style.map('Treeview', background=[('selected', 'firebrick')])

# Modify the font of the heading and select columns
style.configure("Treeview.Heading", font=( "Calibri", 16, 'bold'), background='silver', foreground='black')
tree = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5, 6, 7), height=45, show="headings")
tree.pack(side='left')

tree.heading(1, text="Archived Date", anchor=N)
tree.heading(2, text="Order No.", anchor=N)
tree.heading(3, text="Style/Description")
tree.heading(4, text="To Click")
tree.heading(5, text="In Closing")
tree.heading(6, text="In Despatch")
tree.heading(7, text="Shipped")

tree.column(1, width=220)
tree.column(2, width=190)
tree.column(3, width=270)
tree.column(4, width=190)
tree.column(5, width=190)
tree.column(6, width=190)
tree.column(7, width=190)

scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
scroll.pack(side='right', fill='y')

tree.configure(yscrollcommand=scroll.set)


style = Style()
style.configure('R.TButton', font=('Calibri', 14, 'bold', 'underline'), foreground='dodgerblue4', background='black')
style.configure('B.TButton', font=('Calibri', 14, 'bold', 'underline'), foreground='firebrick', background='black')


def tkinter7():
    ret = os.system('python archive_view_prodbreak.py')
    if ret:
        production()

def close_screen2(e):
    	command=root.destroy()
root.bind('<Escape>', lambda e: close_screen2(e))

btn = Button(root, text='Exit', style='B.TButton', command=root.destroy).pack(side='right')


production()

root.mainloop()
