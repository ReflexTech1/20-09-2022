from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
from datetime import datetime
from tkinter import messagebox

root = Tk()
root.geometry('600x490')
root.title("New ML Slipper Order")
root.config(bg="lightskyblue3")
style = ttk.Style()

OrderNo = StringVar()
Size23 = IntVar()
Size45 = IntVar()
Quantity = IntVar()
Delivery = StringVar()

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y")


with sqlite3.connect('Reflex Footwear.sql3') as conn:
    cursor = conn.cursor()
    soles1_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%ML Soles Boys%%Size 2/3%'")
    soles1_list = [r for r, in soles1_data]
    soles1 = StringVar()
    soles1.set(soles1_list[0])

    soles2_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%ML Soles Boys%%Size 4/5%'")
    soles2_list = [r for r, in soles2_data]
    soles2 = StringVar()
    soles2.set(soles2_list[0])


def submit_root(e):
   command=boys_slipper()

root.bind('<Return>', lambda e: submit_root(e))


def boys_slipper():
    code = OrderNo.get()
    size23 = Size23.get()
    size45 = Size45.get()
    sole1 = soles1.get()
    sole2 = soles2.get()
    delivery = Delivery.get()
    qty = Quantity.get()

    if qty == sum([size23+size45]):
        with sqlite3.connect('Reflex Footwear.sql3') as conn:
            cursor = conn.cursor()
            # Insert into Orders
            cursor.execute(r'INSERT INTO MySlippers (Factory,Planned,OrderNo,Style,DeliveryDate,Quantity,Balances,Soles23,Soles45) VALUES(?,?,?,?,?,?,?,?,?)', [
                           "Reflex", timestampStr, code, "BOYS SLIPPER", delivery, qty, qty, size23, size45])
            # Insert into Production
            cursor.execute(r'INSERT INTO SlipProduction (Factory,Planned,Order2,Style,DelDate,Orderqty,Cutting,Assembly,Closing,Finishing,Despatch,ToShip,Shipped) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)', [
                           "Reflex", timestampStr, code, "BOYS SLIPPER", delivery, qty, qty, "0", "0", "0", "0", qty,"0"])
            # Insert into Production_Balances
            cursor.execute(r'INSERT INTO SlipProd_Balances (Factory,Planned,Order2,Style,DelDate,Orderqty,Cutting,Assembly,Closing,Finishing,Despatch,ToShip,Shipped) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)', [
                           "Reflex", timestampStr, code, "BOYS SLIPPER", delivery, qty, qty, qty, qty, qty, qty, qty, "0",])
            # Insert Into Planning
            cursor.execute(r'INSERT INTO PlanSlip (Factory,DatePlanned,OrderNo,Style,Pairs,Delivery,Size23,Size45) VALUES(?,?,?,?,?,?,?,?)', [
                           "Reflex", timestampStr, code, "BOYS SLIPPER", qty, delivery, size23, size45])
            # Insert Into Required
            cursor.execute(r'INSERT INTO SlipRequired (Factory,InputDate,OrderNo,Style,Pairs,DelDate,Upper,Sock,Ribbon,Elastic,Binding,Gusset,Cartons,MLSize2x3,MLSize4x5)'
                           ' VALUES(?,?,?,?,?,?,?*(1.45/16.5),?*(1.45/29),?*(0.075),?*(0.95),?*(1.3),?*(0.16),?/36,?,?)',
                           ["Reflex", timestampStr, code, "BOYS SLIPPER", qty, delivery, qty, qty, qty, qty, qty, qty, qty, size23, size45])
            # 3mm Ribbon
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(0.075), LastRec=? WHERE ItemCode=?', (qty, timestampStr, "RIB0001",))
            # Soles
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size23, timestampStr, sole1))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size45, timestampStr, sole2))
            # Gusset Elastic
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(0.16), LastRec=? WHERE ItemCode=?', (qty, timestampStr, "ELA0008",))
            # Cartons - Check Cartons packed
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?/36, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "CAR0010",))
            # Made In Lesotho Label
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "LAB0002",))
            # 25mm Tag Pin
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "PIN0001",))
            # Polybag
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "BAG0003",))
            # Hanger Sticker
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (size23, timestampStr, "STI0073",))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (size45, timestampStr, "STI0075",))
            # Hanger
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "HAN0002",))


            updated = cursor.rowcount
            conn.commit()
            cursor.close()

        with sqlite3.connect('Log Sheets.sql3') as conn2:
            cursor2 = conn2.cursor()
            code = OrderNo.get()
            barcode = OrderNo.get()
            size23 = Size23.get()
            size45 = Size45.get()
            delivery = Delivery.get()
            qty = Quantity.get()
            cursor2.execute('CREATE TABLE IF NOT EXISTS [%s] (Barcode,OrderNo,Style,Delivery,Size23,Size45,Qty,Ticket)' %code)
            cursor2.execute(r'INSERT INTO [%s] (Barcode,OrderNo,Style,Delivery,Size23,Size45,Qty,Ticket) VALUES(?,?,?,?,?,?,?,?)' %code, [ barcode, code, "BOYS SLIPPER", delivery, size23, size45, qty, 158])
            updated = cursor2.rowcount
            conn2.commit()
            cursor2.close()
            root.destroy()
            sys.exit(updated)  # return value whether record has been updated

    else:
        messagebox.showwarning(title="Confirmation", message="The Size Range Does Not Equal The Total.\nPlease Confirm Sizes and Total Again.")

label_0 = Label(root, text="BOYS SLIPPER", width=39,  relief='raised', background="lightskyblue3", font=("bold", 20), anchor=CENTER).place(x=5, y=23)

label_on = Label(root, text="Order No:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=200, y=90)
entry_on = Entry(root, textvar=OrderNo, background="", font=("bold", 10)).place(x=300, y=90)

label_2 = Label(root, text="Delivery Date:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=200, y=120)
entry_2 = Entry(root, textvar=Delivery, background="", font=("bold", 10)).place(x=300, y=120)

label_b1 = Label(root, text="Size 2/3:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=180)
entry_b1 = Entry(root, textvar=Size23, background="", font=("bold", 10)).place(x=140, y=180)

label_b2 = Label(root, text="Size 4/5:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=210)
entry_b2 = Entry(root, textvar=Size45, background="", font=("bold", 10)).place(x=140, y=210)

label_b3 = Label(root, text="Total Quantity:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=20, y=240)
entry_b3 = Entry(root, textvar=Quantity, background="", font=("bold", 10)).place(x=140, y=240)

label_b8 = Label(root, text="Soles:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=300, y=180)
option_soles = OptionMenu(root, soles1, *soles1_list).place(x=360, y=180)

# label_b9 = Label(root, text="Soles:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=320, y=210)
option_soles2 = OptionMenu(root, soles2, *soles2_list).place(x=360, y=210)

# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'), relief="raised", foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'), relief="raised", foreground='blue')

# Inserting buttons
submit1 = Button(root, text='Submit', style='S.TButton', width=11, command=boys_slipper).place(x=60, y=430)
exit1 = Button(root, text='Close', style='C.TButton', width=11, command=root.destroy).place(x=430, y=430)

root.mainloop()
