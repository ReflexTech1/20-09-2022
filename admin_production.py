from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
import os
from datetime import datetime
from datetime import timedelta # used to check/manipulate dates from today: yesterday1 = today1 - timedelta(days = 1)
#import customtkinter
#from PIL import Image, ImageTk
#import tkinter.messagebox

root = Tk()
root.state('zoomed') # Windowed view
#root.attributes('-fullscreen', True)
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


def ClickStat(event):
    curItem = tree.focus()
    order = tree.item(curItem)['values'][0]
    desc = 0
    root2 = Tk()
    root2.geometry('820x510')
    root2.title("Production Status")
    root2.config(bg="skyblue2")
    style2 = ttk.Style()
    l_prod = Label(root2, text="Order Details", width=120, anchor=CENTER, font=["Bodoni MT", 30, "bold"], background="grey80", relief="raised").pack(side='top', ipady=10)
    def close_screen2(e):
    	command=root2.destroy()
    root2.bind('<Escape>', lambda e: close_screen2(e))

    if order is not None:
        with sqlite3.connect('Reflex Footwear.sql3') as conn2:
            cursor2 = conn2.cursor()
            cursor2.execute('SELECT Factory,Planned,Order2,Style,Deldate,Orderqty,Clicking,Closing,Finishing,Despatch,Warehouse,ToShip,Shipped FROM Production WHERE Order2=?', (order,))
            results = cursor2.fetchall()

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


            Label(root2, text="Planned:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=40, y=150)
            Label(root2, text=item_0_in_result1, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=250, y=150)

            Label(root2, text="Order No:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=40, y=200)
            Label(root2, text=item_0_in_result2, width=60, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=250, y=200)

            Label(root2, text="Style/Description:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=40, y=250)
            Label(root2, text=result_as_text3, width=22, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=250, y=250)

            Label(root2, text="Delivery Date:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=40, y=300)
            Label(root2, text=item_0_in_result4, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=250, y=300)

            Label(root2, text="Order Quantity:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=40, y=350)
            Label(root2, text=item_0_in_result5, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=250, y=350)

            Label(root2, text="Balance To Click:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=500, y=150)
            Label(root2, text=item_0_in_result6, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=710, y=150)

            Label(root2, text="In Closing:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=500, y=200)
            Label(root2, text=item_0_in_result7, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=710, y=200)

            Label(root2, text="In Finishing:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=500, y=250)
            Label(root2, text=item_0_in_result8, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=710, y=250)

            Label(root2, text="In Despatch:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=500, y=300)
            Label(root2, text=item_0_in_result9, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=710, y=300)

            Label(root2, text="In Warehouse:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=500, y=350)
            Label(root2, text=item_0_in_result10, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=710, y=350)

            Label(root2, text="Balance To Ship:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=500, y=400)
            Label(root2, text=item_0_in_result11, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=710, y=400)

            Label(root2, text="Shipped:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=500, y=450)
            Label(root2, text=item_0_in_result12, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=710, y=450)

            cursor2.close()


def ClickPB():
    curItem = tree.focus()
    order = tree.item(curItem)['values'][0]
    root2 = Tk()
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
            mycursor2.execute("SELECT Date,Order2,Clicking,Closing,Despatch,Shipped FROM ProductionBreakdown WHERE Order2= '{}'".format(order))
            for row in mycursor2:
                    tree2.insert('', 'end',values=row[0:9])

    frame2 = Frame(root2)
    frame2.pack()
    style = ttk.Style()
    style.configure("New.Treeview", bd=2, font=('Calibri', 12))
    style.map('New.Treeview', background=[('selected', 'firebrick')])

    style.configure("New.Heading", font=( "Calibri", 15, 'bold'), background='silver', foreground='black')
    tree2 = ttk.Treeview(frame2, columns=(0, 1, 2, 3, 4, 5), height=44, show="headings", style="New.Treeview")
    tree2.pack(side='left')

    tree2.heading(0, text="Date")
    tree2.heading(1, text="Order No.")
    tree2.heading(2, text="Clicking")
    tree2.heading(3, text="Closing")
    tree2.heading(4, text="Despatch")
    tree2.heading(5, text="Shipped")

    tree2.column(0, width=160)
    tree2.column(1, width=160)
    tree2.column(2, width=230)
    tree2.column(3, width=160)
    tree2.column(4, width=160)
    tree2.column(5, width=160)

    scroll2 = ttk.Scrollbar(frame2, orient="vertical", command=tree2.yview)
    scroll2.pack(side='right', fill='y')

    tree2.configure(yscrollcommand=scroll2.set)

    exit1 = Button(root2, text='Close (Esc)', width=11, command=root2.destroy).pack(side='right')

    prod_break()
    root2.mainloop()
root.bind("<Double-1>", ClickStat)


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
            cursor2.execute('INSERT INTO ProdBal_Archive SELECT * FROM ProductionBalances WHERE Order2=?', [code])
            cursor2.execute('DELETE FROM ProductionBalances WHERE Order2=?', [code])
            updated = cursor2.rowcount
            cursor2.close()
            conn2.commit()
            root3.destroy()


    style3.configure('Yes.Button', font=('Calibri', 14, 'bold', 'underline'), foreground='dodgerblue4', background='grey80')
    style3.configure('No.Button', font=('Calibri', 14, 'bold', 'underline'), foreground='firebrick', background='grey80')

    confirm_but = Button(root3, text='Yes', width=11, command=ClickArch).place(x=50, y=80)
    exit1 = Button(root3, text='No', width=11, command=root3.destroy).place(x=170, y=80)
    # confirm_but = customtkinter.CTkButton(root3, text="Yes", border_width=1, text_font=('Calibri', -14, 'bold'), fg_color='green', command=ClickArch).place(x=90, y=80)
    # exit1 = customtkinter.CTkButton(root3, text="No", border_width=1, text_font=('Calibri', -14, 'bold'), fg_color='red', command=root3.destroy).place(x=90, y=120)

    # root3.mainloop()

edit = Menu(root, tearoff = 0)
edit.add_separator()
edit.add_command(label ="Production", command = ClickPB, activebackground="Blue", font=('Calibri', 14))
edit.add_separator()
edit.add_command(label ="Balance", command = Balance, activebackground="red", font=('Calibri', 14))
edit.add_separator()
edit.add_command(label ="Archive", command = Confirm, activebackground="red", font=('Calibri', 14))
edit.add_separator()
root.bind("<Button-3>", do_popup)

def production():
    tree.delete(*tree.get_children())
    tree.tag_configure("evenrow",background='white')
    # tree.tag_configure("oddrow",background='grey80')
    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        mycursor = conn.cursor()
        mycursor.execute("SELECT Order2,Style,Deldate,Orderqty,Clicking,Closing,Finishing,Despatch,Warehouse,ToShip FROM Production ORDER BY DelDate ASC")
        for row in mycursor:
                tree.insert('', 'end',values=row[0:12])

frame = Frame(root)
frame.pack()

# Treeview and Configuration
style = ttk.Style()
# Modify the font of the body
style.configure("Treeview", bd=2, font=('Calibri', 11))

# Modify OnClick
style.map('Treeview', background=[('selected', 'firebrick')])

# Modify the font of the heading and select columns
style.configure("Treeview.Heading", font=( "Calibri", 13, 'bold'), background='silver', foreground='black')
tree = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), height=24, show="headings")
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

tree.column(1, width=130)
tree.column(2, width=210)
tree.column(3, width=130)
tree.column(4, width=130)
tree.column(5, width=130)
tree.column(6, width=130)
tree.column(7, width=130)
tree.column(8, width=130)
tree.column(9, width=130)
tree.column(10, width=130)

scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
scroll.pack(side='right', fill='y')

tree.configure(yscrollcommand=scroll.set)


style = Style()
style.configure('R.TButton', font=('Calibri', 12, 'bold', 'underline'), foreground='dodgerblue4', background='grey80')
style.configure('B.TButton', font=('Calibri', 12, 'bold', 'underline'), foreground='firebrick', background='grey80')


def tkinter6():
    ret = os.system('python excel_export_prod_1.py')
    if ret:
        production()


def tkinter7():
    ret = os.system('python production_breakdown.py')
    if ret:
        production()


def tkinter8():
    ret = os.system('python admin_production_by_date_dep.py')
    if ret:
        production()


def tkinter9():
    ret = os.system('python admin_production_balances.py')
    if ret:
        production()


#btn = customtkinter.CTkButton(root, text="Close (Esc)", border_width=3, text_font=('Calibri', -15, 'bold'), fg_color='green', command=root.destroy).pack(side='right')
#btn5 = customtkinter.CTkButton(root, text="Export", border_width=3, text_font=('Calibri', -15, 'bold'), fg_color='green', command=tkinter6).pack(side='right')
#btn6 = customtkinter.CTkButton(root, text="View Scores", border_width=3, text_font=('Calibri', -15, 'bold'), fg_color='green', command=tkinter7).pack(side='left')

btn = Button(root, text='Close (Esc)', style='B.TButton', command=root.destroy).pack(side='right')
btn5 = Button(root, text="Export", style='R.TButton', command=tkinter6).pack(side='right')
btn6 = Button(root, text="View Scores", style='R.TButton', command=tkinter7).pack(side='left')
btn6 = Button(root, text="Filter Scores", style='R.TButton', command=tkinter8).pack(side='left')
btn6 = Button(root, text="Balances", style='R.TButton', command=tkinter9).pack(side='left')

production()

update_time()

root.mainloop()
