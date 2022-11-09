from tkinter import *
from tkinter.ttk import *
import os
from datetime import datetime
import customtkinter
from PIL import Image, ImageTk
import tkinter.messagebox

master = Tk()
master.geometry('660x620')
master.title("Manufacturing")
master.config(bg="skyblue1")
master.resizable(0,0)

l1 = Label(master, text="Reflex Footwear", background="skyblue1", relief="raised", foreground="grey10", font=["CF National Stitches", 40], anchor=N)
l1.grid(row=0, column=0, columnspan=4, ipadx=30, pady=10, ipady=5, sticky=N)
l2 = Label(master, text="Administrator", background="skyblue1", relief="raised", foreground="grey10", font=["Arial", 10, "bold"], anchor="center")
l2.grid(row=0, column=4, columnspan=1, ipadx=10, pady=10, ipady=5, sticky=E)

def tkinter1():
    ret = os.system(r'python admin_orders.py')
    if ret:
        exit()


def tkinter2():
    ret = os.system('python orders_slip.py')
    if ret:
        exit()


def tkinter3():
    ret = os.system('python orders_sandal.py')
    if ret:
        exit()


def tkinter_stock():
    ret = os.system('python stock_sheet.py')
    if ret:
        exit()


def tkinter_log():
    ret = os.system('python logistics_view.py')
    if ret:
        exit()


def tkinter6():
    ret = os.system('python admin_production.py')
    if ret:
        exit()


def tkinter7():
    ret = os.system('python production_slip.py')
    if ret:
        exit()


def tkinter8():
    ret = os.system('python production_sandal.py')
    if ret:
        exit()


def tkinter_ex1():
    ret = os.system('python excel_export_orders.py')
    if ret:
        exit()


def tkinter_ex2():
    ret = os.system('python excel_export_prod_1.py')
    if ret:
        exit()


def tkinter_ex3():
    ret = os.system('python excel_export_bal_admin.py')
    if ret:
        exit()


def tkinter_ex4():
    ret = os.system('python excel_export_stock.py')
    if ret:
        exit()


def tkinter_ex5():
    ret = os.system('python excel_export_planning.py')
    if ret:
        exit()


def tkinter_ex6():
    ret = os.system('python excel_export_bal_admin.py')
    if ret:
        exit()


def tkinter_arch():
    ret = os.system('python archive_view_orders.py')
    if ret:
        exit()


# Style of Buttons
style = Style()
style.configure('N.TButton', font=('Arial Narrow', 20, 'bold'), foreground='red', background='skyblue1')

# Images
img = PhotoImage(file=r"C:\RSoft\Current\Buttons\sig.png")
img1 = img.subsample(1, 1)


# Setting image in label
Label(master, image=img1).grid(row=1, column=1, columnspan=4, rowspan=12, padx=30, pady=30, sticky=S + W)

# Menubuttons
# Orders
mb =  Menubutton (master, text = "")
mb.menu  =  Menu (mb, tearoff = 0, activebackground="red", fg="ghost white", bg="chartreuse4", font=["Calibri", 14])
mb["menu"]  =  mb.menu
mb.menu.add_command (label = "School Shoes", command = tkinter1)
mb.menu.add_command (label = "Slipper", command = tkinter2)
mb.menu.add_command (label = "Sandals", command = tkinter3)

# Production
mb2 =  Menubutton (master, text = "")
mb2.menu  =  Menu (mb2, tearoff = 0, activebackground="red", fg="ghost white", bg="chartreuse4", font=["Calibri", 14])
mb2["menu"]  =  mb2.menu
mb2.menu.add_command (label = "School Shoes", command = tkinter6)
mb2.menu.add_command (label = "Slipper", command = tkinter7)
mb2.menu.add_command (label = "Sandals", command = tkinter8)

# Export
mb4 =  Menubutton (master, text = "")
mb4.menu  =  Menu (mb4, tearoff = 0, activebackground="red", fg="ghost white", bg="chartreuse4", font=["Calibri", 14])
mb4["menu"]  =  mb4.menu
mb4.menu.add_command (label = "Orders In House", command = tkinter_ex1)
mb4.menu.add_command (label = "Production Tracker", command = tkinter_ex2)
mb4.menu.add_command (label = "Production Scores", command = tkinter_ex3)
mb4.menu.add_command (label = "Production Balances", command = tkinter_ex3)
mb4.menu.add_command (label = "Inventory List", command = tkinter_ex4)
mb4.menu.add_command (label = "Size Range", command = tkinter_ex5)

# TO COMPILE btn5 = customtkinter.CTkButton(master, text="Forecast", border_width=3, text_font=('Calibri', -15, 'bold'), fg_color='green', command=tkinter6).pack(side='right')
# TO COMPILE btn5 = customtkinter.CTkButton(master, text="Efficiency", border_width=3, text_font=('Calibri', -15, 'bold'), fg_color='green', command=tkinter7).pack(side='right')
b3 = customtkinter.CTkButton(master, text="Stock In House", border_width=1, text_font=('Calibri', -22, 'bold'), fg_color='green', command=tkinter_stock)
b4 = customtkinter.CTkButton(master, text="Logistics", border_width=1, text_font=('Calibri', -22, 'bold'), fg_color='green', command=tkinter_log)
b7 = customtkinter.CTkButton(master, text="Exit", border_width=1, text_font=('Calibri', -22, 'bold'), fg_color='red', command=master.destroy)
b8 = customtkinter.CTkButton(master, text="Archived", border_width=1, text_font=('Calibri', -22, 'bold'), fg_color='green', command=tkinter_arch)

# Arranging Buttons
mb.grid(row=1, column=0, padx=20, pady=5, sticky=W + N)
b3.grid(row=3, column=0, padx=20, pady=5, sticky=W + N)
b4.grid(row=4, column=0, padx=20, pady=5, sticky=W + N)
mb4.grid(row=5, column=0, padx=20, pady=5, sticky=W + N)
mb2.grid(row=6, column=0, padx=20, pady=5, sticky=W + N)
b8.grid(row=7, column=0, padx=20, pady=5, sticky=W + N)
b7.grid(row=8, column=0, padx=20, pady=5, sticky=W + N)


def exit_soft():
   command=master.destroy()

master.bind('<Escape>', lambda e: exit_soft())


mainloop()
