from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
import os
from datetime import datetime
from idlelib.tooltip import Hovertip

root = Tk()
root.attributes('-fullscreen', True)
root.title("School Shoes")
root.config(bg="skyblue3")

OrderNo = StringVar()
Quantity = IntVar()

dateTimeObj = datetime.now()

timestampStr = dateTimeObj.strftime("%d-%b-%Y")
xstampStr = dateTimeObj.strftime("%H:%M:%S %p")

l1 = Label(root, text="Orders In House", width=120, anchor= CENTER, font=["Bodoni MT", 30, "bold"], background="skyblue3", relief="raised").pack(side='top', ipady=10)
label_time = Label(root, text=xstampStr, width=11, anchor = CENTER, font=["Arial", 10, "bold"], background="skyblue3", relief="ridge")
label_time.pack(side='top', anchor = NE, ipady=5, ipadx=5)


def update_time():
    now = datetime.now()
    time_now = now.strftime("%H:%M:%S %p")
    label_time.config(text=time_now)
    root.after(1000, update_time)

def orders():
    tree.delete(*tree.get_children())
    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        mycursor = conn.cursor()
        mycursor.execute("SELECT OrderNo,Style,DeliveryDate,Quantity FROM MyShoe ORDER BY DeliveryDate ASC")
        for row in mycursor:
            tree.insert('', 'end', values=row[0:6])

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
tree = ttk.Treeview(frame, columns=(1, 2, 3, 4), height=44, show="headings")
tree.pack(side='left')
# auto-fill
# tree.pack(fill='x')(fill='y')(fill='both')

tree.heading(1, text="OrderNo", anchor='center')
tree.heading(2, text="Style/Description", anchor=W)
tree.heading(3, text="Delivery Date", anchor='center')
tree.heading(4, text="Quantity", anchor='center')

tree.column(1, width=200, anchor='center')
tree.column(2, width=400, anchor=W)
tree.column(3, width=240, anchor='center')
tree.column(4, width=240, anchor='center')


# Scrollbar
scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
scroll.pack(side='right', fill='y')

tree.configure(yscrollcommand=scroll.set)

# Style of Buttons
style = Style()
style.configure('E.TButton', font=('Calibri', 14, 'bold', 'underline'), foreground='firebrick2', background='skyblue3')
style.configure('N.TButton', font=('Calibri', 14, 'bold', 'underline'), foreground='blue2', background='skyblue3')
style.configure("Vertical.TScrollbar", background="red", bordercolor="red", arrowcolor="white")


def tkinter1():
    ret = os.system('python order_pb.py')
    if ret:
        orders()


def tkinter14():
    ret = os.system('python order_pg.py')
    if ret:
        orders()


def tkinter2():
    ret = os.system('python order_b.py')
    if ret:
        orders()


def tkinter3():
    ret = os.system('python order_m.py')
    if ret:
        orders()


def tkinter15():
    ret = os.system('python order_g.py')
    if ret:
        orders()


def tkinter4():
    ret = os.system('python order_pbl.py')
    if ret:
        orders()


def tkinter16():
    ret = os.system('python order_pgl.py')
    if ret:
        orders()


def tkinter5():
    ret = os.system('python order_bl.py')
    if ret:
        orders()


def tkinter6():
    ret = os.system('python order_ml.py')
    if ret:
        orders()


def tkinter17():
    ret = os.system('python order_gl.py')
    if ret:
        orders()


def tkinter7():
    ret = os.system('python order_pbi.py')
    if ret:
        orders()


def tkinter8():
    ret = os.system('python order_bi.py')
    if ret:
        orders()


def tkinter9():
    ret = os.system('python order_mi.py')
    if ret:
        orders()


def tkinter13():
    ret4 = os.system('python excel_export_orders.py')
    if ret4:
        orders()

#Bind keys
def close_screen(e):
	command=root.destroy()
root.bind('<Escape>', lambda e: close_screen(e))


