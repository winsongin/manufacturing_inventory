from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector

# In Progress List

master = Tk()
tree=ttk.Treeview(master, column=("column", "column1",
"column2", "column3", "column4")) #Needed to create new columns
master.title("Inventory List")
searchEntry = StringVar()
master.resizable(False, False) #Don't allow users to resize window.
# Set up the grid configurations below.
master.grid_rowconfigure(0, weight=1)
master.grid_columnconfigure(0, weight=1)

# Configure the labels and the entry below
lTitle = Label(master, text="Inventory")
lPartName = Label(master, text="Part Name")
lPartNum = Label(master, text="Part No.")
lManufact = Label(master, text="Manfacturer")
lQuantity = Label(master, text="Quantity")
lPartType = Label(master, text="Part Type")
eSearch = Entry(master, textvariable=searchEntry, width=30)
bSearch = Button(master, text="Search")
bQuit = Button(master, text="Quit", command=master.destroy)

# Now arrange all of the parts above in a grid.
lTitle.grid(row=0, column=0, sticky=E+W)
eSearch.grid(row=0, column=1, sticky=E)
bSearch.grid(row=0, column=2, sticky=E)
bQuit.grid(row=1, column=2)

# Create the columns and headings below
tree.column("#0", minwidth=0, width=0)
tree.heading("#1", text="Part Name")
tree.column("#1", minwidth=0, width=100)
tree.heading("#2", text="Part No.")
tree.column("#2", minwidth=0, width=100)
tree.heading("#3", text="Manufacturer")
tree.column("#3", minwidth=0, width=150)
tree.heading("#4", text="Quantity")
tree.column("#4", minwidth=0, width=100)
tree.heading("#5", text="Part Type")
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
    printAll = "SELECT * FROM inventory"
    cursor.execute(printAll)
    records  = cursor.fetchall()
    for row in records:
        print("Part Name: ", row[0])
        print("Part Number: ", row[1])
        print("Manufacturer: ", row[2])
        print("Quantity: ", row[3])
        print("Part Type: ", row[4])

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
