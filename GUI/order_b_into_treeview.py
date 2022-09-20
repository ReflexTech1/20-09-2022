import tkinter as Tkinter
import tkinter.ttk as ttk

from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *

class Boys(Tkinter.Frame):

    def __init__(self, parent):
        Tkinter.Frame.__init__(self, parent)
        self.parent=parent
        self.initialize_user_interface()

    def initialize_user_interface(self):
        OrderNo = StringVar()
        self.parent.title("Canvas Test")
        self.parent.grid_rowconfigure(1, weight=1)
        self.parent.grid_columnconfigure(1, weight=1)
        self.parent.config(background="lavender")

        # Define the different GUI widgets
        self.dose_label = Tkinter.Label(self.parent, text="Order No:")
        self.dose_entry = Tkinter.Entry(self.parent)
        self.dose_label.grid(row=0, column=0, sticky=Tkinter.W)
        self.dose_entry.grid(row=0, column=1)

        self.dose_label = Tkinter.Label(self.parent, text="Style")
        self.dose_entry = Tkinter.Entry(self.parent)
        self.dose_label.grid(row=1, column=0, sticky=Tkinter.W)
        self.dose_entry.grid(row=1, column=1)

        self.dose_label = Tkinter.Label(self.parent, text="Delivery Date:")
        self.dose_entry = Tkinter.Entry(self.parent)
        self.dose_label.grid(row=2, column=0, sticky=Tkinter.W)
        self.dose_entry.grid(row=2, column=1)

        self.dose_label = Tkinter.Label(self.parent, text="Size 2:")
        self.dose_entry = Tkinter.Entry(self.parent)
        self.dose_label.grid(row=3, column=0, sticky=Tkinter.W)
        self.dose_entry.grid(row=3, column=1)

        self.modified_label = Tkinter.Label(self.parent, text="Size 3:")
        self.modified_entry = Tkinter.Entry(self.parent)
        self.modified_label.grid(row=4, column=0, sticky=Tkinter.W)
        self.modified_entry.grid(row=4, column=1)

        self.modified_label = Tkinter.Label(self.parent, text="Size 4:")
        self.modified_entry = Tkinter.Entry(self.parent)
        self.modified_label.grid(row=5, column=0, sticky=Tkinter.W)
        self.modified_entry.grid(row=5, column=1)

        self.modified_label = Tkinter.Label(self.parent, text="Size 5:")
        self.modified_entry = Tkinter.Entry(self.parent)
        self.modified_label.grid(row=6, column=0, sticky=Tkinter.W)
        self.modified_entry.grid(row=6, column=1)

        self.modified_label = Tkinter.Label(self.parent, text="Quantity:")
        self.modified_entry = Tkinter.Entry(self.parent)
        self.modified_label.grid(row=7, column=0, sticky=Tkinter.W)
        self.modified_entry.grid(row=7, column=1)

        self.submit_button = Tkinter.Button(self.parent, text="Insert", command=self.insert_data)
        self.submit_button.grid(row=8, column=1, sticky=Tkinter.W)
        self.exit_button = Tkinter.Button(self.parent, text="Exit", command=self.parent.quit)
        self.exit_button.grid(row=9, column=1)

        # Set the treeview
        self.tree = ttk.Treeview(self.parent, columns=('Order No', 'Style', 'Delivery Date', 'Size', 'Quantity'))
        self.tree.heading('#0', text='Order No')
        self.tree.heading('#1', text='Style')
        self.tree.heading('#2', text='Delivery Date')
        self.tree.heading('#3', text='Size')
        self.tree.heading('#4', text='Quantity')
        self.tree.column('#0', stretch=Tkinter.YES)
        self.tree.column('#1', stretch=Tkinter.YES)
        self.tree.column('#2', stretch=Tkinter.YES)
        self.tree.column('#3', stretch=Tkinter.YES)
        self.tree.column('#4', stretch=Tkinter.YES)
        self.tree.grid(row=10, columnspan=4, sticky='nsew')
        self.treeview = self.tree
        # Initialize the counter
        self.orderno = OrderNo.get()
        self.i = 0

    def insert_data(self):
        """
        Insertion method.
        """
        self.treeview.insert('', 'end', text= (self.orderno + '-' +str(self.i)),  values=(self.dose_entry.get(), self.modified_entry.get()))
        # Increment counter
        self.i = self.i + 1


def main():
    root=Tkinter.Tk()
    d=Boys(root)
    root.mainloop()

if __name__=="__main__":
    main()
