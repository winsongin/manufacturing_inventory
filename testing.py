from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
import mysql.connector
import itertools

import assembly_class
import login
import testing
import shipping
import receiving
import accounting
import admin
import inventory


class TestingWindow:
    def __init__(self, master, emp_id):
        self.master = master
        self.wo = ""
        self.wonum = "Work Order: " + self.wo
        self.emp_id = "Worker ID: " + emp_id
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Razgriz!949",
            database="inventory_system"
        )
        self.cursor = self.mydb.cursor(buffered=True)
        self.testWindow()

    def testWindow(self):

        # Instantiates style for ttk buttons. Please use this for your buttons
        style = Style()

        self.FileMenu = Menu(self.master)
        self.master.config(menu=self.FileMenu)

        self.subMenu = Menu(self.FileMenu)
        self.subMenu2 = Menu(self.FileMenu)
        self.FileMenu.add_cascade(label="File", menu=self.subMenu)
        self.subMenu.add_command(label="Exit", command=self.master.destroy)
        self.subMenu.add_command(label="Logout", command=self.Logoff)

        # creating labels here:
        self.testing_label = Label(self.master, text="TESTING PROCESS", relief="solid", width=17.5, font=("arial", 25, "bold"))

        # displaying worker ID:
        self.workerID_label = Label(self.master, text=self.emp_id, font=("arial", 15, "bold"))
        self.workerID_label.place(x=225, y=110)

        # displaying Order Status:
        self.status_label = Label(self.master, text="Order Status: ", font=("arial", 15, "bold"))
        self.stat = StringVar()
        self.orderStatusEntry = Label(self.master, text="Testing", font=("arial", 15, "bold"))

        self.test1_label = Label(self.master, text="Test 1: Speed ", font=("arial", 13, "bold"))
        self.test2_label = Label(self.master, text="Test 2: Durability ", font=("arial", 13, "bold"))
        self.test3_label = Label(self.master, text="Test 3: Battery Efficiency  ", font=("arial", 13, "bold"))
        self.test4_label = Label(self.master, text="Test 4: Remote Signal Range ", font=("arial", 13, "bold"))
        self.parameters_label = Label(self.master, text="Parameters", relief="solid", width=10, font=("arial", 12, "bold"))

        self.p1 = Label(self.master, text="[5-12 MPH]", font=("arial", 12, "bold"))
        self.p2 = Label(self.master, text="[98% or >]", font=("arial", 12, "bold"))
        self.p3 = Label(self.master, text="[2-4 Hours]", font=("arial", 12, "bold"))
        self.p4 = Label(self.master, text="[98% or >]", font=("arial", 12, "bold"))

        # Creating buttons here:
        style.configure('C.TButton', padding=0, font=("arial", 12), background='gray',
                        foreground='Green')

        self.enter_button = Button(self.master, text="Enter", command=lambda: self.onClick(tree, selection.get()),  style='C.TButton')  # Command is binding to fuction.
        self.reset_button = Button(self.master, text="Reset", command=self.reset, style='C.TButton')

        # User input
        self.E3 = IntVar()
        self.entry3 = Entry(self.master, textvariable=self.E3)
        self.E4 = IntVar()
        self.entry4 = Entry(self.master, textvariable=self.E4)
        self.E5 = IntVar()
        self.entry5 = Entry(self.master, textvariable=self.E5)
        self.E6 = IntVar()
        self.entry6 = Entry(self.master, textvariable=self.E6)

        # Placing all Labels and Buttons on to window.
        self.testing_label.place(x=160, y=10)
        self.workerID_label.place(x=10, y=110)
        self.status_label.place(x=10, y=140)
        self.orderStatusEntry.place(x=150, y=140)
        self.parameters_label.place(x=480, y=190)

        # placing items here on master
        self.test1_label.place(x=50, y=220)
        self.test2_label.place(x=50, y=250)
        self.test3_label.place(x=50, y=280)
        self.test4_label.place(x=50, y=310)

        self.p1.place(x=480, y=220)
        self.p2.place(x=480, y=250)
        self.p3.place(x=480, y=280)
        self.p4.place(x=480, y=310)
        self.enter_button.place(x=440, y=340)
        self.reset_button.place(x=320, y=340)

        self.entry3.place(x=310, y=220)
        self.entry4.place(x=310, y=250)
        self.entry5.place(x=310, y=280)
        self.entry6.place(x=310, y=310)

        #Selection Grid
        tree = Treeview(self.master, column=("column", "column1", "column2", "column3", "column4"))
        searchQuery = StringVar()
        selection = StringVar()

        load_button = Button(self.master, text="Select Work Order", command=lambda: self.select(selection.get()), style='C.TButton')
        selection_entry = Entry(self.master, width=15, textvariable=selection)

        selection_entry.place(x=500, y=110)
        load_button.place(x=500, y=140)

        tree.column("#0", minwidth=0, width=0, stretch=False)
        tree.heading("#1", text="Work Order", command=lambda: self.sort_column(tree, 0, "Testing", False))
        tree.column("#1", minwidth=0, width=100, stretch=False)
        tree.heading("#2", text="Department", command=lambda: self.sort_column(tree, 1, "Testing", False))
        tree.column("#2", minwidth=0, width=100, stretch=False)
        tree.heading("#3", text="Customer", command=lambda: self.sort_column(tree, 2, "Testing", False))
        tree.column("#3", minwidth=0, width=150, stretch=False)
        tree.heading("#4", text="Received Date", command=lambda: self.sort_column(tree, 3, "Testing", False))
        tree.column("#4", minwidth=0, width=150, stretch=False)
        tree.heading("#5", text="Estimated Ship", command=lambda: self.sort_column(tree, 4, "Testing", False))
        tree.column("#5", minwidth=0, width=150, stretch=False)

        tree.configure(height=5)
        tree.place(x=7, y=370) # You may need to increase y's value to fit your form

        printAll = "SELECT * FROM work_in_progress WHERE status = \"" + "Testing" + "\""
        cursor = self.mydb.cursor()
        cursor.execute(printAll)
        records = cursor.fetchall()

        for row in records:
            custQuery = "SELECT name FROM customer WHERE cust_id = %s"
            self.cursor.execute(custQuery, [row[4]])
            cust = self.cursor.fetchone()
            print(cust)
            tree.insert('', 'end', values=
            (row[0], row[1], cust[0], row[2], row[3]))

    # Logout Function
    def Logoff(self):
        answer = tkinter.messagebox.askquestion("Logout", "Are you sure you want to logout? ")

        if answer == "yes":
            tkinter.messagebox.showinfo("Logout", "Goodbye")
            self.master.destroy()

            root = Tk()
            root.geometry("350x200")
            root.title("Login")
            root.resizable(False, False)
            login1 = login.Login(root)
            root.mainloop()
            if login1.dept == "Receiving":
                root = Tk()
                root.geometry("400x500")
                root.title("Receiving")
                root.resizable(False, False)
                root.configure(bg="light gray")
                receiving1 = receiving.Receiving(root)
                root.mainloop()
            elif login1.dept == "Assembly":
                root = Tk()
                root.geometry("665x380")
                root.title("Assembly")
                root.resizable(False, False)
                app = assembly_class.Assembly(root, "0002")
                root.mainloop()
            elif login1.dept == "Testing":
                root = Tk()
                root.geometry("680x500")
                root.title("Testing")
                root.resizable(False, False)
                app = TestingWindow(root, "0003")
                root.mainloop()
            elif login1.dept == "Shipping":
                root = Tk()
                root.geometry("665x380")
                root.title("Shipping")
                root.resizable(False, False)
                shipping.Shipping(root, "0004")
                root.mainloop()
            elif login1.dept == "Accounting":
                root = Tk()
                root.geometry("500x300")
                root.title("Accounting")
                root.resizable(False, False)
                close_window = Button(root, text="Close", command=root.quit)
                close_window.place(x=90, y=230)
                app = accounting.accounting(root, "0005")
                root.mainloop()
            elif login1.dept == "Admin":
                root = Tk()
                root.geometry("600x500")
                root.title("New User")
                root.resizable(False, False)
                root.configure(bg="light gray")
                admin1 = admin.Admin(root)
                root.mainloop()
            elif login1.dept == "Inventory":
                root = Tk()
                root.geometry("620x500")
                root.title("Inventory")
                root.resizable(False, False)
                app = inventory.Inventory(root)
                root.mainloop()
    #function will check if pass or fail.
    def onClick(self,tree, wo):
        answer = tkinter.messagebox.askquestion("RESULT", "Are these tests correct? ")
        cursor = self.mydb.cursor()
        if answer == "yes" and 5 <= int(self.entry3.get()) <= 12 and 98 <= int(self.entry4.get()) <= 100 and \
                2 <= int(self.entry5.get()) <= 4 and 98 <= int(self.entry6.get()) <= 100:
            tkinter.messagebox.showinfo("RESULT", "ALL TEST PASS!")
            cursor = self.mydb.cursor()
            query = "UPDATE work_in_progress SET status = 'Shipping' WHERE wo_number = \'" + wo + "\'"
            print(query)
            cursor.execute(query)
            self.mydb.commit()


        else:
            tkinter.messagebox.showinfo("RESULT", "TESTS FAILED!")
            query = "UPDATE work_in_progress SET status = 'Assembly' WHERE wo_number = \'" + wo + "\'"
            print(query)
            cursor.execute(query)
            self.mydb.commit()

        printAll = "SELECT * FROM work_in_progress WHERE status = \"" + "Testing" + "\""
        cursor = self.mydb.cursor()
        cursor.execute(printAll)
        records = cursor.fetchall()

        for i in tree.get_children():
            tree.delete(i)

        for row in records:
            custQuery = "SELECT name FROM customer WHERE cust_id = %s"
            self.cursor.execute(custQuery, [row[4]])
            cust = self.cursor.fetchone()
            print(cust)
            tree.insert('', 'end', values=
            (row[0], row[1], cust[0], row[2], row[3]))

    # gets status of order
    def getStatus(self):
        cursor3 = self.mydb.cursor()
        statement = "SELECT status  FROM work_in_progress WHERE status = '{}' "
        cursor3.execute(statement)
        stat = cursor3.fetchall()
        return stat

    # Function will Reset all Testing inputs
    def reset(self):
        self.E3.set(' ')
        self.E4.set(' ')
        self.E5.set(' ')
        self.E6.set(' ')

    def sort_column(self, tree, col, department, reverse):
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

        cursor.execute(querySort)
        records = cursor.fetchall()
        for row in records:
            print("Work Number: ", row[0])
            print("Status: ", row[1])
            print("Date Received: ", row[2])
            print("ETA: ", row[3])
            print("Customer ID: ", row[4])

        for row in records:
            custQuery = "SELECT name FROM customer WHERE cust_id = %s"
            self.cursor.execute(custQuery, [row[4]])
            cust = self.cursor.fetchone()
            print(cust)
            tree.insert('', 'end', values=
            (row[0], row[1], cust[0], row[2], row[3]))

    def select(self, wo):
        self.wonum = "Work Order: " + wo
        self.wo = wo
        number = Label(self.master, text=self.wonum, font=("arial", 15, "bold"))
        number.place(x=10, y=80)


if __name__ == "__main__":
    root = Tk()
    root.geometry("680x500")
    root.title("Testing")
    app = TestingWindow(root, "0001")
    root.mainloop()
