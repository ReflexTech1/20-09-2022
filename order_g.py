from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
from datetime import datetime

root = Tk()
root.geometry('350x550')
root.title("New Order Girls Synthetic")
root.config(bg="lightskyblue3")
style = ttk.Style()

OrderNo = StringVar()
Size2 = IntVar()
Size3 = IntVar()
Size4 = IntVar()
Size5 = IntVar()
Size6 = IntVar()
Size7 = IntVar()
Size8b = IntVar()
Quantity = IntVar()
Delivery = StringVar()

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y")


def order_g():
    code = OrderNo.get()
    size2 = Size2.get()
    size3 = Size3.get()
    size4 = Size4.get()
    size5 = Size5.get()
    size6 = Size6.get()
    size7 = Size7.get()
    size8b = Size8b.get()
    delivery = Delivery.get()
    qty = Quantity.get()

    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        cursor = conn.cursor()
        # Insert into Orders
        cursor.execute(r'INSERT INTO MyShoe (Factory,Planned,OrderNo,Style,DeliveryDate,Quantity,Balances) VALUES(?,?,?,?,?,?,?)', [
                       "Reflex", timestampStr, code, "GIRLS SYNTHETIC", delivery, qty, qty])
        # Insert into Production
        cursor.execute(r'INSERT INTO Production (Factory,Planned,Order2,Style,DelDate,Orderqty,Cutting,Assembly,Closing,Finishing,Despatch,ToShip,Shipped) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)', [
                       "Reflex", timestampStr, code, "GIRLS SYNTHETIC", delivery, qty, qty, "0", "0", "0", "0", qty, "0",])
        # Insert into Production_Balances
        cursor.execute(r'INSERT INTO Production_Balances (Factory,Planned,Order2,Style,DelDate,Orderqty,Cutting,Assembly,Closing,Finishing,Despatch,ToShip,Shipped) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)', [
                       "Reflex", timestampStr, code, "GIRLS SYNTHETIC", delivery, qty, qty, qty, qty, qty, qty, qty, "0",])
                       # Insert Into Planning
        cursor.execute(r'INSERT INTO Planning (Factory,DatePlanned,OrderNo,Style,Pairs,Delivery,Size2,Size3,Size4,Size5,Size6,Size7b,Size8b) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)', [
                       "Reflex", timestampStr, code, "GIRLS SYNTHETIC", qty, delivery, size2, size3, size4, size5, size6, size7, size8b])
        # Insert Into Required
        cursor.execute(r'INSERT INTO TBARequired (Factory,InputDate,OrderNo,Style,Pairs,DelDate,Upper,Stiffener,Insole,Sock,Buckles,Foil,Gusset,Rivets,PBA887,IA80,Cartons,TBASize2,TBASize3,TBASize4,TBASize5,TBASize6,TBASize7,TBASize8b)'
                       ' VALUES(?,?,?,?,?,?,?*(1.395/10),?*(1.5/56),?*(1.5/45),?*(1.45/34),?*2,?*0.105,?*0.38,?*2,?*0.013333333,?*0.013333333,?/12,?,?,?,?,?,?,?)',
                       ["Reflex", timestampStr, code, "GIRLS SYNTHETIC", qty, delivery, qty, qty, qty, qty, qty, qty, qty, qty, qty, qty, qty, size2, size3, size4, size5, size6, size7, size8b])
        # Upper Material
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1.395/10), LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "SCH0001",))
        # Stiffener
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1.5/56), LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "DURAGRIP",))
        # Insole Board
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1.5/45), LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "INS0002",))
        # Sock Material
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1.45/34), LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "SCH0002",))
        # 16mm Buckles
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*2, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "BUC0002",))
        # Foil
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*0.105, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "FOI0003",))
        # PBA 887
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*0.027, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "CH0001",))
        # Soles
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size2, timestampStr, "TRU0008",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size3, timestampStr, "TRU0009",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size4, timestampStr, "TRU0010",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size5, timestampStr, "TRU0011",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size6, timestampStr, "TRU0012",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size7, timestampStr, "TRU0013",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size8b, timestampStr, "TRU0014",))
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
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size6, timestampStr, "STI0064",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size7, timestampStr, "STI0065",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size8b, timestampStr, "STI0066",))
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
        size6 = Size5.get()
        size7 = Size5.get()
        size8 = Size5.get()
        delivery = Delivery.get()
        qty = Quantity.get()
        cursor2.execute('CREATE TABLE IF NOT EXISTS [%s] (Barcode,OrderNo,Style,Delivery,Size2,Size3,Size4,Size5,Size6,Size7b,Size8b,Qty,Ticket)' %code)
        cursor2.execute(r'INSERT INTO [%s] (Barcode,OrderNo,Style,Delivery,Size2,Size3,Size4,Size5,Size6,Size7b,Size8b,Qty,Ticket) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)' %code, [ barcode, code, "GIRLS SYNTHETIC", delivery, size2, size3, size4, size5, size6, size7, size8, qty, 158])
        updated = cursor2.rowcount
        conn2.commit()
        cursor2.close()
        root.destroy()
        sys.exit(updated)  # return value whether record has been updated


