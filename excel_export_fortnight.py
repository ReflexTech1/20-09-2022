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
    # Retrieve the variables from the input fieldsT
    variable1 = input1.get()
    variable2 = input2.get()

    # Execute the query and pass the variables
    data = r"SELECT Date,Line,Order2,Style,Despatch,Reason FROM ProductionBreakdown WHERE Date BETWEEN ? AND ? UNION ALL SELECT Date,Line,Order2,Style,Despatch,Reason FROM ProdBreak_Archive WHERE Date BETWEEN ? AND ?"
    cursor.execute(data, (variable1,variable2,variable1,variable2))
    # Fetch the data
    # columns = [col[0] for col in cursor.description]
    # rows = cursor.fetchall()
    data = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Get the directory of the database
    db_dir = os.path.dirname(os.path.abspath("C:\RSoft\Current\Reflex Footweear.sql3"))

    # Create the folder directory where you want to save the file
    folder_dir = os.path.join(db_dir, "Fortnigtly Scores")
    if not os.path.exists(folder_dir):
        os.mkdir(folder_dir)

    # Convert data to dataframe
    data = pd.DataFrame(data)

    # Export the data to an Excel file
    data.to_excel(os.path.join(folder_dir, "Reflex Footwear Fortnightly "+variable1+"-"+variable2+".xlsx"), index=False)
    messagebox.showinfo("Success", "Data exported to excel successfully")

# Create the main window
root = Tk()
root.geometry('600x400')
root.title("Export Fortnight")
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
label1 = Label(root, text = "Enter Start Date: ")
label_des = Label(root, text = "-------->", font=("Calibri Bold", 12, "bold"), background="lightblue2")
label2 = Label(root, text = "Enter end date: ")

label1 = Label(root, text="Start Date", width=20, background="lightblue2", font=("Arial", 12, "bold"))
input1 = Entry(root, textvar=input1, width=20, background="lightblue2", font=("Arial", 12, "bold"))

label2 = Label(root, text="End Date", width=20, background="lightblue2", font=("Arial", 12, "bold"))
input2 = Entry(root, textvar=input2, width=20,background="lightblue2", font=("Arial", 12, "bold"))

# Pack the widgets
label1.place(x=40, y=40)
input1.place(x=40, y=80)
cale.place(x=200, y=200)
label_des.place(x=270, y= 40)

label2.place(x=350, y=40)
input2.place(x=370, y=80)

export_button.place(x=40, y=160)
exit_button.place(x=440, y=160)

# Start the main loop
root.mainloop()
