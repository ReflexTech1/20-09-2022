from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
from datetime import datetime
import os
from tkinter import messagebox

root = Tk()
root.geometry('350x500')
root.title("New Order Mens Leather")
root.config(bg="lightskyblue3")
style = ttk.Style()

OrderNo = StringVar()
Size6 = IntVar()
Size7b = IntVar()
Size8b = IntVar()
Size9b = IntVar()
Size10b = IntVar()
Quantity = IntVar()
Delivery = StringVar()

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y")


def submit_root(e):
   command=order_ml()

root.bind('<Return>', lambda e: submit_root(e))


def order_ml():
    code = OrderNo.get()
    size6 = Size6.get()
    size7b = Size7b.get()
    size8b = Size8b.get()
    size9b = Size9b.get()
    size10b = Size10b.get()
    delivery = Delivery.get()
    qty = Quantity.get()

    if qty == sum([size6+size7b+size8b+size9b+size10b]):
        with sqlite3.connect('Reflex Footwear.sql3') as conn:
            cursor = conn.cursor()
        # Insert into Orders
            cursor.execute(r'INSERT INTO MyShoe (Factory,Planned,OrderNo,Style,DeliveryDate,Quantity,Balances) VALUES(?,?,?,?,?,?,?)', [
                       "Reflex", timestampStr, code, "MENS LEATHER", delivery, qty, qty])
        # Insert into Production
            cursor.execute(r'INSERT INTO Production (Factory,Planned,Order2,Style,DelDate,Orderqty,Cutting,Assembly,Closing,Finishing,Despatch,ToShip,Shipped) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)', [
                       "Reflex", timestampStr, code, "MENS LEATHER", delivery, qty, qty, "0", "0", "0", "0", qty, "0",])
        # Insert into Production_Balances
            cursor.execute(r'INSERT INTO Production_Balances (Factory,Planned,Order2,Style,DelDate,Orderqty,Cutting,Assembly,Closing,Finishing,Despatch,ToShip,Shipped) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)', [
                       "Reflex", timestampStr, code, "MENS LEATHER", delivery, qty, qty, qty, qty, qty, qty, qty, "0",])
        # Insert Into Planning
            cursor.execute(r'INSERT INTO Planning (Factory,DatePlanned,OrderNo,Style,Pairs,Delivery,Size6,Size7b,Size8b,Size9b,Size10b) VALUES(?,?,?,?,?,?,?,?,?,?,?)', [
                       "Reflex", timestampStr, code, "MENS LEATHER", qty, delivery, size6, size7b, size8b, size9b, size10b])
        # Insert Into Required (check Topline + KnitBinding)
            cursor.execute(r'INSERT INTO LURequired (Factory,InputDate,OrderNo,Style,Pairs,DelDate,Upper,Stiffener,Insole,Sock,Laces,Foil,Gusset,KnitBin,Topline,Eyelets,PBA887,IA80,Cartons,SPSize6,SPSize7b,SPSize8b,SPSize9b,SPSize10b)'
                       ' VALUES(?,?,?,?,?,?,?*(6.9/3.5),?*(1.5/70),?*(1.5/32),?*(1.45/28),?*2,?*0.105,?*0.38,?*0.97,?*0.97,?*16,?*0.013333333,?*0.013333333,?/12,?,?,?,?,?)',
                       ["Reflex", timestampStr, code, "MENS LEATHER", qty, delivery, qty, qty, qty, qty, qty, qty, qty, qty, qty, qty, qty, qty, qty, size6, size7b, size8b, size9b, size10b])
        # Upper Material
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(6.9/3.5), LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "FUSION",))
        # Stiffener
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1.5/70), LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "DURAGRIP",))
        # Insole Board
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1.5/32), LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "INS0003",))
        # Sock Material
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1.45/28), LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "SCH0002",))
        # 80cm Laces
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*2, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "LAC0002",))
        # Foil
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*0.105, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "FOI0003",))
        # 13.5mm Knit Binding
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*0.097, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "BIN0001",))
        # Topline - check
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*0.097, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "TOPLINE",))
        # PBA 887
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*0.027, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "CH0001",))
        # Soles
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size6, timestampStr, "S/P0012",))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size7b, timestampStr, "S/P0013",))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size8b, timestampStr, "S/P0014",))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size9b, timestampStr, "S/P0015",))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size10b, timestampStr, "S/P0016",))
        # Eyelets
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*16, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "EYE0001",))
        # IA 80
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*0.013, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "CH0003",))
        # Gusset Elastic
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*0.38, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "ELA0008",))
        # 13.5mm Black Knit Binding
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*0.97, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "BIN0001",))
        # Topline
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*0.97, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "TOPLINE",))
        # Cartons
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?/12, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "CAR0007",))
        # Swingtags
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "SPT0002",))
        # 25mm Tag Pin
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "PIN0001",))
        # Polybag
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "BAG0004",))
        # Hanger Sticker
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size6, timestampStr, "STI0064",))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size7b, timestampStr, "STI0065",))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size8b, timestampStr, "STI0066",))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size9b, timestampStr, "STI0067",))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (size10b, timestampStr, "STI0068",))
        # Hanger
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                       (qty, timestampStr, "HAN0004",))

            updated = cursor.rowcount
            conn.commit()
            cursor.close()

        with sqlite3.connect('Log Sheets.sql3') as conn2:
            cursor2 = conn2.cursor()
            code = OrderNo.get()
            barcode = OrderNo.get()
            size6 = Size6.get()
            size7b = Size7b.get()
            size8b = Size8b.get()
            size9b = Size9b.get()
            size10b = Size10b.get()
            delivery = Delivery.get()
            qty = Quantity.get()
            cursor2.execute('CREATE TABLE IF NOT EXISTS [%s] (Barcode,OrderNo,Style,Delivery,Size6,Size7,Size8,Size9,Size10,Qty,Ticket)' %code)
            cursor2.execute(r'INSERT INTO [%s] (Barcode,OrderNo,Style,Delivery,Size6,Size7,Size8,Size9,Size10,Qty,Ticket) VALUES(?,?,?,?,?,?,?,?,?,?,?)' %code, [ barcode, code, "MENS LEATHER", delivery, size6, size7b, size8b, size9b, size10b, qty, 158])
            updated = cursor2.rowcount
            conn2.commit()
            cursor2.close()
            root.destroy()
            sys.exit(updated)
        
    else:
        messagebox.showwarning(title="Confirmation", message="The Size Range Does Not Equal The Total.\nPlease Confirm Sizes and Total Again.")


