from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
from datetime import datetime
from tkinter import messagebox

root = Tk()
root.geometry('610x570')
root.title("New Sandal Order")
root.config(bg="lightskyblue3")
style = ttk.Style()

OrderNo = StringVar()
Size3 = IntVar()
Size4 = IntVar()
Size5 = IntVar()
Size6 = IntVar()
Size7 = IntVar()
Size8 = IntVar()
Quantity = IntVar()
Delivery = StringVar()

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y")

with sqlite3.connect('Reflex Footwear.sql3') as conn:
    cursor = conn.cursor()
    material_data = cursor.execute("SELECT Description FROM StockSheet WHERE Category=?", ("SANDALM",))
    upper_list = [r for r, in material_data]
    upper = StringVar()
    upper.set(upper_list[0])

    sockm_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%EVA%%Insole%'")
    sockm_list = [r for r, in sockm_data]
    sockm = StringVar()
    sockm.set(sockm_list[0])

    binding_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%14mm%%Binding%'")
    binding_list = [r for r, in binding_data]
    binding = StringVar()
    binding.set(binding_list[0])


    soles_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%Rebel%%Size 3/4%'")
    soles_list = [r for r, in soles_data]
    soles = StringVar()
    soles.set(soles_list[0])

    soles1_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%Rebel%%Size 3/4%'")
    soles1_list = [r for r, in soles1_data]
    soles1 = StringVar()
    soles1.set(soles1_list[0])

    soles2_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%Rebel%%Size 5/6%'")
    soles2_list = [r for r, in soles2_data]
    soles2 = StringVar()
    soles2.set(soles2_list[0])

    soles3_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%Rebel%%Size 5/6%'")
    soles3_list = [r for r, in soles3_data]
    soles3 = StringVar()
    soles3.set(soles3_list[0])

    soles4_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%Rebel%%Size 7/8%'")
    soles4_list = [r for r, in soles4_data]
    soles4 = StringVar()
    soles4.set(soles4_list[0])

    soles5_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%Rebel%%Size 7/8%'")
    soles5_list = [r for r, in soles5_data]
    soles5 = StringVar()
    soles5.set(soles5_list[0])


def submit_root(e):
   command=young_boys_sandal()

root.bind('<Return>', lambda e: submit_root(e))


def young_boys_sandal():
    code = OrderNo.get()
    size3 = Size3.get()
    size4 = Size4.get()
    size5 = Size5.get()
    size6 = Size6.get()
    size7 = Size7.get()
    size8 = Size8.get()
    bind = binding.get()
    material = upper.get()
    sock = sockm.get()
    sole = soles.get()
    sole1 = soles1.get()
    sole2 = soles2.get()
    sole3 = soles3.get()
    sole4 = soles4.get()
    sole5 = soles5.get()
    delivery = Delivery.get()
    qty = Quantity.get()

    if qty == sum([size3+size4+size5+size6+size7+size8]):
        with sqlite3.connect('Reflex Footwear.sql3') as conn:
            cursor = conn.cursor()
            # Insert into Orders
            cursor.execute(r'INSERT INTO MySandals (Factory,Planned,OrderNo,Style,DeliveryDate,Quantity,Balances,Binding,Material,Sock,Soles3,Soles4,Soles5,Soles6,Soles7,Soles8) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', [
                           "Reflex", timestampStr, code, "YOUNGER BOYS SANDAL", delivery, qty, qty, bind, material, sock, size3, size4, size5, size6, size7, size8])
            # Insert into Production
            cursor.execute(r'INSERT INTO SandalProduction (Factory,Planned,Order2,Style,DelDate,Orderqty,Cutting,Assembly,Closing,Finishing,Despatch,ToShip) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', [
                           "Reflex", timestampStr, code, "YOUNGER BOYS SANDAL", delivery, qty, qty, "0", "0", "0", "0", qty])
            # Insert Into Planning
            cursor.execute(r'INSERT INTO PlanSandal (Factory,DatePlanned,OrderNo,Style,Pairs,Delivery,Size3,Size4,Size5,Size6,Size7,Size8) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', ["Reflex", timestampStr, code, "YOUNGER BOYS SANDAL", qty, delivery, size3, size4, size5, size6, size7, size8])
            # Insert Into Required
            cursor.execute(r'INSERT INTO SandalRequired (Factory,InputDate,OrderNo,Style,Pairs,DelDate,Upper,Insole,Binding,Gusset,Cartons,Size3,Size4,Size5,Size6,Size7,Size8)'
                           ' VALUES(?,?,?,?,?,?,?*(1),?*(1),?*(1),?*(1),?*(1),?,?,?,?,?,?)', ["Reflex", timestampStr, code, "YOUNGER BOYS SANDAL", qty, delivery, qty, qty, qty, qty, qty, size3, size4, size5, size6, size7, size8])
            # Upper Material - Average of PB and TB
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1), LastRec=? WHERE Description=?', (qty, timestampStr, material))
            # Binding
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1), LastRec=? WHERE Description=?', (qty, timestampStr, bind))
            # Sock Material
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1), LastRec=? WHERE Description=?', (qty, timestampStr, sock))
            # Soles
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size3, timestampStr, sole))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size4, timestampStr, sole1))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size5, timestampStr, sole2))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size6, timestampStr, sole3))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size7, timestampStr, sole4))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size8, timestampStr, sole5))
            # Gusset Elastic
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1), LastRec=? WHERE ItemCode=?', (qty, timestampStr, "ELA0008",))
            # Cartons - Check Cartons packed
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?/30, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "CAR0010",))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?/30, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "CAR0010",))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?/30, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "CAR0010",))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?/48, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "CAR0010",))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?/48, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "CAR0010",))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?/48, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "CAR0010",))
            # 5-inch String Pin
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "PIN0002",))
            # Polybag
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "BAG0003",))
            # Hanger Sticker
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (size3, timestampStr, "STI0074",))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (size4, timestampStr, "STI0076",))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (size5, timestampStr, "STI0078",))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (size6, timestampStr, "STI0080",))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (size7, timestampStr, "STI0082",))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (size8, timestampStr, "STI0084",))
            # Hanger
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "HAN0002",))


            updated = cursor.rowcount
            conn.commit()
            cursor.close()

        with sqlite3.connect('Log Sheets.sql3') as conn2:
            cursor2 = conn2.cursor()
            code = OrderNo.get()
            barcode = OrderNo.get()
            size3 = Size3.get()
            size4 = Size4.get()
            size5 = Size5.get()
            size6 = Size6.get()
            size7 = Size7.get()
            size8 = Size8.get()
            delivery = Delivery.get()
            qty = Quantity.get()
            cursor2.execute('CREATE TABLE IF NOT EXISTS [%s] (Barcode,OrderNo,Style,Delivery,Size3,Size4,Size5,Size6,Size7,Size8,Qty,Ticket)' %code)
            cursor2.execute(r'INSERT INTO [%s] (Barcode,OrderNo,Style,Delivery,Size3,Size4,Size5,Size6,Size7,Size8,Qty,Ticket) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)' %code, [ barcode, code, "YOUNGER BOYS SANDAL", delivery, size3, size4, size5, size6, size7, size8, qty, 158])
            updated = cursor2.rowcount
            conn2.commit()
            cursor2.close()
            root.destroy()
            sys.exit(updated)  # return value whether record has been updated

    else:
        messagebox.showwarning(title="Confirmation", message="The Size Range Does Not Equal The Total.\nPlease Confirm Sizes and Total Again.")

