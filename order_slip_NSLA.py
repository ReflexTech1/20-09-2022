from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
from datetime import datetime
from tkinter import messagebox

root = Tk()
root.geometry('650x600')
root.title("New Closed Toe (NSLA) Order")
root.config(bg="lightskyblue3")
style = ttk.Style()

OrderNo = StringVar()
Size34 = IntVar()
Size56 = IntVar()
Size78 = IntVar()
Quantity = IntVar()
Delivery = StringVar()

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y")

with sqlite3.connect('Reflex Footwear.sql3') as conn:
    cursor = conn.cursor()
    soles1_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%NSLA Ladies%%Size 3/4%'")
    soles1_list = [r for r, in soles1_data]
    soles1 = StringVar()
    soles1.set(soles1_list[0])

    soles2_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%NSLA Ladies%%Size 5/6%'")
    soles2_list = [r for r, in soles2_data]
    soles2 = StringVar()
    soles2.set(soles2_list[0])

    soles3_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%NSLA Ladies%%Size 7/8%'")
    soles3_list = [r for r, in soles3_data]
    soles3 = StringVar()
    soles3.set(soles3_list[0])


def submit_root(e):
   command=nsme_slipper()

root.bind('<Return>', lambda e: submit_root(e))


def nsme_slipper():
    code = OrderNo.get()
    size34 = Size34.get()
    size56 = Size56.get()
    size78 = Size78.get()
    sole1 = soles1.get()
    sole2 = soles2.get()
    sole3 = soles3.get()
    delivery = Delivery.get()
    qty = Quantity.get()

    if qty == sum([size34+size56+size78]):
        with sqlite3.connect('Reflex Footwear.sql3') as conn:
            cursor = conn.cursor()
            # Insert into Orders
            cursor.execute(r'INSERT INTO MySlippers (Factory,Planned,OrderNo,Style,DeliveryDate,Quantity,Balances,NSLASoles34,NSLASoles56,NSLASoles78) VALUES(?,?,?,?,?,?,?,?,?,?)', [
                           "Reflex", timestampStr, code, "NSLA SLIPPER", delivery, qty, qty, size34, size56, size78])
            # Insert into Production
            cursor.execute(r'INSERT INTO SlipProduction (Factory,Planned,Order2,Style,DelDate,Orderqty,Cutting,Assembly,Closing,Finishing,Despatch,ToShip,Shipped) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)', [
                           "Reflex", timestampStr, code, "NSLA SLIPPER", delivery, qty, qty, "0", "0", "0", "0", qty, "0",])
            # Insert Into Planning
            cursor.execute(r'INSERT INTO PlanSlip (Factory,DatePlanned,OrderNo,Style,Pairs,Delivery,NSLASoles34,NSLASoles56,NSLASoles78) VALUES(?,?,?,?,?,?,?,?,?)', ["Reflex", timestampStr, code, "NSLA SLIPPER", qty, delivery,size34, size56, size78])
            # Insert Into Required
            cursor.execute(r'INSERT INTO SlipRequired (Factory,InputDate,OrderNo,Style,Pairs,DelDate,Upper,Sock,Ribbon,Binding,Gusset,NSLASoles34,NSLASoles56,NSLASoles78)'
                           ' VALUES(?,?,?,?,?,?,?*(1.45/25),?*(1.45/20.4),?*(0.055),?*(1.1),?*(0.16),?,?,?)', ["Reflex", timestampStr, code, "NSLA SLIPPER", qty, delivery, qty, qty, qty, qty, qty, size34, size56, size78])
            # Insert into Production_Balances
            cursor.execute(r'INSERT INTO SlipProd_Balances (Factory,Planned,Order2,Style,DelDate,Orderqty,Cutting,Assembly,Closing,Finishing,Despatch,ToShip,Shipped) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)', [
                           "Reflex", timestampStr, code, "NSLA SLIPPER", delivery, qty, qty, qty, qty, qty,qty, qty, "0",])
            # 3mm Ribbon
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(0.055), LastRec=? WHERE ItemCode=?', (qty, timestampStr, "RIB0001",))
            # Soles
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size34, timestampStr, sole1))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size56, timestampStr, sole2))
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size78, timestampStr, sole3))
            # Gusset Elastic
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(0.16), LastRec=? WHERE ItemCode=?', (qty, timestampStr, "ELA0008",))
            # 25mm Tag Pin
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "PIN0001",))
            # Polybag
            cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "BAG0003",))

            updated = cursor.rowcount
            conn.commit()
            cursor.close()
            root.destroy()
            sys.exit(updated)  # return value whether record has been updated

    else:
        messagebox.showwarning(title="Confirmation", message="The Size Range Does Not Equal The Total.\nPlease Confirm Sizes and Total Again.")

label_0 = Label(root, text="CLOSED TOE NSLA SLIPPER", width=40, background="lightskyblue3", relief='raised', font=("bold", 20), anchor=CENTER).place(x=24, y=23)

label_on = Label(root, text="Order No:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=200, y=90)
entry_on = Entry(root, textvar=OrderNo, background="", font=("bold", 10)).place(x=320, y=90)

label_2 = Label(root, text="Delivery Date:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=200, y=120)
entry_2 = Entry(root, textvar=Delivery, background="", font=("bold", 10)).place(x=320, y=120)

label_si3 = Label(root, text="Size 3/4:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=40, y=180)
entry_si3 = Entry(root, textvar=Size34, background="", font=("bold", 10)).place(x=160, y=180)

label_si4 = Label(root, text="Size 5/6:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=40, y=210)
entry_si4 = Entry(root, textvar=Size56, background="", font=("bold", 10)).place(x=160, y=210)

label_si5 = Label(root, text="Size 7/8:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=40, y=240)
entry_si5 = Entry(root, textvar=Size78, background="", font=("bold", 10)).place(x=160, y=240)

label_si10 = Label(root, text="Total Quantity:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=40, y=360)
entry_si10 = Entry(root, textvar=Quantity, background="", font=("bold", 10)).place(x=160, y=360)

label_si15 = Label(root, text="Soles:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=320, y=180)
option_soles4 = OptionMenu(root, soles1, *soles1_list).place(x=420, y=180)

# label_si16 = Label(root, text="Soles:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=320, y=210)
option_soles5 = OptionMenu(root, soles2, *soles2_list).place(x=420, y=210)

# label_si17 = Label(root, text="Soles:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=320, y=240)
option_soles6= OptionMenu(root, soles3, *soles3_list).place(x=420, y=240)

# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'), relief="raised", foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'), relief="raised", foreground='blue')

# Inserting buttons
submit1 = Button(root, text='Submit', style='S.TButton', width=11, command=nsme_slipper).place(x=20, y=550)
exit1 = Button(root, text='Close', style='C.TButton', width=11, command=root.destroy).place(x=520, y=550)

root.mainloop()
