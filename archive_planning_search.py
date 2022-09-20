from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *

root = Tk()
root.geometry('830x650')
root.title("Planning")
root.config(bg="skyblue2")
style = ttk.Style()

OrderNo = StringVar()

with sqlite3.connect('Reflex Footwear.sql3') as conn:
    cursor = conn.cursor()
    my_data = cursor.execute("SELECT DISTINCT OrderNo FROM Planning_Archive")
    my_list = [r for r, in my_data]
    options = StringVar()
    options.set(my_list[0])


def pre_search():
    order = options.get()

    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT DatePlanned,OrderNo,Style,Pairs,Delivery,Size8,Size9,Size10,Size11,Size12,Size13,Size1 FROM Planning_Archive WHERE OrderNo=?', (order,))
        results = cursor.fetchall()

        item_0_in_result = [_[0] for _ in results]
        item_0_in_result1 = [_[1] for _ in results]
        item_0_in_result2 = [_[2] for _ in results]
        item_0_in_result3 = [_[3] for _ in results]
        item_0_in_result4 = [_[4] for _ in results]
        item_0_in_result5 = [_[5] for _ in results]
        item_0_in_result6 = [_[6] for _ in results]
        item_0_in_result7 = [_[7] for _ in results]
        item_0_in_result8 = [_[8] for _ in results]
        item_0_in_result9 = [_[9] for _ in results]
        item_0_in_result10 = [_[10] for _ in results]
        item_0_in_result11 = [_[11] for _ in results]

        Label(root, text="Date Planned:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=150)
        Label(root, text=item_0_in_result, width=60, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=150)

        Label(root, text="Order No:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=200)
        Label(root, text=item_0_in_result1, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=200)

        Label(root, text="Style/Description:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=250)
        Label(root, text=item_0_in_result2, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=250)

        Label(root, text="Order Quantity:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=300)
        Label(root, text=item_0_in_result3, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=300)

        Label(root, text="Delivery Date:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=350)
        Label(root, text=item_0_in_result4, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=350)

        Label(root, text="Size 8:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=400)
        Label(root, text=item_0_in_result5, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=400)

        Label(root, text="Size 9:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=450)
        Label(root, text=item_0_in_result6, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=450)

        Label(root, text="Size 10:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=500)
        Label(root, text=item_0_in_result7, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=500)

        Label(root, text="Size 11:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=550)
        Label(root, text=item_0_in_result8, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=550)

        Label(root, text="Size 12:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=300, y=400)
        Label(root, text=item_0_in_result9, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=460, y=400)

        Label(root, text="Size 13:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=300, y=450)
        Label(root, text=item_0_in_result10, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=460, y=450)

        Label(root, text="Size 1:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=300, y=500)
        Label(root, text=item_0_in_result11, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=460, y=500)

        cursor.close()
        conn.commit()


def boys_search():
    order = options.get()

    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT DatePlanned,OrderNo,Style,Pairs,Delivery,Size2,Size3,Size4,Size5 FROM Planning_Archive WHERE OrderNo=?', (order,))
        results = cursor.fetchall()

        item_0_in_result = [_[0] for _ in results]
        item_0_in_result1 = [_[1] for _ in results]
        item_0_in_result2 = [_[2] for _ in results]
        item_0_in_result3 = [_[3] for _ in results]
        item_0_in_result4 = [_[4] for _ in results]
        item_0_in_result5 = [_[5] for _ in results]
        item_0_in_result6 = [_[6] for _ in results]
        item_0_in_result7 = [_[7] for _ in results]
        item_0_in_result8 = [_[8] for _ in results]

        Label(root, text="Date Planned:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=150)
        Label(root, text=item_0_in_result, width=60, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=150)

        Label(root, text="Order No:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=200)
        Label(root, text=item_0_in_result1, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=200)

        Label(root, text="Style/Description:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=250)
        Label(root, text=item_0_in_result2, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=250)

        Label(root, text="Order Quantity:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=300)
        Label(root, text=item_0_in_result3, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=300)

        Label(root, text="Delivery Date:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=350)
        Label(root, text=item_0_in_result4, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=350)

        Label(root, text="Size 2:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=400)
        Label(root, text=item_0_in_result5, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=400)

        Label(root, text="Size 3:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=450)
        Label(root, text=item_0_in_result6, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=450)

        Label(root, text="Size 4:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=500)
        Label(root, text=item_0_in_result7, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=500)

        Label(root, text="Size 5:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=550)
        Label(root, text=item_0_in_result8, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=550)

        cursor.close()
        conn.commit()


def mens_search():
    order = options.get()

    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT DatePlanned,OrderNo,Style,Pairs,Delivery,Size6,Size7,Size8b,Size9b,Size10b FROM Planning_Archive WHERE OrderNo=?', (order,))
        results = cursor.fetchall()

        item_0_in_result = [_[0] for _ in results]
        item_0_in_result1 = [_[1] for _ in results]
        item_0_in_result2 = [_[2] for _ in results]
        item_0_in_result3 = [_[3] for _ in results]
        item_0_in_result4 = [_[4] for _ in results]
        item_0_in_result5 = [_[5] for _ in results]
        item_0_in_result6 = [_[6] for _ in results]
        item_0_in_result7 = [_[7] for _ in results]
        item_0_in_result8 = [_[8] for _ in results]
        item_0_in_result9 = [_[9] for _ in results]

        Label(root, text="Date Planned:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=150)
        Label(root, text=item_0_in_result, width=60, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=150)

        Label(root, text="Order No:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=200)
        Label(root, text=item_0_in_result1, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=200)

        Label(root, text="Style/Description:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=250)
        Label(root, text=item_0_in_result2, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=250)

        Label(root, text="Order Quantity:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=300)
        Label(root, text=item_0_in_result3, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=300)

        Label(root, text="Delivery Date:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=350)
        Label(root, text=item_0_in_result4, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=350)

        Label(root, text="Size 6:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=400)
        Label(root, text=item_0_in_result5, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=400)

        Label(root, text="Size 7:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=450)
        Label(root, text=item_0_in_result6, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=450)

        Label(root, text="Size 8:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=500)
        Label(root, text=item_0_in_result7, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=500)

        Label(root, text="Size 9:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=550)
        Label(root, text=item_0_in_result8, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=550)

        Label(root, text="Size 10:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=400, y=400)
        Label(root, text=item_0_in_result9, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=560, y=400)

        cursor.close()
        conn.commit()


def girls_search():
    order = options.get()

    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT DatePlanned,OrderNo,Style,Pairs,Delivery,Size2,Size3,Size4,Size5,Size6,Size7,Size8b FROM Planning_Archive WHERE OrderNo=?', (order,))
        results = cursor.fetchall()

        item_0_in_result = [_[0] for _ in results]
        item_0_in_result1 = [_[1] for _ in results]
        item_0_in_result2 = [_[2] for _ in results]
        item_0_in_result3 = [_[3] for _ in results]
        item_0_in_result4 = [_[4] for _ in results]
        item_0_in_result5 = [_[5] for _ in results]
        item_0_in_result6 = [_[6] for _ in results]
        item_0_in_result7 = [_[7] for _ in results]
        item_0_in_result8 = [_[8] for _ in results]
        item_0_in_result9 = [_[9] for _ in results]
        item_0_in_result10 = [_[10] for _ in results]
        item_0_in_result11 = [_[11] for _ in results]

        Label(root, text="Date Planned:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=150)
        Label(root, text=item_0_in_result, width=60, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=150)

        Label(root, text="Order No:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=200)
        Label(root, text=item_0_in_result1, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=200)

        Label(root, text="Style/Description:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=250)
        Label(root, text=item_0_in_result2, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=250)

        Label(root, text="Order Quantity:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=300)
        Label(root, text=item_0_in_result3, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=300)

        Label(root, text="Delivery Date:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=350)
        Label(root, text=item_0_in_result4, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=350)

        Label(root, text="Size 2:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=400)
        Label(root, text=item_0_in_result5, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=400)

        Label(root, text="Size 3:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=450)
        Label(root, text=item_0_in_result6, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=450)

        Label(root, text="Size 4:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=500)
        Label(root, text=item_0_in_result7, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=500)

        Label(root, text="Size 5:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=20, y=550)
        Label(root, text=item_0_in_result8, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=180, y=550)

        Label(root, text="Size 6:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=400, y=400)
        Label(root, text=item_0_in_result9, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=560, y=400)

        Label(root, text="Size 7:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=400, y=450)
        Label(root, text=item_0_in_result10, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=560, y=450)

        Label(root, text="Size 8:", width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=400, y=500)
        Label(root, text=item_0_in_result11, width=20, background="skyblue2",
              foreground="black", font=("Arial, bold", 12)).place(x=560, y=500)

        cursor.close()
        conn.commit()


label_0 = Label(root, text="Search Size Range", width=18, background="skyblue2",
                foreground="grey15", font=("Arial, bold", 20)).place(x=300, y=23)

label_1 = Label(root, text="Order No.", width=20, background="skyblue2",
                foreground="grey15", font=("Arial, bold", 16)).place(x=250, y=90)

# Changed Normal input to Option Menu
# entry_1 = Entry(root, textvar=OrderNo, background="skyblue2", width=19, font=("Arial Narrow, bold", 14)).place(x=380, y=90)
option_1 = OptionMenu(root, options, *my_list).place(x=380, y=90)

# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'), foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'), foreground='blue')

# Inserting buttons
submit1 = Button(root, text='Pre-Boys/Pre-Girls', style='S.TButton',
                 width=16, command=pre_search).place(x=20, y=600)
submit2 = Button(root, text='Boys', style='S.TButton',
                 width=16, command=boys_search).place(x=180, y=600)
submit3 = Button(root, text='Mens', style='S.TButton',
                 width=16, command=mens_search).place(x=340, y=600)
submit4 = Button(root, text='Girls', style='S.TButton',
                 width=16, command=girls_search).place(x=500, y=600)
exit1 = Button(root, text='Close', style='C.TButton', width=16,
               command=root.destroy).place(x=660, y=600)

root.mainloop()
