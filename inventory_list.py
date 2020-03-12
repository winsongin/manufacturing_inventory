from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector

# In Progress List

master = Tk()
tree=ttk.Treeview(master, column=("column", "column1",
"column2", "column3", "column4")) #Needed to create new columns
master.title("Inventory List")
searchEntry = tk.StringVar()
master.resizable(False, False) #Don't allow users to resize window.
# Set up the grid configurations below.
master.grid_rowconfigure(0, weight=1)
master.grid_columnconfigure(0, weight=1)

#This function will reset the window back to its default state.
def reset_window():
    #Delete all of the entries in the tree first.
    tree.delete(*tree.get_children())

    connection=mysql.connector.connect(host="localhost",
    user="root",password="T1t@n1umus",
    auth_plugin="mysql_native_password", database="inventory_system")
    cursor = connection.cursor()

    #Print all the database records onto the GUI.
    querySearch = "SELECT * FROM inventory"
    cursor.execute(querySearch)
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
            
    cursor.close()
    connection.close()


#This function will display the column based on user input.
def search_columns():
    global queryInput
    queryInput = (searchEntry.get())

    #Delete all of the entries in the tree first.
    tree.delete(*tree.get_children())
    
    #Display all of the data if nothing is entered in the search box.
    if (len(queryInput) == 0):
        connection=mysql.connector.connect(host="localhost",
        user="root",password="T1t@n1umus",
        auth_plugin="mysql_native_password", database="inventory_system")
        cursor = connection.cursor()

        #Print all the database records onto the GUI.
        querySearch = "SELECT * FROM inventory"
        cursor.execute(querySearch)
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
                
        cursor.close()
        connection.close()

    else:
        connection=mysql.connector.connect(host="localhost",
        user="root",password="T1t@n1umus",
        auth_plugin="mysql_native_password", database="inventory_system")
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database()")
        records = cursor.fetchone()
        print("Connected to database called ", records)

        #Print all the database records onto the GUI.
        querySearch = "SELECT * FROM inventory WHERE part_name = 'queryInput'"
        cursor.execute(querySearch)
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
                            
        cursor.close()
        connection.close()

#This function will sort the column by increasing or decreasing order.
def sort_column(tree, col):
    #Delete all of the entries in the tree first.
    tree.delete(*tree.get_children())

    connection=mysql.connector.connect(host="localhost",
    user="root",password="T1t@n1umus",
    auth_plugin="mysql_native_password", database="inventory_system")
    cursor = connection.cursor()

    #Set the search command to a corresponding column according to number.
    if (col == 0):
        querySort = "SELECT * FROM inventory ORDER BY part_name"
    elif (col == 1):
        querySort = "SELECT * FROM inventory ORDER BY part_no"
    elif (col == 2):
        querySort = "SELECT * FROM inventory ORDER BY manufacturer"
    elif (col == 3):
        querySort = "SELECT * FROM inventory ORDER BY qty"
    elif (col == 4):
        querySort = "SELECT * FROM inventory ORDER BY part_type"

    #Print all the database records onto the GUI.
    cursor.execute(querySort)
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
            
    cursor.close()
    connection.close()

#TODO: Fill in the function definition for the low quantity.
#This function will display which inventory items are low on quantity.
def low_on_quantity():
    #Delete all of the entries in the tree first.
    tree.delete(*tree.get_children())

    connection=mysql.connector.connect(host="localhost",
    user="root",password="T1t@n1umus",
    auth_plugin="mysql_native_password", database="inventory_system")
    cursor = connection.cursor()
    
    #Only display the list of items if the quantity is less than 50.
    quantSearch = "SELECT * FROM inventory where qty <= 50"

    #Print all the database records onto the GUI.
    cursor.execute(quantSearch)
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
            
    cursor.close()
    connection.close()

# Configure the following widgets below
lTitle = Label(master, text="Inventory", font=("Arial", 20))
lLowQuantity = Label(master, text="Low on Quantity")
eSearch = Entry(master, textvariable=searchEntry, width=30)
bSearch = Button(master, text="Search", command=search_columns)
bQuantity = Button(master, text="Check Quantity", command=low_on_quantity)
bQuit = Button(master, text="Quit", command=master.destroy)
bReset = Button(master, text="Reset", command=reset_window)

# Now arrange all of the parts above in a grid.
lTitle.grid(row=0, column=0, sticky=E+W)
eSearch.grid(row=0, column=1, sticky=E)
bSearch.grid(row=0, column=2, sticky=E)
bQuantity.grid(row=1, column=2, sticky=E)
bReset.grid(row=2, column=2, sticky=E)
bQuit.grid(row=3, column=2, sticky=E)

# Create the columns and headings below
tree.column("#0", minwidth=0, width=0, stretch=False)
tree.heading("#1", text="Part Name", command=lambda: sort_column(tree, 0))
tree.column("#1", minwidth=0, width=100, stretch=False)
tree.heading("#2", text="Part No.", command=lambda: sort_column(tree, 1))
tree.column("#2", minwidth=0, width=100, stretch=False)
tree.heading("#3", text="Manufacturer", command=lambda: sort_column(tree, 2))
tree.column("#3", minwidth=0, width=150, stretch=False)
tree.heading("#4", text="Quantity", command=lambda: sort_column(tree, 3))
tree.column("#4", minwidth=0, width=100, stretch=False)
tree.heading("#5", text="Part Type", command=lambda: sort_column(tree, 4))
tree.column("#5", minwidth=0, width=150, stretch=False)

tree.configure(height=20)
tree.grid() #Arrange all the TreeView parts in a grid.

#Connect to the database if possible.
connection=mysql.connector.connect(host="localhost",
user="root",password="T1t@n1umus",
auth_plugin="mysql_native_password", database="inventory_system")
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

cursor.close()
connection.close()
print("MySQL connection closed.")
                
mainloop()
