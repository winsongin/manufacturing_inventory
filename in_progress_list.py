from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector
from threading import Thread, Event #Needed to work with events
import time #Needed for sleep function

# In Progress List
        
class In_Progress:
        #This function will reset the window back to its default state.
    def reset_window(self):
        #Delete all of the entries in the tree first.
        self.tree.delete(*self.tree.get_children())

        connection=mysql.connector.connect(host="localhost",
        user="root",password="Razgriz!949",
        auth_plugin="mysql_native_password", database="inventory_system")
        cursor = connection.cursor()

        #Print all the database records onto the GUI.
        querySearch = "SELECT * FROM work_in_progress"
        cursor.execute(querySearch)
        records  = cursor.fetchall()

        counter = 0
        for row in records:
            self.tree.insert('', 'end', values=
            (row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
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
            querySearch = "SELECT * FROM work_in_progress"
            cursor.execute(querySearch)
            records  = cursor.fetchall()

            counter = 0
            for row in records:
                self.tree.insert('', 'end', values=
                (row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
                counter += 1
                    
            cursor.close()
            connection.close()
           
        else:
            connection=mysql.connector.connect(host="localhost",
            user="root",password="Razgriz!949",
            auth_plugin="mysql_native_password", database="inventory_system")
            cursor = connection.cursor()

            #Print all the database records onto the GUI.
            querySearch = ("SELECT * FROM work_in_progress WHERE wo_number LIKE '%{}%'").format(queryInput)
            cursor.execute(querySearch)
            records  = cursor.fetchall()

            counter = 0
            for row in records:
                self.tree.insert('', 'end', values=
                (row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
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
            querySort = "SELECT * FROM work_in_progress ORDER BY wo_number"
        elif (col == 1):
            querySort = "SELECT * FROM work_in_progress ORDER BY status"
        elif (col == 2):
            querySort = "SELECT * FROM work_in_progress ORDER BY date_recv"
        elif (col == 3):
            querySort = "SELECT * FROM work_in_progress ORDER BY eta"
        elif (col == 4):
            querySort = "SELECT * FROM work_in_progress ORDER BY cust_id"
        elif (col == 5):
            querySort = "SELECT * FROM work_in_progress ORDER BY price"
        elif (col == 6):
            querySort = "SELECT * FROM work_in_progress ORDER BY address"        

        #Print all the database records onto the GUI.
        cursor.execute(querySort)
        records  = cursor.fetchall()

        counter = 0
        for row in records:
            self.tree.insert('', 'end', values=
            (row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
            counter += 1
                
        cursor.close()
        connection.close()
        
##    def idle_timer(self):
##        #Increment i by 1 and continue to sleep for a second until loop breaks
##        i = 0
##        while True:
##            i += 1
##            time.sleep(1)
##
##            if self.stop_event.is_set():
##                break
        
    def __init__(self, master):
##      self.stop_event = Event()
        self.master=master
        self.tree=ttk.Treeview(master, column=("column", "column1", "column2",
        "column3", "column4", "column5", "column6")) #Needed to create new columns
        self.master.title("Work In Progress")
        self.master.geometry("900x600")
        self.searchEntry = tk.StringVar()
        self.master.resizable(False, False) #Don't allow users to resize window.

        # Configure the following widgets below
        self.lTitle = tk.Label(master, text="Work In Progress", font=("Arial", 20))
        self.eSearch = tk.Entry(master, textvariable=self.searchEntry, width=25)
        self.bSearch = tk.Button(master, text="Search", command=self.search_columns)
        self.bQuit = tk.Button(master, text="Quit", command=master.destroy)
        self.bReset = tk.Button(master, text="Reset", command=self.reset_window)

        self.lTitle.place(x=300, y=10)
        self.eSearch.place(x=600, y=100)
        self.bSearch.place(x=800, y=100)
        self.bReset.place(x=100, y=500)
        self.bQuit.place(x=800, y=500)

        # Create the columns and headings below
        self.tree.column("#0", minwidth=0, width=0, stretch=False)
        self.tree.heading("#1", text="Work #", command=lambda: self.sort_column(self.tree, 0))
        self.tree.column("#1", minwidth=0, width=50, stretch=False)
        self.tree.heading("#2", text="Status", command=lambda: self.sort_column(self.tree, 1))
        self.tree.column("#2", minwidth=0, width=100, stretch=False)
        self.tree.heading("#3", text="Date Received", command=lambda: self.sort_column(self.tree, 2))
        self.tree.column("#3", minwidth=0, width=150, stretch=False)
        self.tree.heading("#4", text="ETA", command=lambda: self.sort_column(self.tree, 3))
        self.tree.column("#4", minwidth=0, width=150, stretch=False)
        self.tree.heading("#5", text="Customer ID", command=lambda: self.sort_column(self.tree, 4))
        self.tree.column("#5", minwidth=0, width=100, stretch=False)
        self.tree.heading("#6", text="Price", command=lambda: self.sort_column(self.tree, 5))
        self.tree.column("#6", minwidth=0, width=50, stretch=False)
        self.tree.heading("#7", text="Address", command=lambda: self.sort_column(self.tree, 6))
        self.tree.column("#7", minwidth=0, width=250, stretch=False)

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
        printAll = "SELECT * FROM work_in_progress"
        cursor.execute(printAll)
        records  = cursor.fetchall()

        counter = 0
        for row in records:
            self.tree.insert('', 'end', values=
            (row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
            counter += 1

        cursor.close()
        connection.close()
        print("MySQL connection closed.")
        
##        #Create a thread for idle_timer
##        self.action_thread = Thread(target=self.idle_timer)
##
##        #Start the thread and continue for 600 seconds before timeout.
##        self.action_thread.start()
##        self.action_thread.join(timeout=600)
##
##        #Send a signal to stop the thread.
##        self.stop_event.set()

if __name__ == '__main__':
    window = Tk()
    thisMain = In_Progress(window)
    window.mainloop()
