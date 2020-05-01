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
        self.master.geometry("700x600")
        self.searchEntry = tk.StringVar()
        self.master.resizable(False, False) #Don't allow users to resize window.

        # Configure the following widgets below
        self.lTitle = tk.Label(master, text="Inventory", font=("Arial", 20))
        self.lLowQuantity = tk.Label(master, text="Low on Quantity")
        self.eSearch = tk.Entry(master, textvariable=self.searchEntry, width=40)
        self.bSearch = tk.Button(master, text="Search", command=self.search_columns)
        self.bQuantity = tk.Button(master, text="Check Quantity", command=self.low_on_quantity)
        self.bQuit = tk.Button(master, text="Quit", command=master.destroy)
        self.bReset = tk.Button(master, text="Reset", command=self.reset_window)

        self.lTitle.place(x=240, y=10)
        self.eSearch.place(x=250, y=100)
        self.bSearch.place(x=500, y=100)
        self.bQuantity.place(x=50, y=500)
        self.bReset.place(x=250, y=500)
        self.bQuit.place(x=450, y=500)

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

        self.tree.configure(height=15)
        self.tree.place(x=20, y=150)

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
