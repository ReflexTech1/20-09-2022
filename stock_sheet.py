from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
import os
from datetime import datetime
import customtkinter
from PIL import Image, ImageTk
import tkinter.messagebox


# Tkinter Create and Layout
root = Tk()
# root.state('zoomed') # Windowed view
root.attributes('-fullscreen', True)  # To make Full screen
root.title("Inventory Balance")
root.config(bg="skyblue2")

dateTimeObj = datetime.now()
xstampStr = dateTimeObj.strftime("%H:%M:%S %p")

l1 = Label(root, text="Inventory List", width=120, anchor=CENTER, font=["Bodoni MT", 30, "bold"], background="skyblue3", relief="raised").pack(side='top', ipady=10)
label_time = Label(root, text=xstampStr, width=11, anchor = CENTER, font=["Arial", 10, "bold"], background="skyblue3", relief="ridge")
label_time.pack(side='top', anchor = NE, ipady=5, ipadx=5)


def update_time():
    now = datetime.now()
    time_now = now.strftime("%H:%M:%S %p")
    label_time.config(text=time_now)
    root.after(1000, update_time)


def close_stock():
   command=root.destroy()

root.bind('<Escape>', lambda e: close_stock())

# Information from Database
def stock_sheet():
    tree.delete(*tree.get_children())
    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM StockSheet ORDER BY Category ASC")
        for row in mycursor:
            tree.insert('', 'end', values=row[0:6])

def StockRec(event):
    root3 = Toplevel()
    root3.geometry('380x270')
    root3.title("Record Stock")
    root3.config(bg="lightblue2")
    timestampStr = dateTimeObj.strftime("%m-%d-%Y")
    style3 = ttk.Style()
    Quantity = StringVar()
    curItem = tree.focus()
    code = tree.item(curItem)['values'][0]
    desc = tree.item(curItem)['values'][1]
    def StockUpdate():
        quantity = Quantity.get()
        with sqlite3.connect('Reflex Footwear.sql3') as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE StockSheet SET Quantity=Quantity+?, LastRec=? WHERE ItemCode=?', (quantity, timestampStr, code,))
            cursor.execute('INSERT INTO StockRecord (ItemCode,Description,Quantity,ReceiveDate) VALUES(?,?,?,?)', (code, desc, quantity, timestampStr,))
            updated = cursor.rowcount
            cursor.close()
            conn.commit()
            root3.destroy()
            stock_sheet()

    def submit_root(e):
       command=StockUpdate()

    root3.bind('<Return>', lambda e: submit_root(e))

    style3.configure('C.TButton', font=('Arial', 12, 'bold'), foreground='red')
    style3.configure('S.TButton', font=('Arial', 12, 'bold'), foreground='blue')

    label_0 = Label(root3, text="Receive Stock", background="lightblue2", width=20, font=("Arial", 20, "bold"))
    label_0.place(x=100, y=23)
    label_2 = Label(root3, text="Quantity", width=20, background="lightblue2", font=("Arial", 12, "bold"))
    label_2.place(x=20, y=100)
    entry_2 = Entry(root3, textvar=Quantity, background="lightblue2", font=("Arial", 12, "bold"))
    entry_2.place(x=180, y=100)

    # submitbtn = customtkinter.CTkButton(root3, text="Submit", border_width=3, text_font=('Calibri', -15, 'bold'), fg_color='blue', command=ClickUpdate).place(x=60, y=200)
    submit_btn = Button(root3, text='Submit', width=11, style='S.TButton', command=StockUpdate)
    submit_btn.place(x=60, y=220)
    exit1 = Button(root3, text='Close', width=11, style='C.TButton', command=root3.destroy)
    exit1.place(x=250, y=220)


root.bind("<Double-1>", StockRec)

frame = Frame(root)
frame.pack()

# Treeview and Configuration
style = ttk.Style()
# Modify the font of the body
style.configure("Treeview", bd=1, font=('Calibri', 11))
# Modify the font of the heading
style.configure("Treeview.Heading", font=("Calibri", 16, 'bold'), foreground='black')  # 'antiquewhite4')

tree = ttk.Treeview(frame, columns=(0, 1, 2, 3, 4, 5),
                    height=43, show="headings")
tree.pack(side='left')

tree.heading(0, text="Item Code")
tree.heading(1, text="Description")
tree.heading(2, text="Category")
tree.heading(3, text="Unit")
tree.heading(4, text="Quantity")
tree.heading(5, text="Last Received")

tree.column(0, width=150)
tree.column(1, width=400)
tree.column(2, width=200)
tree.column(3, width=200)
tree.column(4, width=200)
tree.column(5, width=200)

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


# Program to Open on Button Click
def tkinter2():
    ret = os.system('python stock_search.py')
    if ret:
        stock_sheet()


def tkinter3():
    ret = os.system('python stock_movement.py')
    if ret:
        stock_sheet()


def tkinter4():
    ret = os.system('python excel_export_req.py')
    if ret:
        stock_sheet()


def require1():
    ret = os.system('python excel_export_lu_req.py')
    if ret:
        stock_sheet()


def require2():
    ret = os.system('python excel_export_hop_req.py')
    if ret:
        stock_sheet()


def require3():
    ret = os.system('python excel_export_tba_req.py')
    if ret:
        stock_sheet()


def require4():
    ret = os.system('python excel_export_slip_req.py')
    if ret:
        stock_sheet()


def tkinter5():
    ret = os.system('python bill.py')
    if ret:
        stock_sheet()


# Buttons
''' Button Exit'''
btn = Button(root, text='Exit', style='E.TButton', command=root.destroy).pack(side='right')

''' Button 1'''
btn1 = Button(root, text="Current Stock", style='I/S.TButton', command=tkinter2).pack(side='left')

''' Button 2'''
btn2 = Button(root, text="View Movement", style='I/S.TButton', command=tkinter3).pack(side='left')

''' Button 3'''
# btn3 = Button(root, text="Export", style='I/S.TButton', command=tkinter4).pack(side='right')
# Export
mb4 =  Menubutton (root, text="Export", style='I/S.TButton')
mb4.menu  =  Menu ( mb4, tearoff = 0, activebackground="red", fg="ghost white", bg="chartreuse4", font=["Calibri", 14])
mb4["menu"]  =  mb4.menu
mb4.menu.add_command (label = "Lace Up", command = require1)
mb4.menu.add_command (label = "Idler", command = require2)
mb4.menu.add_command (label = "T-Bar", command = require3)
mb4.menu.add_command (label = "Slippers", command = require4)
mb4.pack(side='right')

''' Button 4'''
btn4 = Button(root, text="Costing", style='I/S.TButton', command=tkinter5).pack(side='right')

stock_sheet()

update_time()

root.mainloop()