label_0 = Label(root, text="Mens Leather", width=13,
                background="lightskyblue3", font=("bold", 20)).place(x=90, y=23)

label_on = Label(root, text="Order No:", width=20,
                 background="lightskyblue3", font=("bold", 11)).place(x=40, y=90)
entry_on = Entry(root, textvar=OrderNo, background="yellow",
                 font=("bold", 10)).place(x=160, y=90)

label_2 = Label(root, text="Delivery Date:", width=20,
                background="lightskyblue3", font=("bold", 11)).place(x=40, y=120)
entry_2 = Entry(root, textvar=Delivery, background="yellow",
                font=("bold", 10)).place(x=160, y=120)

label_m6 = Label(root, text="Size 6:", width=20,
                 background="lightskyblue3", font=("bold", 11)).place(x=40, y=180)
entry_m6 = Entry(root, textvar=Size6, background="yellow",
                 font=("bold", 10)).place(x=160, y=180)

label_m7 = Label(root, text="Size 7:", width=20,
                 background="lightskyblue3", font=("bold", 11)).place(x=40, y=210)
entry_m7 = Entry(root, textvar=Size7b, background="yellow",
                 font=("bold", 10)).place(x=160, y=210)

label_m8 = Label(root, text="Size 8:", width=20,
                 background="lightskyblue3", font=("bold", 11)).place(x=40, y=240)
entry_m8 = Entry(root, textvar=Size8b, background="yellow",
                 font=("bold", 10)).place(x=160, y=240)

label_m9 = Label(root, text="Size 9:", width=20,
                 background="lightskyblue3", font=("bold", 11)).place(x=40, y=270)
entry_m9 = Entry(root, textvar=Size9b, background="yellow",
                 font=("bold", 10)).place(x=160, y=270)

label_m10 = Label(root, text="Size 10:", width=20,
                  background="lightskyblue3", font=("bold", 11)).place(x=40, y=300)
entry_m10 = Entry(root, textvar=Size10b, background="yellow",
                  font=("bold", 10)).place(x=160, y=300)

label_qty = Label(root, text="Total Quantity:", width=20,
                  background="lightskyblue3", font=("bold", 11)).place(x=40, y=360)
entry_qty = Entry(root, textvar=Quantity, background="yellow",
                  font=("bold", 10)).place(x=160, y=360)

# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'),
                relief="raised", foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'),
                relief="raised", foreground='blue')

# Inserting buttons
submit1 = Button(root, text='Submit', style='S.TButton',
                 width=11, command=order_ml).place(x=20, y=450)
exit1 = Button(root, text='Close', style='C.TButton', width=11,
               command=root.destroy).place(x=220, y=450)

root.mainloop()
