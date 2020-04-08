from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector

# Inventory List

class Inventory:
    #This function will reset the window back to its default state.
    def reset_window(self):
        #Delete all of the entries in the tree first.
        self.tree.delete(*self.tree.get_children())

        connection=mysql.connector.connect(host="localhost",
        user="root",password="Razgriz!949",
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
            self.tree.insert('', 'end', values=
            (row[0],row[1],row[2],row[3],row[4]))
            counter += 1
                
        cursor.close()
        connection.close()


    #This function will display the column based on user input.
    def search_columns(self):
        queryInput = self.searchEntry.get()

        #Delete all of the entries in the tree first.
        self.tree.delete(*self.tree.get_children())
        
        #Display all of the data if nothing is entered in the search box.
        if (len(queryInput) == 0):
            connection=mysql.connector.connect(host="localhost",
            user="root",password="Razgriz!949",
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
                self.tree.insert('', 'end', values=
                (row[0],row[1],row[2],row[3],row[4]))
                counter += 1
                    
            cursor.close()
            connection.close()

        else:
            connection=mysql.connector.connect(host="localhost",
            user="root",password="Razgriz!949",
            auth_plugin="mysql_native_password", database="inventory_system")
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database()")
            records = cursor.fetchone()
            print("Connected to database called ", records)

            #Print all the database records onto the GUI.
            querySearch = ("SELECT * FROM inventory WHERE part_name LIKE '%{}%'").format(queryInput)
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
                self.tree.insert('', 'end', values=
                (row[0],row[1],row[2],row[3],row[4]))
                counter += 1
                                
            cursor.close()
            connection.close()

    #This function will sort the column by increasing or decreasing order.
    def sort_column(self, tree, col):
        #Delete all of the entries in the tree first.
        self.tree.delete(*self.tree.get_children())

        connection=mysql.connector.connect(host="localhost",
        user="root",password="Razgriz!949",
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
            self.tree.insert('', 'end', values=
            (row[0],row[1],row[2],row[3],row[4]))
            counter += 1
                
        cursor.close()
        connection.close()

    #TODO: Fill in the function definition for the low quantity.
    #This function will display which inventory items are low on quantity.
    def low_on_quantity(self):
        #Delete all of the entries in the tree first.
        self.tree.delete(*self.tree.get_children())

        connection=mysql.connector.connect(host="localhost",
        user="root",password="Razgriz!949",
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
            self.tree.insert('', 'end', values=
            (row[0],row[1],row[2],row[3],row[4]))
            counter += 1
                
        cursor.close()
        connection.close()
    
    def __init__(self, master):
        self.master=master
        self.tree=ttk.Treeview(master, column=("column", "column1",
        "column2", "column3", "column4")) #Needed to create new columns
        self.master.title("Inventory List")
        self.searchEntry = tk.StringVar()
        self.master.resizable(False, False) #Don't allow users to resize window.
        # Set up the grid configurations below.
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

        # Configure the following widgets below
        self.lTitle = tk.Label(master, text="Inventory", font=("Arial", 20))
        self.lLowQuantity = tk.Label(master, text="Low on Quantity")
        self.eSearch = tk.Entry(master, textvariable=self.searchEntry, width=40)
        self.bSearch = tk.Button(master, text="Search", command=self.search_columns)
        self.bQuantity = tk.Button(master, text="Check Quantity", command=self.low_on_quantity)
        self.bQuit = tk.Button(master, text="Quit", command=master.destroy)
        self.bReset = tk.Button(master, text="Reset", command=self.reset_window)

        # Now arrange all of the parts above in a grid.
        self.lTitle.grid(row=0, column=0, sticky=E+W)
        self.eSearch.grid(row=0, column=1, sticky=E)
        self.bSearch.grid(row=0, column=2, sticky=E)
        self.bQuantity.grid(row=1, column=2, sticky=E)
        self.bReset.grid(row=2, column=2, sticky=E)
        self.bQuit.grid(row=3, column=2, sticky=E)

        # Create the columns and headings below
        self.tree.column("#0", minwidth=0, width=0, stretch=False)
        self.tree.heading("#1", text="Part Name", command=lambda: self.sort_column(self.tree, 0))
        self.tree.column("#1", minwidth=0, width=100, stretch=False)
        self.tree.heading("#2", text="Part No.", command=lambda: self.sort_column(self.tree, 1))
        self.tree.column("#2", minwidth=0, width=100, stretch=False)
        self.tree.heading("#3", text="Manufacturer", command=lambda: self.sort_column(self.tree, 2))
        self.tree.column("#3", minwidth=0, width=150, stretch=False)
        self.tree.heading("#4", text="Quantity", command=lambda: self.sort_column(self.tree, 3))
        self.tree.column("#4", minwidth=0, width=100, stretch=False)
        self.tree.heading("#5", text="Part Type", command=lambda: self.sort_column(self.tree, 4))
        self.tree.column("#5", minwidth=0, width=150, stretch=False)

        self.tree.configure(height=20)
        self.tree.grid() #Arrange all the TreeView parts in a grid.

        #Connect to the database if possible.
        connection=mysql.connector.connect(host="localhost",
        user="root",password="Razgriz!949",
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
            self.tree.insert('', 'end', values=
            (row[0],row[1],row[2],row[3],row[4]))
            counter += 1

        cursor.close()
        connection.close()
        print("MySQL connection closed.")

if __name__ == "__main__":
    window = Tk()
    thisMain = Inventory(window)
    window.mainloop()
