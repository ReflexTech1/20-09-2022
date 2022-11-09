from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
from datetime import datetime

root = Tk()
root.geometry('350x450')
root.title("Send Pre-Boys Idler")
root.config(bg="lightgreen")
style = ttk.Style()


OrderNo = StringVar()
Supplier = StringVar()
suppliers = ("MANKOKANA", "RALEHLATHE", "DURBAN")
Size9 = IntVar()
Size10 = IntVar()
Size11 = IntVar()
Size12 = IntVar()
Size13 = IntVar()
Size1 = IntVar()

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y")


def pb_send():
    code = OrderNo.get()
    supplier = Supplier.get()
    size9 = Size9.get()
    size10 = Size10.get()
    size11 = Size11.get()
    size12 = Size12.get()
    size13 = Size13.get()
    size1 = Size1.get()

    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        cursor = conn.cursor()
        cursor.execute(r'INSERT INTO HandlacingPB (DatePB,Order3,SupplierPB,Size9,Size10,Size11,Size12,Size13,Size1,Sent,Received)'
                       r'VALUES(?,?,?,?,?,?,?,?,?,?,?)', [timestampStr, code, supplier, size9, size10, size11, size12, size13, size1, "Sent", ""])
        updated = cursor.rowcount
        conn.commit()
        cursor.close()
        root.destroy()
        sys.exit(updated)


label_0 = Label(root, text="Send Uppers", width=11, relief="sunken",
                background="lightgreen", font=("bold", 20)).place(x=95, y=23)

label_on = Label(root, text="Order No:", width=20,
                 background="lightgreen", font=("bold", 11)).place(x=40, y=90)
entry_on = Entry(root, textvar=OrderNo, background="yellow",
                 font=("bold", 10)).place(x=160, y=90)

label_2 = Label(root, text="Supplier:", width=12,
                background="lightgreen", font=("bold", 11)).place(x=40, y=120)

# Changed from input to Optionmenu
# entry_2 = Entry(root, textvar=Supplier, background="yellow", font=("bold", 10)).place(x=160, y=120)
option_1 = OptionMenu(root, Supplier, *suppliers).place(x=160, y=120)
Supplier.set("RALEHLATHE")

label_pb = Label(root, text="Pre-Boys Idler", width=15,
                 background="lightgreen", font=("bold", 10)).place(x=40, y=160)

label_pb9 = Label(root, text="Size 9:", width=20,
                  background="lightgreen", font=("bold", 11)).place(x=40, y=180)
entry_pb9 = Entry(root, textvar=Size9, background="yellow",
                  font=("bold", 10)).place(x=160, y=180)

label_pb10 = Label(root, text="Size 10:", width=20,
                   background="lightgreen", font=("bold", 11)).place(x=40, y=210)
entry_pb10 = Entry(root, textvar=Size10, background="yellow",
                   font=("bold", 10)).place(x=160, y=210)

label_pb11 = Label(root, text="Size 11:", width=20,
                   background="lightgreen", font=("bold", 11)).place(x=40, y=240)
entry_pb11 = Entry(root, textvar=Size11, background="yellow",
                   font=("bold", 10)).place(x=160, y=240)

label_pb12 = Label(root, text="Size 12:", width=20,
                   background="lightgreen", font=("bold", 11)).place(x=40, y=270)
entry_pb12 = Entry(root, textvar=Size12, background="yellow",
                   font=("bold", 10)).place(x=160, y=270)

label_pb13 = Label(root, text="Size 13:", width=20,
                   background="lightgreen", font=("bold", 11)).place(x=40, y=300)
entry_pb13 = Entry(root, textvar=Size13, background="yellow",
                   font=("bold", 10)).place(x=160, y=300)

label_pb1 = Label(root, text="Size 1:", width=20,
                  background="lightgreen", font=("bold", 11)).place(x=40, y=330)
entry_pb1 = Entry(root, textvar=Size1, background="yellow",
                  font=("bold", 10)).place(x=160, y=330)


style.configure('C.TButton', font=('Arial', 12, 'bold'),
                relief="raised", foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'),
                relief="raised", foreground='blue')

submit1 = Button(root, text='Submit', style='S.TButton',
                 width=11, command=pb_send).place(x=20, y=400)
exit1 = Button(root, text='Close', style='C.TButton', width=11,
               command=root.destroy).place(x=220, y=400)

root.mainloop()