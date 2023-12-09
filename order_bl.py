from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
from datetime import datetime

root = Tk()
root.geometry('350x470')
root.title("New Order Boys Leather")
root.config(bg="lightskyblue3")
style = ttk.Style()

OrderNo = StringVar()
Size2 = IntVar()
Size3 = IntVar()
Size4 = IntVar()
Size5 = IntVar()
Quantity = IntVar()
Delivery = StringVar()

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y")


def order_bl():
    code = OrderNo.get()
    size2 = Size2.get()
    size3 = Size3.get()
    size4 = Size4.get()
    size5 = Size5.get()
    delivery = Delivery.get()
    qty = Quantity.get()

    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        cursor = conn.cursor()
        # Insert into Orders
        cursor.execute(r'INSERT INTO MyShoe (Factory,Planned,OrderNo,Style,DeliveryDate,Quantity,Balances) VALUES(?,?,?,?,?,?,?)', [
                       "Reflex", timestampStr, code, "BOYS LEATHER", delivery, qty, qty])
        # Insert into Production
        cursor.execute(r'INSERT INTO Production (Factory,Planned,Order2,Style,DelDate,Orderqty,Cutting,Assembly,Closing,Finishing,Despatch,ToShip,Shipped) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)', [
                       "Reflex", timestampStr, code, "BOYS LEATHER", delivery, qty, qty, "0", "0", "0", "0", qty, "0",])
        # Insert into Production_Balances
        cursor.execute(r'INSERT INTO Production_Balances (Factory,Planned,Order2,Style,DelDate,Orderqty,Cutting,Assembly,Closing,Finishing,Despatch,ToShip,Shipped) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)', [
                       "Reflex", timestampStr, code, "BOYS LEATHER", delivery, qty, qty, qty, qty, qty, qty, qty, "0",])
                       # Insert Into Planning
        cursor.execute(r'INSERT INTO Planning (Factory,DatePlanned,OrderNo,Style,Pairs,Delivery,Size2,Size3,Size4,Size5) VALUES(?,?,?,?,?,?,?,?,?,?)', [
                       "Reflex", timestampStr, code, "BOYS LEATHER", qty, delivery, size2, size3, size4, size5])
        # Insert Into Required
        cursor.execute(r'INSERT INTO LURequired (Factory,InputDate,OrderNo,Style,Pairs,DelDate,Upper,Stiffener,Insole,Sock,Laces,Foil,Gusset,KnitBin,Topline,Eyelets,PBA887,IA80,Cartons,SPSize2,SPSize3,SPSize4,SPSize5)'
                       ' VALUES(?,?,?,?,?,?,?*(5.9/3.8),?*(1.5/78.5),?*(1.5/36.5),?*(1.45/36),?*2,?*0.105,?*0.38,?*0.9,?*0.9,?*16,?*0.027,?*0.027,?/12,?,?,?,?)',
                       ["Reflex", timestampStr, code, "BOYS LEATHER", qty, delivery, qty, qty, qty, qty, qty, qty, qty, qty, qty, qty, qty, qty, qty, size2, size3, size4, size5])
        # Upper Material
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(5.9/3.8), LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "FUSION",))
        # Stiffener
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1.5/78.5), LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "DURAGRIP",))
        # Insole Board
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1.5/36.5), LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "INS0002",))
        # Sock Material
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1.45/36), LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "SCH0002",))
        # 80cm Laces
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*2, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "LAC0002",))
        # Foil
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*0.105, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "FOI0003",))
        # Gusset Elastic
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*0.38, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "ELA0008",))
        # 13.5mm Knit Binding
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*0.9, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "BIN0001",))
        # Topline
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*0.9, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "TOPLINE",))
        # PBA 887
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*0.027, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "CH0001",))
        # Soles
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size2, timestampStr, "S/P0008",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size3, timestampStr, "S/P0009",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size4, timestampStr, "S/P0010",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size5, timestampStr, "S/P0011",))
        # Eyelets
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*16, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "EYE0001",))
        # IA 80
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*0.013, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "CH0003",))
        # Cartons
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?/12, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "CAR0004",))
        # Swingtags
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "SPT0001",))
        # 25mm Tag Pin
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "PIN0001",))
        # Polybag
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "BAG0004",))
        # Hanger Sticker
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size2, timestampStr, "STI0060",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size3, timestampStr, "STI0061",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size4, timestampStr, "STI0062",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size5, timestampStr, "STI0063",))
        # Hanger
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "HAN0003",))

        updated = cursor.rowcount
        conn.commit()
        cursor.close()

    with sqlite3.connect('Log Sheets.sql3') as conn2:
        cursor2 = conn2.cursor()
        code = OrderNo.get()
        barcode = OrderNo.get()
        size2 = Size2.get()
        size3 = Size3.get()
        size4 = Size4.get()
        size5 = Size5.get()
        delivery = Delivery.get()
        qty = Quantity.get()
        cursor2.execute('CREATE TABLE IF NOT EXISTS [%s] (Barcode,OrderNo,Style,Delivery,Size2,Size3,Size4,Size5,Qty,Ticket)' %code)
        cursor2.execute(r'INSERT INTO [%s] (Barcode,OrderNo,Style,Delivery,Size2,Size3,Size4,Size5,Qty,Ticket) VALUES(?,?,?,?,?,?,?,?,?,?)' %code, [ barcode, code, "BOYS LEATHER", delivery, size2, size3, size4, size5, qty, 158])
        updated = cursor2.rowcount
        conn2.commit()
        cursor2.close()
        root.destroy()
        sys.exit(updated)  # return value whether record has been updated