label_0 = Label(root, text="YOUNGER BOYS SANDAL", width=39,  relief='raised', background="lightskyblue3", font=("bold", 20), anchor=CENTER).place(x=10, y=23)

label_on = Label(root, text="Order No:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=180, y=90)
entry_on = Entry(root, textvar=OrderNo, background="", font=("bold", 10)).place(x=300, y=90)

label_2 = Label(root, text="Delivery Date:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=180, y=120)
entry_2 = Entry(root, textvar=Delivery, background="", font=("bold", 10)).place(x=300, y=120)

label_yb1 = Label(root, text="Size 3:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=180)
entry_yb1 = Entry(root, textvar=Size3, background="", font=("bold", 10)).place(x=160, y=180)

label_yb1 = Label(root, text="Size 4:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=210)
entry_yb1 = Entry(root, textvar=Size4, background="", font=("bold", 10)).place(x=160, y=210)

label_yb1 = Label(root, text="Size 5:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=240)
entry_yb1 = Entry(root, textvar=Size5, background="", font=("bold", 10)).place(x=160, y=240)

label_yb2 = Label(root, text="Size 6:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=270)
entry_yb2 = Entry(root, textvar=Size6, background="", font=("bold", 10)).place(x=160, y=270)

label_yb3 = Label(root, text="Size 7:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=300)
entry_yb3 = Entry(root, textvar=Size7, background="", font=("bold", 10)).place(x=160, y=300)

label_yb3 = Label(root, text="Size 8:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=330)
entry_yb3 = Entry(root, textvar=Size8, background="", font=("bold", 10)).place(x=160, y=330)

label_yb4 = Label(root, text="Total Quantity:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=360)
entry_yb4 = Entry(root, textvar=Quantity, background="", font=("bold", 10)).place(x=160, y=360)

label_yb5 = Label(root, text="Binding:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=420)
option_upper = OptionMenu(root, binding, *binding_list).place(x=160, y=420)

label_yb7 = Label(root, text="Upper:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=20, y=450)
option_upper = OptionMenu(root, upper, *upper_list).place(x=160, y=450)

label_yb8 = Label(root, text="Sock:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=20, y=480)
option_upper = OptionMenu(root, sockm, *sockm_list).place(x=160, y=480)

label_yb34 = Label(root, text="Soles:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=320, y=180)
option_soles3 = OptionMenu(root, soles, *soles_list).place(x=370, y=210)
option_soles4 = OptionMenu(root, soles1, *soles1_list).place(x=370, y=180)
option_soles5 = OptionMenu(root, soles2, *soles2_list).place(x=370, y=240)
option_soles6 = OptionMenu(root, soles3, *soles3_list).place(x=370, y=270)
option_soles7 = OptionMenu(root, soles4, *soles4_list).place(x=370, y=300)
option_soles8 = OptionMenu(root, soles5, *soles5_list).place(x=370, y=330)

# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'), relief="raised", foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'), relief="raised", foreground='blue')

# Inserting buttons
submit1 = Button(root, text='Submit', style='S.TButton', width=11, command=young_boys_sandal).place(x=60, y=520)
exit1 = Button(root, text='Close', style='C.TButton', width=11, command=root.destroy).place(x=440, y=520)

root.mainloop()
