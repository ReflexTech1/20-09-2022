from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *
from datetime import datetime

root = Tk()
root.geometry('450x250')
root.title("Logistics")
root.config(bg="lightgreen")
style = ttk.Style()

Truck = StringVar()
Document = StringVar()

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y")


def logistics():
    truck = Truck.get()
    ref = Document.get()

    with sqlite3.connect('Reflex Footwear.sql3') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Logistics (Date,Truck,Reference) VALUES(?,?,?)', [
                       timestampStr, truck, ref])
        updated = cursor.rowcount
        cursor.close()
        conn.commit()
        root.destroy()
        sys.exit(updated)  # return value whether record has been updated


label_0 = Label(root, text="Send Truck and Document(s)", width=30,
                background="lightgreen", font=("bold", 18)).place(x=70, y=25)

label_1 = Label(root, text="Registration:", width=20,
                background="lightgreen", font=("bold", 13)).place(x=40, y=90)
entry_1 = Entry(root, textvar=Truck, background="yellow",
                font=("bold", 12)).place(x=230, y=90)

label_2 = Label(root, text="Invoice Number(s):", width=20,
                background="lightgreen", font=("bold", 13)).place(x=40, y=140)
entry_2 = Entry(root, textvar=Document, background="yellow",
                font=("bold", 12)).place(x=230, y=140)

# Style of buttons
style.configure('C.TButton', font=('Arial', 12, 'bold'),
                relief="raised", foreground='red')
style.configure('S.TButton', font=('Arial', 12, 'bold'),
                relief="raised", foreground='blue')

# Inserting buttons
submit1 = Button(root, text='Submit', style='S.TButton',
                 width=11, command=logistics).place(x=20, y=200)
exit1 = Button(root, text='Close', style='C.TButton', width=11,
               command=root.destroy).place(x=320, y=200)

root.mainloop()
