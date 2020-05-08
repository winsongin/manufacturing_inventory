#Change these as needed
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
import mysql.connector
import itertools
import openpyxl
from datetime import date
import shutil
import login
import testing
import shipping
import receiving
import accounting
import admin
import inventory
import assembly_class


class Shipping:# Change Department to your department
    def __init__(self, master, emp_id):
        self.master = master
        self.wo = ""
        self.customer = "Customer: "
        self.addr = "Address: "
        self.price = "Price: $"
        self.wonum = "Work Order: " + self.wo
        self.emp_id = "Worker ID: " + emp_id
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Razgriz!949",
            database="inventory_system"
        )
        self.cursor = self.mydb.cursor(buffered=True)
        self.shipping() # Change MyWindow to your window name

    # Change MyWindow to your window name
    def shipping(self):

        # Worker ID Label. Do Not Move
        id = Label(self.master, text=self.emp_id, font=("arial", 12, "bold"))
        id.place(x=5, y=65)

        # Instantiates style for ttk buttons. Please use this for your buttons
        style = Style()
        style.configure('C.TButton', padding=0, font=("arial", 12), background='gray',
                        foreground='Green')

        # Creating file menu
        self.FileMenu = Menu(self.master)
        self.master.config(menu=self.FileMenu)
        self.subMenu = Menu(self.master)
        self.subMenu2 = Menu(self.master)
        self.FileMenu.add_cascade(label="File", menu=self.subMenu)
        self.subMenu.add_command(label="Exit", command=self.master.destroy)
        self.subMenu.add_command(label="Logout", command=self.Logoff)

        # INSERT CODE HERE YOU CAN BASICALLY COPY AND PASTE

        tracking = StringVar()

        self.testing_label = Label(self.master, text="Shipping", relief="solid", width=8,
                                   font=("arial", 25, "bold"))
        self.woLabel = Label(self.master, text=self.wonum,font=("arial", 12, "bold"))
        self.custLabel = Label(self.master, text=self.customer, font=("arial", 13, "bold"))
        self.addrLabel = Label(self.master, text=self.addr, font=("arial", 13, "bold"))
        self.priceLabel = Label(self.master, text=self.price,font=("arial", 13, "bold"))
        self.trackingLabel = Label(self.master, text="Tracking: ", font=("arial", 13, "bold"))
        self.trackingEntry = Entry(self.master, width=20, textvariable=tracking)

        self.testing_label.place(x=260, y=10)
        self.woLabel.place(x=5, y=85)
        self.custLabel.place(x=5, y=140)
        self.addrLabel.place(x=5, y=165)
        self.priceLabel.place(x=5, y=190)
        self.trackingLabel.place(x=5, y=215)
        self.trackingEntry.place(x=90, y=215)

        # BELOW IS THE CODE FOR THE SELECTION WINDOW

        #Selection Grid
        tree = Treeview(self.master, column=("column", "column1", "column2", "column3", "column4"))
        searchQuery = StringVar()
        selection = StringVar()

        load_button = Button(self.master, text="Select Work Order", command=lambda: self.select(selection.get()), style='C.TButton')
        selection_entry = Entry(self.master, width=15, textvariable=selection)

        selection_entry.place(x=400, y=68)
        load_button.place(x=500, y=67)

        tree.column("#0", minwidth=0, width=0, stretch=False)
        tree.heading("#1", text="Work Order", command=lambda: self.sort_column(tree, 0, False))
        tree.column("#1", minwidth=0, width=100, stretch=False)
        tree.heading("#2", text="Department", command=lambda: self.sort_column(tree, 1, False))
        tree.column("#2", minwidth=0, width=100, stretch=False)
        tree.heading("#3", text="Customer", command=lambda: self.sort_column(tree, 2, False))
        tree.column("#3", minwidth=0, width=150, stretch=False)
        tree.heading("#4", text="Received Date", command=lambda: self.sort_column(tree, 3, False))
        tree.column("#4", minwidth=0, width=150, stretch=False)
        tree.heading("#5", text="Estimated Ship", command=lambda: self.sort_column(tree, 4, False))
        tree.column("#5", minwidth=0, width=150, stretch=False)

        tree.configure(height=5)
        tree.place(x=7, y=240) # You may need to increase y's value to fit your form

        printAll = "SELECT * FROM work_in_progress WHERE status = \"" + "Shipping" + "\"" # CHANGE "ASSEMBLY" TO YOUR DEPARTMENT
        cursor = self.mydb.cursor()
        cursor.execute(printAll)
        records = cursor.fetchall()

        for row in records:
            custQuery = "SELECT name FROM customer WHERE cust_id = %s"
            self.cursor.execute(custQuery, [row[4]])
            cust = self.cursor.fetchone()
            tree.insert('', 'end', values=
            (row[0], row[1], cust[0], row[2], row[3]))

        submitBtn = Button(self.master, text="Submit", command=lambda: self.submit(tree), style='C.TButton')
        printBtn = Button(self.master, text="Print", command=self.print, style='C.TButton')

        submitBtn.place(x=480, y=95, width=80)
        printBtn.place(x=480, y=125, width=80)

    # INSERT FUNCTIONS BELOW

    def submit(self, tree):
        update = "UPDATE work_in_progress SET status = 'Completed' WHERE wo_number = \"" + self.wo + "\""
        self.cursor.execute(update)
        self.mydb.commit()

        tree.delete(*tree.get_children())

        tree.column("#0", minwidth=0, width=0, stretch=False)
        tree.heading("#1", text="Work Order", command=lambda: self.sort_column(tree, 0, False))
        tree.column("#1", minwidth=0, width=100, stretch=False)
        tree.heading("#2", text="Department", command=lambda: self.sort_column(tree, 1, False))
        tree.column("#2", minwidth=0, width=100, stretch=False)
        tree.heading("#3", text="Customer", command=lambda: self.sort_column(tree, 2, False))
        tree.column("#3", minwidth=0, width=150, stretch=False)
        tree.heading("#4", text="Received Date", command=lambda: self.sort_column(tree, 3, False))
        tree.column("#4", minwidth=0, width=150, stretch=False)
        tree.heading("#5", text="Estimated Ship", command=lambda: self.sort_column(tree, 4, False))
        tree.column("#5", minwidth=0, width=150, stretch=False)

        tree.configure(height=5)
        tree.place(x=7, y=240)  # You may need to increase y's value to fit your form

        printAll = "SELECT * FROM work_in_progress WHERE status = \"" + "Shipping" + "\""  # CHANGE "ASSEMBLY" TO YOUR DEPARTMENT
        cursor = self.mydb.cursor()
        cursor.execute(printAll)
        records = cursor.fetchall()

        for row in records:
            custQuery = "SELECT name FROM customer WHERE cust_id = %s"
            self.cursor.execute(custQuery, [row[4]])
            cust = self.cursor.fetchone()
            tree.insert('', 'end', values=
            (row[0], row[1], cust[0], row[2], row[3]))

        tkinter.messagebox.showinfo("Success", "Part Shipped")

    def print(self):
        query = "SELECT cust_id, address, price FROM work_in_progress WHERE wo_number = \"" + self.wo + "\""
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        cust_id = result[0]
        custQuery = "SELECT name FROM customer WHERE cust_id = \"" + cust_id + "\""
        self.cursor.execute(custQuery)
        custResult = self.cursor.fetchone()
        data = [result[0], custResult[0], result[1], result[2]]
        today = date.today()
        tracking = self.trackingEntry.get()

        file = "invoice_template.xlsx"
        workbook = openpyxl.load_workbook(file)
        active = workbook.active
        active["B9"] = 1
        active["C4"] = custResult[0]
        active["C5"] = result[1]
        active["D9"] = 1
        active["E9"] = float(result[2])
        active["F9"] = 0
        active["G4"] = tracking
        active["G5"] = today

        newfile = custResult[0] + " Invoice.xlsx"

        workbook.save(newfile)
        savemessage = "Saved " + newfile

        oldpath = 'C:/Users/Ralph/Desktop/manufacturing_inventory/' + newfile
        newpath = 'C:/Users/Ralph/Desktop/manufacturing_inventory/Invoices'

        shutil.move(oldpath, newpath)
        tkinter.messagebox.showinfo("Saved", savemessage)

    # BELOW IS CODE FOR THE TREE. DO NOT CHANGE

    def sort_column(self, tree, col, reverse):
        tree.delete(*tree.get_children())

        if (col == 0):
            querySort = "SELECT * FROM work_in_progress WHERE status = 'Shipping' ORDER BY wo_number"
        elif (col == 1):
            querySort = "SELECT * FROM work_in_progress WHERE status = 'Shipping' ORDER BY status"
        elif (col == 2):
            querySort = "SELECT * FROM work_in_progress WHERE status = 'Shipping' ORDER BY cust_id"
        elif (col == 3):
            querySort = "SELECT * FROM work_in_progress WHERE status = 'Shipping' ORDER BY date_recv"
        elif (col == 4):
            querySort = "SELECT * FROM work_in_progress WHERE status = 'Shipping' ORDER BY eta"

        self.cursor.execute(querySort)
        records = self.cursor.fetchall()

        for row in records:
            custQuery = "SELECT name FROM customer WHERE cust_id = %s"
            self.cursor.execute(custQuery, [row[4]])
            cust = self.cursor.fetchone()
            tree.insert('', 'end', values=
            (row[0], row[1], cust[0], row[2], row[3]))


    def select(self, wo):
        self.wonum = "Work Order: " + wo
        self.wo = str(wo)
        query = "SELECT cust_id, address, price FROM work_in_progress WHERE wo_number = \"" + self.wo + "\""
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        cust_id = result[0]
        custQuery = "SELECT name FROM customer WHERE cust_id = \"" + cust_id + "\""
        self.cursor.execute(custQuery)
        custResult = self.cursor.fetchone()
        data = [result[0], custResult[0], result[1], result[2]]

        self.customer = "Customer: " + data[1]
        self.addr = "Address: " + data[2]
        self.price = "Price: $" + data[3]

        self.woLabel.destroy()
        self.custLabel.destroy()
        self.addrLabel.destroy()
        self.priceLabel.destroy()


        self.custLabel = Label(self.master, text=self.customer, font=("arial", 13, "bold"))
        self.addrLabel = Label(self.master, text=self.addr, font=("arial", 13, "bold"))
        self.priceLabel = Label(self.master, text=self.price, font=("arial", 13, "bold"))

        self.custLabel.place(x=5, y=140)
        self.addrLabel.place(x=5, y=165)
        self.priceLabel.place(x=5, y=190)


        self.woLabel = Label(self.master, text=self.wonum, font=("arial", 12, "bold"))
        self.woLabel.place(x=5, y=85)

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
                app = testing.TestingWindow(root, "0003")
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

if __name__ == "__main__":
    root = Tk()
    root.geometry("665x380") #You may need to change this to fit your window
    root.title("Department") # Change to your department
    app = Shipping(root, "0001") #Change to your window name
    root.mainloop()