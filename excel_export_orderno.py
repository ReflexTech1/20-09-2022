import sqlite3
import pandas as pd
import os
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from tkcalendar import Calendar

dateTimeObj = datetime.now()

timestampStr = dateTimeObj.strftime("%d-%b")

# Connect to the database
conn = sqlite3.connect("Reflex Footwear.sql3")
cursor = conn.cursor()

def export_to_excel():
    # Retrieve the variables from the input fields
    variable1 = input1.get()

    # Execute the query and pass the variables
    data = r"SELECT Date,Line,Order2,Style,Clicking,Closing,Moulding,Finishing,Despatch,Reason FROM ProductionBreakdown WHERE Order2=? UNION SELECT Date,Line,Order2,Style,Clicking,Closing,Moulding,Finishing,Despatch,Reason FROM ProdBreak_Archive WHERE Order2=?"
    cursor.execute(data, (variable1,variable1))
    # Fetch the data
    # columns = [col[0] for col in cursor.description]
    # rows = cursor.fetchall()
    data = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Get the directory of the database
    db_dir = os.path.dirname(os.path.abspath("C:\RSoft\Current\Reflex Footweear.sql3"))

    # Create the folder directory where you want to save the file
    folder_dir = os.path.join(db_dir, "Production")
    if not os.path.exists(folder_dir):
        os.mkdir(folder_dir)

    # Convert data to dataframe
    data = pd.DataFrame(data)

    # Export the data to an Excel file
    data.to_excel(os.path.join(folder_dir, "Production"+timestampStr+".xlsx"), index=False)
    messagebox.showinfo("Success", "Data exported to excel successfully")

# Create the main window
root = Tk()
root.geometry('600x400')
root.title("Export Order Breakdown")
root.config(bg="lightblue2")

cale = Calendar(root,selectmode = "day",year=2022,month=1,date=1)

def fetch_date():
    date.config(text = "Current month:" + cale.get_date())

date = Label(root,text="",bg='black',fg='white')

# Create the input fields for the variables
input1 = Entry(root)
input2 = Entry(root)

# Create the export button
export_button = Button(root, text="Export", command=export_to_excel, width=16, background="lightblue3", font=("Arial", 12, "bold"))

# Create the Exit button
exit_button = Button(root, text="Exit", command=root.destroy, width=10, background="lightblue2",foreground="red", font=("Arial", 12, "bold"))

# Create the labels
label1 = Label(root, text = "Enter OrderNo: ")

label1 = Label(root, text="Start Date", width=20, background="lightblue2", font=("Arial", 12, "bold"))
input1 = Entry(root, textvar=input1, width=20, background="lightblue2", font=("Arial", 12, "bold"))

# Pack the widgets
label1.place(x=40, y=40)
input1.place(x=40, y=80)
cale.place(x=200, y=200)
export_button.place(x=40, y=160)
exit_button.place(x=440, y=160)

# Start the main loop
root.mainloop()
