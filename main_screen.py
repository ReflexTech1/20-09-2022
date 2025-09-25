from tkinter import *
from tkinter.ttk import *
import os

master = Tk()
master.geometry('650x620')
master.title("Manufacturing")
master.config(bg="skyblue1")
master.resizable(0,0)

l1 = Label(master, text="Reflex Footwear", background="skyblue1", relief="raised", foreground="grey10", font=["CF National Stitches", 40], anchor=N)
l1.grid(row=0, column=0, columnspan=7, ipadx=30, pady=10, ipady=5, sticky=N)


def tkinter1():
    ret = os.system(r'python C:\RSoft\Current\Main\NewOrders\orders.py')
    if ret:
        exit()


def tkinter2():
    ret = os.system('python C:\RSoft\Current\Main\NewOrders\orders_slip.py')
    if ret:
        exit()


def tkinter3():
    ret = os.system('python C:\RSoft\Current\Main\NewOrders\orders_sandal.py')
    if ret:
        exit()


def tkinter_stock():
    ret = os.system('python C:\RSoft\Current\Main\NewOrders\stock_sheet.py')
    if ret:
        exit()


def tkinter_log():
    ret = os.system('python C:\RSoft\Current\Main\NewOrders\logistics_view.py')
    if ret:
        exit()


def tkinter6():
    ret = os.system('python C:\RSoft\Current\Main\NewOrders\production.py')
    if ret:
        exit()


def tkinter7():
    ret = os.system('python C:\RSoft\Current\Main\NewOrders\production_slip.py')
    if ret:
        exit()


def tkinter8():
    ret = os.system('python C:\RSoft\Current\Main\NewOrders\production_sandal.py')
    if ret:
        exit()


def tkinter9():
    ret = os.system('python C:\RSoft\Current\Main\NewOrders\handlacing.py')
    if ret:
        exit()


def tkinter10():
    ret = os.system('python C:\RSoft\Current\Main\NewOrders\pb_lacing.py')
    if ret:
        exit()


def tkinter11():
    ret = os.system('python C:\RSoft\Current\Main\NewOrders\b_lacing.py')
    if ret:
        exit()


def tkinter12():
    ret = os.system('python C:\RSoft\Current\Main\NewOrders\m_lacing.py')
    if ret:
        exit()


def tkinter_ex1():
    ret = os.system('python C:\RSoft\Current\Main\NewOrders\excel_export_orders.py')
    if ret:
        exit()


def tkinter_ex2():
    ret = os.system('python C:\RSoft\Current\Main\NewOrders\excel_export_prod_1.py')
    if ret:
        exit()


def tkinter_ex3():
    ret = os.system('python C:\RSoft\Current\Main\NewOrders\excel_export_bal.py')
    if ret:
        exit()


def tkinter_ex4():
    ret = os.system('python C:\RSoft\Current\Main\NewOrders\excel_export_stock.py')
    if ret:
        exit()


def tkinter_ex5():
    ret = os.system('python C:\RSoft\Current\Main\NewOrders\excel_export_planning.py')
    if ret:
        exit()


def tkinter_ex6():
    ret = os.system('python C:\RSoft\Current\Main\NewOrders\excel_export_fortnight.py')
    if ret:
        exit()


def tkinter_ex7():
    ret = os.system('python C:\RSoft\Current\Main\NewOrders\excel_export_orderno.py')
    if ret:
        exit()


def tkinter_arch():
    ret = os.system('python C:\RSoft\Current\Main\NewOrders\archive_view_orders.py')
    if ret:
        exit()


# Style of Buttons
style = Style()
style.configure('N.TButton', font=('Arial Narrow', 20, 'bold'), foreground='red', background='skyblue1')

# Images
img = PhotoImage(file=r"C:\RSoft\Current\Buttons\sig.png")
img1 = img.subsample(1, 1)

