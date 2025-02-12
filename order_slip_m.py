from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
from datetime import datetime
from tkinter import messagebox

root = Tk()
root.geometry('610x500')
root.title("New ML Slipper Order")
root.config(bg="lightskyblue3")
style = ttk.Style()

OrderNo = StringVar()
Size67 = IntVar()
Size89 = IntVar()
Size1011 = IntVar()
Quantity = IntVar()
Delivery = StringVar()

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y")

with sqlite3.connect('Reflex Footwear.sql3') as conn:
    cursor = conn.cursor()
    material_data = cursor.execute("SELECT Description FROM StockSheet WHERE Category=?", ("STOKIEM",))
    upper_list = [r for r, in material_data]
    upper = StringVar()
    upper.set(upper_list[0])

    soles1_data = cursor.execute(r"SELECT Description FROM StockSheet WHERE Description LIKE '%ML Soles Mens%%6/7%'")
    soles1_list = [r for r, in soles1_data]
    soles1 = StringVar()
    soles1.set(soles1_list[0])

    soles2_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%ML Soles Mens%%8/9%'")
    soles2_list = [r for r, in soles2_data]
    soles2 = StringVar()
    soles2.set(soles2_list[0])

    soles3_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%ML Soles Mens%%10/11%'")
    soles3_list = [r for r, in soles3_data]
    soles3 = StringVar()
    soles3.set(soles3_list[0])


def submit_root(e):
   command=mens_slipper()

root.bind('<Return>', lambda e: submit_root(e))


def mens_slipper():
    code = OrderNo.get()
    size67 = Size67.get()
    size89 = Size89.get()
    size1011 = Size1011.get()
    sole1 = soles1.get()
    sole2 = soles2.get()
    sole3 = soles3.get()
    delivery = Delivery.get()
    qty = Quantity.get()

    if qty == sum([size67+size89+size1011]):
        with sqlite3.connect('Reflex Footwear.sql3') as conn:
            cursor = conn.cursor()
            # Insert into Orders
            cursor.execute(r'INSERT INTO MySlippers (Factory,Planned,OrderNo,Style,DeliveryDate,Quantity,Balances,Soles67,Soles89,Soles1011) VALUES(?,?,?,?,?,?,?,?,?,?)', [
                           "Reflex", timestampStr, code, "MENS SLIPPER", delivery, qty, qty, size67, size89, size1011])
            # Insert into Production
            cursor.execute(r'INSERT INTO SlipProduction (Factory,Planned,Order2,Style,DelDate,Orderqty,Cutting,Assembly,Closing,Finishing,Despatch,ToShip,Shipped) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', [
                           "Reflex", timestampStr, code, "MENS SLIPPER", delivery, qty, qty, "0", "0", "0", "0", qty])
            # Insert into Production_Balances
            cursor.execute(r'INSERT INTO SlipProd_Balances (Factory,Planned,Order2,Style,DelDate,Orderqty,Cutting,Assembly,Closing,Finishing,Despatch,ToShip,Shipped) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)', [
                           "Reflex", timestampStr, code, "MENS SLIPPER", delivery, qty, qty, qty, qty, qty, qty, qty, "0",])
            # Insert Into Planning
            cursor.execute(r'INSERT INTO PlanSlip (Factory,DatePlanned,OrderNo,Style,Pairs,Delivery,Size67,Size89,Size1011) VALUES(?,?,?,?,?,?,?,?,?)', ["Reflex", timestampStr, code, "MENS SLIPPER", qty, delivery, size67, size89, size1011])
            # Insert Into Required
            cursor.execute(r'INSERT INTO SlipRequired (Factory,InputDate,OrderNo,Style,Pairs,DelDate,Upper,Sock,Ribbon,Elastic,Binding,Gusset,Cartons,MLSize6x7,MLSize8x9,MLSize10x11)'
                           ' VALUES(?,?,?,?,?,?,?*(1.45/12),?*(1.45/20.4),?*(0.087),?*(1.08),?*(1.5),?*(0.16),?/12,?,?,?)',
                           ["Reflex", timestampStr, code, "MENS SLIPPER", qty, delivery, qty, qty, qty, qty, qty, qty, qty, size67, size89, size1011])
            # 3mm Ribbon
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(0.087), LastRec=? WHERE ItemCode=?', (qty, timestampStr, "RIB0001",))
            # Soles
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size67, timestampStr, sole1))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size89, timestampStr, sole2))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size1011, timestampStr, sole3))
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
            # Hanger Sticker
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (size67, timestampStr, "STI0077",))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (size89, timestampStr, "STI0079",))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (size1011, timestampStr, "STI0081",))
            # Hanger
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "HAN0001",))


            updated = cursor.rowcount
            conn.commit()
            cursor.close()

        with sqlite3.connect('Log Sheets.sql3') as conn2:
            cursor2 = conn2.cursor()
            code = OrderNo.get()
            barcode = OrderNo.get()
            size67 = Size67.get()
            size89 = Size89.get()
            size1011 = Size1011.get()
            delivery = Delivery.get()
            qty = Quantity.get()
            cursor2.execute('CREATE TABLE IF NOT EXISTS [%s] (Barcode,OrderNo,Style,Delivery,Size67,Size89,Size1011,Qty,Ticket)' %code)
            cursor2.execute(r'INSERT INTO [%s] (Barcode,OrderNo,Style,Delivery,Size67,Size89,Size1011,Qty,Ticket) VALUES(?,?,?,?,?,?,?,?,?)' %code, [ barcode, code, "MENS SLIPPER",delivery, size67, size89, size1011, qty, 158])
            updated = cursor2.rowcount
            conn2.commit()
            cursor2.close()
            root.destroy()
            sys.exit(updated)  # return value whether record has been updated

    else:
        messagebox.showwarning(title="Confirmation", message="The Size Range Does Not Equal The Total.\nPlease Confirm Sizes and Total Again.")

