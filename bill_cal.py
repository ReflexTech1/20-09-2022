from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
import math

root = Tk()
root.geometry('550x600')
root.title("Costing / Order")
root.config(bg="lightgreen")
style = ttk.Style()

Quantity = StringVar()


def calc(filter):
    qty = Quantity.get()
    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        cursor = conn.cursor()
        conn.create_function("CEIL", 1, lambda v: int(math.ceil(v)))
        # ^ to round Quantity
        cursor.execute('SELECT CEIL(Upper*?),'
                       'CEIL(Stiffener*?),'
                       'CEIL(Insole*?),'
                       'CEIL(Sock*?),'
                       'CEIL(Laces*?),'
                       'CEIL(Eyelets*?),'
                       'CEIL(Foil*?),'
                       'CEIL(GussetElastic*?),'
                       'CEIL(Soles*?),'
                       'CEIL(PBA887*?),'
                       'CEIL(IA80*?),'
                       'CEIL(Cartons*?)'
                       'FROM Costing WHERE Type=?',
                       (qty, qty, qty, qty, qty, qty, qty, qty, qty, qty, qty, qty, filter,))
        results = cursor.fetchall()

        item_0_in_result0 = [_[0] for _ in results]
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

        result0.config(text=item_0_in_result0)
        result1.config(text=item_0_in_result1)
        result2.config(text=item_0_in_result2)
        result3.config(text=item_0_in_result3)
        result4.config(text=item_0_in_result4)
        result5.config(text=item_0_in_result5)
        result6.config(text=item_0_in_result6)
        result7.config(text=item_0_in_result7)
        result8.config(text=item_0_in_result8)
        result9.config(text=item_0_in_result9)
        result10.config(text=item_0_in_result10)
        result11.config(text=item_0_in_result11)

        cursor.close()
        conn.commit()


# Result labels
Label(root, text="Upper Material:", width=20, background="lightgreen",
      font=("Arial, bold", 11)).place(x=80, y=160)
result0 = Label(root, width=40, background="lightgreen",
                font=("Arial, bold", 11))
result0.place(x=250, y=160)
Label(root, text="MET", width=20, background="lightgreen",
      font=("Arial, bold", 11)).place(x=320, y=160)

Label(root, text="Stiffener:", width=20, background="lightgreen",
      font=("Arial, bold", 11)).place(x=80, y=180)
result1 = Label(root, width=20, background="lightgreen",
                font=("Arial, bold", 11))
result1.place(x=250, y=180)
Label(root, text="M2", width=20, background="lightgreen",
      font=("Arial, bold", 11)).place(x=320, y=180)

Label(root, text="Insole:", width=20, background="lightgreen",
      font=("Arial, bold", 11)).place(x=80, y=200)
result2 = Label(root, width=20, background="lightgreen",
                font=("Arial, bold", 11))
result2.place(x=250, y=200)
Label(root, text="M2", width=20, background="lightgreen",
      font=("Arial, bold", 11)).place(x=320, y=200)

Label(root, text="PU Lining:", width=20, background="lightgreen",
      font=("Arial, bold", 11)).place(x=80, y=220)
result3 = Label(root, width=20, background="lightgreen",
                font=("Arial, bold", 11))
result3.place(x=250, y=220)
Label(root, text="MET", width=20, background="lightgreen",
      font=("Arial, bold", 11)).place(x=320, y=220)

Label(root, text="Laces:", width=20, background="lightgreen",
      font=("Arial, bold", 11)).place(x=80, y=240)
result4 = Label(root, width=20, background="lightgreen",
                font=("Arial, bold", 11))
result4.place(x=250, y=240)
Label(root, text="PAIR", width=20, background="lightgreen",
      font=("Arial, bold", 11)).place(x=320, y=240)

Label(root, text="Eyelets:", width=20, background="lightgreen",
      font=("Arial, bold", 11)).place(x=80, y=260)
result5 = Label(root, width=20, background="lightgreen",
                font=("Arial, bold", 11))
result5.place(x=250, y=260)
Label(root, text="EACH", width=20, background="lightgreen",
      font=("Arial, bold", 11)).place(x=320, y=260)

Label(root, text="Foil:", width=20, background="lightgreen",
      font=("Arial, bold", 11)).place(x=80, y=280)
