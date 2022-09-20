from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
from datetime import datetime

root = Tk()
root.geometry('650x670')
root.title("New SI Slipper Order")
root.config(bg="lightskyblue3")
style = ttk.Style()

OrderNo = StringVar()
Size4 = IntVar()
Size5 = IntVar()
Size6 = IntVar()
Size7 = IntVar()
Size8 = IntVar()
Size9 = IntVar()
Size10 = IntVar()
Size11 = IntVar()
Size12 = IntVar()
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

    soles1_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%MRP SI Soles%%Pre Size 4%'")
    soles1_list = [r for r, in soles1_data]
    soles1 = StringVar()
    soles1.set(soles1_list[0])

    soles2_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%MRP SI Soles%%Pre Size 5%'")
    soles2_list = [r for r, in soles2_data]
    soles2 = StringVar()
    soles2.set(soles2_list[0])

    soles3_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%MRP SI Soles%%Pre Size 6%'")
    soles3_list = [r for r, in soles3_data]
    soles3 = StringVar()
    soles3.set(soles3_list[0])

    soles4_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%MRP SI Soles%%Pre Size 7%'")
    soles4_list = [r for r, in soles4_data]
    soles4 = StringVar()
    soles4.set(soles4_list[0])

    soles5_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%MRP SI Soles%%Pre Size 8%'")
    soles5_list = [r for r, in soles5_data]
    soles5 = StringVar()
    soles5.set(soles5_list[0])

    soles6_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%MRP SI Soles%%Big Size 9%'")
    soles6_list = [r for r, in soles6_data]
    soles6 = StringVar()
    soles6.set(soles6_list[0])

    soles7_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%MRP SI Soles%%Big Size 10%'")
    soles7_list = [r for r, in soles7_data]
    soles7 = StringVar()
    soles7.set(soles7_list[0])

    soles8_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%MRP SI Soles%%Big Size 11%'")
    soles8_list = [r for r, in soles8_data]
    soles8 = StringVar()
    soles8.set(soles8_list[0])

    soles9_data = cursor.execute("SELECT Description FROM StockSheet WHERE Description LIKE '%MRP SI Soles%%Big Size 12%'")
    soles9_list = [r for r, in soles9_data]
    soles9 = StringVar()
    soles9.set(soles9_list[0])


def submit_root(e):
   command=si_sml_slipper()

root.bind('<Return>', lambda e: submit_root(e))