def DblClick(event):
    curItem = tree.focus()
    order = tree.item(curItem)['values'][0]
    desc = tree.item(curItem)['values'][1]
    root2 = Tk()
    root2.geometry('650x600')
    root2.title("Order In House")
    root2.config(bg="skyblue2")
    style2 = ttk.Style()

    l1 = Label(root2, text="Order Details", width=80, anchor= CENTER, font=["Bodoni MT", 23, "bold"], background="skyblue3", relief="raised").pack(side='top', ipady=10)

    if 'PRE' in desc:
        with sqlite3.connect('Reflex Footwear.sql3') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT DatePlanned,OrderNo,Style,Pairs,Delivery,Size8,Size9,Size10,Size11,Size12,Size13,Size1 FROM Planning WHERE OrderNo=?', (order,))
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
            item_0_in_result11 = [_[11] for _ in results]

            Label(root2, text="Date Planned:", width=20, background="skyblue2", foreground="black", font=("Arial", 14)).place(x=20, y=100)
            Label(root2, text=item_0_in_result, width=60, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=200, y=100)

            Label(root2, text="Order No:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=20, y=150)
            Label(root2, text=item_0_in_result1, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=200, y=150)

            Label(root2, text="Style/Description:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=20, y=200)
            Label(root2, text=result_as_text2, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=200, y=200)

            Label(root2, text="Order Quantity:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=20, y=250)
            Label(root2, text=item_0_in_result3, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=200, y=250)

            Label(root2, text="Delivery Date:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=20, y=300)
            Label(root2, text=item_0_in_result4, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=200, y=300)

            Label(root2, text="Size 8:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=370)
            Label(root2, text=item_0_in_result5, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=370)

            Label(root2, text="Size 9:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=420)
            Label(root2, text=item_0_in_result6, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=420)

            Label(root2, text="Size 10:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=470)
            Label(root2, text=item_0_in_result7, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=470)

            Label(root2, text="Size 11:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=520)
            Label(root2, text=item_0_in_result8, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=520)

            Label(root2, text="Size 12:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=400, y=370)
            Label(root2, text=item_0_in_result9, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=560, y=370)

            Label(root2, text="Size 13:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=400, y=420)
            Label(root2, text=item_0_in_result10, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=560, y=420)

            Label(root2, text="Size 1:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=400, y=470)
            Label(root2, text=item_0_in_result11, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=560, y=470)

            cursor.close()
    elif 'BOYS' in desc:
        with sqlite3.connect('Reflex Footwear.sql3') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT DatePlanned,OrderNo,Style,Pairs,Delivery,Size2,Size3,Size4,Size5 FROM Planning WHERE OrderNo=?', (order,))
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

            Label(root2, text="Date Planned:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=20, y=100)
            Label(root2, text=item_0_in_result, width=60, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=200, y=100)

            Label(root2, text="Order No:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=20, y=150)
            Label(root2, text=item_0_in_result1, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=200, y=150)

            Label(root2, text="Style/Description:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=20, y=200)
            Label(root2, text=result_as_text2, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=200, y=200)

            Label(root2, text="Order Quantity:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=20, y=250)
            Label(root2, text=item_0_in_result3, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=200, y=250)

            Label(root2, text="Delivery Date:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=20, y=300)
            Label(root2, text=item_0_in_result4, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=200, y=300)

            Label(root2, text="Size 2:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=370)
            Label(root2, text=item_0_in_result5, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=370)

            Label(root2, text="Size 3:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=420)
            Label(root2, text=item_0_in_result6, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=420)

            Label(root2, text="Size 4:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=470)
            Label(root2, text=item_0_in_result7, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=470)

            Label(root2, text="Size 5:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=520)
            Label(root2, text=item_0_in_result8, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=520)

            cursor.close()
    elif 'GIRLS' in desc:
        with sqlite3.connect('Reflex Footwear.sql3') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT DatePlanned,OrderNo,Style,Pairs,Delivery,Size2,Size3,Size4,Size5,Size6,Size7,Size8b FROM Planning WHERE OrderNo=?', (order,))
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
            item_0_in_result11 = [_[11] for _ in results]

            Label(root2, text="Date Planned:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=20, y=100)
            Label(root2, text=item_0_in_result, width=60, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=200, y=100)

            Label(root2, text="Order No:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=20, y=150)
            Label(root2, text=item_0_in_result1, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=200, y=150)

            Label(root2, text="Style/Description:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=20, y=200)
            Label(root2, text=result_as_text2, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=200, y=200)

            Label(root2, text="Order Quantity:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=20, y=250)
            Label(root2, text=item_0_in_result3, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=200, y=250)

            Label(root2, text="Delivery Date:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=20, y=300)
            Label(root2, text=item_0_in_result4, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=200, y=300)

            Label(root2, text="Size 2:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=370)
            Label(root2, text=item_0_in_result5, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=370)

            Label(root2, text="Size 3:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=420)
            Label(root2, text=item_0_in_result6, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=420)

            Label(root2, text="Size 4:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=470)
            Label(root2, text=item_0_in_result7, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=470)

            Label(root2, text="Size 5:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=520)
            Label(root2, text=item_0_in_result8, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=520)

            Label(root2, text="Size 6:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=400, y=370)
            Label(root2, text=item_0_in_result9, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=560, y=370)

            Label(root2, text="Size 7:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=400, y=420)
            Label(root2, text=item_0_in_result10, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=560, y=420)

            Label(root2, text="Size 8:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=400, y=470)
            Label(root2, text=item_0_in_result11, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=560, y=470)

            cursor.close()

    else:
        with sqlite3.connect('Reflex Footwear.sql3') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT DatePlanned,OrderNo,Style,Pairs,Delivery,Size6,Size7,Size8b,Size9b,Size10b FROM Planning WHERE OrderNo=?', (order,))
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

            Label(root2, text="Date Planned:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=20, y=100)
            Label(root2, text=item_0_in_result, width=60, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=200, y=100)

            Label(root2, text="Order No:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=20, y=150)
            Label(root2, text=item_0_in_result1, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=200, y=150)

            Label(root2, text="Style/Description:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=20, y=200)
            Label(root2, text=result_as_text2, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=200, y=200)

            Label(root2, text="Order Quantity:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=20, y=250)
            Label(root2, text=item_0_in_result3, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=200, y=250)

            Label(root2, text="Delivery Date:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=20, y=300)
            Label(root2, text=item_0_in_result4, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 14)).place(x=200, y=300)

            Label(root2, text="Size 6:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=370)
            Label(root2, text=item_0_in_result5, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=370)

            Label(root2, text="Size 7:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=420)
            Label(root2, text=item_0_in_result6, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=420)

            Label(root2, text="Size 8:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=470)
            Label(root2, text=item_0_in_result7, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=470)

            Label(root2, text="Size 9:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=520)
            Label(root2, text=item_0_in_result8, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=520)

            Label(root2, text="Size 10:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=300, y=370)
            Label(root2, text=item_0_in_result9, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=460, y=370)

            cursor.close()

# root.bind("<Double-1>",lambda event :DblClick(event))
root.bind("<Double-1>", DblClick)

# Buttons
btn = Button(root, text='Exit (Esc)', style='E.TButton', command=root.destroy).pack(side='right')

# New Orders
mb =  Menubutton ( root, text = "New Order", style='N.TButton' )
mb.menu  =  Menu ( mb, tearoff = 0, activebackground="red", fg="ghost white", bg="chartreuse4", font=["Calibri", 14])
mb["menu"]  =  mb.menu
mb.menu.add_command (label = "Pre-Boys Synthetic", command = tkinter1)
mb.menu.add_command (label = "Boys Synthetic", command = tkinter2)
mb.menu.add_command (label = "Mens Synthetic", command = tkinter3)
# newTip = Hovertip(mb,'Click this to create a \n New Order.')

mb.menu.add_command (label = "Pre-Boys Leather", command = tkinter4)
mb.menu.add_command (label = "Boys Leather", command = tkinter5)
mb.menu.add_command (label = "Mens Leather", command = tkinter6)

mb.menu.add_command (label = "Pre-Boys Idler", command = tkinter7)
mb.menu.add_command (label = "Boys Idler", command = tkinter8)
mb.menu.add_command (label = "Mens Idler", command = tkinter9)

mb.menu.add_command (label = "Pre-Girls Synthetic", command = tkinter14)
mb.menu.add_command (label = "Pre-Girls Leather", command = tkinter16)

mb.menu.add_command (label = "Girls Synthetic", command = tkinter15)
mb.menu.add_command (label = "Girls Leather", command = tkinter17)

mb.pack(side="left")

btn6 = Button(root, text='Export', style='N.TButton', command=tkinter13).pack(side='right') #.pack(fill = BOTH, expand = True)

orders()

update_time()
root.mainloop()