label_0 = Label(root, text="MENS ML", width=39,  relief='raised', background="lightskyblue3", font=("bold", 20), anchor=CENTER).place(x=10, y=23)

label_on = Label(root, text="Order No:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=180, y=90)
entry_on = Entry(root, textvar=OrderNo, background="", font=("bold", 10)).place(x=300, y=90)

label_2 = Label(root, text="Delivery Date:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=180, y=120)
entry_2 = Entry(root, textvar=Delivery, background="", font=("bold", 10)).place(x=300, y=120)

label_m1 = Label(root, text="Size 6/7:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=180)
entry_m1 = Entry(root, textvar=Size67, background="", font=("bold", 10)).place(x=140, y=180)

label_m2 = Label(root, text="Size 8/9:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=210)
entry_m2 = Entry(root, textvar=Size89, background="", font=("bold", 10)).place(x=140, y=210)

label_m3 = Label(root, text="Size 10/11:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=240)
entry_m3 = Entry(root, textvar=Size1011, background="", font=("bold", 10)).place(x=140, y=240)

label_m4 = Label(root, text="Total Quantity:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=270)
entry_m4 = Entry(root, textvar=Quantity, background="", font=("bold", 10)).place(x=140, y=270)

label_m9 = Label(root, text="Soles:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=300, y=180)
option_soles = OptionMenu(root, soles1, *soles1_list).place(x=360, y=180)

# label_m10 = Label(root, text="Soles:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=40, y=450)
option_soles2 = OptionMenu(root, soles2, *soles2_list).place(x=360, y=210)

# label_m10 = Label(root, text="Soles:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=40, y=480)
option_soles23= OptionMenu(root, soles3, *soles3_list).place(x=360, y=240)


# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'), relief="raised", foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'), relief="raised", foreground='blue')

# Inserting buttons
submit1 = Button(root, text='Submit', style='S.TButton', width=11, command=mens_slipper).place(x=60, y=450)
exit1 = Button(root, text='Close', style='C.TButton', width=11, command=root.destroy).place(x=450, y=450)

root.mainloop()
