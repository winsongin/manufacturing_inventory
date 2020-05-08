from datetime import datetime, timedelta
import time as tm
from tkinter import *
import mysql.connector
import sys
import random
import tkinter as tk
import tkinter.messagebox
import login
import testing
import shipping
import receiving
import accounting
import admin
import inventory
import assembly_class

myDb = mysql.connector.connect(host = "localhost", user = "root", passwd = "Razgriz!949", database = "inventory_system")

class Receiving: 
    def datentime(self):
        self.now = datetime.now()
        self.now = self.now.strftime("%m/%d/%Y, %H:%M:%S")
        return self.now

    def workOrderNumber(self): 
        myCursor = myDb.cursor()
        latestWorkOrder = "SELECT MAX(wo_number) FROM work_in_progress"
        myCursor.execute(latestWorkOrder)
        result = myCursor.fetchall()
        myDb.commit()
        list = [x[0] for x in result]
        lastWorkOrder = str(list[0])
        print(lastWorkOrder)
        if(lastWorkOrder == 'None'):
            nextWorkOrder = "1"
            print(nextWorkOrder)
            return nextWorkOrder
        nextWorkOrder = int(lastWorkOrder) + 1
        return nextWorkOrder

    # ETA of manufacturing a product is roughly 2 hours after the work order is received
    def estimatedTimeOfArrival(self): 
        self.eta = (datetime.now() + timedelta(days=2))
        self.eta = self.eta.strftime("%m/%d/%Y, %H:%M:%S")
        return self.eta

    def owe(self):
        myCursor = myDb.cursor()
        custWorkOrders = "SELECT (price) FROM work_in_progress WHERE cust_id = {}"
        myCursor.execute(custWorkOrders.format(self.customerIDEntry.get()))
        result = myCursor.fetchall()
        myDb.commit()

        owed = 0 
        for i in result:
            owed = owed + i[0]
        print(owed)
        return owed

    def onSubmit(self):
        myCursor = myDb.cursor()

        orderNumber = self.workOrderNumber()
        stat = "Assembly" 
        dateTime = self.datentime()
        estTimeArrv = self.estimatedTimeOfArrival()
        orderPrice = self.priceEntry.get()
        orderQuantity = self.quantityEntry.get()
        custName = self.customerNameEntry.get()
        custID = self.customerIDEntry.get()
        #trackingNum = self.trackingNumberEntry.get()
        orderStat = self.orderStatusEntry.get()
        custAddr = self.addressEntry.get()
        custOwe = self.priceEntry.get()

        query2 = "INSERT INTO customer (cust_id, name, address, owe) VALUES (%s, %s, %s, %s)"
        myCursor.execute(query2, (custID, custName, custAddr, custOwe))
        myDb.commit()

        query = "INSERT INTO work_in_progress (wo_number, status, date_recv, eta, price, cust_id, address) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        myCursor.execute(query, (orderNumber, orderStat, dateTime, estTimeArrv, orderPrice, custID, custAddr))
        myDb.commit()
        tkinter.messagebox.showinfo("Success", "New Part Successfully Added")

        self.dateTimeInput.set(self.datentime())
        self.workOrderInput.set(self.workOrderNumber())
        self.ETAInput.set(self.estimatedTimeOfArrival())
        self.priceInput.set("")
        self.customerNameInput.set("")
        self.customerIDInput.set("")
        self.addressInput.set("")
        self.orderStatusInput.set("")
        self.quantityInput.set("")

    def reset(self):
        self.dateTimeInput.set(self.datentime())
        self.workOrderInput.set(self.workOrderNumber())
        self.ETAInput.set(self.estimatedTimeOfArrival())
        self.priceInput.set("")
        self.customerNameInput.set("")
        self.customerIDInput.set("")
        self.addressInput.set("")
        #self.trackingNumberInput.set("")
        self.orderStatusInput.set("")
        self.quantityInput.set("")

    def __init__(self, root):
        self.root = root

        myCursor = myDb.cursor()

        # Creating file menu
        self.FileMenu = Menu(self.root)
        self.root.config(menu=self.FileMenu)
        self.subMenu = Menu(self.root)
        self.subMenu2 = Menu(self.root)
        self.FileMenu.add_cascade(label="File", menu=self.subMenu)
        self.subMenu.add_command(label="Exit", command=self.root.destroy)
        self.subMenu.add_command(label="Logout", command=self.Logoff)

        # Prints the Date/Time
        self.dateTimeInput = tk.StringVar()
        self.dateTimeLabel = tk.Label(self.root, text="Date/Time:", bg="light gray")
        self.dateTimeEntry = tk.Entry(self.root, textvariable=self.dateTimeInput, highlightbackground="light gray",
                                      width=25)
        self.dateTimeInput.set(self.datentime())
        self.dateTimeLabel.place(x=40, y=20)
        self.dateTimeEntry.place(x=150, y=20)

        # ETA is computed and displayed to the user
        self.ETAInput = tk.StringVar()
        self.ETALabel = tk.Label(self.root, text="ETA:", bg="light gray")
        self.ETAEntry = tk.Entry(self.root, textvariable=self.ETAInput, highlightbackground="light gray", width=25)
        self.ETAInput.set(self.estimatedTimeOfArrival())
        # self.ETALabel.place(x=40, y=100)
        # self.ETAEntry.place(x=150, y=100)
        self.ETALabel.place(x=40, y=60)
        self.ETAEntry.place(x=150, y=60)

        # Auto-increments the last Work Order Number and displays it to the user
        self.workOrderInput = tk.StringVar()
        self.workOrderLabel = tk.Label(self.root, text="Work Order #:", bg="light gray")
        self.workOrderEntry = tk.Entry(self.root, textvariable=self.workOrderInput, highlightbackground="light gray",
                                       width=25)
        self.workOrderInput.set(self.workOrderNumber())
        # self.workOrderLabel.place(x=40, y=60)
        # self.workOrderEntry.place(x=150, y=60) Switched position with ETA
        self.workOrderLabel.place(x=40, y=100)
        self.workOrderEntry.place(x=150, y=100)



        # Prompts the user for the customer's ID
        self.customerIDInput = tk.StringVar()
        self.customerIDLabel = tk.Label(self.root, text="Customer ID:", bg="light gray")
        self.customerIDEntry = tk.Entry(self.root, textvariable=self.customerIDInput, highlightbackground="light gray",
                                        width=25)
        # self.customerIDLabel.place(x=40, y=260)
        # self.customerIDEntry.place(x=150, y=260) Switched with Price
        self.customerIDLabel.place(x=40, y=140)
        self.customerIDEntry.place(x=150, y=140)

        # Prompts the user for the customer's name
        self.customerNameInput = tk.StringVar()
        self.customerNameLabel = tk.Label(self.root, text="Name:", bg="light gray")
        self.customerNameEntry = tk.Entry(self.root, textvariable=self.customerNameInput,
                                          highlightbackground="light gray", width=25)
        self.customerNameLabel.place(x=40, y=180) # 220
        self.customerNameEntry.place(x=150, y=180)

        # Prompts the user for the customer's address
        self.addressInput = tk.StringVar()
        self.addressLabel = tk.Label(self.root, text="Address:", bg="light gray")
        self.addressEntry = tk.Entry(self.root, textvariable=self.addressInput, highlightbackground="light gray",
                                     width=25)
        # self.addressLabel.place(x=40, y=340)
        # self.addressEntry.place(x=150, y=340) Moved to Quantity
        self.addressLabel.place(x=40, y=220)
        self.addressEntry.place(x=150, y=220)

        # Prompts the user for the quantity
        self.quantityInput = tk.StringVar()
        self.quantityLabel = tk.Label(self.root, text="Quantity:", bg="light gray")
        self.quantityEntry = tk.Entry(self.root, textvariable=self.quantityInput, highlightbackground="light gray",
                                      width=25)
        self.quantityLabel.place(x=40, y=260)
        self.quantityEntry.place(x=150, y=260)

        # Prompts the user for the order status
        self.orderStatusInput = tk.StringVar()
        self.orderStatusLabel = tk.Label(self.root, text="Order status:", bg="light gray")
        self.orderStatusEntry = tk.Entry(self.root, textvariable=self.orderStatusInput,
                                         highlightbackground="light gray", width=25)
        self.orderStatusLabel.place(x=40, y=300)
        self.orderStatusEntry.place(x=150, y=300)

        # Prompts the user for the price of the product
        self.priceInput = tk.StringVar()
        self.priceLabel = tk.Label(self.root, text="Price:", bg="light gray")
        self.priceEntry = tk.Entry(self.root, textvariable=self.priceInput, highlightbackground="light gray", width=25)
        # self.priceLabel.place(x=40, y=140)
        # self.priceEntry.place(x=150, y=140) Switched with customer name
        self.priceLabel.place(x=40, y=340)
        self.priceEntry.place(x=150, y=340)

        self.submit = tk.Button(self.root, text="Submit", bg='red', highlightbackground="light gray",
                                command=self.onSubmit)
        self.submit.place(x=250, y=380)

        self.reset = tk.Button(self.root, text="Reset", bg='red', highlightbackground="light gray", command=self.reset)
        self.reset.place(x=200, y=380)

    def Logoff(self):
        answer = tkinter.messagebox.askquestion("Logout", "Are you sure you want to logout? ")

        if answer == "yes":
            tkinter.messagebox.showinfo("Logout", "Goodbye")
            self.root.destroy()

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
    root = tk.Tk()
    root.geometry("650x500")
    root.title("Receiving")
    root.configure(bg="light gray")
    receiving1 = Receiving(root)
    root.mainloop()