def si_sml_slipper():
    code = OrderNo.get()
    size4 = Size4.get()
    size5 = Size5.get()
    size6 = Size6.get()
    size7 = Size7.get()
    size8 = Size8.get()
    size9 = Size9.get()
    size10 = Size10.get()
    size11 = Size11.get()
    size12 = Size12.get()
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
    sole7 = soles7.get()
    sole8 = soles8.get()
    sole9 = soles9.get()
    delivery = Delivery.get()
    qty = Quantity.get()

    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        cursor = conn.cursor()
        # Insert into Orders
        cursor.execute(r'INSERT INTO MySlippers (Factory,Planned,OrderNo,Style,DeliveryDate,Quantity,Balances,Binding,Elastic,Material,Sock,SISoles4,SISoles5,SISoles6,SISoles7,SISoles8,SISoles9,SISoles10,SISoles11,SISoles12) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', [
                       "Reflex", timestampStr, code, "SI SMALL SLIPPER", delivery, qty, qty, bind, elast, material, sock, size4, size5, size6, size7, size8, size9, size10, size11, size12])
        # Insert into Production
        cursor.execute(r'INSERT INTO SlipProduction (Factory,Planned,Order2,Style,DelDate,Orderqty,Clicking,Closing,Finishing,Despatch,ToShip) VALUES(?,?,?,?,?,?,?,?,?,?,?)', [
                       "Reflex", timestampStr, code, "SI SMALL SLIPPER", delivery, qty, qty, "0", "0", "0", qty])
        # Insert Into Planning
        cursor.execute(r'INSERT INTO PlanSlip (Factory,DatePlanned,OrderNo,Style,Pairs,Delivery,SISoles4,SISoles5,SISoles6,SISoles7,SISoles8,SISoles9,SISoles10,SISoles11,SISoles12) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', ["Reflex", timestampStr, code, "SI SMALL SLIPPER", qty, delivery, size4, size5, size6, size7, size8, size9, size10, size11, size12])
        # Insert Into Required
        cursor.execute(r'INSERT INTO SlipRequired (Factory,InputDate,OrderNo,Style,Pairs,DelDate,Upper,Sock,Ribbon,Elastic,Binding,Gusset,SISoles4,SISoles5,SISoles6,SISoles7,SISoles8,SISoles9,SISoles10,SISoles11,SISoles12)'
                       ' VALUES(?,?,?,?,?,?,?*(1.45/25),?*(1.45/46),?*(0.065),?*(0.73),?*(1.1),?*(0.16),?,?,?,?,?,?,?,?,?)', ["Reflex", timestampStr, code, "SI SMALL SLIPPER", qty, delivery, qty, qty, qty, qty, qty, qty, size4, size5, size6, size7, size8, size9, size10, size11, size12])
        # Upper Material - Average of PB and TB
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1.45/25), LastRec=? WHERE Description=?', (qty, timestampStr, material))
        # Binding
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1.1), LastRec=? WHERE Description=?', (qty, timestampStr, bind))
        # Elastic
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(0.73), LastRec=? WHERE Description=?', (qty, timestampStr, elast))
        # Sock Material
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(1.45/46), LastRec=? WHERE Description=?', (qty, timestampStr, sock))
        # 3mm Ribbon
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(0.065), LastRec=? WHERE ItemCode=?', (qty, timestampStr, "RIB0001",))
        # Soles
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size4, timestampStr, sole1))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size5, timestampStr, sole2))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size6, timestampStr, sole3))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size7, timestampStr, sole4))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size8, timestampStr, sole5))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size9, timestampStr, sole6))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size10, timestampStr, sole7))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size11, timestampStr, sole8))
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=?', (size12, timestampStr, sole9))
        # Gusset Elastic
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?*(0.16), LastRec=? WHERE ItemCode=?', (qty, timestampStr, "ELA0008",))
        # Cartons - Pre-Pack
        # Made In Lesotho Label
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "LAB0002",))
        # 25mm Tag Pin
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "PIN0001",))
        # Polybag
        cursor.execute(r'UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE ItemCode=?', (qty, timestampStr, "BAG0003",))
        # Size Labels
        cursor.execute(r"UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=? AND ItemCode=?", (size4, timestampStr,sole1, "MLP0001"))
        cursor.execute(r"UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=? AND ItemCode=?", (size5, timestampStr,sole1, "MLP0002"))
        cursor.execute(r"UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=? AND ItemCode=?", (size6, timestampStr,sole1, "MLP0003"))
        cursor.execute(r"UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=? AND ItemCode=?", (size7, timestampStr,sole1, "MLP0004"))
        cursor.execute(r"UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=? AND ItemCode=?", (size8, timestampStr,sole1, "MLP0005"))
        cursor.execute(r"UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=? AND ItemCode=?", (size9, timestampStr,sole1, "MLP0006"))
        cursor.execute(r"UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=? AND ItemCode=?", (size10, timestampStr,sole1, "MLP0007"))
        cursor.execute(r"UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=? AND ItemCode=?", (size11, timestampStr,sole1, "MLP0008"))
        cursor.execute(r"UPDATE StockSheet SET Quantity=Quantity-?, LastRec=? WHERE Description=? AND ItemCode=?", (size12, timestampStr,sole1, "MLP0009"))

        updated = cursor.rowcount
        conn.commit()
        cursor.close()
        root.destroy()
        sys.exit(updated)  # return value whether record has been updated


