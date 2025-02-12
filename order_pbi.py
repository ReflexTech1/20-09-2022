from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
from datetime import datetime
from tkinter import messagebox

root = Tk()
root.geometry('350x510')
root.title("New Order Pre-Boys Idler")
root.config(bg="lightskyblue3")
style = ttk.Style()

OrderNo = StringVar()
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
   command=order_pbi()

root.bind('<Return>', lambda e: submit_root(e))


def order_pbi():
    code = OrderNo.get()
    size9 = Size9.get()
    size10 = Size10.get()
    size11 = Size11.get()
    size12 = Size12.get()
    size13 = Size13.get()
    size1 = Size1.get()
    delivery = Delivery.get()
    qty = Quantity.get()

    if qty == sum([size9+size10+size11+size12+size13+size1]):
        with sqlite3.connect('Reflex Footwear.sql3') as conn:
            cursor = conn.cursor()
            # Insert into Orders
            cursor.execute(r'INSERT INTO MyShoe (Factory,Planned,OrderNo,Style,DeliveryDate,Quantity,Balances) VALUES(?,?,?,?,?,?,?)', [
                           "Reflex", timestampStr, code, "PRE BOYS MOCCASIN", delivery, qty, qty])
            # Insert into Production
            cursor.execute(r'INSERT INTO Production (Factory,Planned,Order2,Style,DelDate,Orderqty,Cutting,Assembly,Closing,Finishing,Despatch,ToShip,Shipped) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)', [
                           "Reflex", timestampStr, code, "PRE BOYS MOCCASIN", delivery, qty, qty, "0", "0", "0", "0", qty, "0",])
            # Insert into Production_Balances
            cursor.execute(r'INSERT INTO Production_Balances (Factory,Planned,Order2,Style,DelDate,Orderqty,Cutting,Assembly,Closing,Finishing,Despatch,ToShip,Shipped) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)', [
                           "Reflex", timestampStr, code, "PRE BOYS MOCCASIN", delivery, qty, qty, qty, qty, qty, qty, qty, "0",])
            # Insert Into Planning
            cursor.execute(r'INSERT INTO Planning (Factory,DatePlanned,OrderNo,Style,Pairs,Delivery,Size9,Size10,Size11,Size12,Size13,Size1) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', [
                           "Reflex", timestampStr, code, "PRE BOYS MOCCASIN", qty, delivery, size9, size10, size11, size12, size13, size1])
            # Insert Into Required
            cursor.execute(r'INSERT INTO HOPRequired (Factory,InputDate,OrderNo,Style,Pairs,DelDate,Upper,Stiffener,Insole,Sock,Laces,Foil,Gusset,HandLacing,PBA887,IA80,Cartons,HOPSize9,HOPSize10,HOPSize11,HOPSize12,HOPSize13,HOPSize1)'
                           ' VALUES(?,?,?,?,?,?,?*(1.395/11),?*(1.5/76),?*(1.5/115),?*(1.45/83),?*2,?*0.105,?*0.38,?*2.308,?*0.027,?*0.027,?/12,?,?,?,?,?,?)',
                           ["Reflex", timestampStr, code, "PRE BOYS MOCCASIN", qty, delivery, qty, qty, qty, qty, qty, qty, qty, qty, qty, qty, qty, size9, size10, size11, size12, size13, size1])
            # Upper Material
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1.395/11), LastRec=? WHERE ItemCode=?',
                           (qty, timestampStr, "SCH0001",))
            # Stiffener
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1.5/76), LastRec=? WHERE ItemCode=?',
                           (qty, timestampStr, "DURAGRIP",))
            # Insole Board
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1.5/115), LastRec=? WHERE ItemCode=?',
                           (qty, timestampStr, "INS0002",))
            # Sock Material
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1.45/83), LastRec=? WHERE ItemCode=?',
                           (qty, timestampStr, "SCH0002",))
            # 60cm Laces
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*2, LastRec=? WHERE ItemCode=?',
                           (qty, timestampStr, "LAC0001",))
            # Foil
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*0.105, LastRec=? WHERE ItemCode=?',
                           (qty, timestampStr, "FOI0003",))
            # PBA 887
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*0.027, LastRec=? WHERE ItemCode=?',
                           (qty, timestampStr, "CH0001",))
            # Soles
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                           (size9, timestampStr, "IDL0001",))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                           (size10, timestampStr, "IDL0002",))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                           (size11, timestampStr, "IDL0003",))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                           (size12, timestampStr, "IDL0004",))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                           (size13, timestampStr, "IDL0005",))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?',
                           (size1, timestampStr, "IDL0006",))
            # IA 80
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*0.013, LastRec=? WHERE ItemCode=?',
                           (qty, timestampStr, "CH0003",))
            # Gusset Elastic
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*0.31, LastRec=? WHERE ItemCode=?',
                           (qty, timestampStr, "ELA0008",))
            # Handlacing Thread
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*2.308, LastRec=? WHERE ItemCode=?',
                           (qty, timestampStr, "THR0023",))
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
            size9 = Size9.get()
            size10 = Size10.get()
            size11 = Size11.get()
            size12 = Size12.get()
            size13 = Size13.get()
            size1 = Size1.get()
            delivery = Delivery.get()
            qty = Quantity.get()
            cursor2.execute('CREATE TABLE IF NOT EXISTS [%s] (Barcode,OrderNo,Style,Delivery,Size9,Size10,Size11,Size12,Size13,Size1,Qty,Ticket)' %code)
            cursor2.execute(r'INSERT INTO [%s] (Barcode,OrderNo,Style,Delivery,Size9,Size10,Size11,Size12,Size13,Size1,Qty,Ticket) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)' %code, [ barcode, code, "PRE BOYS IDLER", delivery, size9, size10, size11, size12, size13, size1, qty, 158])
            updated = cursor2.rowcount
            conn2.commit()
            cursor2.close()
            root.destroy()
            sys.exit(updated)

    else:
        messagebox.showwarning(title="Confirmation", message="The Size Range Does Not Equal The Total.\nPlease Confirm Sizes and Total Again.")

