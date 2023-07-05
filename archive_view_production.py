from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
import os
from datetime import datetime
import customtkinter

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
        mycursor.execute("SELECT Order2,Style,Deldate,Orderqty,Clicking,Closing,Despatch,ToShip FROM Production_Archive")
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
tree = ttk.Treeview(frame, columns=(0, 1, 2, 3, 4, 5, 6, 7), height=45, show="headings")
tree.pack(side='left')

tree.heading(0, text="Order No.", anchor=N)
tree.heading(1, text="Style/Description")
tree.heading(2, text="Delivery Date")
tree.heading(3, text="Order Qty")
tree.heading(4, text="To Click")
tree.heading(5, text="In Closing")
tree.heading(6, text="In Despatch")
tree.heading(7, text="To Ship")

tree.column(0, width=140)
tree.column(1, width=210)
tree.column(2, width=140)
tree.column(3, width=140)
tree.column(4, width=140)
tree.column(5, width=140)
tree.column(6, width=140)
tree.column(7, width=140)

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


def ClickPB():
    curItem = tree.focus()
    order = tree.item(curItem)['values'][0]
    root2 = Toplevel()
    #root2.state('zoomed') # Windowed view
    root2.attributes('-fullscreen', True)
    root2.title("Production Breakdown")
    root2.config(bg="skyblue2")
    style2 = ttk.Style()
    l_logsheet = Label(root2, text="Production Per Order", width=120, anchor=CENTER, font=["Bodoni MT", 30, "bold"], background="grey80", relief="raised").pack(side='top', ipady=10)

    def close_screen(e):
    	command=root2.destroy()
    root2.bind('<Escape>', lambda e: close_screen(e))

    def prod_break():
        tree2.delete(*tree2.get_children())
        with sqlite3.connect('Reflex Footwear.sql3') as conn:
            mycursor2 = conn.cursor()
            mycursor2.execute("SELECT Date,Order2,Clicking,Closing,Despatch,Shipped FROM ProdBreak_Archive WHERE Order2= '{}'".format(order))
            for row in mycursor2:
                    tree2.insert('', 'end',values=row[0:7])

    frame2 = Frame(root2)
    frame2.pack()
    style = ttk.Style()
    style.configure("New.Treeview", bd=2, font=('Calibri', 12))
    style.map('New.Treeview', background=[('selected', 'firebrick')])

    style.configure("New.Heading", font=( "Calibri", 15, 'bold'), background='silver', foreground='black')
    tree2 = ttk.Treeview(frame2, columns=(0, 1, 2, 3, 4, 5, 6), height=44, show="headings", style="New.Treeview")
    tree2.pack(side='left')

    tree2.heading(0, text="Date")
    tree2.heading(1, text="Order No.")
    tree2.heading(2, text="Clicking")
    tree2.heading(3, text="Closing")
    tree2.heading(4, text="Despatch")
    tree2.heading(6, text="Shipped")

    tree2.column(0, width=160)
    tree2.column(1, width=160)
    tree2.column(2, width=230)
    tree2.column(3, width=160)
    tree2.column(4, width=160)
    tree2.column(5, width=160)
    tree2.column(6, width=160)

    scroll2 = ttk.Scrollbar(frame2, orient="vertical", command=tree2.yview)
    scroll2.pack(side='right', fill='y')

    tree2.configure(yscrollcommand=scroll2.set)

    btn = customtkinter.CTkButton(root2, text="Close (Esc)", border_width=3, text_font=('Calibri', -15, 'bold'), fg_color='red', command=root2.destroy).pack(side='right')

    prod_break()
    root2.mainloop()


btn = Button(root, text='Exit', style='B.TButton', command=root.destroy).pack(side='right')
btn6 = Button(root, text="View Scores", style='R.TButton', command=tkinter7).pack(side='left')
btn2 = Button(root, text='Production', style='B.TButton', command=ClickPB).pack(side='left')

def close_screen2(e):
    	command=root.destroy()
root.bind('<Escape>', lambda e: close_screen2(e))

production()

root.mainloop()
