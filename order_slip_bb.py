from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
from datetime import datetime

root = Tk()
root.geometry('660x480')
root.title("New ML Slipper Order")
root.config(bg="lightskyblue3")
style = ttk.Style()

OrderNo = StringVar()
Size12 = IntVar()
Size34 = IntVar()
Quantity = IntVar()
Delivery = StringVar()

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y")

with sqlite3.connect('Reflex Footwear.sql3') as conn:
    cursor = conn.cursor()
    material_data = cursor.execute(
        "SELECT Description FROM StockSheet WHERE Category=?", ("STOKIEM",))
    upper_list = [r for r, in material_data]
    upper = StringVar()
    upper.set(upper_list[0])

    sockm_data = cursor.execute(
        "SELECT Description FROM StockSheet WHERE Category=?", ("STOKIEM",))
    sockm_list = [r for r, in sockm_data]
    sockm = StringVar()
    sockm.set(sockm_list[0])

    binding_data = cursor.execute(
        "SELECT Description FROM StockSheet WHERE  Description LIKE '%16mm%%Binding%'")
    binding_list = [r for r, in binding_data]
    binding = StringVar()
    binding.set(binding_list[0])

    elastic_data = cursor.execute(
        "SELECT Description FROM StockSheet WHERE Category=?", ("ELASTIC",))
    elastic_list = [r for r, in elastic_data]
    elastic = StringVar()
    elastic.set(elastic_list[0])

    soles1_data = cursor.execute(
        "SELECT Description FROM StockSheet WHERE  Description LIKE '%PEP% %Size 1/2%'")
    soles1_list = [r for r, in soles1_data]
    soles1 = StringVar()
    soles1.set(soles1_list[0])

    soles2_data = cursor.execute(
        "SELECT Description FROM StockSheet WHERE Description LIKE '%PEP% %Size 3/4%'")
    soles2_list = [r for r, in soles2_data]
    soles2 = StringVar()
    soles2.set(soles2_list[0])


def submit_root(e):
   command=bboys_slipper()

root.bind('<Return>', lambda e: submit_root(e))


def bboys_slipper():
    code = OrderNo.get()
    size12 = Size12.get()
    size34 = Size34.get()
    bind = binding.get()
    elast = elastic.get()
    material = upper.get()
    sock = sockm.get()
    sole1 = soles1.get()
    sole2 = soles2.get()
    delivery = Delivery.get()
    qty = Quantity.get()

    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        cursor = conn.cursor()
        # Insert into Orders
        cursor.execute(r'INSERT INTO MySlippers (Factory,Planned,OrderNo,Style,DeliveryDate,Quantity,Balances,Binding,Elastic,Material,Sock,Soles12,Soles34) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)', [
                       "Reflex", timestampStr, code, "BBOYS SLIPPER", delivery, qty, qty, bind, elast, material, sock, size12, size34])
        # Insert into Production
        cursor.execute(r'INSERT INTO SlipProduction (Factory,Planned,Order2,Style,DelDate,Orderqty,Clicking,Closing,Finishing,Despatch,Warehouse,ToShip) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', [
                       "Reflex", timestampStr, code, "BBOYS SLIPPER", delivery, qty, qty, "0", "0", "0", "0", qty])
        # Insert Into Planning
        cursor.execute(r'INSERT INTO PlanSlip (Factory,DatePlanned,OrderNo,Style,Pairs,Delivery,Size12,Size34) VALUES(?,?,?,?,?,?,?,?)', [
                       "Reflex", timestampStr, code, "BBOYS SLIPPER", qty, delivery, size12, size34])
        # Insert Into Required
        cursor.execute(r'INSERT INTO SlipRequired (Factory,InputDate,OrderNo,Style,Pairs,DelDate,Upper,Sock,Ribbon,Elastic,Binding,Gusset,Cartons,MLSize1x2,MLSize3x4)'
                       ' VALUES(?,?,?,?,?,?,?*(1.45/32.2),?*(1.45/63),?*(0.065),?*(0.66),?*(0.85),?*(0.16),?/,?,?)',
                       ["Reflex", timestampStr, code, "BBOYS SLIPPER", qty, delivery, qty, qty, qty, qty, qty, qty, qty, size12, size34])
        # Upper Material
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1.45/32.2), LastRec=? WHERE Description=?',
                       (qty, timestampStr, material))
        # Binding
        cursor.execute(
            r'UPDATE StockSheet SET Quantity=Quantity-?*(0.85), LastRec=? WHERE Description=?', (qty, timestampStr, bind))
        # Elastic
        cursor.execute(
            r'UPDATE StockSheet SET Quantity=Quantity-?*(0.66), LastRec=? WHERE Description=?', (qty, timestampStr, elast))
        # Sock Material
        cursor.execute(
            r'UPDATE StockSheet SET Quantity=Quantity-?*(1.45/63), LastRec=? WHERE Description=?', (qty, timestampStr, sock))
        # 3mm Ribbon
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(0.065), LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "RIB0001",))
        # Soles
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?',
                       (size12, timestampStr, sole1))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?',
                       (size34, timestampStr, sole2))
        # Gusset Elastic
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(0.16), LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "ELA0008",))
        # Cartons
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?/, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "CAR0010",))
        # Made In Lesotho Label
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "LAB0002",))
        # 25mm Tag Pin
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "PIN0001",))
        # Polybag
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "BAG0002",))
        # Hanger Sticker
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size67, timestampStr, "STI0072",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size89, timestampStr, "STI0074",))
        # Hanger
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "HAN0001",))

        updated = cursor.rowcount
        conn.commit()
        cursor.close()
        root.destroy()
        sys.exit(updated)  # return value whether record has been updated