label_0 = Label(root, text="Girls Synthetic", width=13,
                background="lightskyblue3", font=("bold", 20)).place(x=85, y=23)

label_on = Label(root, text="Order No:", width=20,
                 background="lightskyblue3", font=("bold", 11)).place(x=40, y=90)
entry_on = Entry(root, textvar=OrderNo, background="yellow",
                 font=("bold", 10)).place(x=160, y=90)

label_2 = Label(root, text="Delivery Date:", width=20,
                background="lightskyblue3", font=("bold", 11)).place(x=40, y=120)
entry_2 = Entry(root, textvar=Delivery, background="yellow",
                font=("bold", 10)).place(x=160, y=120)

label_g2 = Label(root, text="Size 2:", width=20,
                 background="lightskyblue3", font=("bold", 11)).place(x=40, y=180)
entry_g2 = Entry(root, textvar=Size2, background="yellow",
                 font=("bold", 10)).place(x=160, y=180)

label_g3 = Label(root, text="Size 3:", width=20,
                 background="lightskyblue3", font=("bold", 11)).place(x=40, y=210)
entry_g3 = Entry(root, textvar=Size3, background="yellow",
                 font=("bold", 10)).place(x=160, y=210)

label_g4 = Label(root, text="Size 4:", width=20,
                 background="lightskyblue3", font=("bold", 11)).place(x=40, y=240)
entry_g4 = Entry(root, textvar=Size4, background="yellow",
                 font=("bold", 10)).place(x=160, y=240)

label_g5 = Label(root, text="Size 5:", width=20,
                 background="lightskyblue3", font=("bold", 11)).place(x=40, y=270)
entry_g5 = Entry(root, textvar=Size5, background="yellow",
                 font=("bold", 10)).place(x=160, y=270)

label_g6 = Label(root, text="Size 6:", width=20,
                 background="lightskyblue3", font=("bold", 11)).place(x=40, y=300)
entry_g6 = Entry(root, textvar=Size6, background="yellow",
                 font=("bold", 10)).place(x=160, y=300)

label_g7 = Label(root, text="Size 7:", width=20,
                 background="lightskyblue3", font=("bold", 11)).place(x=40, y=330)
entry_g7 = Entry(root, textvar=Size7, background="yellow",
                 font=("bold", 10)).place(x=160, y=330)

label_g8 = Label(root, text="Size 8:", width=20,
                 background="lightskyblue3", font=("bold", 11)).place(x=40, y=360)
entry_g8 = Entry(root, textvar=Size8b, background="yellow",
                 font=("bold", 10)).place(x=160, y=360)

label_g9 = Label(root, text="Total Quantity:", width=20,
                 background="lightskyblue3", font=("bold", 11)).place(x=40, y=420)
entry_g9 = Entry(root, textvar=Quantity, background="yellow",
                 font=("bold", 10)).place(x=160, y=420)

# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'),
                relief="raised", foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'),
                relief="raised", foreground='blue')

# Inserting buttons
submit1 = Button(root, text='Submit', style='S.TButton',
                 width=11, command=order_g).place(x=20, y=480)
exit1 = Button(root, text='Close', style='C.TButton', width=11,
               command=root.destroy).place(x=220, y=480)


def submit_root(e):
   command=order_g()

root.bind('<Return>', lambda e: submit_root(e))

root.mainloop()
