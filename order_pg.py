from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
from datetime import datetime

root = Tk()
root.geometry('350x560')
root.title("New Order Pre-Girls Synthetic")
root.config(bg="lightskyblue3")
style = ttk.Style()

OrderNo = StringVar()
Size8 = IntVar()
Size9 = IntVar()
Size10 = IntVar()
Size11 = IntVar()
Size12 = IntVar()
Size13 = IntVar()
Size1 = IntVar()
Quantity = IntVar()
Delivery = StringVar()

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y")


def submit_root(e):
   command=order_pg()

root.bind('<Return>', lambda e: submit_root(e))


def order_pg():
    code = OrderNo.get()
    size8 = Size8.get()
    size9 = Size9.get()
    size10 = Size10.get()
    size11 = Size11.get()
    size12 = Size12.get()
    size13 = Size13.get()
    size1 = Size1.get()
    delivery = Delivery.get()
    qty = Quantity.get()

    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        cursor = conn.cursor()
        # Insert into Orders
        cursor.execute(r'INSERT INTO MyShoe (Factory,Planned,OrderNo,Style,DeliveryDate,Quantity,Balances) VALUES(?,?,?,?,?,?,?)', [
                       "Reflex", timestampStr, code, "PRE GIRLS SYNTHETIC", delivery, qty, qty])
        # Insert into Production
        cursor.execute(r'INSERT INTO Production (Factory,Planned,Order2,Style,DelDate,Orderqty,Clicking,Closing,Finishing,Despatch,Warehouse,ToShip,Shipped) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)', [
                       "Reflex", timestampStr, code, "PRE GIRLS SYNTHETIC", delivery, qty, qty, "0", "0", "0", "0", qty, "0",])
        # Insert into Production_Balances
        cursor.execute(r'INSERT INTO Production_Balances (Factory,Planned,Order2,Style,DelDate,Orderqty,Clicking,Closing,Finishing,Despatch,Warehouse,ToShip,Shipped) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)', [
                       "Reflex", timestampStr, code, "PRE GIRLS SYNTHETIC", delivery, qty, qty, qty, qty, qty, qty, qty, "0",])
        # Insert Into Planning
        cursor.execute(r'INSERT INTO Planning (Factory,DatePlanned,OrderNo,Style,Pairs,Delivery,Size8,Size9,Size10,Size11,Size12,Size13,Size1) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)', [
                       "Reflex", timestampStr, code, "PRE GIRLS SYNTHETIC", qty, delivery, size8, size9, size10, size11, size12, size13, size1])
        # Insert Into Required
        cursor.execute(r'INSERT INTO TBARequired (Factory,InputDate,OrderNo,Style,Pairs,DelDate,Upper,Stiffener,Insole,Sock,Buckles,Foil,Gusset,Rivets,PBA887,IA80,Cartons,TBASize8,TBASize9,TBASize10,TBASize11,TBASize12,TBASize13,TBASize1)'
                       ' VALUES(?,?,?,?,?,?,?*(1.395/14),?*(1.5/63),?*(1.45/75.5),?*(1.45/46),?*2,?*0.105,?*0.38,?*2,?*0.027,?*0.027,?/12,?,?,?,?,?,?,?)',
                       ["Reflex", timestampStr, code, "PRE GIRLS SYNTHETIC", qty, delivery, qty, qty, qty, qty, qty, qty, qty, qty, qty, qty, qty, size8, size9, size10, size11, size12, size13, size1])
        # Upper Material
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1.395/14), LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "SCH0001",))
        # Stiffener
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1.45/75.5), LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "DURAGRIP",))
        # Insole Board
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1.5/63), LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "INS0002",))
        # Sock Material
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1.45/46), LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "SCH0002",))
        # 14mm Buckles
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*2, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "BUC0001",))
        # Foil
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*0.105, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "FOI0003",))
        # PBA 887
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*0.027, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "CH0001",))
        # Soles
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size8, timestampStr, "TBA0001",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size9, timestampStr, "TBA0002",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size10, timestampStr, "TBA0003",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size11, timestampStr, "TBA0004",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size12, timestampStr, "TBA0005",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size13, timestampStr, "TBA0006",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size1, timestampStr, "TBA0007",))
        # Rivets
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*6, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "RIV0001",))
        # IA 80
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*0.013, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "CH0003",))
        # Gusset Elastic
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*0.31, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "ELA0008",))
        # Cartons
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?/12, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "CAR0001",))
        # Swingtags
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "SPT0001",))
        # 25mm Tag Pin
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "PIN0001",))
        # Polybag
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "BAG0003",))
        # Hanger Sticker
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size8, timestampStr, "STI0066",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size9, timestampStr, "STI0067",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size10, timestampStr, "STI0068",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size11, timestampStr, "STI0069",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size12, timestampStr, "STI0070",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size13, timestampStr, "STI0071",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size1, timestampStr, "STI0059",))
        # Hanger
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "HAN0002",))

        updated = cursor.rowcount
        conn.commit()
        cursor.close()

    with sqlite3.connect('Log Sheets.sql3') as conn2:
        cursor2 = conn2.cursor()
        code = OrderNo.get()
        barcode = OrderNo.get()
        size8 = Size8.get()
        size9 = Size9.get()
        size10 = Size10.get()
        size11 = Size11.get()
        size12 = Size12.get()
        size13 = Size13.get()
        size1 = Size1.get()
        delivery = Delivery.get()
        qty = Quantity.get()
        cursor2.execute('CREATE TABLE IF NOT EXISTS [%s] (Barcode,OrderNo,Style,Delivery,Size8,Size9,Size10,Size11,Size12,Size13,Size1,Qty,Ticket)' %code)
        cursor2.execute(r'INSERT INTO [%s] (Barcode,OrderNo,Style,Delivery,Size8,Size9,Size10,Size11,Size12,Size13,Size1,Qty,Ticket) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)' %code, [ barcode, code, "PRE GIRLS SYNTHETIC", delivery, size8, size9, size10, size11, size12, size13, size1, qty, 158])
        updated = cursor2.rowcount
        conn2.commit()
        cursor2.close()
        root.destroy()
        sys.exit(updated)


