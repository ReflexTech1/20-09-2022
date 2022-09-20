from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
import os
from datetime import datetime

root = Tk()
root.attributes('-fullscreen', True)
root.title("Sandals")
root.config(bg="skyblue3")

OrderNo = StringVar()
Quantity = IntVar()

dateTimeObj = datetime.now()

xstampStr = dateTimeObj.strftime("%H:%M:%S %p")
timestampStr = dateTimeObj.strftime("%d-%b-%Y")

l1 = Label(root, text="Sandal Orders In House", width=120, anchor=CENTER, font=["Bodoni MT", 30, "bold"], background="skyblue3", relief="raised").pack(side='top', ipady=10)

label_time = Label(root, text=xstampStr, width=11, anchor = CENTER, font=["Arial", 10, "bold"], background="skyblue3", relief="ridge")
label_time.pack(side='top', anchor = NE, ipady=5, ipadx=5)


def update_time():
    now = datetime.now()
    time_now = now.strftime("%H:%M:%S %p")
    label_time.config(text=time_now)
    root.after(1000, update_time)


#Bind keys
def close_screen(e):
	command=root.destroy()
root.bind('<Escape>', lambda e: close_screen(e))


def DblClick(event):
    curItem = tree.focus()
    order = tree.item(curItem)['values'][0]
    root2 = Tk()
    root2.geometry('800x700')
    root2.title("Order In House")
    root2.config(bg="skyblue2")
    style2 = ttk.Style()

    l1 = Label(root2, text="Order Details", width=80, anchor= CENTER, font=["Bodoni MT", 23, "bold"], background="skyblue3", relief="raised").pack(side='top', ipady=10)

    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT Planned,OrderNo,Style,DeliveryDate,Quantity,Soles3,Soles4,Soles5,Soles6,Soles7,Soles8,Material,Sock,Binding FROM MySANDALS WHERE OrderNo=?', (order,))
        results = cursor.fetchall()

        item_0_in_result = [_[0] for _ in results]
        item_0_in_result1 = [_[1] for _ in results]
        result_as_text2 = '\n'.join([x[2] for x in results])
        item_0_in_result3 = [_[3] for _ in results]
        item_0_in_result4 = [_[4] for _ in results]
        item_0_in_result5 = [_[5] for _ in results]
        item_0_in_result6 = [_[6] for _ in results]
        item_0_in_result7 = [_[7] for _ in results]
        item_0_in_result8 = [_[8] for _ in results]
        item_0_in_result9 = [_[9] for _ in results]
        item_0_in_result10 = [_[10] for _ in results]
        result_as_text11 = '\n'.join([x[11] for x in results])
        result_as_text12 = '\n'.join([x[12] for x in results])
        result_as_text13 = '\n'.join([x[13] for x in results])

        Label(root2, text="Date Planned:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=20, y=100)
        Label(root2, text=item_0_in_result, width=60, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=200, y=100)

        Label(root2, text="Order No:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=20, y=150)
        Label(root2, text=item_0_in_result1, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=200, y=150)

        Label(root2, text="Style/Description:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=20, y=200)
        Label(root2, text=result_as_text2, width=30, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=200, y=200)

        Label(root2, text="Delivery Date:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=20, y=250)
        Label(root2, text=item_0_in_result3, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=200, y=250)

        Label(root2, text="Order Quantity:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=20, y=300)
        Label(root2, text=item_0_in_result4, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=200, y=300)

        Label(root2, text="Size 3:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=370)
        Label(root2, text=item_0_in_result5, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=370)

        Label(root2, text="Size 4:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=420)
        Label(root2, text=item_0_in_result6, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=420)

        Label(root2, text="Size 5:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=470)
        Label(root2, text=item_0_in_result7, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=470)

        Label(root2, text="Size 6:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=520)
        Label(root2, text=item_0_in_result8, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=520)

        Label(root2, text="Size 7:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=570)
        Label(root2, text=item_0_in_result9, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=570)

        Label(root2, text="Size 8:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=620)
        Label(root2, text=item_0_in_result10, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=620)

        Label(root2, text="Upper:", width=25, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=400, y=370)
        Label(root2, text=result_as_text11, width=30, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=560, y=370)

        Label(root2, text="Sock:", width=25, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=400, y=420)
        Label(root2, text=result_as_text12, width=25, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=560, y=420)

        Label(root2, text="Binding:", width=25, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=400, y=470)
        Label(root2, text=result_as_text13, width=25, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=560, y=470)

        # Label(root2, text="Elastic:", width=25, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=400, y=570)
        # Label(root2, text=item_0_in_result14, width=25, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=560, y=570)

        cursor.close()

root.bind("<Double-1>", DblClick)

def orders_sandal():
    tree.delete(*tree.get_children())
    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        mycursor = conn.cursor()
        # WHERE Factory=?", ("RF2",))
        mycursor.execute("SELECT OrderNo,Style,DeliveryDate,Quantity,Binding,Material FROM MySandals")
        for row in mycursor:
            tree.insert('', 'end', values=row[0:8])


frame = Frame(root)
frame.pack()

# Treeview and Configuration
style = ttk.Style()
# Modify the font of the body
style.configure("Treeview", bd=2, font=('Calibri', 14))

# Modify OnClick
style.map('Treeview', background=[('selected', 'firebrick')])

# Modify the font of the heading and select columns
style.configure("Treeview.Heading", font=( "Calibri", 18, 'bold'), background='silver', foreground='black')
tree = ttk.Treeview(frame, columns=(0, 1, 2, 3), height=44, show="headings")
tree.pack(side='left')

tree.heading(0, text="OrderNo", anchor='center')
tree.heading(1, text="Style/Description", anchor=W)
tree.heading(2, text="Delivery Date", anchor='center')
tree.heading(3, text="Quantity", anchor='center')

tree.column(0, width=200, anchor='center')
tree.column(1, width=400, anchor=W)
tree.column(2, width=240, anchor='center')
tree.column(3, width=240, anchor='center')

# Scrollbar
scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
scroll.pack(side='right', fill='y')

tree.configure(yscrollcommand=scroll.set)

# Style of Buttons
style = Style()
style.configure('E.TButton', font=('Calibri', 14, 'bold', 'underline'), foreground='firebrick2', background='skyblue3')
style.configure('N.TButton', font=('Calibri', 14, 'bold', 'underline'), foreground='blue2', background='skyblue3')

def tkinter1():
    ret = os.system('python order_sandal.py')
    if ret:
        orders_sandal()

def tkinter8():
    ret2 = os.system('python order_delete_sandal.py')
    if ret2:
        orders_sandal()


def tkinter12():
    ret6 = os.system('python excel_export_orders_sandal.py')
    if ret6:
        orders_sandal()

# Buttons
btn = Button(root, text='Exit (Esc)', style='E.TButton', command=root.destroy).pack(side='right')
btn6 = Button(root, text='Export', style='N.TButton', command=tkinter12).pack(side='right')

# New Orders
mb =  Menubutton ( root, text = "New Order", style='N.TButton' )
mb.menu  =  Menu ( mb, tearoff = 0, activebackground="red", fg="ghost white", bg="chartreuse4", font=["Calibri", 14])
mb["menu"]  =  mb.menu
mb.menu.add_command (label = "Young Boys", command = tkinter1)
mb.pack(side="left")

btn2 = Button(root, text='Delete Order', style='N.TButton', command=tkinter8).pack(side='left')

orders_sandal()

update_time()

root.mainloop()
