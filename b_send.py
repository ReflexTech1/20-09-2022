from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
from datetime import datetime

root = Tk()
root.geometry('350x450')
root.title("Send Boys Idler")
root.config(bg="lightgreen")
style = ttk.Style()

# List of Variables used
OrderNo = StringVar()
Supplier = StringVar()
suppliers = ("MANKOKANA", "RALEHLATHE", "DURBAN")
Size2 = IntVar()
Size3 = IntVar()
Size4 = IntVar()
Size5 = IntVar()

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y")


def b_send():
    code = OrderNo.get()
    supplier = Supplier.get()
    size2 = Size2.get()
    size3 = Size3.get()
    size4 = Size4.get()
    size5 = Size5.get()

    with sqlite3.connect('Test.sql3') as conn:
        cursor = conn.cursor()
        cursor.execute(r'INSERT INTO HandlacingB (DateB,Order3,SupplierB,Size2,Size3,Size4,Size5,Sent,Received)'
                       r'VALUES(?,?,?,?,?,?,?,?,?)', [timestampStr, code, supplier, size2, size3, size4, size5, "Sent", ""])
        updated = cursor.rowcount
        conn.commit()
        cursor.close()
        root.destroy()
        sys.exit(updated)  # return value whether record has been updated


label_0 = Label(root, text="Send Uppers", width=11, relief="sunken",
                background="lightgreen", font=("bold", 20)).place(x=95, y=23)

label_on = Label(root, text="Order No:", width=20,
                 background="lightgreen", font=("bold", 11)).place(x=40, y=90)
entry_on = Entry(root, textvar=OrderNo, background="yellow",
                 font=("bold", 10)).place(x=160, y=90)

label_2 = Label(root, text="Supplier:", width=12,
                background="lightgreen", font=("bold", 11)).place(x=40, y=120)
option_1 = OptionMenu(root, Supplier, *suppliers).place(x=160, y=120)
Supplier.set("RALEHLATHE")

label_b = Label(root, text="Boys Idler", width=30,
                background="lightgreen", font=("bold", 10)).place(x=40, y=160)

label_b2 = Label(root, text="Size 2:", width=20,
                 background="lightgreen", font=("bold", 11)).place(x=40, y=180)
entry_b2 = Entry(root, textvar=Size2, background="yellow",
                 font=("bold", 10)).place(x=160, y=180)

label_b3 = Label(root, text="Size 3:", width=20,
                 background="lightgreen", font=("bold", 11)).place(x=40, y=210)
entry_b3 = Entry(root, textvar=Size3, background="yellow",
                 font=("bold", 10)).place(x=160, y=210)

label_b4 = Label(root, text="Size 4:", width=20,
                 background="lightgreen", font=("bold", 11)).place(x=40, y=240)
entry_b4 = Entry(root, textvar=Size4, background="yellow",
                 font=("bold", 10)).place(x=160, y=240)

label_b5 = Label(root, text="Size 5:", width=20,
                 background="lightgreen", font=("bold", 11)).place(x=40, y=270)
entry_b5 = Entry(root, textvar=Size5, background="yellow",
                 font=("bold", 10)).place(x=160, y=270)

# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'),
                relief="raised", foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'),
                relief="raised", foreground='blue')

# Inserting buttons
submit1 = Button(root, text='Submit', style='S.TButton',
                 width=11, command=b_send).place(x=20, y=400)
exit1 = Button(root, text='Close', style='C.TButton', width=11,
               command=root.destroy).place(x=220, y=400)

root.mainloop()
