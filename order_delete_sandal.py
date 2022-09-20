from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *

root = Tk()
root.geometry('400x200')
root.title("Delete Order")
root.config(bg="firebrick3")
style = ttk.Style()

OrderNo = StringVar()


def order_delete():
    code = OrderNo.get()

    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM MySandals WHERE OrderNo=?', [code])
        cursor.execute('DELETE FROM SandalProduction WHERE Order2=?', [code])
        cursor.execute('DELETE FROM PlanSandal WHERE OrderNo=?', [code])
        updated = cursor.rowcount
        cursor.close()
        conn.commit()
        root.destroy()
        sys.exit(updated)


label_0 = Label(root, text="Remove Order", width=20, background="firebrick3", font=("Arial, bold", 20)).place(x=110, y=23)

label_1 = Label(root, text="Order No.", width=20, background="firebrick3", font=("Arial, bold", 16)).place(x=20, y=90)
entry_1 = Entry(root, textvar=OrderNo, background="firebrick3", font=("Arial Narrow, bold", 14)).place(x=160, y=90)

# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'), foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'), foreground='blue')

# Inserting buttons
submit1 = Button(root, text='Submit', style='S.TButton',
                 width=11, command=order_delete).place(x=20, y=150)
exit1 = Button(root, text='Close', style='C.TButton', width=11,
               command=root.destroy).place(x=276, y=150)

root.mainloop()
