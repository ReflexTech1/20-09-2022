from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *

root = Tk()
root.geometry('600x400')
root.title("Search Item Balance")
root.config(bg="lightgreen")
style = ttk.Style()

ItemCode = StringVar()
Quantity = StringVar()

with sqlite3.connect('Reflex Footwear.sql3') as conn:
    cursor = conn.cursor()
    my_data = cursor.execute(
        "SELECT Description FROM StockSheet ORDER BY Category ASC")
    my_list = [r for r, in my_data]
    options = StringVar()
    options.set(my_list[0])


def stock_lookup():
    code = options.get()

    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT ItemCode,Description,Quantity,Unit FROM StockSheet WHERE Description=?', (code,))
        results = cursor.fetchall()
        item_0_in_result1 = [_[1] for _ in results]
        item_0_in_result2 = [_[2] for _ in results]
        item_0_in_result3 = [_[3] for _ in results]
        Label(root, text="Description:", width=20, background="lightgreen",
              font=("Arial, bold", 14)).place(x=40, y=160)
        Label(root, text=item_0_in_result1, width=40, background="lightgreen", font=(
            "Arial, bold", 14)).place(x=250, y=160)
        Label(root, text="Unit:", width=20, background="lightgreen",
              font=("Arial, bold", 14)).place(x=40, y=210)
        Label(root, text=item_0_in_result3, width=20, background="lightgreen", font=(
            "Arial, bold", 14)).place(x=250, y=210)
        Label(root, text="Quantity:", width=20, background="lightgreen",
              font=("Arial, bold", 14)).place(x=40, y=260)
        Label(root, text=item_0_in_result2, width=20, background="lightgreen", font=(
            "Arial, bold", 14)).place(x=250, y=260)
        cursor.close()
        conn.commit()


label_0 = Label(root, text="Search Item", width=12, background="lightgreen",
                foreground="grey15", font=("Arial, bold", 20)).place(x=235, y=23)

label_1 = Label(root, text="Item Code", width=20, background="lightgreen",
                foreground="grey15", font=("Arial, bold", 16)).place(x=120, y=90)

# Changed Normal input to Option Menu
# entry_1 = Entry(root, textvar=ItemCode, background="lightgreen", font=("Arial Narrow, bold", 14)).place(x=250, y=90)
option_1 = OptionMenu(root, options, *my_list).place(x=250, y=90)

# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'), foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'), foreground='blue')

# Inserting buttons
submit1 = Button(root, text='Search', style='S.TButton',
                 width=11, command=stock_lookup).place(x=20, y=350)
exit1 = Button(root, text='Close', style='C.TButton', width=11,
               command=root.destroy).place(x=470, y=350)

root.mainloop()
