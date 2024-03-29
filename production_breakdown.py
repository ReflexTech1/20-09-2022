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

l1 = Label(root, text="Production Scores", width=120, anchor=CENTER, font=["Bodoni MT", 30, "bold"], background="grey80", relief="raised").pack(side='top', ipady=10)


def close_screen(e):
    command=root.destroy()
root.bind('<Escape>', lambda e: close_screen(e))


# Information from Database
def reflex_prod():
    tree.delete(*tree.get_children())
    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        mycursor = conn.cursor()
        mycursor.execute("SELECT Factory,Date,Line,Order2,Style,Cutting,Assembly,Closing,Despatch,Shipped,Reason FROM ProductionBreakdown")
        for row in mycursor:
            tree.insert('', 'end', values=row[1:11])


frame = Frame(root)
frame.pack()

# Treeview and Configuration
style = ttk.Style()
# Modify the font of the body
style.configure("Treeview", highlightthickness=0, bd=1, font=('Calibri', 12))
# Modify the font of the heading
style.configure("Treeview.Heading", font=( "Calibri", 15, 'bold'), foreground='black')

tree = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                    height=44, show="headings")
tree.pack(side='left')

tree.heading(1, text="Date")
tree.heading(2, text="Line")
tree.heading(3, text="OrderNo")
tree.heading(4, text="Style")
tree.heading(5, text="Cutting")
tree.heading(6, text="Assembly")
tree.heading(7, text="Closing")
tree.heading(8, text="Despatch")
tree.heading(9, text="Shipped")
tree.heading(10, text="Reason")

tree.column(1, width=150)
tree.column(2, width=150)
tree.column(3, width=180)
tree.column(4, width=220)
tree.column(5, width=180)
tree.column(6, width=180)
tree.column(7, width=180)
tree.column(8, width=180)
tree.column(9, width=180)
tree.column(10, width=180)


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
    ret = os.system(r'python excel_export_bal.py')
    if ret:
        exit()


def tkinter2():
    ret = os.system(r'python admin_production_by_filter.py')
    if ret:
        exit()

# Buttons
''' Button Exit'''
btn = Button(root, text='Exit', style='E.TButton', command=root.destroy).pack(side='right')

btn1 = Button(root, text='Export', style='I/S.TButton', command=tkinter1).pack(side='right')
btn2 = Button(root, text="Filter", style='I/S.TButton', command=tkinter2).pack(side='left')

reflex_prod()

root.mainloop()
