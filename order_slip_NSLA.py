from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
from datetime import datetime

root = Tk()
root.geometry('650x600')
root.title("New Closed Toe (NSLA) Order")
root.config(bg="lightskyblue3")
style = ttk.Style()

OrderNo = StringVar()
Size6 = IntVar()
Size7 = IntVar()
Size8 = IntVar()
Size9 = IntVar()
Size10 = IntVar()
Size11 = IntVar()
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

    sockm_data = cursor.execute("SELECT Description FROM StockSheet WHERE Category=?", ("STOKIEM",))
    sockm_list = [r for r, in sockm_data]
    sockm = StringVar()
    sockm.set(sockm_list[0])

    binding_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%16mm%%Binding%'")
    binding_list = [r for r, in binding_data]
    binding = StringVar()
    binding.set(binding_list[0])

    elastic_data = cursor.execute("SELECT Description FROM StockSheet WHERE Category=?", ("ELASTIC",))
    elastic_list = [r for r, in elastic_data]
    elastic = StringVar()
    elastic.set(elastic_list[0])

    soles1_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%NSME Mens Soles%%Size 6%'")
    soles1_list = [r for r, in soles1_data]
    soles1 = StringVar()
    soles1.set(soles1_list[0])

    soles2_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%NSME Mens Soles%%Size 7%'")
    soles2_list = [r for r, in soles2_data]
    soles2 = StringVar()
    soles2.set(soles2_list[0])

    soles3_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%NSME Mens Soles%%Size 8%'")
    soles3_list = [r for r, in soles3_data]
    soles3 = StringVar()
    soles3.set(soles3_list[0])

    soles4_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%NSME Mens Soles%%Size 9%'")
    soles4_list = [r for r, in soles4_data]
    soles4 = StringVar()
    soles4.set(soles4_list[0])

    soles5_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%NSME Mens Soles%%Size 10%'")
    soles5_list = [r for r, in soles5_data]
    soles5 = StringVar()
    soles5.set(soles5_list[0])

    soles6_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%NSME Mens Soles%%Size 11%'")
    soles6_list = [r for r, in soles6_data]
    soles6 = StringVar()
    soles6.set(soles6_list[0])


def submit_root(e):
   command=nsme_slipper()

root.bind('<Return>', lambda e: submit_root(e))


def nsme_slipper():
    code = OrderNo.get()
    size6 = Size6.get()
    size7 = Size7.get()
    size8 = Size8.get()
    size9 = Size9.get()
    size10 = Size10.get()
    size11 = Size11.get()
    bind = binding.get()
    elast = elastic.get()
    material = upper.get()
    sock = sockm.get()
    vamp = upper.get()
    quarter = upper.get()
    sole1 = soles1.get()
    sole2 = soles2.get()
    sole3 = soles3.get()
    sole4 = soles4.get()
    sole5 = soles5.get()
    sole6 = soles6.get()
    delivery = Delivery.get()
    qty = Quantity.get()

    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        cursor = conn.cursor()
        # Insert into Orders
        cursor.execute(r'INSERT INTO MySlippers (Factory,Planned,OrderNo,Style,DeliveryDate,Quantity,Balances,Binding,Elastic,Material,Sock,NSMESoles6,NSMESoles7,NSMESoles8,NSMESoles9,NSMESoles10,NSMESoles11) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', [
                       "Reflex", timestampStr, code, "NSLA SLIPPER", delivery, qty, qty, bind, elast, material,sock,size6, size7, size8, size9, size10, size11])
        # Insert into Production
        cursor.execute(r'INSERT INTO SlipProduction (Factory,Planned,Order2,Style,DelDate,Orderqty,Clicking,Closing,Finishing,Despatch,Warehouse,ToShip,Shipped) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)', [
                       "Reflex", timestampStr, code, "NSLA SLIPPER", delivery, qty, qty, "0", "0", "0", "0", qty, "0",])
        # Insert Into Planning
        cursor.execute(r'INSERT INTO PlanSlip (Factory,DatePlanned,OrderNo,Style,Pairs,Delivery,NSMESoles6,NSMESoles7,NSMESoles8,NSMESoles9,NSMESoles10,NSMESoles11) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', ["Reflex", timestampStr, code, "NSLA SLIPPER", qty, delivery,size6, size7, size8, size9, size10, size11])
        # Insert Into Required
        cursor.execute(r'INSERT INTO SlipRequired (Factory,InputDate,OrderNo,Style,Pairs,DelDate,Upper,Sock,Ribbon,Binding,Gusset,NSMESoles6,NSMESoles7,NSMESoles8,NSMESoles9,NSMESoles10,NSMESoles11)'
                       ' VALUES(?,?,?,?,?,?,?*(1.45/25),?*(1.45/20.4),?*(0.055),?*(1.1),?*(0.16),?,?,?,?,?,?)', ["Reflex", timestampStr, code, "NSLA SLIPPER", qty, delivery, qty, qty, qty, qty, qty, size6, size7, size8, size9, size10, size11])
        # Upper Material
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1.45/25), LastRec=? WHERE Description=?', (qty, timestampStr, material))
        # Binding
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1.5), LastRec=? WHERE Description=?', (qty, timestampStr, bind))
        # Sock Material
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1.45/20.4), LastRec=? WHERE Description=?', (qty, timestampStr, sock))
        # 3mm Ribbon
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(0.055), LastRec=? WHERE ItemCode=?', (qty, timestampStr, "RIB0001",))
        # Soles
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size6, timestampStr, sole1))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size7, timestampStr, sole2))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size8, timestampStr, sole3))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size9, timestampStr, sole4))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size10, timestampStr, sole5))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size11, timestampStr, sole6))
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


