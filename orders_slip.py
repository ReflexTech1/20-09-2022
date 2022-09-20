from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
import os
from datetime import datetime

root = Tk()
root.attributes('-fullscreen', True)
root.title("Stokies")
root.config(bg="skyblue3")

OrderNo = StringVar()
Quantity = IntVar()

dateTimeObj = datetime.now()

timestampStr = dateTimeObj.strftime("%d-%b-%Y")
xstampStr = dateTimeObj.strftime("%H:%M:%S %p")

l1 = Label(root, text="Slipper Orders In House", width=120, anchor= CENTER, font=["Bodoni MT", 30, "bold"], background="skyblue3", relief="raised").pack(side='top', ipady=10)
label_time = Label(root, text=xstampStr, width=11, anchor = CENTER, font=["Arial", 10, "bold"], background="skyblue3", relief="ridge")
label_time.pack(side='top', anchor = NE, ipady=5, ipadx=5)


def update_time():
    now = datetime.now()
    time_now = now.strftime("%H:%M:%S %p")
    label_time.config(text=time_now)
    root.after(1000, update_time)


def orders_slip():
    tree.delete(*tree.get_children())
    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        mycursor = conn.cursor()
        # WHERE Factory=?", ("RF2",))
        mycursor.execute("SELECT OrderNo,Style,DeliveryDate,Quantity,Binding,Elastic,Material,Sock FROM MySlippers")
        for row in mycursor:
            tree.insert('', 'end', values=row[0:4])


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
    ret = os.system('python order_slip_bb.py')
    if ret:
        exit()


def tkinter2():
    ret2 = os.system('python order_slip_yb.py')
    if ret2:
        exit()


def tkinter3():
    ret3 = os.system('python order_slip_b.py')
    if ret3:
        exit()


def tkinter4():
    ret4 = os.system('python order_slip_m.py')
    if ret4:
        exit()


def tkinter5():
    ret5 = os.system('python order_slip_si_sml.py')
    if ret5:
        exit()


def tkinter6():
    ret6 = os.system('python order_slip_si_big.py')
    if ret6:
        exit()


def tkinter7():
    ret7 = os.system('python order_slip_NSLA.py')
    if ret7:
        exit()

def tkinter8():
    ret2 = os.system('python order_delete_slip.py')
    if ret2:
        orders_slip()


def tkinter12():
    ret6 = os.system('python excel_export_orders_slip.py')
    if ret6:
        orders_slip()


#Bind keys
def close_screen(e):
	command=root.destroy()
root.bind('<Escape>', lambda e: close_screen(e))


