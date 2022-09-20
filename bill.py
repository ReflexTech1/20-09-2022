from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
import os

root = Tk()
root.geometry('600x680')
root.title("Search Item")
root.config(bg="lightgreen")
style = ttk.Style()

Style = StringVar()
Quantity = StringVar()

with sqlite3.connect('Reflex Footwear.sql3') as conn:
    cursor = conn.cursor()
    my_data = cursor.execute("SELECT Type FROM Bill2")
    my_list = [r for r, in my_data]
    options = StringVar()
    options.set(my_list[0])


def bill():
    style1 = options.get()
    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT Type,Upper,Stiffener,Insole,Sock,Laces,Foil,PBA887,GussetElastic,IA80 FROM Bill2 WHERE Type=?', (style1,))
        results = cursor.fetchall()

        item_0_in_result1 = [_[1] for _ in results]
        item_0_in_result2 = [_[2] for _ in results]
        item_0_in_result3 = [_[3] for _ in results]
        item_0_in_result4 = [_[4] for _ in results]
        item_0_in_result5 = [_[5] for _ in results]
        item_0_in_result6 = [_[6] for _ in results]
        item_0_in_result7 = [_[7] for _ in results]
        item_0_in_result8 = [_[8] for _ in results]
        item_0_in_result9 = [_[9] for _ in results]

        Label(root, text="Upper Material:", width=20, background="lightgreen", font=(
            "Arial, bold", 14)).place(x=40, y=160)
        Label(root, text=item_0_in_result1, width=40, background="lightgreen", font=(
            "Arial, bold", 14)).place(x=250, y=160)

        Label(root, text="Stiffener:", width=20, background="lightgreen",
              font=("Arial, bold", 14)).place(x=40, y=210)
        Label(root, text=item_0_in_result2, width=20, background="lightgreen", font=(
            "Arial, bold", 14)).place(x=250, y=210)

        Label(root, text="Insole:", width=20, background="lightgreen",
              font=("Arial, bold", 14)).place(x=40, y=260)
        Label(root, text=item_0_in_result3, width=20, background="lightgreen", font=(
            "Arial, bold", 14)).place(x=250, y=260)

        Label(root, text="PU Lining:", width=20, background="lightgreen",
              font=("Arial, bold", 14)).place(x=40, y=310)
        Label(root, text=item_0_in_result4, width=20, background="lightgreen", font=(
            "Arial, bold", 14)).place(x=250, y=310)

        Label(root, text="Laces:", width=20, background="lightgreen",
              font=("Arial, bold", 14)).place(x=40, y=360)
        Label(root, text=item_0_in_result5, width=20, background="lightgreen", font=(
            "Arial, bold", 14)).place(x=250, y=360)

        Label(root, text="Foil:", width=20, background="lightgreen",
              font=("Arial, bold", 14)).place(x=40, y=410)
        Label(root, text=item_0_in_result6, width=20, background="lightgreen", font=(
            "Arial, bold", 14)).place(x=250, y=410)

        Label(root, text="PBA 887:", width=20, background="lightgreen",
              font=("Arial, bold", 14)).place(x=40, y=460)
        Label(root, text=item_0_in_result7, width=20, background="lightgreen", font=(
            "Arial, bold", 14)).place(x=250, y=460)

        Label(root, text="Gusset Elastic:", width=20, background="lightgreen", font=(
            "Arial, bold", 14)).place(x=40, y=510)
        Label(root, text=item_0_in_result8, width=20, background="lightgreen", font=(
            "Arial, bold", 14)).place(x=250, y=510)

        Label(root, text="IA 80 Solution:", width=20, background="lightgreen", font=(
            "Arial, bold", 14)).place(x=40, y=560)
        Label(root, text=item_0_in_result9, width=20, background="lightgreen", font=(
            "Arial, bold", 14)).place(x=250, y=560)

        cursor.close()
        conn.commit()


def tkinter():
    ret = os.system('python calculations.py')
    if ret:
        bill()


def tkinter1():
    ret = os.system('python bill_cal.py')
    if ret:
        bill()


label_0 = Label(root, text="Search Costing", width=14, background="lightgreen",
                foreground="grey15", font=("Arial, bold", 20)).place(x=230, y=23)

label_1 = Label(root, text="Style", width=20, background="lightgreen",
                foreground="grey15", font=("Arial, bold", 16)).place(x=120, y=90)

# Changed Normal input to Option Menu
# entry_1 = Entry(root, textvar=Style, background="lightgreen", font=("Arial Narrow, bold", 14)).place(x=250, y=90)
option_1 = OptionMenu(root, options, *my_list).place(x=250, y=90)

# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'), foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'), foreground='blue')

# Inserting buttons
submit1 = Button(root, text='Search', style='S.TButton',
                 width=11, command=bill).place(x=20, y=610)
calculations = Button(root, text='Calculations', style='S.TButton',
                      width=11, command=tkinter).place(x=140, y=610)
costing = Button(root, text='Requirements/Order', style='S.TButton',
                 width=20, command=tkinter1).place(x=260, y=610)
exit1 = Button(root, text='Close', style='C.TButton', width=11,
               command=root.destroy).place(x=470, y=610)

root.mainloop()
