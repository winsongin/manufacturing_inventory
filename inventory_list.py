from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

# Inventory List

class inventory:
    def __init__(self,master):
        self.master=master
        self.tree=ttk.Treeview(master, column=
        ("column", "column1", "column2", "column3"))#Needed to create new columns
        self.master.title("Inventory List")
        searchEntry = StringVar()
        self.master.resizable(False, False) #Don't allow users to resize window.
        # Set up the grid configurations below.
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        
        # Configure the labels and the entry below
        self.lTitle = Label(self.master, text="Inventory")
        self.lPartName = Label(self.master, text="Part Name")
        self.lPartNum = Label(self.master, text="Part No.")
        self.lManufact = Label(self.master, text="Manfacturer")
        self.lQuantity = Label(self.master, text="Quantity")
        self.eSearch = Entry(self.master, textvariable=searchEntry, width=30)
        self.bSearch = Button(self.master, text="Search")

        # Now arrange all of the parts above in a grid.
        self.lTitle.grid(row=0, column=0, sticky=E+W)
        self.eSearch.grid(row=0, column=1, sticky=E)
        self.bSearch.grid(row=0, column=2, sticky=E)

        # Create the columns and headings below
        self.tree.column("#0", minwidth=0, width=0)
        self.tree.heading("#1", text="Part Name")
        self.tree.column("#1", minwidth=0, width=150)
        self.tree.heading("#2", text="Part No.")
        self.tree.column("#2", minwidth=0, width=100)
        self.tree.heading("#3", text="Manufacturer")
        self.tree.column("#3", minwidth=0, width=125)
        self.tree.heading("#4", text="Quantity")
        self.tree.column("#4", minwidth=0, width=100)

        self.tree.configure(height=20)
        self.tree.grid() #Arrange all the TreeView parts in a grid.

    def connectSQL(self):
        try:
            #Connect to the database if possible.
            connection=mysql.connector.connect(host="127.0.0.1",
            user="root",password="T1t@n1umus",
            auth_plugin="mysql_native_password", database="inventory")
            if connection.is_connected():
                db_Info = newConnect.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute("select database()")
                records = cursor.fetchone()
                print("Connected to database called ", record)

                #Print all the database records onto the GUI.
                printAll = "select * from inventory"
                cursor.execute(printAll)
                records  = cursor.fetchall()

                #Query command when intiating searches
                search_query = "SELECT * FROM inventory WHERE part_name = searchEntry"
                cursor.execute(search_query)
                records = cursor.fetchall()
                
        except Error as e:
            print("An unexpected error occured.")
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection closed.")

    #def search_list(self):
        # If search button is pressed, search through the entire list by inputted entry.


if __name__ == "__main__":
    window = Tk()
    main = inventory(window)