def DblClick(event):
    curItem = tree.focus()
    order = tree.item(curItem)['values'][0]
    desc = tree.item(curItem)['values'][1]
    root2 = Tk()
    root2.geometry('1000x700')
    root2.title("Planning")
    root2.config(bg="skyblue2")
    style2 = ttk.Style()

    l1 = Label(root2, text="Order Details", width=80, anchor= CENTER, font=["Bodoni MT", 23, "bold"], background="skyblue3", relief="raised").pack(side='top', ipady=10)

    if 'YOUNGER' in desc:
        with sqlite3.connect('Reflex Footwear.sql3') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT Planned,OrderNo,Style,DeliveryDate,Quantity,Soles34,Soles56,Soles78,Soles910,Soles1112,Soles131,Material,Sock,Binding,Elastic FROM MySlippers WHERE OrderNo=?', (order,))
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
            result_as_text14 = '\n'.join([x[14] for x in results])

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

            Label(root2, text="Size 3/4:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=370)
            Label(root2, text=item_0_in_result5, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=370)

            Label(root2, text="Size 5/6:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=420)
            Label(root2, text=item_0_in_result6, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=420)

            Label(root2, text="Size 7/8:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=470)
            Label(root2, text=item_0_in_result7, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=470)

            Label(root2, text="Size 9/10:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=520)
            Label(root2, text=item_0_in_result8, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=520)

            Label(root2, text="Size 11/12:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=570)
            Label(root2, text=item_0_in_result9, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=570)

            Label(root2, text="Size 13/1:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=620)
            Label(root2, text=item_0_in_result10, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=620)

            Label(root2, text="Upper:", width=25, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=400, y=420)
            Label(root2, text=result_as_text11, width=30, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=560, y=420)

            Label(root2, text="Sock:", width=25, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=400, y=470)
            Label(root2, text=result_as_text12, width=25, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=560, y=470)

            Label(root2, text="Binding:", width=25, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=400, y=520)
            Label(root2, text=result_as_text13, width=25, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=560, y=520)

            Label(root2, text="Elastic:", width=25, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=400, y=570)
            Label(root2, text=result_as_text14, width=25, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=560, y=570)

            cursor.close()

    if desc =='BOYS SLIPPER':
        with sqlite3.connect('Reflex Footwear.sql3') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT Planned,OrderNo,Style,DeliveryDate,Quantity,Soles23,Soles45,Material,Sock,Binding,Elastic FROM MySlippers WHERE OrderNo=?', (order,))
            results = cursor.fetchall()

            item_0_in_result = [_[0] for _ in results]
            item_0_in_result1 = [_[1] for _ in results]
            result_as_text2 = '\n'.join([x[2] for x in results])
            item_0_in_result3 = [_[3] for _ in results]
            item_0_in_result4 = [_[4] for _ in results]
            item_0_in_result5 = [_[5] for _ in results]
            item_0_in_result6 = [_[6] for _ in results]
            result_as_text7 = '\n'.join([x[7] for x in results])
            result_as_text8 = '\n'.join([x[8] for x in results])
            result_as_text9 = '\n'.join([x[9] for x in results])
            result_as_text10 = '\n'.join([x[10] for x in results])

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

            Label(root2, text="Size 2/3:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=370)
            Label(root2, text=item_0_in_result5, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=370)

            Label(root2, text="Size 4/5:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=420)
            Label(root2, text=item_0_in_result6, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=420)

            Label(root2, text="Upper:", width=25, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=400, y=370)
            Label(root2, text=result_as_text7, width=30, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=560, y=370)

            Label(root2, text="Sock:", width=25, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=400, y=420)
            Label(root2, text=result_as_text8, width=25, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=560, y=420)

            Label(root2, text="Binding:", width=25, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=400, y=470)
            Label(root2, text=result_as_text9, width=25, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=560, y=470)

            Label(root2, text="Elastic:", width=25, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=400, y=520)
            Label(root2, text=result_as_text10, width=25, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=560, y=520)

            cursor.close()


    if 'MENS' in desc:
        with sqlite3.connect('Reflex Footwear.sql3') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT Planned,OrderNo,Style,DeliveryDate,Quantity,Soles67,Soles89,Soles1011,Material,Sock,Binding,Elastic FROM MySlippers WHERE OrderNo=?', (order,))
            results = cursor.fetchall()

            item_0_in_result = [_[0] for _ in results]
            item_0_in_result1 = [_[1] for _ in results]
            result_as_text2 = '\n'.join([x[2] for x in results])
            item_0_in_result3 = [_[3] for _ in results]
            item_0_in_result4 = [_[4] for _ in results]
            item_0_in_result5 = [_[5] for _ in results]
            item_0_in_result6 = [_[6] for _ in results]
            item_0_in_result7 = [_[7] for _ in results]
            result_as_text8 = '\n'.join([x[8] for x in results])
            result_as_text9 = '\n'.join([x[9] for x in results])
            result_as_text10 = '\n'.join([x[10] for x in results])
            result_as_text11 = '\n'.join([x[11] for x in results])

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

            Label(root2, text="Size 6/7:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=370)
            Label(root2, text=item_0_in_result5, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=370)

            Label(root2, text="Size 8/9:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=420)
            Label(root2, text=item_0_in_result6, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=420)

            Label(root2, text="Size 10/11:", width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=20, y=470)
            Label(root2, text=item_0_in_result7, width=20, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=180, y=470)

            Label(root2, text="Upper:", width=25, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=400, y=370)
            Label(root2, text=result_as_text8, width=30, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=560, y=370)

            Label(root2, text="Sock:", width=25, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=400, y=420)
            Label(root2, text=result_as_text9, width=25, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=560, y=420)

            Label(root2, text="Binding:", width=25, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=400, y=470)
            Label(root2, text=result_as_text10, width=25, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=560, y=470)

            Label(root2, text="Elastic:", width=25, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=400, y=520)
            Label(root2, text=result_as_text11, width=25, background="skyblue2", foreground="black", font=("Arial, bold", 12)).place(x=560, y=520)

            cursor.close()


# root.bind("<Double-1>",lambda event :DblClick(event))
root.bind("<Double-1>", DblClick)

# Buttons
btn = Button(root, text='Exit (Esc)', style='E.TButton', command=root.destroy).pack(side='right')
btn6 = Button(root, text='Export', style='N.TButton', command=tkinter12).pack(side='right')

# New Orders
mb =  Menubutton ( root, text = "New Order", style='N.TButton' )
mb.menu  =  Menu ( mb, tearoff = 0, activebackground="red", fg="ghost white", bg="chartreuse4", font=["Calibri", 14])
mb["menu"]  =  mb.menu
mb.menu.add_command (label = "Baby Boys", command = tkinter1)
mb.menu.add_command (label = "Young Boys", command = tkinter2)
mb.menu.add_command (label = "Boys", command = tkinter3)
mb.menu.add_command (label = "Mens", command = tkinter4)
mb.menu.add_command (label = "SI Small", command = tkinter5)
mb.menu.add_command (label = "SI Big", command = tkinter6)
mb.menu.add_command (label = "Closed Toe NSLA", command = tkinter7)
mb.pack(side="left")

btn2 = Button(root, text='Delete Order', style='N.TButton', command=tkinter8).pack(side='left')

orders_slip()

update_time()

root.mainloop()
