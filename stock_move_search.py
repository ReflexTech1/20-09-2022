from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *

root = Tk()
root.geometry('600x400')
root.title("Search Item")
root.config(bg="antiquewhite2")
style = ttk.Style()

ItemCode = StringVar()
Quantity = StringVar()

with sqlite3.connect('Reflex Footwear.sql3') as conn:
    cursor = conn.cursor()
    my_data = cursor.execute("SELECT ItemCode FROM StockRecord")
    my_list = [r for r, in my_data]
    options = StringVar()
    options.set(my_list[0])


def stock_lookup():
    code = options.get()

    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT DISTINCT ReceiveDate FROM StockRecord WHERE ItemCode=?', (code,))
        results = cursor.fetchall()
        item_0_in_result0 = [_[0] for _ in results]
        Label(root, text="Last Received", width=20, background="antiquewhite2", font=(
            "Arial, bold", 14)).place(x=40, y=210)
        Label(root, text=item_0_in_result0, width=10, background="antiquewhite2", font=(
            "Arial, bold", 14)).place(x=250, y=210)

        cursor.close()
        conn.commit()


label_0 = Label(root, text="Search Last Received", width=18, background="antiquewhite2",
                foreground="grey15", font=("Arial, bold", 20)).place(x=170, y=23)

label_1 = Label(root, text="Item Code", width=20, background="antiquewhite2",
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
