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


# Information from Database
def reflex_prod():
    tree.delete(*tree.get_children())
    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        mycursor = conn.cursor()
        mycursor.execute("SELECT Factory,Planned,Order2,Style,Deldate,Orderqty,Cutting,Assembly,Closing,Finishing,Despatch,ToShip,Shipped FROM Production_Balances")
        for row in mycursor:
            tree.insert('', 'end', values=row[1:14])


frame = Frame(root)
frame.pack()

# Treeview and Configuration
style = ttk.Style()
# Modify the font of the body
style.configure("Treeview", highlightthickness=0, bd=1, font=('Calibri', 11))
# Modify the font of the heading
style.configure("Treeview.Heading", font=( "Calibri", 15, 'bold'), foreground='black')

tree = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
                    height=44, show="headings")
tree.pack(side='left')

tree.heading(1, text="Date")
tree.heading(2, text="OrderNo")
tree.heading(3, text="Style / Description")
tree.heading(4, text="Delivery Date")
tree.heading(5, text="Quantity")
tree.heading(6, text="Cutting")
tree.heading(7, text="Assembly")
tree.heading(8, text="Closing")
tree.heading(9, text="Finishing")
tree.heading(10, text="Despatch")
tree.heading(11, text="To Ship")
tree.heading(12, text="Shipped")

tree.column(1, width=150)
tree.column(2, width=150)
tree.column(3, width=170)
tree.column(4, width=150)
tree.column(5, width=150)
tree.column(6, width=150)
tree.column(7, width=150)
tree.column(8, width=150)
tree.column(9, width=150)
tree.column(10, width=150)
tree.column(11, width=150)
tree.column(12, width=150)


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
    ret = os.system(r'python excel_export_balances.py')
    if ret:
        exit()


# Buttons
''' Button Exit'''
btn = Button(root, text='Exit', style='E.TButton', command=root.destroy).pack(side='right')

btn1 = Button(root, text='Export', style='I/S.TButton', command=tkinter1).pack(side='right')


reflex_prod()

root.mainloop()
