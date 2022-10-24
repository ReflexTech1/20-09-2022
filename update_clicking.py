from tkinter import *
import sqlite3
from tkinter.ttk import *
import sys
from datetime import datetime

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y")

root = Tk()
root.geometry('380x250')
root.title("Balances")
root.config(bg="lightblue1")
style = Style()

OrderNo = StringVar()
Balance = StringVar()

with sqlite3.connect('Reflex Footwear.sql3') as conn:
    cursor = conn.cursor()
    my_data = cursor.execute(
        "SELECT OrderNo FROM Planning ORDER BY OrderNo ASC")
    my_list = [r for r, in my_data]
    options = StringVar()
    options.set(my_list[0])


def submit_root(e):
   command=update_clicking()

root.bind('<Return>', lambda e: submit_root(e))


def update_clicking():
    code = options.get()
    balance = Balance.get()

    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE Production SET Clicking=Clicking-? WHERE Order2=?', [balance, code, ])
        cursor.execute('UPDATE Production SET Closing=Closing+? WHERE Order2=?', [balance, code, ])
        cursor.execute('UPDATE Production_Balances SET Clicking=Clicking-? WHERE Order2=?', [balance, code, ])
        cursor.execute(r'INSERT INTO ProductionBreakdown (Factory,Date,Order2,Clicking) VALUES(?,?,?,?)', [
                       "Reflex", timestampStr, code, balance])
        updated = cursor.rowcount
        cursor.close()
        conn.commit()
        root.destroy()
        sys.exit(updated)


# Inserting labels and field of input
label_0 = Label(root, text="Clicking Score", background="lightblue1",
                width=20, font=("Arial", 20, "bold")).place(x=80, y=23)

label_1 = Label(root, text="Order No.", width=20, background="lightblue1", font=(
    "Arial", 12, "bold")).place(x=20, y=100)
option_1 = OptionMenu(root, options, *my_list).place(x=180, y=100)

label_2 = Label(root, text="Quantity Clicked", width=20,
                background="lightblue1", font=("Arial", 12, "bold")).place(x=20, y=140)
entry_2 = Entry(root, textvar=Balance, background="lightblue1",
                font=("Arial", 12, "bold")).place(x=180, y=140)


# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'), foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'), foreground='blue')

# Inserting buttons
submit1 = Button(root, text='Submit', style='S.TButton',
                 width=11, command=update_clicking).place(x=20, y=190)
exit1 = Button(root, text='Close', style='C.TButton', width=11,
               command=root.destroy).place(x=260, y=190)

root.mainloop()
