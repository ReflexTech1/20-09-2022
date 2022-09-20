from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *

root = Tk()
root.geometry('310x150')
root.title("Export Status")

root.config(bg="#4a7a8c")
root.wm_attributes('-transparentcolor','#4a7a8c')

style = ttk.Style()


label_0 = Label(root, text="Export Successfull", width=20, background='#4a7a8c', foreground="white", font=("Arial, bold", 20)).place(x=50, y=30)

exit1 = Button(root, text='Done', style='C.TButton', width=12, command=root.destroy).place(x=110, y=80)

#Bind Esc key
def close_root(e):
   root.destroy()

root.bind('<Escape>', lambda e: close_root(e))

root.mainloop()
