from tkinter import *
import sqlite3
from tkinter.ttk import *
import sys
from datetime import datetime

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%m-%d-%Y")

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
        "SELECT OrderNo FROM PlanSandal ORDER BY OrderNo ASC")
    my_list = [r for r, in my_data]
    options = StringVar()
    options.set(my_list[0])

def submit_root(e):
   command=update_despatch_sandal()

root.bind('<Return>', lambda e: submit_root(e))


def update_despatch_sandal():
    code = options.get()
    balance = Balance.get()

    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE SandalProduction SET Despatch=Despatch+? WHERE Order2=?', [balance, code, ])
        cursor.execute('UPDATE SandalProduction SET Finishing=Finishing-? WHERE Order2=?', [balance, code, ])
        cursor.execute('UPDATE SandalProd_Balances SET Despatch=Despatch-? WHERE Order2=?', [balance, code, ])
        cursor.execute('UPDATE SandalProd_Balances SET Finishing=Finishing-? WHERE Order2=?', [balance, code, ])
        cursor.execute(r'INSERT INTO ProductionBreakdown (Factory,Date,Order2,Despatch) VALUES(?,?,?,?)', [
                       "Reflex", timestampStr, code, balance])
        updated = cursor.rowcount
        cursor.close()
        conn.commit()
        root.destroy()
        sys.exit(updated)


# Inserting labels and field of input
label_0 = Label(root, text="Despatch Score", background="lightblue1",
                width=20, font=("Arial", 20, "bold")).place(x=80, y=23)

label_1 = Label(root, text="Order No.", width=20, background="lightblue1", font=(
    "Arial", 12, "bold")).place(x=20, y=100)
option_1 = OptionMenu(root, options, *my_list).place(x=180, y=100)

label_2 = Label(root, text="Quantity Received", width=20,
                background="lightblue1", font=("Arial", 12, "bold")).place(x=20, y=140)
entry_2 = Entry(root, textvar=Balance, background="lightblue1",
                font=("Arial", 12, "bold")).place(x=180, y=140)


# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'), foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'), foreground='blue')

# Inserting buttons
submit1 = Button(root, text='Submit', style='S.TButton',
                 width=11, command=update_despatch_sandal).place(x=20, y=190)
exit1 = Button(root, text='Close', style='C.TButton', width=11,
               command=root.destroy).place(x=260, y=190)


def submit_root(e):
   command=order_b()

root.bind('<Return>', lambda e: submit_root(e))

root.mainloop()