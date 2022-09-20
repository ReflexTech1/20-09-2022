from tkinter import * #Import the Tkinter module
from tkinter import messagebox #Imports the message box module
from tkinter import font #Imports fonts from tkinter
import json #Imports JSON

a = ('') #Variable for price and quantity/mass
b = ('') #^

r = ('') #Result Var

aa = ('')
ba = ('')

q1 = ('')
q2 = ('')

count = 2 #For extra Fields

global row_count, entries, item_count, output
row_count = 10
item_count = 2
entries = []
output = []
price = {}
sort_count = 1

master = Tk() #Tkinter

m = StringVar(master) #Defines m as yhe variable from the option menu
c = StringVar(master) #Defines m as yhe variable from the option menu

entry1 = Entry(master) #Entry Feilds
entry2 = Entry(master)

entry3 = Entry(master) #Entry Feilds (Variables)
entry4 = Entry(master)

entryq1 = Entry(master) #Entry Feilds (Variables)
entryq2 = Entry(master)


def bestCur(*entries):
    # each entry should be a tuple e.g. (curEntry, mesEntry)
    entries = list(entries)
    for entry in entries:
        entry.append(float(entry[0].get())/float(entry[1].get()))
    entries.sort(key=lambda x: x[2])
    print(entries)


but1 = Button(master, text="press me", bg="red", command=lambda: bestCur([entry1, entry2], [entry3, entry4]))
but1.grid(row=101, column=2)

def create_entry():
    global row_count, entries, item_count
    item_count += 1

    Label(master, text=("Item #"+ str(item_count)), font=("Helvetica", 20, "bold underline")).grid(row=(row_count))

    temp_entry = Entry(master)
    temp_entry.grid(row=(row_count+1), column=1)

    entries.append(temp_entry)
    Label(master, textvariable=c).grid(row=(row_count+1))

    temp_entry = Entry(master)
    temp_entry.grid(row=(row_count+2), column=1)

    entries.append(temp_entry)
    Label(master, textvariable=m).grid(row=(row_count+2))

    temp_entry = Entry(master)
    temp_entry.grid(row=(row_count+2), column=1)

    entries.append(temp_entry)
    Label(master, text='Rating out of 5').grid(row=(row_count+3))

    temp_entry = Entry(master)
    temp_entry.grid(row=(row_count+3), column=1)


    row_count += 4

def showinfo():
   messagebox.showinfo("Best buy", r) #Creates a message box with pops up which shows r (result)

def addnew():
   global count, entryq1, entryq2
   count = count+1
   create_entry()

def sort_entries():
    while sort_count != count:
        if sort_count == 2:
            a = entry1.get() #Gets value from the entry fields
            ap = entry2.get()
            b = entry3.get()
            bp = entry4.get()
            aa = float(a)/float(ap) #Calcultes Price per item/ quantity of item 1
            ba = float(b)/float(bp) #Calculates price per item/quantity of item 2
    pass

def calculate():
   print(count) #Debugging
   if count == 2:
      item_two()
   else:
       sort_entries()

def item_two():
   q1 = float(entryq1.get())
   q2 = float(entryq2.get())
   checkrating(q1, '(First rating)')
   checkrating(q2, '(Second rating)')
   a = entry1.get() #Gets value from the entry fields
   ap = entry2.get()
   b = entry3.get()
   bp = entry4.get()
   aa = float(a)/float(ap) #Calcultes Price per item/ quantity of item 1
   ba = float(b)/float(bp) #Calculates price per item/quantity of item 2

   if aa == ba: #Finds which one is better
       print('They are the same pice') #Outputs value in output
       quailitys()
   else:
       if aa > ba:
           print('The second item is cheaper') #^
           r = ('The second item is cheaper') #Sets Value to R
       else:
           if ba > aa:
              print('The first item is cheaper') #^
              r = ('The first item is cheaper') #Sets Value to R
           else:
              r = ('Malfunction Occured Please check the input Values')
       messagebox.showinfo("Best buy", r) #Creates a message box with pops up which shows r (result)

def checkrating(var, rantingno):
    try:
        var = float(var)
        if var > 5 or var < 0:
           messagebox.showinfo("Best buy", "Please Enter a Valid Number for the rating", '(', rantingno, ')')
    except ValueError:
        messagebox.showinfo("Best buy", "Please Enter a Valid Number for the rating")

def quailitys():
   if count == 2:
      q1 = float(entryq1.get())
      q2 = float(entryq2.get())
      if q1 == q2: #Finds which one is better
       print('They are the same value') #Outputs value in output
       r = ('They are the same value') #Sets Value to R
      elif q1 < q2:
           print('The second item is better value') #^
           r = ('The second item is better value') #Sets Value to R
      elif q2 < q1:
              print('The first item is better value') #^
              r = ('The first item is better value') #Sets Value to R
      messagebox.showinfo("Best buy", r) #Creates a message box with pops up which shows r (result)

Label(master, text="Best Buy Calculator", font=("Helvetica", 20, "bold underline")).grid(row=0)
Label(master, text="Item #1", font=("Helvetica", 17, "bold underline")).grid(row=2) #1st Item Fields
Label(master, textvariable=c).grid(row=3)
Label(master, textvariable=m).grid(row=4)


entry1.grid(row=3, column=1) #Puts Entry fields in a certain location
entry2.grid(row=4, column=1) # ^


entryq1.grid(row=5, column=1) # ^
entryq2.grid(row=9, column=1) # ^
Label(master, text='Rating out of 5').grid(row=5)
Label(master, text='Rating out of 5').grid(row=9)


Label(master, text="Item #2", font=("Helvetica", 17, "bold underline")).grid(row=6) #2nd Item Fields
Label(master, textvariable=c).grid(row=7)
Label(master, textvariable=m).grid(row=8)


entry3.grid(row=7, column=1) #2nd Item Entry fields
entry4.grid(row=8, column=1)


Button(master, text='+', command=addnew).grid(row=100, column=0, pady=4) #Cancel Button
Button(master, text='Cancel', command=quit).grid(row=101, column=0, pady=4) #Cancel Button
Button(master, text='Find Better Value', command=calculate).grid(row=101, column=1, pady=4) #Button to calculate better value


m.set("Measurement") # This is what the drop down box shows when no options are selected
c.set('Currency')
mes = OptionMenu(master, m, "Weight (kg)","Weight (g)", "Volume (mL)", "Quantity").grid(row=1) #Options and grid placement of the option menu
cur = OptionMenu(master, c, "AUD ($)","USD ($)", "EUR (€)", "GBP (£)", "CNY (¥)").grid(row=1, column=1) #Options and grid placement of the option menu


mainloop()
