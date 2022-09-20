from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *

root = Tk()
root.geometry('430x400')
root.title("Search Item")
root.config(bg="skyblue2")
style = ttk.Style()

OrderNo = StringVar()

with sqlite3.connect('Reflex Footwear.sql3') as conn:
    cursor = conn.cursor()
    my_data = cursor.execute(
        "SELECT OrderNo FROM MyShoe_Archive")
    my_list = [r for r, in my_data]
    options = StringVar()
    options.set(my_list[0])


def order_search():
    order = options.get()

    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT Style,DeliveryDate,Quantity,Balances FROM MyShoe_Archive WHERE OrderNo=?', (order,))
        results = cursor.fetchall()

        item_0_in_result = [_[0] for _ in results]
        item_0_in_result1 = [_[1] for _ in results]
        item_0_in_result2 = [_[2] for _ in results]

        Label(root, text="Style/Description:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=150)
        Label(root, text=item_0_in_result, width=60, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=150)

        Label(root, text="Delivery Date:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=200)
        Label(root, text=item_0_in_result1, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=200)

        Label(root, text="Quantity of Order:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=250)
        Label(root, text=item_0_in_result2, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=250)

        cursor.close()
        conn.commit()


label_0 = Label(root, text="Search Order", width=12, background="skyblue2",
                foreground="grey15", font=("Arial, bold", 20)).place(x=135, y=23)

label_1 = Label(root, text="Order No.", width=20, background="skyblue2",
                foreground="grey15", font=("Arial, bold", 16)).place(x=20, y=90)
# Changed Normal input to Option Menu
# entry_1 = Entry(root, textvar=OrderNo, background="skyblue2", width=19, font=("Arial Narrow, bold", 14)).place(x=180, y=90)
option_1 = OptionMenu(root, options, *my_list).place(x=180, y=90)

# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'), foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'), foreground='blue')

# Inserting buttons
submit1 = Button(root, text='Search', style='S.TButton',
                 width=11, command=order_search).place(x=20, y=350)
exit1 = Button(root, text='Close', style='C.TButton', width=11,
               command=root.destroy).place(x=290, y=350)

root.mainloop()
