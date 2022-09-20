from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
import os

root = Tk()
# root.state('zoomed')
root.attributes('-fullscreen', True)
root.title("Logistics")
root.config(bg="skyblue2")

l1 = Label(root, text="Logistics", width=120, anchor=CENTER, font=["Bodoni MT", 30, "bold"], background="skyblue3", relief="raised").pack(side='top', ipady=10)

def logistics_view():
    tree.delete(*tree.get_children())
    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM Logistics")
        for row in mycursor:
            tree.insert('', 'end', values=row[0:4])


frame = Frame(root)
frame.pack()

style = ttk.Style()
style.configure("Treeview.Heading", font=("Calibri", 18,
                                          'bold'), foreground='black')  # 'antiquewhite4')

tree = ttk.Treeview(frame, columns=(0, 1, 2), height=30, show="headings")
tree.pack(side='left')

tree.heading(0, text="Date")
tree.heading(1, text="Truck Registration")
tree.heading(2, text="Document Reference")

tree.column(0, width=200)
tree.column(1, width=300)
tree.column(2, width=300)


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


def tkinter1():
    ret = os.system('python logistics_receive.py')
    if ret:
        logistics_view()


def tkinter2():
    ret = os.system('python logistics_send.py')
    if ret:
        logistics_view()


# Buttons
btn = Button(root, text='Exit', style='E.TButton',
             command=root.destroy).pack(side='right')
btn2 = Button(root, text="Send", style='I/S.TButton',
              command=tkinter2).pack(side='left')
btn1 = Button(root, text="Receive", style='I/S.TButton',
              command=tkinter1).pack(side='left')


logistics_view()

root.mainloop()
