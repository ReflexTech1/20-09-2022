from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
from datetime import datetime

root = Tk()
root.geometry('610x570')
root.title("New ML Slipper Order")
root.config(bg="lightskyblue3")
style = ttk.Style()

OrderNo = StringVar()
Size34 = IntVar()
Size56 = IntVar()
Size78 = IntVar()
Size910 = IntVar()
Size1112 = IntVar()
Size131 = IntVar()
Quantity = IntVar()
Delivery = StringVar()

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y")

with sqlite3.connect('Reflex Footwear.sql3') as conn:
    cursor = conn.cursor()
    soles_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%ML Soles%%Size 3/4%'")
    soles_list = [r for r, in soles_data]
    soles = StringVar()
    soles.set(soles_list[0])

    soles1_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%ML Soles%%Size 5/6%'")
    soles1_list = [r for r, in soles1_data]
    soles1 = StringVar()
    soles1.set(soles1_list[0])

    soles2_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%ML Soles%%Size 7/8%'")
    soles2_list = [r for r, in soles2_data]
    soles2 = StringVar()
    soles2.set(soles2_list[0])

    soles3_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%ML Soles%%Size 9/10%'")
    soles3_list = [r for r, in soles3_data]
    soles3 = StringVar()
    soles3.set(soles3_list[0])

    soles4_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%ML Soles%%Size 11/12%'")
    soles4_list = [r for r, in soles4_data]
    soles4 = StringVar()
    soles4.set(soles4_list[0])

    soles5_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%ML Soles%%Size 13/1%'")
    soles5_list = [r for r, in soles5_data]
    soles5 = StringVar()
    soles5.set(soles5_list[0])


def submit_root(e):
   command=young_boys_slipper()

root.bind('<Return>', lambda e: submit_root(e))


def young_boys_slipper():
    code = OrderNo.get()
    size34 = Size34.get()
    size56 = Size56.get()
    size78 = Size78.get()
    size910 = Size910.get()
    size1112 = Size1112.get()
    size131 = Size131.get()
    sole = soles.get()
    sole1 = soles1.get()
    sole2 = soles2.get()
    sole3 = soles3.get()
    sole4 = soles4.get()
    sole5 = soles5.get()
    delivery = Delivery.get()
    qty = Quantity.get()

    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        cursor = conn.cursor()
        # Insert into Orders
        cursor.execute(r'INSERT INTO MySlippers (Factory,Planned,OrderNo,Style,DeliveryDate,Quantity,Balances,Soles34,Soles56,Soles78,Soles910,Soles1112,Soles131) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)', [
                       "Reflex", timestampStr, code, "YOUNGER BOYS SLIPPER", delivery, qty, qty, size34, size56, size78, size910, size1112, size131])
        # Insert into Production
        cursor.execute(r'INSERT INTO SlipProduction (Factory,Planned,Order2,Style,DelDate,Orderqty,Clicking,Closing,Finishing,Despatch,Warehouse,ToShip) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', [
                       "Reflex", timestampStr, code, "YOUNGER BOYS SLIPPER", delivery, qty, qty, "0", "0", "0", "0", qty])
        # Insert into Production_Balances
        cursor.execute(r'INSERT INTO SlipProd_Balances (Factory,Planned,Order2,Style,DelDate,Orderqty,Clicking,Closing,Finishing,Despatch,Warehouse,ToShip,Shipped) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)', [
                       "Reflex", timestampStr, code, "YOUNGER BOYS SLIPPER", delivery, qty, qty, qty, qty, qty, qty, qty, "0",])               
        # Insert Into Planning
        cursor.execute(r'INSERT INTO PlanSlip (Factory,DatePlanned,OrderNo,Style,Pairs,Delivery,Size34,Size56,Size78,Size910,Size1112,Size131) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', ["Reflex", timestampStr, code, "YOUNGER BOYS SLIPPER", qty, delivery, size34, size56, size78, size910, size1112, size131])
        # Insert Into Required
        cursor.execute(r'INSERT INTO SlipRequired (Factory,InputDate,OrderNo,Style,Pairs,DelDate,Upper,Sock,Ribbon,Elastic,Binding,Gusset,Cartons,MLSize3x4,MLSize5x6,MLSize7x8,MLSize9x10,MLSize11x12,MLSize13x1)'
                       ' VALUES(?,?,?,?,?,?,?*(1.45/25.5),?*(1.45/46.7),?*(0.07),?*(0.8),?*(1),?*(1),?/39,?,?,?,?,?,?)', ["Reflex", timestampStr, code, "YOUNGER BOYS SLIPPER", qty, delivery, qty, qty, qty, qty, qty, qty, qty, size34, size56, size78, size910, size1112, size131])
        # 3mm Ribbon
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(0.07), LastRec=? WHERE ItemCode=?', (qty, timestampStr, "RIB0001",))
        # Soles
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size34, timestampStr, sole))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size56, timestampStr, sole1))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size78, timestampStr, sole2))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size910, timestampStr, sole3))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size1112, timestampStr, sole4))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size131, timestampStr, sole5))
        # Gusset Elastic
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1), LastRec=? WHERE ItemCode=?', (qty, timestampStr, "ELA0008",))
        # Cartons - Check Cartons packed
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?/30, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "CAR0010",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?/30, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "CAR0010",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?/30, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "CAR0010",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?/48, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "CAR0010",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?/48, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "CAR0010",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?/48, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "CAR0010",))
        # Made In Lesotho Label
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "LAB0002",))
        # 25mm Tag Pin
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "PIN0001",))
        # Polybag
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "BAG0003",))
        # Hanger Sticker
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (size34, timestampStr, "STI0074",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (size56, timestampStr, "STI0076",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (size78, timestampStr, "STI0078",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (size910, timestampStr, "STI0080",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (size1112, timestampStr, "STI0082",))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (size131, timestampStr, "STI0084",))
        # Hanger
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "HAN0002",))


        updated = cursor.rowcount
        conn.commit()
        cursor.close()
        root.destroy()
        sys.exit(updated)  # return value whether record has been updated

    with sqlite3.connect('Log Sheets.sql3') as conn2:
        cursor2 = conn2.cursor()
        code = OrderNo.get()
        barcode = OrderNo.get()
        size34 = Size34.get()
        size56 = Size56.get()
        size78 = Size78.get()
        size910 = Size910.get()
        size1112 = Size1112.get()
        size131 = Size131.get()
        delivery = Delivery.get()
        qty = Quantity.get()
        cursor2.execute('CREATE TABLE IF NOT EXISTS [%s] (Barcode,OrderNo,Style,Delivery,Size34,Size56,Size78,Size910,Size1112,Size131,Qty,Ticket)' %code)
        cursor2.execute(r'INSERT INTO [%s] (Barcode,OrderNo,Style,Delivery,Size34,Size56,Size78,Size910,Size1112,Size131,Qty,Ticket) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)' %code, [ barcode, code, "YOUNGER BOYS SLIPPER", delivery, size34, size56, size78, size910, size1112, size131, qty, 158])
        updated = cursor2.rowcount
        conn2.commit()
        cursor2.close()
        root.destroy()
        sys.exit(updated)