result6 = Label(root, width=20, background="lightgreen",
                font=("Arial, bold", 11))
result6.place(x=250, y=280)
Label(root, text="ROLL", width=20, background="lightgreen",
      font=("Arial, bold", 11)).place(x=320, y=280)

Label(root, text="Gusset Elastic:", width=20, background="lightgreen",
      font=("Arial, bold", 11)).place(x=80, y=300)
result7 = Label(root, width=20, background="lightgreen",
                font=("Arial, bold", 11))
result7.place(x=250, y=300)
Label(root, text="MET", width=20, background="lightgreen",
      font=("Arial, bold", 11)).place(x=320, y=300)

Label(root, text="Soles:", width=20, background="lightgreen",
      font=("Arial, bold", 11)).place(x=80, y=320)
result8 = Label(root, width=20, background="lightgreen",
                font=("Arial, bold", 11))
result8.place(x=250, y=320)
Label(root, text="PAIR", width=20, background="lightgreen",
      font=("Arial, bold", 11)).place(x=320, y=320)

Label(root, text="PBA 887:", width=20, background="lightgreen",
      font=("Arial, bold", 11)).place(x=80, y=340)
result9 = Label(root, width=20, background="lightgreen",
                font=("Arial, bold", 11))
result9.place(x=250, y=340)
Label(root, text="EACH", width=20, background="lightgreen",
      font=("Arial, bold", 11)).place(x=320, y=340)

Label(root, text="IA 80 Solution:", width=20, background="lightgreen",
      font=("Arial, bold", 11)).place(x=80, y=360)
result10 = Label(root, width=20, background="lightgreen",
                 font=("Arial, bold", 11))
result10.place(x=250, y=360)
Label(root, text="EACH", width=20, background="lightgreen",
      font=("Arial, bold", 11)).place(x=320, y=360)

Label(root, text="Cartons:", width=20, background="lightgreen",
      font=("Arial, bold", 11)).place(x=80, y=380)
result11 = Label(root, width=20, background="lightgreen",
                 font=("Arial, bold", 11))
result11.place(x=250, y=380)
Label(root, text="EACH", width=20, background="lightgreen",
      font=("Arial, bold", 11)).place(x=320, y=380)

label_0 = Label(root, text="Calculate Costing / Order", width=25, background="lightgreen",
                foreground="grey15", font=("Arial, bold", 20)).place(x=120, y=23)

label_1 = Label(root, text="Quantity", width=18, background="lightgreen",
                foreground="grey15", font=("Arial, bold", 16)).place(x=80, y=70)
entry_1 = Entry(root, textvar=Quantity, width=15, background="lightgreen", font=(
    "Arial Narrow, bold", 14)).place(x=250, y=70)

# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'), foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'), foreground='blue')

# Inserting buttons
Button(root, text='Pre-Boys Synthetic', style='S.TButton', width=17,
       command=lambda: calc(r'Pre-Boys Synthetic')).place(x=20, y=420)
Button(root, text='Boys Synthetic', style='S.TButton', width=17,
       command=lambda: calc(r'Boys Synthetic')).place(x=20, y=460)
Button(root, text='Mens Synthetic', style='S.TButton', width=17,
       command=lambda: calc(r'Mens Synthetic')).place(x=20, y=500)
Button(root, text='Pre-Boys Leather', style='S.TButton', width=17,
       command=lambda: calc(r'Pre-Boys Leather',)).place(x=190, y=420)
Button(root, text='Boys Leather', style='S.TButton', width=17,
       command=lambda: calc(r'Boys Leather',)).place(x=190, y=460)
Button(root, text='Mens Leather', style='S.TButton', width=17,
       command=lambda: calc(r'Mens Leather',)).place(x=190, y=500)
Button(root, text='Pre-Boys Idler', style='S.TButton', width=17,
       command=lambda: calc(r'Pre-Boys Idler',)).place(x=360, y=420)
Button(root, text='Boys Idler', style='S.TButton', width=17,
       command=lambda: calc(r'Boys Idler',)).place(x=360, y=460)
Button(root, text='Mens Idler', style='S.TButton', width=17,
       command=lambda: calc(r'Mens Idler',)).place(x=360, y=500)

exit1 = Button(root, text='Close', style='C.TButton', width=11,
               command=root.destroy).place(x=370, y=550)

root.mainloop()
