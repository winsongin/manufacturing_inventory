from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector

# In Progress List

class in_progress:
    def __init__(self,master):
        self.master=master
        self.tree=ttk.Treeview(master, column=("column", "column1",
        "column2", "column3", "column4")) #Needed to create new columns
        self.master.title("Work In Progress")
        searchEntry = StringVar()
        self.master.resizable(False, False) #Don't allow users to resize window.
        # Set up the grid configurations below.
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        
        # Configure the labels and the entry below
        self.lTitle = Label(self.master, text="Work In Progress")
        self.lWorkNum = Label(self.master, text="Work #")
        self.lStatus = Label(self.master, text="Status")
        self.lDaysLeft = Label(self.master, text="Days Until Shipment")
        self.lDateRecv = Label(self.master, text="Date Received")
        self.lETA = Label(self.master, text="Estimated Time of Arrival")
        self.eSearch = Entry(self.master, textvariable=searchEntry, width=25)
        self.bSearch = Button(self.master, text="Search")
        self.bQuit = Button(self.master, text="Quit", command=self.master.destroy)
        
        # Now arrange all of the parts above in a grid.
        self.lTitle.grid(row=0, column=0, sticky=E+W)
        self.eSearch.grid(row=0, column=1, sticky=E)
        self.bSearch.grid(row=0, column=2, sticky=E)
        self.bQuit.grid(row=1, column=2)

        # Create the columns and headings below
        self.tree.column("#0", minwidth=0, width=0)
        self.tree.heading("#1", text="Work #")
        self.tree.column("#1", minwidth=0, width=100)
        self.tree.heading("#2", text="Status")
        self.tree.column("#2", minwidth=0, width=100)
        self.tree.heading("#3", text="Days Until Shipment")
        self.tree.column("#3", minwidth=0, width=150)
        self.tree.heading("#4", text="Date Received")
        self.tree.column("#4", minwidth=0, width=100)
        self.tree.heading("#5", text="Estimated Time of Arrival")
        self.tree.column("#5", minwidth=0, width=150)

        self.tree.configure(height=20)
        self.tree.grid() #Arrange all the TreeView parts in a grid.

        #Connect to the database if possible.
        connection=mysql.connector.connect(host="localhost",
        user="root",password="T1t@n1umus",
        auth_plugin="mysql_native_password", database="inventory_system")
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
                self.tree.insert('', 'end', values=
                (row[0],row[1],row[2],row[3],row[4]))
                counter += 1

        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection closed.")
                
if __name__ == "__main__":
    window = Tk()
    main = in_progress(window)
