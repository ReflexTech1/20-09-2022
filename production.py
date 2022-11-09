from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
import os
from datetime import datetime
import customtkinter
from PIL import Image, ImageTk
import tkinter.messagebox

root = Tk()
# root.state('zoomed') # Windowed view
root.attributes('-fullscreen', True)
root.title("Manufacturing")
root.config(bg="lightblue2")

dateTimeObj = datetime.now()
xstampStr = dateTimeObj.strftime("%H:%M:%S %p")

l1 = Label(root, text="Production Tracker", width=120, anchor=CENTER, font=["Bodoni MT", 30, "bold"], background="grey80", relief="raised").pack(side='top', ipady=10)
label_time = Label(root, text=xstampStr, width=11, anchor = CENTER, font=["Arial", 10, "bold"], background="lightblue2", relief="ridge")
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


def do_popup(event):
    try:
        edit.tk_popup(event.x_root, event.y_root)
    finally:
        edit.grab_release()


def scores(e):
    try:
        edit2.tk_popup(e.x_root, e.y_root)
    finally:
        edit2.grab_release()

root.bind("<Button-3>", do_popup)
root.bind('<Double-1>', lambda e: scores(e))


def Balance():
    curItem = tree.focus()
    order = tree.item(curItem)['values'][0]
    desc = 0
    root4 = Tk()
    root4.geometry('820x500')
    root4.title("Production Status")
    root4.config(bg="skyblue2")
    style2 = ttk.Style()
    l_prod = Label(root4, text="Balance To Complete", width=120, anchor=CENTER, font=["Bodoni MT", 30, "bold"], background="grey80", relief="raised").pack(side='top', ipady=10)
    def close_screen2(e):
    	command=root4.destroy()
    root4.bind('<Escape>', lambda e: close_screen2(e))

    if order is not None:
        with sqlite3.connect('Reflex Footwear.sql3') as conn4:
            cursor4 = conn4.cursor()
            cursor4.execute('SELECT Factory,Planned,Order2,Style,Deldate,Orderqty,Clicking,Closing,Finishing,Despatch,Warehouse,ToShip,Shipped FROM Production_Balances WHERE Order2=?', (order,))
            results = cursor4.fetchall()

            item_0_in_result = [_[0] for _ in results] # Factory
            item_0_in_result1 = [_[1] for _ in results] # Planned
            item_0_in_result2 = [_[2] for _ in results] # OrderNo
            result_as_text3 = '\n'.join([x[3] for x in results]) # Style
            item_0_in_result4 = [_[4] for _ in results] # Delivery date
            item_0_in_result5 = [_[5] for _ in results] # Quantity
            item_0_in_result6 = [_[6] for _ in results] # Clicking
            item_0_in_result7 = [_[7] for _ in results] # Closing
            item_0_in_result8 = [_[8] for _ in results] # Finishing
            item_0_in_result9 = [_[9] for _ in results] # Despatch
            item_0_in_result10 = [_[10] for _ in results] # Warehouse
            item_0_in_result11 = [_[11] for _ in results] # To Ship
            item_0_in_result12 = [_[12] for _ in results] # Shipped


            Label(root4, text="Planned:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=40, y=150)
            Label(root4, text=item_0_in_result1, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=250, y=150)

            Label(root4, text="Order No:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=40, y=200)
            Label(root4, text=item_0_in_result2, width=60, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=250, y=200)

            Label(root4, text="Style/Description:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=40, y=250)
            Label(root4, text=result_as_text3, width=22, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=250, y=250)

            Label(root4, text="Delivery Date:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=40, y=300)
            Label(root4, text=item_0_in_result4, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=250, y=300)

            Label(root4, text="Order Quantity:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=40, y=350)
            Label(root4, text=item_0_in_result5, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=250, y=350)

            Label(root4, text="Balance To Click:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=500, y=150)
            Label(root4, text=item_0_in_result6, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=710, y=150)

            Label(root4, text="Closing:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=500, y=200)
            Label(root4, text=item_0_in_result7, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=710, y=200)

            Label(root4, text="Finishing:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=500, y=250)
            Label(root4, text=item_0_in_result8, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=710, y=250)

            Label(root4, text="Despatch:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=500, y=300)
            Label(root4, text=item_0_in_result9, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=710, y=300)

            Label(root4, text="Warehouse:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=500, y=350)
            Label(root4, text=item_0_in_result9, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=710, y=350)

            Label(root4, text="Balance To Ship:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=500, y=350)
            Label(root4, text=item_0_in_result11, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=710, y=350)

            Label(root4, text="Shipped:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=500, y=400)
            Label(root4, text=item_0_in_result12, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=710, y=400)

            cursor4.close()


def Clicking():
    root3 = Toplevel()
    root3.geometry('380x250')
    root3.title("Record Score")
    root3.config(bg="lightblue2")
    timestampStr = dateTimeObj.strftime("%m-%d-%Y")
    style3 = ttk.Style()
    Balance = StringVar()
    Reason = StringVar()
    curItem = tree.focus()
    code = tree.item(curItem)['values'][0]
    desc = tree.item(curItem)['values'][1]
    def ClickUpdate():
        balance = Balance.get()
        reason = Reason.get()
        with sqlite3.connect('Reflex Footwear.sql3') as conn:
            cursor3 = conn.cursor()
            cursor3.execute('UPDATE Production SET Clicking=Clicking-? WHERE Order2=?', [balance, code,])
            cursor3.execute('UPDATE Production SET Closing=Closing+? WHERE Order2=?', [balance, code,])
            cursor3.execute('UPDATE Production_Balances SET Clicking=Clicking-? WHERE Order2=?', [balance, code, ])
            cursor3.execute('INSERT INTO ProductionBreakdown (Factory,Date,Order2,Style,Clicking,Reason) VALUES(?,?,?,?,?,?)', ["Reflex", timestampStr, code, desc, balance, reason])
            updated = cursor3.rowcount
            cursor3.close()
            conn.commit()
            root3.destroy()
            production()

    def submit_root(e):
       command=ClickUpdate()

    root3.bind('<Return>', lambda e: submit_root(e))

    style3.configure('C.TButton', font=('Arial', 12, 'bold'), foreground='red')
    style3.configure('S.TButton', font=('Arial', 12, 'bold'), foreground='blue')

    label_0 = Label(root3, text="Clicking Score", background="lightblue2", width=20, font=("Arial", 20, "bold"))
    label_0.place(x=100, y=23)

    label_3 = Label(root3, text="Quantity Clicked", width=20, background="lightblue2", font=("Arial", 12, "bold"))
    label_3.place(x=20, y=100)
    entry_3 = Entry(root3, textvar=Balance, background="lightblue2", font=("Arial", 12, "bold"))
    entry_3.place(x=180, y=100)

    label_4 = Label(root3, text="Reason", width=20, background="lightblue2", font=("Arial", 12, "bold"))
    label_4.place(x=20, y=140)
    entry_4 = Entry(root3, textvar=Reason, background="lightblue2", font=("Arial", 12, "bold"))
    entry_4.place(x=180, y=140)

    # submitbtn = customtkinter.CTkButton(root3, text="Submit", border_width=3, text_font=('Calibri', -15, 'bold'), fg_color='blue', command=ClickUpdate).place(x=60, y=200)
    submit_btn = Button(root3, text='Submit', width=11, style='S.TButton', command=ClickUpdate)
    submit_btn.place(x=60, y=200)
    exit1 = Button(root3, text='Close', width=11, style='C.TButton', command=root3.destroy)
    exit1.place(x=250, y=200)


def Closing():
    root3 = Toplevel()
    root3.geometry('380x270')
    root3.title("Record Score")
    root3.config(bg="lightblue2")
    timestampStr = dateTimeObj.strftime("%m-%d-%Y")
    style3 = ttk.Style()
    Balance = StringVar()
    Line  = StringVar()
    Reason = StringVar()
    curItem = tree.focus()
    code = tree.item(curItem)['values'][0]
    desc = tree.item(curItem)['values'][1]
    def ClosingUpdate():
        balance = Balance.get()
        line = Line.get()
        reason = Reason.get()
        with sqlite3.connect('Reflex Footwear.sql3') as conn:
            cursor3 = conn.cursor()
            cursor3.execute('UPDATE Production SET Closing=Closing-? WHERE Order2=?', [balance, code,])
            cursor3.execute('UPDATE Production SET Finishing=Finishing+? WHERE Order2=?', [balance, code,])
            cursor3.execute('UPDATE Production_Balances SET Closing=Closing-? WHERE Order2=?', [balance, code, ])
            cursor3.execute('INSERT INTO ProductionBreakdown (Factory,Date,Line,Order2,Style,Closing,Reason) VALUES(?,?,?,?,?,?,?)', ["Reflex", timestampStr, line, code, desc, balance, reason])
            updated = cursor3.rowcount
            cursor3.close()
            conn.commit()
            root3.destroy()
            production()

    def submit_root(e):
       command=ClosingUpdate()

    root3.bind('<Return>', lambda e: submit_root(e))

    style3.configure('C.TButton', font=('Arial', 12, 'bold'), foreground='red')
    style3.configure('S.TButton', font=('Arial', 12, 'bold'), foreground='blue')

    label_0 = Label(root3, text="Closing Score", background="lightblue2", width=20, font=("Arial", 20, "bold"))
    label_0.place(x=100, y=23)
    label_2 = Label(root3, text="Line No", width=20, background="lightblue2", font=("Arial", 12, "bold"))
    label_2.place(x=20, y=100)
    entry_2 = Entry(root3, textvar=Line, background="lightblue2", font=("Arial", 12, "bold"))
    entry_2.place(x=180, y=100)

    label_3 = Label(root3, text="Quantity Closed", width=20, background="lightblue2", font=("Arial", 12, "bold"))
    label_3.place(x=20, y=140)
    entry_3 = Entry(root3, textvar=Balance, background="lightblue2", font=("Arial", 12, "bold"))
    entry_3.place(x=180, y=140)

    label_4 = Label(root3, text="Reason", width=20, background="lightblue2", font=("Arial", 12, "bold"))
    label_4.place(x=20, y=180)
    entry_4 = Entry(root3, textvar=Reason, background="lightblue2", font=("Arial", 12, "bold"))
    entry_4.place(x=180, y=180)

    # submitbtn = customtkinter.CTkButton(root3, text="Submit", border_width=3, text_font=('Calibri', -15, 'bold'), fg_color='blue', command=ClickUpdate).place(x=60, y=200)
    submit_btn = Button(root3, text='Submit', width=11, style='S.TButton', command=ClosingUpdate)
    submit_btn.place(x=60, y=220)
    exit1 = Button(root3, text='Close', width=11, style='C.TButton', command=root3.destroy)
    exit1.place(x=250, y=220)


def Despatch():
    root3 = Toplevel()
    root3.geometry('380x270')
    root3.title("Record Score")
    root3.config(bg="lightblue2")
    timestampStr = dateTimeObj.strftime("%m-%d-%Y")
    style3 = ttk.Style()
    Balance = StringVar()
    Line  = StringVar()
    Reason = StringVar()
    curItem = tree.focus()
    code = tree.item(curItem)['values'][0]
    desc = tree.item(curItem)['values'][1]
    def DespUpdate():
        balance = Balance.get()
        line = Line.get()
        reason = Reason.get()
        with sqlite3.connect('Reflex Footwear.sql3') as conn:
            cursor3 = conn.cursor()
            cursor3.execute('UPDATE Production SET Despatch=Despatch+? WHERE Order2=?', [balance, code, ])
            cursor3.execute('UPDATE Production SET Finishing=Finishing-? WHERE Order2=?', [balance, code, ])
            cursor3.execute('UPDATE Production_Balances SET Finishing=Finishing-? WHERE Order2=?', [balance, code, ])
            cursor3.execute('UPDATE Production_Balances SET Despatch=Despatch-? WHERE Order2=?', [balance, code, ])
            cursor3.execute('INSERT INTO ProductionBreakdown (Factory,Date,Line,Order2,Style,Despatch,Reason) VALUES(?,?,?,?,?,?,?)', ["Reflex", timestampStr, line, code, desc, balance, reason])
            updated = cursor3.rowcount
            cursor3.close()
            conn.commit()
            root3.destroy()
            production()

    def submit_root(e):
       command=DespUpdate()

    root3.bind('<Return>', lambda e: submit_root(e))

    style3.configure('C.TButton', font=('Arial', 12, 'bold'), foreground='red')
    style3.configure('S.TButton', font=('Arial', 12, 'bold'), foreground='blue')

    label_0 = Label(root3, text="Despatch Score", background="lightblue2", width=20, font=("Arial", 20, "bold"))
    label_0.place(x=100, y=23)
    label_2 = Label(root3, text="Line No", width=20, background="lightblue2", font=("Arial", 12, "bold"))
    label_2.place(x=20, y=100)
    entry_2 = Entry(root3, textvar=Line, background="lightblue2", font=("Arial", 12, "bold"))
    entry_2.place(x=180, y=100)

    label_3 = Label(root3, text="Quantity Received", width=20, background="lightblue2", font=("Arial", 12, "bold"))
    label_3.place(x=20, y=140)
    entry_3 = Entry(root3, textvar=Balance, background="lightblue2", font=("Arial", 12, "bold"))
    entry_3.place(x=180, y=140)

    label_4 = Label(root3, text="Reason", width=20, background="lightblue2", font=("Arial", 12, "bold"))
    label_4.place(x=20, y=180)
    entry_4 = Entry(root3, textvar=Reason, background="lightblue2", font=("Arial", 12, "bold"))
    entry_4.place(x=180, y=180)

    # submitbtn = customtkinter.CTkButton(root3, text="Submit", border_width=3, text_font=('Calibri', -15, 'bold'), fg_color='blue', command=ClickUpdate).place(x=60, y=200)
    submit_btn = Button(root3, text='Submit', width=11, style='S.TButton', command=DespUpdate)
    submit_btn.place(x=60, y=220)
    exit1 = Button(root3, text='Close', width=11, style='C.TButton', command=root3.destroy)
    exit1.place(x=250, y=220)


def Warehouse():
    root3 = Toplevel()
    root3.geometry('380x270')
    root3.title("Record Score")
    root3.config(bg="lightblue2")
    timestampStr = dateTimeObj.strftime("%m-%d-%Y")
    style3 = ttk.Style()
    Balance = StringVar()
    Line  = StringVar()
    Reason = StringVar()
    curItem = tree.focus()
    code = tree.item(curItem)['values'][0]
    desc = tree.item(curItem)['values'][1]
    def WareUpdate():
        balance = Balance.get()
        line = Line.get()
        reason = Reason.get()
        with sqlite3.connect('Reflex Footwear.sql3') as conn:
            cursor3 = conn.cursor()
            cursor3.execute('UPDATE Production SET Warehouse=Warehouse+? WHERE Order2=?', [balance, code, ])
            cursor3.execute('UPDATE Production SET Despatch=Despatch-? WHERE Order2=?', [balance, code, ])
            cursor3.execute('UPDATE Production_Balances SET Warehouse=Warehouse-? WHERE Order2=?', [balance, code,])
            cursor3.execute('INSERT INTO ProductionBreakdown (Factory,Date,Line,Order2,Style,Warehouse,Reason) VALUES(?,?,?,?,?,?,?)', ["Reflex", timestampStr, line, code, desc, balance, reason])
            updated = cursor3.rowcount
            cursor3.close()
            conn.commit()
            root3.destroy()
            production()

    def submit_root(e):
       command=WareUpdate()

    root3.bind('<Return>', lambda e: submit_root(e))

    style3.configure('C.TButton', font=('Arial', 12, 'bold'), foreground='red')
    style3.configure('S.TButton', font=('Arial', 12, 'bold'), foreground='blue')

    label_0 = Label(root3, text="Warehouse Score", background="lightblue2", width=20, font=("Arial", 20, "bold"))
    label_0.place(x=100, y=23)
    label_2 = Label(root3, text="Line No", width=20, background="lightblue2", font=("Arial", 12, "bold"))
    label_2.place(x=20, y=100)
    entry_2 = Entry(root3, textvar=Line, background="lightblue2", font=("Arial", 12, "bold"))
    entry_2.place(x=180, y=100)

    label_3 = Label(root3, text="Quantity Received", width=20, background="lightblue2", font=("Arial", 12, "bold"))
    label_3.place(x=20, y=140)
    entry_3 = Entry(root3, textvar=Balance, background="lightblue2", font=("Arial", 12, "bold"))
    entry_3.place(x=180, y=140)

    label_4 = Label(root3, text="Reason", width=20, background="lightblue2", font=("Arial", 12, "bold"))
    label_4.place(x=20, y=180)
    entry_4 = Entry(root3, textvar=Reason, background="lightblue2", font=("Arial", 12, "bold"))
    entry_4.place(x=180, y=180)

    # submitbtn = customtkinter.CTkButton(root3, text="Submit", border_width=3, text_font=('Calibri', -15, 'bold'), fg_color='blue', command=ClickUpdate).place(x=60, y=200)
    submit_btn = Button(root3, text='Submit', width=11, style='S.TButton', command=WareUpdate)
    submit_btn.place(x=60, y=220)
    exit1 = Button(root3, text='Close', width=11, style='C.TButton', command=root3.destroy)
    exit1.place(x=250, y=220)


def Shipped():
    root3 = Toplevel()
    root3.geometry('380x270')
    root3.title("Record Score")
    root3.config(bg="lightblue2")
    timestampStr = dateTimeObj.strftime("%m-%d-%Y")
    style3 = ttk.Style()
    Balance = StringVar()
    Line  = StringVar()
    Reason = StringVar()
    curItem = tree.focus()
    code = tree.item(curItem)['values'][0]
    desc = tree.item(curItem)['values'][1]
    def ShipUpdate():
        balance = Balance.get()
        line = Line.get()
        reason = Reason.get()
        with sqlite3.connect('Reflex Footwear.sql3') as conn:
            cursor3 = conn.cursor()
            cursor3.execute('UPDATE Production SET ToShip=ToShip-? WHERE Order2=?', [balance, code, ])
            cursor3.execute('UPDATE Production SET Shipped=Shipped+? WHERE Order2=?', [balance, code, ])
            cursor3.execute('UPDATE Production_Balances SET ToShip=ToShip-? WHERE Order2=?', [balance, code, ])
            cursor3.execute('UPDATE Production SET Warehouse=Warehouse-? WHERE Order2=?', [balance, code, ])
            cursor3.execute('INSERT INTO ProductionBreakdown (Factory,Date,Line,Order2,Style,Shipped,Reason) VALUES(?,?,?,?,?,?,?)', ["Reflex", timestampStr, line, code, desc, balance, reason])
            updated = cursor3.rowcount
            cursor3.close()
            conn.commit()
            root3.destroy()
            production()

    def submit_root(e):
       command=ShipUpdate()

    root3.bind('<Return>', lambda e: submit_root(e))

    style3.configure('C.TButton', font=('Arial', 12, 'bold'), foreground='red')
    style3.configure('S.TButton', font=('Arial', 12, 'bold'), foreground='blue')

    label_0 = Label(root3, text="Shipped Quantity", background="lightblue2", width=20, font=("Arial", 20, "bold"))
    label_0.place(x=100, y=23)
    label_2 = Label(root3, text="Truck Reg.", width=20, background="lightblue2", font=("Arial", 12, "bold"))
    label_2.place(x=20, y=100)
    entry_2 = Entry(root3, textvar=Line, background="lightblue2", font=("Arial", 12, "bold"))
    entry_2.place(x=180, y=100)

    label_3 = Label(root3, text="Quantity Sent", width=20, background="lightblue2", font=("Arial", 12, "bold"))
    label_3.place(x=20, y=140)
    entry_3 = Entry(root3, textvar=Balance, background="lightblue2", font=("Arial", 12, "bold"))
    entry_3.place(x=180, y=140)

    label_4 = Label(root3, text="Reason", width=20, background="lightblue2", font=("Arial", 12, "bold"))
    label_4.place(x=20, y=180)
    entry_4 = Entry(root3, textvar=Reason, background="lightblue2", font=("Arial", 12, "bold"))
    entry_4.place(x=180, y=180)

    # submitbtn = customtkinter.CTkButton(root3, text="Submit", border_width=3, text_font=('Calibri', -15, 'bold'), fg_color='blue', command=ClickUpdate).place(x=60, y=200)
    submit_btn = Button(root3, text='Submit', width=11, style='S.TButton', command=ShipUpdate)
    submit_btn.place(x=60, y=220)
    exit1 = Button(root3, text='Close', width=11, style='C.TButton', command=root3.destroy)
    exit1.place(x=250, y=220)

edit2 = Menu(root, tearoff = 0)
#edit.add_separator()
edit2.add_command(label ="Clicking", command = Clicking, activebackground="Blue", font=('Calibri', 14, 'bold'))
#edit.add_separator()
edit2.add_command(label ="Closing", command = Closing, activebackground="Blue", font=('Calibri', 14, 'bold'))
#edit.add_separator()
edit2.add_command(label ="Despatch", command = Despatch, activebackground="Blue", font=('Calibri', 14, 'bold'))
#edit.add_separator()
edit2.add_command(label ="Warehouse", command = Warehouse, activebackground="Blue", font=('Calibri', 14, 'bold'))
#edit.add_separator()
edit2.add_command(label ="Shipped", command = Shipped, activebackground="Blue", font=('Calibri', 14, 'bold'))
#edit.add_separator()


def ClickPB():
    curItem = tree.focus()
    order = tree.item(curItem)['values'][0]
    root2 = Toplevel()
    #root2.state('zoomed') # Windowed view
    root2.attributes('-fullscreen', True)
    root2.title("Production Breakdown")
    root2.config(bg="skyblue2")
    style2 = ttk.Style()
    l_logsheet = Label(root2, text="Production Per Order", width=120, anchor=CENTER, font=["Bodoni MT", 30, "bold"], background="grey80", relief="raised").pack(side='top', ipady=10)

    def close_screen(e):
    	command=root2.destroy()
    root2.bind('<Escape>', lambda e: close_screen(e))

    def prod_break():
        tree2.delete(*tree2.get_children())
        with sqlite3.connect('Reflex Footwear.sql3') as conn:
            mycursor2 = conn.cursor()
            mycursor2.execute("SELECT Date,Order2,Clicking,Closing,Despatch,Warehouse,Shipped FROM ProductionBreakdown WHERE Order2= '{}'".format(order))
            for row in mycursor2:
                    tree2.insert('', 'end',values=row[0:9])

    frame2 = Frame(root2)
    frame2.pack()
    style = ttk.Style()
    style.configure("New.Treeview", bd=2, font=('Calibri', 12))
    style.map('New.Treeview', background=[('selected', 'firebrick')])

    style.configure("New.Heading", font=( "Calibri", 15, 'bold'), background='silver', foreground='black')
    tree2 = ttk.Treeview(frame2, columns=(0, 1, 2, 3, 4, 5, 6), height=44, show="headings", style="New.Treeview")
    tree2.pack(side='left')

    tree2.heading(0, text="Date")
    tree2.heading(1, text="Order No.")
    tree2.heading(2, text="Clicking")
    tree2.heading(3, text="Closing")
    tree2.heading(4, text="Despatch")
    tree2.heading(5, text="Warehouse")
    tree2.heading(6, text="Shipped")

    tree2.column(0, width=160)
    tree2.column(1, width=160)
    tree2.column(2, width=230)
    tree2.column(3, width=160)
    tree2.column(4, width=160)
    tree2.column(5, width=160)
    tree2.column(6, width=160)

    scroll2 = ttk.Scrollbar(frame2, orient="vertical", command=tree2.yview)
    scroll2.pack(side='right', fill='y')

    tree2.configure(yscrollcommand=scroll2.set)

    btn = customtkinter.CTkButton(root2, text="Close (Esc)", border_width=3, text_font=('Calibri', -15, 'bold'), fg_color='red', command=root2.destroy).pack(side='right')

    prod_break()
    root2.mainloop()


def Confirm():
    root3 = Tk()
    root3.geometry('300x160')
    root3.title("Confirm?")
    root3.config(bg="#4a7a8c")
    style3 = ttk.Style()
    label_archive = Label(root3, text="Confirm Archive", width=20, background='#4a7a8c', foreground="white", font=("Arial, bold", 20)).place(x=50, y=30)
    style3 = Style()

    def ClickArch():
        curItem = tree.focus()
        code = tree.item(curItem)['values'][0]

        with sqlite3.connect('Reflex Footwear.sql3') as conn2:
            cursor2 = conn2.cursor()
            cursor2.execute('INSERT INTO MyShoe_Archive SELECT * FROM MyShoe WHERE OrderNo=?', [code])
            cursor2.execute('DELETE FROM MyShoe WHERE OrderNo=?', [code])
            cursor2.execute('INSERT INTO Production_Archive SELECT * FROM Production WHERE Order2=?', [code])
            cursor2.execute('DELETE FROM Production WHERE Order2=?', [code])
            cursor2.execute('INSERT INTO Planning_Archive SELECT * FROM Planning WHERE OrderNo=?', [code])
            cursor2.execute('DELETE FROM Planning WHERE OrderNo=?', [code])
            cursor2.execute('INSERT INTO ProdBreak_Archive SELECT * FROM ProductionBreakdown WHERE Order2=?', [code])
            cursor2.execute('DELETE FROM ProductionBreakdown WHERE Order2=?', [code])
            cursor2.execute('INSERT INTO ProdBal_Archive SELECT * FROM ProductionBreakdown WHERE Order2=?', [code])
            cursor2.execute('DELETE FROM Production_Balances WHERE Order2=?', [code])
            updated = cursor2.rowcount
            cursor2.close()
            conn2.commit()
            root3.destroy()


    style3.configure('Yes.Button', font=('Calibri', 14, 'bold', 'underline'), foreground='dodgerblue4', background='grey80')
    style3.configure('No.Button', font=('Calibri', 14, 'bold', 'underline'), foreground='firebrick', background='grey80')

    confirm_but = Button(root3, text='Yes', width=11, command=ClickArch).place(x=50, y=80)
    exit1 = Button(root3, text='No', width=11, command=root3.destroy).place(x=170, y=80)
    # root3.mainloop()

edit = Menu(root, tearoff = 0)
edit.add_separator()
edit.add_command(label ="Production", command = ClickPB, activebackground="Blue", font=('Calibri', 14))
edit.add_separator()
edit.add_command(label ="Balance", command = Balance, activebackground="red", font=('Calibri', 14))
edit.add_separator()
edit.add_command(label ="Archive", command = Confirm, activebackground="red", font=('Calibri', 14))
edit.add_separator()


def production():
    tree.delete(*tree.get_children())
    tree.tag_configure("evenrow",background='white')
    # tree.tag_configure("oddrow",background='grey80')
    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        mycursor = conn.cursor()
        mycursor.execute("SELECT Order2,Style,Deldate,Orderqty,Clicking,Closing,Finishing,Despatch,Warehouse,ToShip,Shipped FROM Production")
        for row in mycursor:
                tree.insert('', 'end',values=row[0:12])

root.after(1000, production)

frame = Frame(root)
frame.pack()

# Treeview and Configuration
style = ttk.Style()
# Modify the font of the body
style.configure("Treeview", bd=2, font=('Calibri', 12))

# Modify OnClick
style.map('Treeview', background=[('selected', 'firebrick')])

# Modify the font of the heading and select columns
style.configure("Treeview.Heading", font=( "Calibri", 15, 'bold'), background='silver', foreground='black')
tree = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), height=44, show="headings")
tree.pack(side='left')

tree.heading(1, text="Order No.", anchor=N)
tree.heading(2, text="Style/Description")
tree.heading(3, text="Delivery Date")
tree.heading(4, text="Order Qty")
tree.heading(5, text="To Click")
tree.heading(6, text="In Closing")
tree.heading(7, text="In Finishing")
tree.heading(8, text="In Despatch")
tree.heading(9, text="In Warehouse")
tree.heading(10, text="To Ship")
tree.heading(11, text="Shipped")

tree.column(1, width=160)
tree.column(2, width=230)
tree.column(3, width=160)
tree.column(4, width=160)
tree.column(5, width=160)
tree.column(6, width=160)
tree.column(7, width=160)
tree.column(8, width=160)
tree.column(9, width=160)
tree.column(10, width=160)
tree.column(11, width=160)

scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
scroll.pack(side='right', fill='y')

tree.configure(yscrollcommand=scroll.set)


style = Style()
style.configure('R.TButton', font=('Calibri', 14, 'bold', 'underline'), foreground='dodgerblue4', background='grey80')
#style.configure('B.TButton', font=('Calibri', 14, 'bold', 'underline'), foreground='firebrick', background='grey80')


def tkinter1():
    ret = os.system('python update_clicking.py')
    if ret:
        production()


def tkinter2():
    ret = os.system('python update_closing.py')
    if ret:
        production()


def tkinter3():
    ret = os.system('python update_despatch.py')
    if ret:
        production()


def tkinter4():
    ret = os.system('python update_warehouse.py')
    if ret:
        production()


def tkinter5():
    ret = os.system('python update_shipped.py')
    if ret:
        production()


def tkinter6():
    ret = os.system('python excel_export_prod_1.py')
    if ret:
        production()


def tkinter7():
    ret = os.system('python production_breakdown.py')
    if ret:
        production()


def tkinter8():
    ret = os.system('python production_balances.py')
    if ret:
        production()


mb =  Menubutton ( root, text = "Scores", style='R.TButton' )
mb.pack(side='left')
mb.menu  =  Menu ( mb, tearoff = 0, activebackground="red", fg="ghost white", bg="chartreuse4", font=["Calibri", 14])
mb["menu"]  =  mb.menu

mb.menu.add_command (label = "Clicking", command = tkinter1)
mb.menu.add_command (label = "Closing", command = tkinter2)
mb.menu.add_command (label = "Despatch", command = tkinter3)
mb.menu.add_command (label = "Warehouse", command = tkinter4)
mb.menu.add_command (label = "Shipped", command = tkinter5)

mb.pack()
btn = customtkinter.CTkButton(root, text="Close (Esc)", border_width=3, text_font=('Calibri', -15, 'bold'), fg_color='red', command=root.destroy).pack(side='right')
btn5 = customtkinter.CTkButton(root, text="Export", border_width=3, text_font=('Calibri', -15, 'bold'), fg_color='green', command=tkinter6).pack(side='right')
btn6 = customtkinter.CTkButton(root, text="View Scores", border_width=3, text_font=('Calibri', -15, 'bold'), fg_color='green', command=tkinter7).pack(side='left')
btn6 = customtkinter.CTkButton(root, text="View Balances", border_width=3, text_font=('Calibri', -15, 'bold'), fg_color='green', command=tkinter8).pack(side='left')

# btn = Button(root, text='Close (Esc)', style='B.TButton', command=root.destroy).pack(side='right')
# btn5 = Button(root, text="Export", style='R.TButton', command=tkinter6).pack(side='right')
# btn6 = Button(root, text="View Scores", style='R.TButton', command=tkinter7).pack(side='left')

production()

update_time()

root.mainloop()
