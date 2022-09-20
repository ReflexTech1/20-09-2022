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
        mycursor.execute("SELECT Order2,Style,Deldate,Orderqty,Clicking,Closing,Finishing,Despatch,ToShip FROM SandalProd_Archive")
        for row in mycursor:
                tree.insert('', 'end',values=row[0:9], tags=('evenrow'))

frame = Frame(root)
frame.pack()

# Treeview and Configuration
style = ttk.Style()
# Modify the font of the body
style.configure("Treeview", bd=2, font=('Calibri', 12))

# Modify OnClick
style.map('Treeview', background=[('selected', 'firebrick')])

# Modify the font of the heading and select columns
style.configure("Treeview.Heading", font=( "Calibri", 15, 'bold'), background='silver', foreground='black')
tree = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), height=45, show="headings")
tree.pack(side='left')

tree.heading(1, text="Order No.", anchor=N)
tree.heading(2, text="Style/Description")
tree.heading(3, text="Delivery Date")
tree.heading(4, text="Order Qty")
tree.heading(5, text="To Click")
tree.heading(6, text="In Closing")
tree.heading(7, text="In Finishing")
tree.heading(8, text="In Despatch")
tree.heading(9, text="To Ship")

tree.column(1, width=140)
tree.column(2, width=210)
tree.column(3, width=140)
tree.column(4, width=140)
tree.column(5, width=140)
tree.column(6, width=140)
tree.column(7, width=140)
tree.column(8, width=140)
tree.column(9, width=140)

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


btn = Button(root, text='Exit', style='B.TButton', command=root.destroy).pack(side='right')
btn6 = Button(root, text="View Scores", style='R.TButton', command=tkinter7).pack(side='left')


production()

root.mainloop()