label_0 = Label(root, text="Pre-Boys Moccasin", width=16,
                background="lightskyblue3", font=("bold", 20)).place(x=50, y=23)

label_on = Label(root, text="Order No:", width=20,
                 background="lightskyblue3", font=("bold", 11)).place(x=40, y=90)
entry_on = Entry(root, textvar=OrderNo, background="yellow",
                 font=("bold", 10)).place(x=160, y=90)

label_2 = Label(root, text="Delivery Date:", width=20,
                background="lightskyblue3", font=("bold", 11)).place(x=40, y=120)
entry_2 = Entry(root, textvar=Delivery, background="yellow",
                font=("bold", 10)).place(x=160, y=120)

label_pb9 = Label(root, text="Size 9:", width=20,
                  background="lightskyblue3", font=("bold", 11)).place(x=40, y=180)
entry_pb9 = Entry(root, textvar=Size9, background="yellow",
                  font=("bold", 10)).place(x=160, y=180)

label_pb10 = Label(root, text="Size 10:", width=20,
                   background="lightskyblue3", font=("bold", 11)).place(x=40, y=210)
entry_pb10 = Entry(root, textvar=Size10, background="yellow",
                   font=("bold", 10)).place(x=160, y=210)

label_pb11 = Label(root, text="Size 11:", width=20,
                   background="lightskyblue3", font=("bold", 11)).place(x=40, y=240)
entry_pb11 = Entry(root, textvar=Size11, background="yellow",
                   font=("bold", 10)).place(x=160, y=240)

label_pb12 = Label(root, text="Size 12:", width=20,
                   background="lightskyblue3", font=("bold", 11)).place(x=40, y=270)
entry_pb12 = Entry(root, textvar=Size12, background="yellow",
                   font=("bold", 10)).place(x=160, y=270)

label_pb13 = Label(root, text="Size 13:", width=20,
                   background="lightskyblue3", font=("bold", 11)).place(x=40, y=300)
entry_pb13 = Entry(root, textvar=Size13, background="yellow",
                   font=("bold", 10)).place(x=160, y=300)

label_pb1 = Label(root, text="Size 1:", width=20,
                  background="lightskyblue3", font=("bold", 11)).place(x=40, y=330)
entry_pb1 = Entry(root, textvar=Size1, background="yellow",
                  font=("bold", 10)).place(x=160, y=330)

label_qty = Label(root, text="Total Quantity:", width=20,
                  background="lightskyblue3", font=("bold", 11)).place(x=40, y=390)
entry_qty = Entry(root, textvar=Quantity, background="yellow",
                  font=("bold", 10)).place(x=160, y=390)

# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'),
                relief="raised", foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'),
                relief="raised", foreground='blue')

# Inserting buttons
submit1 = Button(root, text='Submit', style='S.TButton',
                 width=11, command=order_pbi).place(x=20, y=460)
exit1 = Button(root, text='Close', style='C.TButton', width=11,
               command=root.destroy).place(x=220, y=460)

root.mainloop()
