from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *

root = Tk()
root.geometry('800x550')
root.title("")
root.config(bg="skyblue2")
style = ttk.Style()

OrderNo = StringVar()

with sqlite3.connect('Reflex Footwear.sql3') as conn:
    cursor = conn.cursor()
    my_data = cursor.execute(
        "SELECT Order2 FROM SandalProduction ORDER BY Order2 ASC")
    my_list = [r for r, in my_data]
    options = StringVar()
    options.set(my_list[0])

l1 = Label(root, text="Search Individual Order", width=120, anchor=CENTER, font=["Bodoni MT", 30, "bold"], background="skyblue2", relief="raised").pack(side='top', ipady=10)

def production_search():
    order = options.get()

    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT Factory,Planned,Order2,Style,Deldate,Orderqty,Cutting,Assembly,Closing,Finishing,Despatch,ToShip,Shipped FROM SlipProduction WHERE Order2=?', (order,))
        results = cursor.fetchall()

        item_0_in_result = [_[0] for _ in results] # Factory
        item_0_in_result1 = [_[1] for _ in results] # Planned
        item_0_in_result2 = [_[2] for _ in results] # OrderNo
        item_0_in_result3 = [_[3] for _ in results] # Style
        item_0_in_result4 = [_[4] for _ in results] # Delivery date
        item_0_in_result5 = [_[5] for _ in results] # Quantity
        item_0_in_result6 = [_[6] for _ in results] # Clicking
        item_0_in_result7 = [_[7] for _ in results] # Closing
        item_0_in_result8 = [_[8] for _ in results] # Finishing
        item_0_in_result9 = [_[9] for _ in results] # Despatch
        item_0_in_result10 = [_[10] for _ in results] # To Ship
        item_0_in_result11 = [_[11] for _ in results] # Shipped

        Label(root, text="Factory:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=40, y=150)
        Label(root, text=item_0_in_result, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=250, y=150)

        Label(root, text="Planned:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=40, y=200)
        Label(root, text=item_0_in_result1, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=250, y=200)

        Label(root, text="Order No:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=40, y=250)
        Label(root, text=item_0_in_result2, width=60, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=250, y=250)

        Label(root, text="Style/Description:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=40, y=300)
        Label(root, text=item_0_in_result3, width=22, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=250, y=300)

        Label(root, text="Delivery Date:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=40, y=350)
        Label(root, text=item_0_in_result4, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=250, y=350)

        Label(root, text="Order Quantity:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=40, y=400)
        Label(root, text=item_0_in_result5, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=250, y=400)

        Label(root, text="Balance To Click:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=500, y=150)
        Label(root, text=item_0_in_result6, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=710, y=150)

        Label(root, text="In Closing:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=500, y=200)
        Label(root, text=item_0_in_result7, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=710, y=200)

        Label(root, text="In Finishing:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=500, y=250)
        Label(root, text=item_0_in_result8, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=710, y=250)

        Label(root, text="In Despatch:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=500, y=300)
        Label(root, text=item_0_in_result9, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=710, y=300)

        Label(root, text="Balance To Ship:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=500, y=350)
        Label(root, text=item_0_in_result10, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=710, y=350)

        Label(root, text="Shipped:", width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=500, y=400)
        Label(root, text=item_0_in_result11, width=20, background="skyblue2", foreground="", font=("Arial, bold", 14)).place(x=710, y=400)

        cursor.close()
        conn.commit()



label_1 = Label(root, text="Order No.", width=20, background="skyblue2", foreground="grey15", font=("Arial", 16, "bold")).place(x=120, y=90)

# Changed Normal input to Option Menu
# entry_1 = Entry(root, textvar=OrderNo, width=18, background="skyblue2", font=("Arial Narrow, bold", 14)).place(x=250, y=90)
option_1 = OptionMenu(root, options, *my_list).place(x=260, y=90)

# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'), foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'), foreground='blue')

# Inserting buttons
submit1 = Button(root, text='Search', style='S.TButton', width=11, command=production_search).place(x=20, y=500)
exit1 = Button(root, text='Close', style='C.TButton', width=11, command=root.destroy).place(x=650, y=500)

root.mainloop()
