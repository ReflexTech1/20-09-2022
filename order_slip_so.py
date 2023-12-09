from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
from datetime import datetime

root = Tk()
root.geometry('610x500')
root.title("New NSME Order")
root.config(bg="lightskyblue3")
style = ttk.Style()

OrderNo = StringVar()
Size6 = IntVar()
Size7 = IntVar()
Size8 = IntVar()
Size9 = IntVar()
Size10 = IntVar()
Size11 = IntVar()
Quantity = IntVar()
Delivery = StringVar()

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y")

with sqlite3.connect('Reflex Footwear.sql3') as conn:
    cursor = conn.cursor()
    soles1_data = cursor.execute(r"SELECT Description FROM StockSheet WHERE Description LIKE '%NSME%%Size 6%'")
    soles1_list = [r for r, in soles1_data]
    soles1 = StringVar()
    soles1.set(soles1_list[0])

    soles2_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%NSME%%Size 7%'")
    soles2_list = [r for r, in soles2_data]
    soles2 = StringVar()
    soles2.set(soles2_list[0])

    soles3_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%NSME%%Size 8%'")
    soles3_list = [r for r, in soles3_data]
    soles3 = StringVar()
    soles3.set(soles3_list[0])

    soles4_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%NSME%%Size 8%'")
    soles4_list = [r for r, in soles4_data]
    soles4 = StringVar()
    soles4.set(soles4_list[0])

    soles5_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%NSME%%Size 8%'")
    soles5_list = [r for r, in soles5_data]
    soles5 = StringVar()
    soles5.set(soles5_list[0])

    soles6_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%NSME%%Size 8%'")
    soles6_list = [r for r, in soles6_data]
    soles6 = StringVar()
    soles6.set(soles6_list[0])



def submit_root(e):
   command=so_slipper()

root.bind('<Return>', lambda e: submit_root(e))


