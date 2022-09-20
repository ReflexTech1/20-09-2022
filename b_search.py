from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *

root = Tk()
root.geometry('480x550')
root.title("Balance")
root.config(bg="")
style = ttk.Style()

OrderNo = StringVar()

with sqlite3.connect('Reflex Footwear.sql3') as conn:
    cursor = conn.cursor()
    my_data = cursor.execute("SELECT Order3 FROM HandlacingB")
    my_list = [r for r, in my_data]
    options = StringVar()
    options.set(my_list[0])


def b_search():
    order = options.get()

    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT DateB,SUM(Size2),SUM(Size3),SUM(Size4),SUM(Size5) FROM HandlacingB WHERE Order3=?', (order,))
        results = cursor.fetchall()

        item_0_in_result = [_[0] for _ in results]
        item_0_in_result1 = [_[1] for _ in results]
        item_0_in_result2 = [_[2] for _ in results]
        item_0_in_result3 = [_[3] for _ in results]
        item_0_in_result4 = [_[4] for _ in results]

        Label(root, text="Last movement:", width=20, background="white",
              foreground="", font=("Arial, bold", 14)).place(x=40, y=200)
        Label(root, text=item_0_in_result, width=15, background="white",
              foreground="", font=("Arial, bold", 14)).place(x=250, y=200)

        Label(root, text="Size 2:", width=20, background="white",
              foreground="", font=("Arial, bold", 14)).place(x=40, y=250)
        Label(root, text=item_0_in_result1, width=15, background="white",
              foreground="", font=("Arial, bold", 14)).place(x=250, y=250)

        Label(root, text="Size 3:", width=20, background="white",
              foreground="", font=("Arial, bold", 14)).place(x=40, y=300)
        Label(root, text=item_0_in_result2, width=15, background="white",
              foreground="", font=("Arial, bold", 14)).place(x=250, y=300)

        Label(root, text="Size 4:", width=20, background="white",
              foreground="", font=("Arial, bold", 14)).place(x=40, y=350)
        Label(root, text=item_0_in_result3, width=15, background="white",
              foreground="", font=("Arial, bold", 14)).place(x=250, y=350)

        Label(root, text="Size 5:", width=20, background="white",
              foreground="", font=("Arial, bold", 14)).place(x=40, y=400)
        Label(root, text=item_0_in_result4, width=15, background="white",
              foreground="", font=("Arial, bold", 14)).place(x=250, y=400)

        cursor.close()
        conn.commit()


label_0 = Label(root, text="Search Boys Idler", width=16, background="white",
                foreground="", font=("Arial, bold", 20)).place(x=140, y=23)

label_1 = Label(root, text="Order No.", width=20, background="white",
                foreground="", font=("Arial, bold", 16)).place(x=60, y=90)

# Changed Normal input to Option Menu
# entry_1 = Entry(root, textvar=OrderNo, background="", font=("Arial Narrow, bold", 14)).place(x=200, y=90)
option_1 = OptionMenu(root, options, *my_list).place(x=160, y=90)

# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'), foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'), foreground='blue')

# Inserting buttons
submit1 = Button(root, text='Search', style='S.TButton',
                 width=11, command=b_search).place(x=20, y=500)
exit1 = Button(root, text='Close', style='C.TButton', width=11,
               command=root.destroy).place(x=350, y=500)

root.mainloop()
