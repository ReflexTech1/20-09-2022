from tkinter import *
import sqlite3
from tkinter.ttk import *
import sys
from datetime import datetime

root = Tk()
root.geometry('400x250')
root.title("Receive Stock")
root.config(bg="tomato")
style = Style()

ItemCode = StringVar()
Description = StringVar()
Quantity = IntVar()
var = IntVar()
c = StringVar()
var1 = IntVar()
var2 = IntVar()

dateTimeObj = datetime.now()

timestampStr = dateTimeObj.strftime("%d-%b-%Y")

with sqlite3.connect('Reflex Footwear.sql3') as conn:
    cursor = conn.cursor()
    my_data = cursor.execute(
        "SELECT Description FROM StockSheet ORDER BY Category ASC")
    my_list = [r for r, in my_data]
    options = StringVar()
    options.set(my_list[0])


def stock_rec():
    code = ItemCode.get()
    quantity = Quantity.get()

    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE StockSheet SET Quantity=Quantity+?, LastRec=? WHERE ItemCode=?',
                       (quantity, timestampStr, code,))
        cursor.execute('INSERT INTO StockRecord (ItemCode,Quantity,ReceiveDate) VALUES(?,?,?)',
                       (code, quantity, timestampStr,))
        updated = cursor.rowcount
        cursor.close()
        conn.commit()
        root.destroy()
        sys.exit(updated)  # return value whether record has been updated


# Inserting labels and field of input
label_0 = Label(root, text="Receive Stock", background="tomato",
                width=20, font=("Arial", 20, "bold")).place(x=90, y=23)

label_1 = Label(root, text="Item Code", width=20, background="tomato", font=(
    "Arial", 12, "bold")).place(x=20, y=100)

#  Changed Normal input to Option Menu
entry_1 = Entry(root, textvar=ItemCode, background="tomato",
                font=("Arial", 12, "bold")).place(x=180, y=100)
# option_1 = OptionMenu(root,options, *my_list).place(x=180, y=100)

label_2 = Label(root, text="Quantity", width=10, background="tomato", font=(
    "Arial", 12, "bold")).place(x=20, y=140)

entry_2 = Entry(root, textvar=Quantity, background="tomato",
                font=("Arial", 12, "bold")).place(x=180, y=140)


# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'), foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'), foreground='blue')

# Inserting buttons
submit1 = Button(root, text='Submit', style='S.TButton',
                 width=11, command=stock_rec).place(x=20, y=190)
exit1 = Button(root, text='Close', style='C.TButton', width=11,
               command=root.destroy).place(x=260, y=190)

root.mainloop()