label_0 = Label(root, text="Boys Leather", width=13,
                background="lightskyblue3", font=("bold", 20)).place(x=85, y=23)

label_on = Label(root, text="Order No:", width=20,
                 background="lightskyblue3", font=("bold", 11)).place(x=40, y=90)
entry_on = Entry(root, textvar=OrderNo, background="yellow",
                 font=("bold", 10)).place(x=160, y=90)

label_2 = Label(root, text="Delivery Date:", width=20,
                background="lightskyblue3", font=("bold", 11)).place(x=40, y=120)
entry_2 = Entry(root, textvar=Delivery, background="yellow",
                font=("bold", 10)).place(x=160, y=120)

label_b2 = Label(root, text="Size 2:", width=20,
                 background="lightskyblue3", font=("bold", 11)).place(x=40, y=180)
entry_b2 = Entry(root, textvar=Size2, background="yellow",
                 font=("bold", 10)).place(x=160, y=180)

label_b3 = Label(root, text="Size 3:", width=20,
                 background="lightskyblue3", font=("bold", 11)).place(x=40, y=210)
entry_b3 = Entry(root, textvar=Size3, background="yellow",
                 font=("bold", 10)).place(x=160, y=210)

label_b4 = Label(root, text="Size 4:", width=20,
                 background="lightskyblue3", font=("bold", 11)).place(x=40, y=240)
entry_b4 = Entry(root, textvar=Size4, background="yellow",
                 font=("bold", 10)).place(x=160, y=240)

label_b5 = Label(root, text="Size 5:", width=20,
                 background="lightskyblue3", font=("bold", 11)).place(x=40, y=270)
entry_b5 = Entry(root, textvar=Size5, background="yellow",
                 font=("bold", 10)).place(x=160, y=270)

label_b6 = Label(root, text="Total Quantity:", width=20,
                 background="lightskyblue3", font=("bold", 11)).place(x=40, y=330)
entry_b6 = Entry(root, textvar=Quantity, background="yellow",
                 font=("bold", 10)).place(x=160, y=330)

# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'),
                relief="raised", foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'),
                relief="raised", foreground='blue')

# Inserting buttons
submit1 = Button(root, text='Submit', style='S.TButton',
                 width=11, command=order_bl).place(x=20, y=420)
exit1 = Button(root, text='Close', style='C.TButton', width=11,
               command=root.destroy).place(x=220, y=420)


def submit_root(e):
   command=order_bl()

root.bind('<Return>', lambda e: submit_root(e))

root.mainloop()
