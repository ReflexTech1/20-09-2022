from tkinter import *
import sqlite3
from tkinter.ttk import *
import sys
from datetime import datetime

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%m-%d-%Y")

root = Tk()
root.geometry('390x380')
root.title("Shipping")
root.config(bg="lightblue1")
style = Style()

#OrderNo = StringVar()
Balance = StringVar()
Line = StringVar()
Reason = StringVar()

with sqlite3.connect('Reflex Footwear.sql3') as conn:
    cursor = conn.cursor()
    my_data = cursor.execute(
        "SELECT Order2 FROM Production ORDER BY Order2 ASC")
    my_list = [r for r, in my_data]
    options = StringVar()
    options.set(my_list[0])

with sqlite3.connect('Reflex Footwear.sql3') as conn:
    cursor = conn.cursor()
    my_data2 = cursor.execute(
        "SELECT DISTINCT Style FROM Planning")
    my_list2 = [r for r, in my_data2]
    options2 = StringVar()
    options2.set(my_list2[0])


def submit_root(e):
   command=update_shipped()

root.bind('<Return>', lambda e: submit_root(e))


def update_shipped():
    code = options.get()
    balance = Balance.get()
    line = Line.get()
    reason = Reason.get()
    desc = options2.get()
    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE Production SET ToShip=ToShip-? WHERE Order2=?', [balance, code, ])
        cursor.execute('UPDATE Production SET Shipped=Shipped+? WHERE Order2=?', [balance, code, ])
        cursor.execute('UPDATE Production_Balances SET ToShip=ToShip-? WHERE Order2=?', [balance, code, ])
        cursor.execute('UPDATE Production_Balances SET Shipped=Shipped+? WHERE Order2=?', [balance, code, ])
        cursor.execute('UPDATE Production SET Warehouse=Warehouse-? WHERE Order2=?', [balance, code, ])
        cursor.execute('INSERT INTO ProductionBreakdown (Factory,Date,Line,Order2,Style,Shipped,Reason) VALUES(?,?,?,?,?,?,?)', ["Reflex", timestampStr, line, code, desc, balance, reason])
        updated = cursor.rowcount
        cursor.close()
        conn.commit()
        root.destroy()
        sys.exit(updated)


# Inserting labels and field of input
label_0 = Label(root, text="Shipped", background="lightblue1", width=20, font=("Arial", 20, "bold")).place(x=130, y=23)

#OrderNo
label_1 = Label(root, text="Order No.", width=20, background="lightblue1", font=("Arial", 12, "bold")).place(x=20, y=100)
option_1 = OptionMenu(root, options, *my_list).place(x=180, y=100)

#Description
label_1 = Label(root, text="Style", width=20, background="lightblue1", font=("Arial", 12, "bold")).place(x=20, y=140)
option_1 = OptionMenu(root, options2, *my_list2).place(x=180, y=140)

#line
label_2 = Label(root, text="Truck Reg.", width=20, background="lightblue1", font=("Arial", 12, "bold")).place(x=20, y=180)
option_2 = Entry(root, textvar=Line, background="lightblue1", font=("Arial", 12, "bold")).place(x=180, y=180)

#Quantity
label_3 = Label(root, text="Score Quantity", width=20, background="lightblue1", font=("Arial", 12, "bold")).place(x=20, y=220)
entry_3 = Entry(root, textvar=Balance, background="lightblue1", font=("Arial", 12, "bold")).place(x=180, y=220)

#Reason
label_4 = Label(root, text="Reason", width=20, background="lightblue1", font=("Arial", 12, "bold")).place(x=20, y=260)
entry_4 = Entry(root, textvar=Reason, background="lightblue1", font=("Arial", 12, "bold")).place(x=180, y=260)

# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'), foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'), foreground='blue')

# Inserting buttons
submit1 = Button(root, text='Submit', style='S.TButton',
                 width=11, command=update_shipped).place(x=20, y=320)
exit1 = Button(root, text='Close', style='C.TButton', width=11,
               command=root.destroy).place(x=260, y=320)

root.mainloop()