label_0 = Label(root, text="CLOSED TOE NSLA SLIPPER", width=40, background="lightskyblue3", relief='raised', font=("bold", 20), anchor=CENTER).place(x=24, y=23)

label_on = Label(root, text="Order No:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=200, y=90)
entry_on = Entry(root, textvar=OrderNo, background="", font=("bold", 10)).place(x=320, y=90)

label_2 = Label(root, text="Delivery Date:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=200, y=120)
entry_2 = Entry(root, textvar=Delivery, background="", font=("bold", 10)).place(x=320, y=120)

label_si3 = Label(root, text="Size 6:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=40, y=180)
entry_si3 = Entry(root, textvar=Size6, background="", font=("bold", 10)).place(x=160, y=180)

label_si4 = Label(root, text="Size 7:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=40, y=210)
entry_si4 = Entry(root, textvar=Size7, background="", font=("bold", 10)).place(x=160, y=210)

label_si5 = Label(root, text="Size 8:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=40, y=240)
entry_si5 = Entry(root, textvar=Size8, background="", font=("bold", 10)).place(x=160, y=240)

label_si6 = Label(root, text="Size 9:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=40, y=270)
entry_si6 = Entry(root, textvar=Size9, background="", font=("bold", 10)).place(x=160, y=270)

label_si7 = Label(root, text="Size 10:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=40, y=300)
entry_si7 = Entry(root, textvar=Size10, background="", font=("bold", 10)).place(x=160, y=300)

label_si8 = Label(root, text="Size 11:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=40, y=330)
entry_si8 = Entry(root, textvar=Size11, background="", font=("bold", 10)).place(x=160, y=330)

label_si10 = Label(root, text="Total Quantity:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=40, y=360)
entry_si10 = Entry(root, textvar=Quantity, background="", font=("bold", 10)).place(x=160, y=360)

label_si11 = Label(root, text="Binding:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=40, y=390)
option_upper = OptionMenu(root, binding, *binding_list).place(x=160, y=390)

label_si12 = Label(root, text="Elastic:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=40, y=420)
option_upper = OptionMenu(root, elastic, *elastic_list).place(x=160, y=420)

label_si13 = Label(root, text="1-Tone Upper:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=40, y=450)
option_upper = OptionMenu(root, upper, *upper_list).place(x=160, y=450)

label_si14 = Label(root, text="Sock:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=40, y=480)
option_upper = OptionMenu(root, sockm, *sockm_list).place(x=160, y=480)

label_si15 = Label(root, text="Soles:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=320, y=180)
option_soles4 = OptionMenu(root, soles1, *soles1_list).place(x=420, y=180)

# label_si16 = Label(root, text="Soles:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=320, y=210)
option_soles5 = OptionMenu(root, soles2, *soles2_list).place(x=420, y=210)

# label_si17 = Label(root, text="Soles:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=320, y=240)
option_soles6= OptionMenu(root, soles3, *soles3_list).place(x=420, y=240)

# label_si18 = Label(root, text="Soles:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=320, y=270)
option_soles7= OptionMenu(root, soles4, *soles4_list).place(x=420, y=270)

# label_si19 = Label(root, text="Soles:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=320, y=300)
option_soles8= OptionMenu(root, soles5, *soles5_list).place(x=420, y=300)

# label_si20 = Label(root, text="Soles:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=320, y=330)
option_soles9= OptionMenu(root, soles6, *soles6_list).place(x=420, y=330)

# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'), relief="raised", foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'), relief="raised", foreground='blue')

# Inserting buttons
submit1 = Button(root, text='Submit', style='S.TButton', width=11, command=nsme_slipper).place(x=20, y=550)
exit1 = Button(root, text='Close', style='C.TButton', width=11, command=root.destroy).place(x=520, y=550)

root.mainloop()
