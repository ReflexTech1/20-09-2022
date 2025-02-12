from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
from datetime import datetime

root = Tk()
root.geometry('350x450')
root.title("Receive Mens Idler")
root.config(bg="tomato")
style = ttk.Style()

OrderNo = StringVar()
Supplier = StringVar()
suppliers = ("RALEHLATHE", "RALEHLATHE", "MANKOKANA", "DURBAN")
Size6 = IntVar()
Size7 = IntVar()
Size8 = IntVar()
Size9 = IntVar()
Size10 = IntVar()

with sqlite3.connect('Reflex Footwear.sql3') as conn:
    cursor = conn.cursor()
    orderno_data = cursor.execute("SELECT Order3 FROM HandlacingM")
    orderno_list = [r for r, in orderno_data]
    orderno = StringVar()
    orderno.set(orderno_list[0])

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y")

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y")


def m_receive():
    code = OrderNo.get()
    supplier = Supplier.get()
    size6 = Size6.get()
    size7 = Size7.get()
    size8 = Size8.get()
    size9 = Size9.get()
    size10 = Size10.get()

    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        cursor = conn.cursor()
        cursor.execute(r'INSERT INTO HandlacingM (DateM,Order3,SupplierM,Size6,Size7,Size8,Size9,Size10,Sent,Received) '
                       r'VALUES(?,?,?,-?,-?,-?,-?,-?,?,?)', [timestampStr, code, supplier, size6, size7, size8, size9, size10, "", "Received"])
        updated = cursor.rowcount
        conn.commit()
        cursor.close()
        root.destroy()
        sys.exit(updated)  # return value whether record has been updated


label_0 = Label(root, text="Receive Uppers", width=13, relief="sunken",
                background="tomato", font=("bold", 20)).place(x=80, y=23)

label_on = Label(root, text="Order No:", width=20, background="tomato", font=("bold", 11)).place(x=40, y=90)
orderno_option = OptionMenu(root, OrderNo, *orderno_list).place(x=160, y=90)
#entry_on = Entry(root, textvar=OrderNo, background="yellow", font=("bold", 10)).place(x=160, y=90)

label_2 = Label(root, text="Supplier:", width=20,
                background="tomato", font=("bold", 11)).place(x=40, y=120)

# Changed from input to Optionmenu
# entry_2 = Entry(root, textvar=Supplier, background="yellow", font=("bold", 10)).place(x=160, y=120)
option_1 = OptionMenu(root, Supplier, *suppliers).place(x=160, y=120)
Supplier.set("RALEHLATHE")

label_m = Label(root, text="Mens Idler", width=30,
                background="tomato", font=("bold", 10)).place(x=40, y=160)

label_m6 = Label(root, text="Size 6:", width=20,
                 background="tomato", font=("bold", 11)).place(x=40, y=180)
entry_m6 = Entry(root, textvar=Size6, background="yellow",
                 font=("bold", 10)).place(x=160, y=180)

label_m7 = Label(root, text="Size 7:", width=20,
                 background="tomato", font=("bold", 11)).place(x=40, y=210)
entry_m7 = Entry(root, textvar=Size7, background="yellow",
                 font=("bold", 10)).place(x=160, y=210)

label_m8 = Label(root, text="Size 8:", width=20,
                 background="tomato", font=("bold", 11)).place(x=40, y=240)
entry_m8 = Entry(root, textvar=Size8, background="yellow",
                 font=("bold", 10)).place(x=160, y=240)

label_m9 = Label(root, text="Size 9:", width=20,
                 background="tomato", font=("bold", 11)).place(x=40, y=270)
entry_m9 = Entry(root, textvar=Size9, background="yellow",
                 font=("bold", 10)).place(x=160, y=270)

label_m10 = Label(root, text="Size 10:", width=20,
                  background="tomato", font=("bold", 11)).place(x=40, y=300)
entry_m10 = Entry(root, textvar=Size10, background="yellow",
                  font=("bold", 10)).place(x=160, y=300)

# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'),
                relief="raised", foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'),
                relief="raised", foreground='blue')

# Inserting buttons
submit1 = Button(root, text='Submit', style='S.TButton',
                 width=11, command=m_receive).place(x=20, y=400)
exit1 = Button(root, text='Close', style='C.TButton', width=11,
               command=root.destroy).place(x=220, y=400)

root.mainloop()
