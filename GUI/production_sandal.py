from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
import os
from datetime import datetime

root = Tk()
# root.state('zoomed') # Windowed view
root.attributes('-fullscreen', True)
root.title("Manufacturing")
root.config(bg="lightblue2")

dateTimeObj = datetime.now()
xstampStr = dateTimeObj.strftime("%H:%M:%S %p")

l1 = Label(root, text="Sandal Production Tracker", width=120, anchor=CENTER, font=["Bodoni MT", 30, "bold"], background="grey80", relief="raised").pack(side='top', ipady=10)
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


def DblClick(event):
    curItem = tree.focus()
    order = tree.item(curItem)['values'][0]
    desc = 0
    root2 = Tk()
    root2.geometry('820x500')
    root2.title("Production Breakdown")
    root2.config(bg="skyblue2")
    style2 = ttk.Style()
    l_prod = Label(root2, text="Order Details", width=120, anchor=CENTER, font=["Bodoni MT", 30, "bold"], background="grey80", relief="raised").pack(side='top', ipady=10)
    if order is not None:
        with sqlite3.connect('Reflex Footwear.sql3') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT Factory,Planned,Order2,Style,Deldate,Orderqty,Clicking,Closing,Finishing,Despatch,ToShip,Shipped FROM SlipProduction WHERE Order2=?', (order,))
            results = cursor.fetchall()

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
            item_0_in_result10 = [_[10] for _ in results] # To Ship
            item_0_in_result11 = [_[11] for _ in results] # Shipped


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

            Label(root2, text="Balance To Ship:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=500, y=350)
            Label(root2, text=item_0_in_result10, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=710, y=350)

            Label(root2, text="Shipped:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=500, y=400)
            Label(root2, text=item_0_in_result11, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=710, y=400)

            cursor.close()

root.bind("<Double-1>", DblClick)


def production():
    tree.delete(*tree.get_children())
    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        mycursor = conn.cursor()
        mycursor.execute("SELECT Factory,Planned,Order2,Style,Deldate,Orderqty,Clicking,Closing,Finishing,Despatch,ToShip FROM SandalProduction ORDER BY Order2 ASC")
        for row in mycursor:
            tree.insert('', 'end', values=row[2:11])


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
tree = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), height=44, show="headings")
tree.pack(side='left')

tree.heading(1, text="Order No.")
tree.heading(2, text="Style/Description")
tree.heading(3, text="Delivery Date")
tree.heading(4, text="Quantity")
tree.heading(5, text="Clicking")
tree.heading(6, text="Closing")
tree.heading(7, text="Finishing")
tree.heading(8, text="Despatch")
tree.heading(9, text="To Ship")

tree.column(1, width=160)
tree.column(2, width=230)
tree.column(3, width=160)
tree.column(4, width=160)
tree.column(5, width=160)
tree.column(6, width=160)
tree.column(7, width=160)
tree.column(8, width=160)
tree.column(9, width=160)

scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
scroll.pack(side='right', fill='y')

tree.configure(yscrollcommand=scroll.set)

style = Style()
style.configure('R.TButton', font=('Calibri', 14, 'bold', 'underline'), foreground='dodgerblue4', background='grey80')
style.configure('B.TButton', font=('Calibri', 14, 'bold', 'underline'), foreground='firebrick', background='grey80')


def tkinter1():
    ret = os.system('python update_clicking_sandal.py')
    if ret:
        production()


def tkinter2():
    ret = os.system('python update_closing_sandal.py')
    if ret:
        production()


def tkinter3():
    ret = os.system('python update_despatch_sandal.py')
    if ret:
        production()


def tkinter4():
    ret = os.system('python update_shipped_sandal.py')
    if ret:
        production()


def tkinter6():
    ret = os.system('python excel_export_prod_sand.py')
    if ret:
        production()


def tkinter7():
    ret = os.system('python production_breakdown.py')
    if ret:
        production()


btn = Button(root, text='Close (Esc)', style='B.TButton',
             command=root.destroy).pack(side='right')

mb =  Menubutton ( root, text = "Scores", style='R.TButton' )
mb.pack(side='left')
mb.menu  =  Menu ( mb, tearoff = 0, activebackground="red", fg="ghost white", bg="chartreuse4", font=["Calibri", 14])
mb["menu"]  =  mb.menu

mb.menu.add_command (label = "Clicking", command = tkinter1)
mb.menu.add_command (label = "Closing", command = tkinter2)
mb.menu.add_command (label = "Despatch", command = tkinter3)
mb.menu.add_command (label = "Shipped", command = tkinter4)

mb.pack()
btn6 = Button(root, text="View Scores", style='R.TButton', command=tkinter4).pack(side='left')
btn5 = Button(root, text="Export", style='R.TButton', command=tkinter6).pack(side='right')


production()

update_time()

root.mainloop()