def so_slipper():
    code = OrderNo.get()
    size6 = Size6.get()
    size7 = Size7.get()
    size8 = Size8.get()
    size9 = Size9.get()
    size10 = Size10.get()
    size11 = Size11.get()
    sole1 = soles1.get()
    sole2 = soles2.get()
    sole3 = soles3.get()
    sole4 = soles4.get()
    sole5 = soles5.get()
    sole6 = soles6.get()
    delivery = Delivery.get()
    qty = Quantity.get()

    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        cursor = conn.cursor()
        # Insert into Orders
        cursor.execute(r'INSERT INTO MySlippers (Factory,Planned,OrderNo,Style,DeliveryDate,Quantity,Balances,Soles6,Soles7,Soles8,Soles9,Soles10,Soles11) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)', [
                       "Reflex", timestampStr, code, "MENS SLIPPER", delivery, qty, qty, sock, size6, size7, size8, size9, size10, size11])
        # Insert into Production
        cursor.execute(r'INSERT INTO SlipProduction (Factory,Planned,Order2,Style,DelDate,Orderqty,Cutting,Assembly,Closing,Finishing,Despatch,ToShip) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', [
                       "Reflex", timestampStr, code, "MENS SLIPPER", delivery, qty, qty, "0", "0", "0", "0", qty])
        # Insert Into Planning
        cursor.execute(r'INSERT INTO PlanSlip (Factory,DatePlanned,OrderNo,Style,Pairs,Delivery,Size6,Size7,Size8,Size9,Size10,Size11) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', ["Reflex", timestampStr, code, "MENS SLIPPER", qty, delivery, size6, size7, size8, size9, size10, size11])
        # Insert Into Required
        cursor.execute(r'INSERT INTO SlipRequired (Factory,InputDate,OrderNo,Style,Pairs,DelDate,Upper,Sock,Ribbon,Elastic,Binding,Gusset,Cartons,NSize6,NSize7,NSize8,NSize9,NSize10,NSize11)'
                       ' VALUES(?,?,?,?,?,?,?*(1.4/13.8),?*(1.4/20.4),?*(0.087),?*(1.08),?*(1.5),?*(0.16),?/12,?,?,?,?,?,?)',
                       ["Reflex", timestampStr, code, "MENS SLIPPER", qty, delivery, qty, qty, qty, qty, qty, qty, qty, size6, size7, size8, size9, size10, size11])
        # 3mm Ribbon
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(0.087), LastRec=? WHERE ItemCode=?', (qty, timestampStr, "RIB0001",))
        # Soles
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size6, timestampStr, sole1))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size7, timestampStr, sole2))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size8, timestampStr, sole3))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size9, timestampStr, sole3))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size10, timestampStr, sole3))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size11, timestampStr, sole3))
        # Gusset Elastic
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(0.16), LastRec=? WHERE ItemCode=?', (qty, timestampStr, "ELA0008",))
        # Cartons
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?/12, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "CAR0010",))
        # Made In Lesotho Label
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "LAB0002",))
        # 25mm Tag Pin
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "PIN0001",))
        # Polybag
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "BAG0003",))
        # Hanger Sticker - TO CHECK CODES
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (size6, timestampStr, "STI0077",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (size7, timestampStr, "STI0079",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (size8, timestampStr, "STI0081",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (size9, timestampStr, "STI0081",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (size10, timestampStr, "STI0081",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (size11, timestampStr, "STI0081",))
        # Hanger
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "HAN0001",))


        updated = cursor.rowcount
        conn.commit()
        cursor.close()
        root.destroy()
        sys.exit(updated)  # return value whether record has been updated


label_0 = Label(root, text="NSME Slip-On Slipper", width=39,  relief='raised', background="lightskyblue3", font=("bold", 20), anchor=CENTER).place(x=10, y=23)

label_on = Label(root, text="Order No:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=180, y=90)
entry_on = Entry(root, textvar=OrderNo, background="", font=("bold", 10)).place(x=300, y=90)

label_2 = Label(root, text="Delivery Date:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=180, y=120)
entry_2 = Entry(root, textvar=Delivery, background="", font=("bold", 10)).place(x=300, y=120)

label_m1 = Label(root, text="Size 6:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=180)
entry_m1 = Entry(root, textvar=Size6, background="", font=("bold", 10)).place(x=140, y=180)

label_m2 = Label(root, text="Size 7:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=210)
entry_m2 = Entry(root, textvar=Size7, background="", font=("bold", 10)).place(x=140, y=210)

label_m3 = Label(root, text="Size 8:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=240)
entry_m3 = Entry(root, textvar=Size8, background="", font=("bold", 10)).place(x=140, y=240)

label_m3 = Label(root, text="Size 9:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=270)
entry_m3 = Entry(root, textvar=Size9, background="", font=("bold", 10)).place(x=140, y=270)

label_m3 = Label(root, text="Size 10:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=300)
entry_m3 = Entry(root, textvar=Size10, background="", font=("bold", 10)).place(x=140, y=300)

label_m3 = Label(root, text="Size 11:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=330)
entry_m3 = Entry(root, textvar=Size11, background="", font=("bold", 10)).place(x=140, y=330)

label_m4 = Label(root, text="Total Quantity:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=370)
entry_m4 = Entry(root, textvar=Quantity, background="", font=("bold", 10)).place(x=140, y=370)

label_m9 = Label(root, text="Soles:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=300, y=180)
option_soles = OptionMenu(root, soles1, *soles1_list).place(x=370, y=180)

# label_m10 = Label(root, text="Soles:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=40, y=450)
option_soles2 = OptionMenu(root, soles2, *soles2_list).place(x=370, y=210)

# label_m10 = Label(root, text="Soles:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=40, y=480)
option_soles23= OptionMenu(root, soles3, *soles3_list).place(x=370, y=240)

# label_m10 = Label(root, text="Soles:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=40, y=480)
option_soles23= OptionMenu(root, soles4, *soles3_list).place(x=370, y=270)

# label_m10 = Label(root, text="Soles:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=40, y=480)
option_soles23= OptionMenu(root, soles5, *soles3_list).place(x=370, y=300)

# label_m10 = Label(root, text="Soles:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=40, y=480)
option_soles23= OptionMenu(root, soles6, *soles3_list).place(x=370, y=330)

# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'), relief="raised", foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'), relief="raised", foreground='blue')

# Inserting buttons
submit1 = Button(root, text='Submit', style='S.TButton', width=11, command=so_slipper).place(x=60, y=450)
exit1 = Button(root, text='Close', style='C.TButton', width=11, command=root.destroy).place(x=450, y=450)

root.mainloop()
