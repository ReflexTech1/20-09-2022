from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *

root = Tk()
root.state('zoomed')
root.title("Logistics")
root.config(bg="skyblue2")


def costing2():
    tree.delete(*tree.get_children())
    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM CostingCal")
        for row in mycursor:
            tree.insert('', 'end', values=row[0:14])


frame = Frame(root)
frame.pack()

style = ttk.Style()
style.configure("Treeview.Heading", font=(
    "Arial Narrow", 14, 'bold', 'underline'), foreground='black')

tree = ttk.Treeview(frame, columns=(0, 1, 2, 3, 4, 5, 6, 7,
                                    8, 9, 10, 11, 12, 13), height=32, show="headings")
tree.pack(side='left')

tree.heading(0, text="Description")
tree.heading(1, text="Upper")
tree.heading(2, text="Stiffener")
tree.heading(3, text="Insole")
tree.heading(4, text="PU Lining")
tree.heading(5, text="Buckle")
tree.heading(6, text="Rivets")
tree.heading(7, text="Laces")
tree.heading(8, text="Eyelets")
tree.heading(9, text="Foil")
tree.heading(10, text="PBA 887")
tree.heading(11, text="Gusset Elastic")
tree.heading(12, text="IA 80")
tree.heading(13, text="Cartons")

tree.column(0, width=150)
tree.column(1, width=110)
tree.column(2, width=120)
tree.column(3, width=120)
tree.column(4, width=110)
tree.column(5, width=80)
tree.column(6, width=80)
tree.column(7, width=80)
tree.column(8, width=90)
tree.column(9, width=80)
tree.column(10, width=70)
tree.column(11, width=120)
tree.column(12, width=70)
tree.column(13, width=90)

# Button Style Configuration
style = Style()
style.configure('E.TButton', font=('Century Gothic', 12, 'bold',
                                   'underline'), foreground='firebrick3', background='black')

# Buttons
btn = Button(root, text='Exit', style='E.TButton',
             command=root.destroy).pack(side='right')

costing2()

root.mainloop()