label_0 = Label(root, text="BABY BOYS SLIPPER", width=43,  relief='raised', background="lightskyblue3", font=("bold", 20), anchor=CENTER).place(x=5, y=23)

label_on = Label(root, text="Order No:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=180, y=90)
entry_on = Entry(root, textvar=OrderNo, background="", width=21, font=("bold", 12)).place(x=300, y=90)

label_2 = Label(root, text="Delivery Date:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=180, y=120)
entry_2 = Entry(root, textvar=Delivery, background="", width=21, font=("bold", 12)).place(x=300, y=120)

label_bb1 = Label(root, text="Size 1/2:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=180)
entry_bb1 = Entry(root, textvar=Size12, background="", width=21, font=("bold", 12)).place(x=140, y=180)

label_bb2 = Label(root, text="Size 3/4:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=210)
entry_bb2 = Entry(root, textvar=Size34, background="", width=21, font=("bold", 12)).place(x=140, y=210)

label_bb3 = Label(root, text="Total Quantity:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=240)
entry_bb3 = Entry(root, textvar=Quantity, background="", width=21, font=("bold", 12)).place(x=140, y=240)

label_bb4 = Label(root, text="Binding:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=270)
option_upper = OptionMenu(root, binding, *binding_list).place(x=140, y=270)

label_bb5 = Label(root, text="Elastic:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=300)
option_upper = OptionMenu(root, elastic, *elastic_list).place(x=140, y=300)

label_bb6 = Label(root, text="1-Tone Upper:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=20, y=330)
option_upper = OptionMenu(root, upper, *upper_list).place(x=140, y=330)

label_bb7 = Label(root, text="Sock:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=20, y=360)
option_upper = OptionMenu(root, sockm, *sockm_list).place(x=140, y=360)

label_bb8 = Label(root, text="Soles:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=360, y=180)
option_soles = OptionMenu(root, soles1, *soles1_list).place(x=420, y=180)

# label_bb9 = Label(root, text="Soles 3/4:", width=20, background="lightskyblue3", font=("bold", 12)).place(x=40, y=210)
option_soles2 = OptionMenu(root, soles2, *soles2_list).place(x=420, y=210)

# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'), relief="raised", foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'), relief="raised", foreground='blue')

# Inserting buttons
submit1 = Button(root, text='Submit', style='S.TButton', width=11, command=bboys_slipper).place(x=60, y=420)
exit1 = Button(root, text='Close', style='C.TButton', width=11, command=root.destroy).place(x=520, y=420)

root.mainloop()