label_0 = Label(root, text="Mr. Price SMALL SLIPPER", width=40, background="lightskyblue3", relief='raised', font=("bold", 20), anchor=CENTER).place(x=24, y=23)

label_on = Label(root, text="Order No:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=200, y=90)
entry_on = Entry(root, textvar=OrderNo, background="", font=("bold", 10)).place(x=320, y=90)

label_2 = Label(root, text="Delivery Date:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=200, y=120)
entry_2 = Entry(root, textvar=Delivery, background="", font=("bold", 10)).place(x=320, y=120)

label_si1 = Label(root, text="Size 4:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=40, y=180)
entry_si1 = Entry(root, textvar=Size4, background="", font=("bold", 10)).place(x=160, y=180)

label_si2 = Label(root, text="Size 5:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=40, y=210)
entry_si2 = Entry(root, textvar=Size5, background="", font=("bold", 10)).place(x=160, y=210)

label_si3 = Label(root, text="Size 6:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=40, y=240)
entry_si3 = Entry(root, textvar=Size6, background="", font=("bold", 10)).place(x=160, y=240)

label_si4 = Label(root, text="Size 7:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=40, y=270)
entry_si4 = Entry(root, textvar=Size7, background="", font=("bold", 10)).place(x=160, y=270)

label_si5 = Label(root, text="Size 8:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=40, y=300)
entry_si5 = Entry(root, textvar=Size8, background="", font=("bold", 10)).place(x=160, y=300)

label_si6 = Label(root, text="Size 9:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=40, y=330)
entry_si6 = Entry(root, textvar=Size9, background="", font=("bold", 10)).place(x=160, y=330)

label_si7 = Label(root, text="Size 10:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=40, y=360)
entry_si7 = Entry(root, textvar=Size10, background="", font=("bold", 10)).place(x=160, y=360)

label_si8 = Label(root, text="Size 11:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=40, y=390)
entry_si8 = Entry(root, textvar=Size11, background="", font=("bold", 10)).place(x=160, y=390)

label_si9 = Label(root, text="Size 12:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=40, y=420)
entry_si9 = Entry(root, textvar=Size12, background="", font=("bold", 10)).place(x=160, y=420)

label_si10 = Label(root, text="Total Quantity:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=40, y=450)
entry_si10 = Entry(root, textvar=Quantity, background="", font=("bold", 10)).place(x=160, y=450)

label_si11 = Label(root, text="Binding:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=40, y=480)
option_upper = OptionMenu(root, binding, *binding_list).place(x=160, y=480)

label_si12 = Label(root, text="Elastic:", width=30, background="lightskyblue3", font=("bold", 11)).place(x=40, y=510)
option_upper = OptionMenu(root, elastic, *elastic_list).place(x=160, y=510)

label_si13 = Label(root, text="1-Tone Upper:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=40, y=540)
option_upper = OptionMenu(root, upper, *upper_list).place(x=160, y=540)

label_si14 = Label(root, text="Sock:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=40, y=570)
option_upper = OptionMenu(root, sockm, *sockm_list).place(x=160, y=570)

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

# label_si21 = Label(root, text="Soles:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=320, y=360)
option_soles10= OptionMenu(root, soles7, *soles7_list).place(x=420, y=360)

# label_si22 = Label(root, text="Soles:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=320, y=390)
option_soles11= OptionMenu(root, soles8, *soles8_list).place(x=420, y=390)

# label_si23 = Label(root, text="Soles:", width=20, background="lightskyblue3", font=("bold", 11)).place(x=320, y=420)
option_soles12= OptionMenu(root, soles9, *soles9_list).place(x=420, y=420)

# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'), relief="raised", foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'), relief="raised", foreground='blue')

# Inserting buttons
submit1 = Button(root, text='Submit', style='S.TButton', width=11, command=si_sml_slipper).place(x=20, y=610)
exit1 = Button(root, text='Close', style='C.TButton', width=11, command=root.destroy).place(x=520, y=610)

root.mainloop()
