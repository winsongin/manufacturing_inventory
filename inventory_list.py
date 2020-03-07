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

#This function will display the column based on user input.
def search_columns():
    global queryInput
    queryInput = searchEntry.get()

    #Delete all of the entries in the tree first.
    tree.delete(*tree.get_children())
    
    #Display all of the data if nothing is entered in the search box.
    if (len(queryInput) == 0):
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
        print("MySQL connection closed.")

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
            querySearch = "SELECT * FROM inventory WHERE part_name = %s"
            cursor.execute(querySearch, queryInput)
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

#This function will sort the column by increasing or decreasing order.
def sort_column(tree, col, reverse):
    #Delete all of the entries in the tree first.
    tree.delete(*tree.get_children())

    connection=mysql.connector.connect(host="localhost",
    user="root",password="T1t@n1umus",
    auth_plugin="mysql_native_password", database="inventory")
    db_Info = connection.get_server_info()
    print("Connected to MySQL Server version ", db_Info)
    cursor = connection.cursor()
    cursor.execute("select database()")
    records = cursor.fetchone()
    print("Connected to database called ", records)

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
    print("MySQL connection closed.")
    
##    n = [(tree.set(m, col), m) for m in tree.get_children('')]
##    n.sort(reverse=reverse)
##
##    #Rearrange the items when sorting
##    for index, (val, m) in enumerate(1):
##        tree.move(m, '', index)
##
##    #Perform the sort again the next time user clicks on the header again
##    tree.heading(col, command=lambda: \
##                 sort_column(tree, col, not reverse))

# Configure the labels and the entry below
lTitle = Label(master, text="Inventory")
lPartName = Label(master, text="Part Name")
lPartNum = Label(master, text="Part No.")
lManufact = Label(master, text="Manfacturer")
lQuantity = Label(master, text="Quantity")
lPartType = Label(master, text="Part Type")
eSearch = Entry(master, textvariable=searchEntry, width=30)
bSearch = Button(master, text="Search", command=search_columns)
bQuit = Button(master, text="Quit", command=master.destroy)

# Now arrange all of the parts above in a grid.
lTitle.grid(row=0, column=0, sticky=E+W)
eSearch.grid(row=0, column=1, sticky=E)
bSearch.grid(row=0, column=2, sticky=E)
bQuit.grid(row=1, column=2)

# Create the columns and headings below
tree.column("#0", minwidth=0, width=0, stretch=False)
tree.heading("#1", text="Part Name", command=lambda: \
             sort_column(tree, 0, False))
tree.column("#1", minwidth=0, width=100, stretch=False)
tree.heading("#2", text="Part No.", command=lambda: \
             sort_column(tree, 1, False))
tree.column("#2", minwidth=0, width=100, stretch=False)
tree.heading("#3", text="Manufacturer", command=lambda: \
             sort_column(tree, 2, False))
tree.column("#3", minwidth=0, width=150, stretch=False)
tree.heading("#4", text="Quantity", command=lambda: \
             sort_column(tree, 3, False))
tree.column("#4", minwidth=0, width=100, stretch=False)
tree.heading("#5", text="Part Type", command=lambda: \
             sort_column(tree, 4, False))
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
