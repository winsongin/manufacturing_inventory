from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector

# In Progress List




def WOWindow(department):
    master = Tk()
    tree = ttk.Treeview(master, column=("column", "column1",
                                        "column2", "column3", "column4"))  # Needed to create new columns
    master.title("Work In Progress")
    searchEntry = tk.StringVar()
    master.resizable(False, False)  # Don't allow users to resize window.
    # Set up the grid configurations below.
    master.grid_rowconfigure(0, weight=1)
    master.grid_columnconfigure(0, weight=1)

    selection = StringVar()

    # Configure the labels and the entry below
    lTitle = Label(master, text="Select Work Order")
    bQuit = Button(master, text="Quit", command=master.destroy)
    search_button = Button(master, text="Search", command=lambda: select(selection.get()))
    selection_entry = Entry(master, width=10, textvariable=selection)

    # Now arrange all of the parts above in a grid.
    lTitle.grid(row=0, column=0, sticky=E + W)
    bQuit.grid(row=1, column=2)
    search_button.grid(row=2, column=0)
    selection_entry.grid(row=2, column=1)

    # Create the columns and headings below
    tree.column("#0", minwidth=0, width=0, stretch=False)
    tree.heading("#1", text="Work Order", command=lambda: sort_column(tree, 0, department, False))
    tree.column("#1", minwidth=0, width=100, stretch=False)
    tree.heading("#2", text="Department", command=lambda: sort_column(tree, 1, department, False))
    tree.column("#2", minwidth=0, width=100, stretch=False)
    tree.heading("#3", text="Received", command=lambda: sort_column(tree, 2, department, False))
    tree.column("#3", minwidth=0, width=150, stretch=False)
    tree.heading("#4", text="Estimated Ship Date", command=lambda: sort_column(tree, 3, department, False))
    tree.column("#4", minwidth=0, width=100, stretch=False)
    tree.heading("#5", text="Customer ID", command=lambda: sort_column(tree, 4, department, False))
    tree.column("#5", minwidth=0, width=150, stretch=False)

    tree.configure(height=20)
    tree.grid()  # Arrange all the TreeView parts in a grid.

    # Connect to the database if possible.
    connection = mysql.connector.connect(host="localhost",
                                         user="root", password="Razgriz!949",
                                         auth_plugin="mysql_native_password", database="inventory_system")
    db_Info = connection.get_server_info()
    cursor = connection.cursor()
    cursor.execute("select database()")
    records = cursor.fetchone()

    # Print all the database records onto the GUI.
    printAll = "SELECT * FROM work_in_progress WHERE status = \"" + department + "\""
    cursor.execute(printAll)
    records = cursor.fetchall()

    counter = 0
    for row in records:
        tree.insert('', 'end', values=
        (row[0], row[1], row[2], row[3], row[4]))
        counter += 1

    # This function will display the column based on user input.
    def search_columns():
        global queryInput
        queryInput = searchEntry.get()

        # Delete all of the entries in the tree first.
        tree.delete(*tree.get_children())

        # Display all of the data if nothing is entered in the search box.
        if (len(queryInput) == 0):
            connection = mysql.connector.connect(host="localhost",
                                                 user="root", password="Razgriz!949",
                                                 auth_plugin="mysql_native_password", database="inventory_system")
            db_Info = connection.get_server_info()
            cursor = connection.cursor()
            cursor.execute("select database()")
            records = cursor.fetchone()

            # Print all the database records onto the GUI.
            querySearch = "SELECT * FROM work_in_progress"
            cursor.execute(querySearch)
            records = cursor.fetchall()
            for row in records:
                print("Work Number: ", row[0])
                print("Status: ", row[1])
                print("Company: ", row[2])
                print("Date Received: ", row[3])
                print("ETA: ", row[4])

            counter = 0
            for row in records:
                tree.insert('', 'end', values=
                (row[0], row[1], row[2], row[3], row[4]))
                counter += 1

            cursor.close()
            connection.close()
        else:
            connection = mysql.connector.connect(host="localhost",
                                                 user="root", password="Razgriz!949",
                                                 auth_plugin="mysql_native_password", database="inventory_system")
            db_Info = connection.get_server_info()
            cursor = connection.cursor()
            cursor.execute("select database()")
            records = cursor.fetchone()

            # Print all the database records onto the GUI.
            querySearch = "SELECT * FROM work_in_progress WHERE wo_number = %s"
            cursor.execute(querySearch, queryInput)
            records = cursor.fetchall()
            for row in records:
                print("Work Number: ", row[0])
                print("Status: ", row[1])
                print("Company: ", row[2])
                print("Date Received: ", row[3])
                print("ETA: ", row[4])

            counter = 0
            for row in records:
                tree.insert('', 'end', values=
                (row[0], row[1], row[2], row[3], row[4]))
                counter += 1

            cursor.close()
            connection.close()

    # This function will sort the column by increasing or decreasing order.
    def sort_column(tree, col, department, reverse):
        # Delete all of the entries in the tree first.
        tree.delete(*tree.get_children())

        connection = mysql.connector.connect(host="localhost",
                                             user="root", password="Razgriz!949",
                                             auth_plugin="mysql_native_password", database="inventory_system")
        db_Info = connection.get_server_info()
        cursor = connection.cursor()
        cursor.execute("select database()")
        records = cursor.fetchone()

        if (col == 0):
            querySort = "SELECT * FROM work_in_progress WHERE status = \"" + department + "\" ORDER BY wo_number"
        elif (col == 1):
            querySort = "SELECT * FROM work_in_progress WHERE status = \"" + department + "\" ORDER BY status"
        elif (col == 2):
            querySort = "SELECT * FROM work_in_progress WHERE status = \"" + department + "\" ORDER BY date_recv"
        elif (col == 3):
            querySort = "SELECT * FROM work_in_progress WHERE status = \"" + department + "\" ORDER BY eta"
        elif (col == 4):
            querySort = "SELECT * FROM work_in_progress WHERE status = \"" + department + "\" ORDER BY cust_id"

        # Print all the database records onto the GUI.
        cursor.execute(querySort)
        records = cursor.fetchall()
        for row in records:
            print("Work Number: ", row[0])
            print("Status: ", row[1])
            print("Date Received: ", row[2])
            print("ETA: ", row[3])
            print("Customer ID: ", row[4])

        counter = 0
        for row in records:
            tree.insert('', 'end', values=
            (row[0], row[1], row[2], row[3], row[4]))
            counter += 1

        cursor.close()
        connection.close()
        print("MySQL connection closed.")

    def select(select):
        global wonum
        wonum = select
        master.destroy()
        return

    cursor.close()
    connection.close()

    mainloop()

    return selection.get()