label_0 = Label(root, text="Pre-Girls Synthetic", width=16,
                background="lightskyblue3", font=("bold", 20)).place(x=50, y=23)

label_on = Label(root, text="Order No:", width=20,
                 background="lightskyblue3", font=("bold", 11)).place(x=40, y=90)
entry_on = Entry(root, textvar=OrderNo, background="yellow",
                 font=("bold", 10)).place(x=160, y=90)

label_2 = Label(root, text="Delivery Date:", width=20,
                background="lightskyblue3", font=("bold", 11)).place(x=40, y=120)
entry_2 = Entry(root, textvar=Delivery, background="yellow",
                font=("bold", 10)).place(x=160, y=120)

label_pb8 = Label(root, text="Size 8:", width=20,
                  background="lightskyblue3", font=("bold", 11)).place(x=40, y=180)
entry_pb8 = Entry(root, textvar=Size8, background="yellow",
                  font=("bold", 10)).place(x=160, y=180)

label_pb9 = Label(root, text="Size 9:", width=20,
                  background="lightskyblue3", font=("bold", 11)).place(x=40, y=210)
entry_pb9 = Entry(root, textvar=Size9, background="yellow",
                  font=("bold", 10)).place(x=160, y=210)

label_pb10 = Label(root, text="Size 10:", width=20,
                   background="lightskyblue3", font=("bold", 11)).place(x=40, y=240)
entry_pb10 = Entry(root, textvar=Size10, background="yellow",
                   font=("bold", 10)).place(x=160, y=240)

label_pb11 = Label(root, text="Size 11:", width=20,
                   background="lightskyblue3", font=("bold", 11)).place(x=40, y=270)
entry_pb11 = Entry(root, textvar=Size11, background="yellow",
                   font=("bold", 10)).place(x=160, y=270)

label_pb12 = Label(root, text="Size 12:", width=20,
                   background="lightskyblue3", font=("bold", 11)).place(x=40, y=300)
entry_pb12 = Entry(root, textvar=Size12, background="yellow",
                   font=("bold", 10)).place(x=160, y=300)

label_pb13 = Label(root, text="Size 13:", width=20,
                   background="lightskyblue3", font=("bold", 11)).place(x=40, y=330)
entry_pb13 = Entry(root, textvar=Size13, background="yellow",
                   font=("bold", 10)).place(x=160, y=330)

label_pb1 = Label(root, text="Size 1:", width=20,
                  background="lightskyblue3", font=("bold", 11)).place(x=40, y=360)
entry_pb1 = Entry(root, textvar=Size1, background="yellow",
                  font=("bold", 10)).place(x=160, y=360)

label_qty = Label(root, text="Total Quantity:", width=20,
                  background="lightskyblue3", font=("bold", 11)).place(x=40, y=420)
entry_qty = Entry(root, textvar=Quantity, background="yellow",
                  font=("bold", 10)).place(x=160, y=420)

# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'),
                relief="raised", foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'),
                relief="raised", foreground='blue')

# Inserting buttons
submit1 = Button(root, text='Submit', style='S.TButton',
                 width=11, command=order_pg).place(x=20, y=510)
exit1 = Button(root, text='Close', style='C.TButton', width=11,
               command=root.destroy).place(x=220, y=510)

root.mainloop()
