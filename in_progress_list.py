from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector

# In Progress List

master = Tk()
tree=ttk.Treeview(master, column=("column", "column1",
"column2", "column3", "column4")) #Needed to create new columns
master.title("Work In Progress")
searchEntry = StringVar()
master.resizable(False, False) #Don't allow users to resize window.
# Set up the grid configurations below.
master.grid_rowconfigure(0, weight=1)
master.grid_columnconfigure(0, weight=1)

# Configure the labels and the entry below
lTitle = Label(master, text="Work In Progress")
lWorkNum = Label(master, text="Work #")
lStatus = Label(master, text="Status")
lDaysLeft = Label(master, text="Days Until Shipment")
lDateRecv = Label(master, text="Date Received")
lETA = Label(master, text="Estimated Time of Arrival")
eSearch = Entry(master, textvariable=searchEntry, width=25)
bSearch = Button(master, text="Search")
bQuit = Button(master, text="Quit", command=master.destroy)

# Now arrange all of the parts above in a grid.
lTitle.grid(row=0, column=0, sticky=E+W)
eSearch.grid(row=0, column=1, sticky=E)
bSearch.grid(row=0, column=2, sticky=E)
bQuit.grid(row=1, column=2)

# Create the columns and headings below
tree.column("#0", minwidth=0, width=0)
tree.heading("#1", text="Work #")
tree.column("#1", minwidth=0, width=100)
tree.heading("#2", text="Status")
tree.column("#2", minwidth=0, width=100)
tree.heading("#3", text="Days Until Shipment")
tree.column("#3", minwidth=0, width=150)
tree.heading("#4", text="Date Received")
tree.column("#4", minwidth=0, width=100)
tree.heading("#5", text="Estimated Time of Arrival")
tree.column("#5", minwidth=0, width=150)

tree.configure(height=20)
tree.grid() #Arrange all the TreeView parts in a grid.

#Connect to the database if possible.
connection=mysql.connector.connect(host="localhost",
user="root",password="T1t@n1umus",
auth_plugin="mysql_native_password", database="inventory")
if connection.is_connected():
    db_Info = connection.get_server_info()
    print("Connected to MySQL Server version ", db_Info)
    cursor = connection.cursor()
    cursor.execute("select database()")
    records = cursor.fetchone()
    print("Connected to database called ", records)

    #Print all the database records onto the GUI.
    printAll = "SELECT * FROM work_in_progress"
    cursor.execute(printAll)
    records  = cursor.fetchall()
    for row in records:
        print("Work Number: ", row[0])
        print("Status: ", row[1])
        print("Company: ", row[2])
        print("Date Received: ", row[3])
        print("ETA: ", row[4])

    counter = 0
    for row in records:
        tree.insert('', 'end', values=
        (row[0],row[1],row[2],row[3],row[4]))
        counter += 1

if (connection.is_connected()):
    cursor.close()
    connection.close()
    print("MySQL connection closed.")
                
mainloop()