img = PhotoImage(file=r"C:\RSoft\Current\Buttons\exit.png")
img2 = img.subsample(2, 2)

img = PhotoImage(file=r"C:\RSoft\Current\Buttons\orders_in_house.png")
img3 = img.subsample(2, 2)

img = PhotoImage(file=r"C:\RSoft\Current\Buttons\handlacing.png")
img4 = img.subsample(2, 2)

img = PhotoImage(file=r"C:\RSoft\Current\Buttons\stock_in_house.png")
img5 = img.subsample(2, 2)

img = PhotoImage(file=r"C:\RSoft\Current\Buttons\logistics.png")
img6 = img.subsample(2, 2)

img = PhotoImage(file=r"C:\RSoft\Current\Buttons\production.png")
img8 = img.subsample(2, 2)

img = PhotoImage(file=r"C:\RSoft\Current\Buttons\export.png")
img9 = img.subsample(2, 2)

img = PhotoImage(file=r"C:\RSoft\Current\Buttons\archive.png")
img10 = img.subsample(2, 2)

# Setting image in label
Label(master, image=img1).grid(row=1, column=1, columnspan=4, rowspan=12, padx=30, pady=30, sticky=S + W)

# Menubuttons
# Orders
mb =  Menubutton ( master, image=img3)
mb.menu  =  Menu ( mb, tearoff = 0, activebackground="red", fg="ghost white", bg="chartreuse4", font=["Calibri", 14])
mb["menu"]  =  mb.menu
mb.menu.add_command (label = "School Shoes", command = tkinter1)
mb.menu.add_command (label = "Slipper", command = tkinter2)
mb.menu.add_command (label = "Sandals", command = tkinter3)

# Production
mb2 =  Menubutton (master, image=img8)
mb2.menu  =  Menu ( mb2, tearoff = 0, activebackground="red", fg="ghost white", bg="chartreuse4", font=["Calibri", 14])
mb2["menu"]  =  mb2.menu
mb2.menu.add_command (label = "School Shoes", command = tkinter6)
mb2.menu.add_command (label = "Slipper", command = tkinter7)
mb2.menu.add_command (label = "Sandals", command = tkinter8)

# Handlacing
mb3 =  Menubutton (master, image=img4)
mb3.menu  =  Menu ( mb3, tearoff = 0, activebackground="red", fg="ghost white", bg="chartreuse4", font=["Calibri", 14])
mb3["menu"]  =  mb3.menu
mb3.menu.add_command (label = "Pre-Boys", command = tkinter10)
mb3.menu.add_command (label = "Boys", command = tkinter11)
mb3.menu.add_command (label = "Mens", command = tkinter12)

# Export
mb4 =  Menubutton (master, image=img9)
mb4.menu  =  Menu ( mb4, tearoff = 0, activebackground="red", fg="ghost white", bg="chartreuse4", font=["Calibri", 14])
mb4["menu"]  =  mb4.menu
mb4.menu.add_command (label = "Orders In House", command = tkinter_ex1)
mb4.menu.add_command (label = "Production Tracker", command = tkinter_ex2)
mb4.menu.add_command (label = "Production Scores", command = tkinter_ex3)
mb4.menu.add_command (label = "Inventory List", command = tkinter_ex4)
mb4.menu.add_command (label = "Size Range", command = tkinter_ex5)
mb4.menu.add_command (label = "Fortnightly Scores", command = tkinter_ex6)
mb4.menu.add_command (label = "Production of O/N", command = tkinter_ex7)

b3 = Button(master, image=img5, command=tkinter_stock)
b4 = Button(master, image=img6, command=tkinter_log)
b7 = Button(master, image=img2, command=master.destroy)
b8 = Button(master, image=img10, command=tkinter_arch)

# Arranging Buttons
mb.grid(row=1, column=0, padx=20, pady=5, sticky=W + N)
mb3.grid(row=2, column=0, padx=20, pady=5, sticky=W + N)
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
