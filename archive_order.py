from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *

root = Tk()
root.geometry('400x200')
root.title("Order Archive")
root.config(bg="tomato")
style = ttk.Style()

OrderNo = StringVar()


def delete_order():
    code = OrderNo.get()

    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO MyShoe_Archive SELECT * FROM MyShoe WHERE OrderNo=?', [code])
        cursor.execute('DELETE FROM MyShoe WHERE OrderNo=?', [code])
        cursor.execute('INSERT INTO Production_Archive SELECT * FROM Production WHERE Order2=?', [code])
        cursor.execute('DELETE FROM Production WHERE Order2=?', [code])
        cursor.execute('INSERT INTO Planning_Archive SELECT * FROM Planning WHERE OrderNo=?', [code])
        cursor.execute('DELETE FROM Planning WHERE OrderNo=?', [code])
        cursor.execute('INSERT INTO ProdBreak_Archive SELECT * FROM ProductionBreakdown WHERE Order2=?', [code])
        cursor.execute('DELETE FROM ProductionBreakdown WHERE Order2=?', [code])
        updated = cursor.rowcount
        cursor.close()
        conn.commit()
        root.destroy()
        sys.exit(updated)  # return value whether record has been updated


label_0 = Label(root, text="Archive Order", width=20, background="tomato", font=("Arial, bold", 20)).place(x=110, y=23)

label_1 = Label(root, text="Order No.", width=20, background="tomato", font=("Arial, bold", 16)).place(x=20, y=90)
entry_1 = Entry(root, textvar=OrderNo, background="tomato", font=("Arial Narrow, bold", 14)).place(x=160, y=90)


# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'), foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'), foreground='blue')

# Inserting buttons
submit1 = Button(root, text='Submit', style='S.TButton', width=11, command=delete_order).place(x=20, y=150)
exit1 = Button(root, text='Close', style='C.TButton', width=11, command=root.destroy).place(x=276, y=150)

root.mainloop()