label_0 = Label(root, text="YOUNGER BOYS SLIPPER", width=39,  relief='raised', background="lightskyblue3", font=("bold", 20), anchor=CENTER).place(x=10, y=23)

label_on = Label(root, text="Order No:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=180, y=90)
entry_on = Entry(root, textvar=OrderNo, background="", font=("bold", 10)).place(x=300, y=90)

label_2 = Label(root, text="Delivery Date:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=180, y=120)
entry_2 = Entry(root, textvar=Delivery, background="", font=("bold", 10)).place(x=300, y=120)

label_yb1 = Label(root, text="Size 3/4:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=180)
entry_yb1 = Entry(root, textvar=Size34, background="", font=("bold", 10)).place(x=160, y=180)

label_yb1 = Label(root, text="Size 5/6:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=210)
entry_yb1 = Entry(root, textvar=Size56, background="", font=("bold", 10)).place(x=160, y=210)

label_yb2 = Label(root, text="Size 7/8:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=240)
entry_yb2 = Entry(root, textvar=Size78, background="", font=("bold", 10)).place(x=160, y=240)

label_yb3 = Label(root, text="Size 9/10:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=270)
entry_yb3 = Entry(root, textvar=Size910, background="", font=("bold", 10)).place(x=160, y=270)

label_yb3 = Label(root, text="Size 11/12:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=300)
entry_yb3 = Entry(root, textvar=Size1112, background="", font=("bold", 10)).place(x=160, y=300)

label_yb3 = Label(root, text="Size 13/1:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=330)
entry_yb3 = Entry(root, textvar=Size131, background="", font=("bold", 10)).place(x=160, y=330)

label_yb4 = Label(root, text="Total Quantity:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=360)
entry_yb4 = Entry(root, textvar=Quantity, background="", font=("bold", 10)).place(x=160, y=360)

label_yb34 = Label(root, text="Soles:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=320, y=180)
option_soles = OptionMenu(root, soles, *soles_list).place(x=370, y=180)

option_soles1 = OptionMenu(root, soles1, *soles1_list).place(x=370, y=210)

# label_yb10 = Label(root, text="Soles 7/8:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=40, y=510)
option_soles2 = OptionMenu(root, soles2, *soles2_list).place(x=370, y=240)

# label_yb10 = Label(root, text="Soles 9/10:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=40, y=540)
option_soles23= OptionMenu(root, soles3, *soles3_list).place(x=370, y=270)

# label_yb10 = Label(root, text="Soles 11/12:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=40, y=570)
option_soles23= OptionMenu(root, soles4, *soles4_list).place(x=370, y=300)

# label_yb10 = Label(root, text="Soles 13/1:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=40, y=600)
option_soles23= OptionMenu(root, soles5, *soles5_list).place(x=370, y=330)

# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'), relief="raised", foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'), relief="raised", foreground='blue')

# Inserting buttons
submit1 = Button(root, text='Submit', style='S.TButton', width=11, command=young_boys_slipper).place(x=60, y=520)
exit1 = Button(root, text='Close', style='C.TButton', width=11, command=root.destroy).place(x=440, y=520)

root.mainloop()
