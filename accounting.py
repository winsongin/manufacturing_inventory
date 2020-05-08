from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
import mysql.connector
import itertools
import login
import testing
import shipping
import receiving
import accounting
import admin
import inventory
import assembly_class


class accounting:
    def __init__(self, master, emp_id):
        self.master = master
        self.emp_id = emp_id
        self.cust_code = ""
        self.cust_name = ""
        self.cust_address = ""
        self.cust_owe = 0.00
        self.accounting_window()
        self.totalSales = 0.00


    def __open(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Razgriz!949",
            database="inventory_system"
        )
        self.cursor = self.mydb.cursor(buffered=True)
    def accounting_window(self):

        self.__open()
        cust_query = "SELECT name FROM customer"
        self.cursor.execute(cust_query)
        cust_list = self.cursor.fetchall()
        cust_list = list(itertools.chain(*cust_list))
        self.cust_id = StringVar(self.master)
        pay = StringVar()

        # Creating file menu
        self.FileMenu = Menu(self.master)
        self.master.config(menu=self.FileMenu)
        self.subMenu = Menu(self.master)
        self.subMenu2 = Menu(self.master)
        self.FileMenu.add_cascade(label="File", menu=self.subMenu)
        self.subMenu.add_command(label="Exit", command=self.master.destroy)
        self.subMenu.add_command(label="Logout", command=self.Logoff)

        #Displays Employee number
        self.empLabel = Label(self.master, text="Employee: ", font=("arial", 12))
        self.empLabel.place(x=5, y=5)
        self.emp = Label(self.master, text=self.emp_id, font=("arial", 12))
        self.emp.place(x=90, y=6)

        #Displays Customer and Customer Selection
        self.cust_label = Label(self.master, text="Customer: ", font=("arial", 12))
        self.cust_label.place(x=5, y=30)

        #Dropdown for Customer ID
        self.cust_list = OptionMenu(self.master, self.cust_id, *cust_list)
        self.cust_list.place(x=80, y = 30)

        #Gets customer name
        self.cust_get = Button(self.master, text="Update Values", command=lambda: self.update_data(self.cust_id.get()))
        self.cust_get.place(x=220, y=30)

        #Retrieved Data
        self.cust_id_label = Label(self.master, text="Customer ID: (Please Select Customer)", font=("arial", 12))
        self.cust_id_label.place(x=5, y=130)
        self.cust_add_label = Label(self.master, text="Customer Address: (Please Select Customer)", font=("arial", 12))
        self.cust_add_label.place(x=5, y=155)
        self.cust_owe_label = Label(self.master, text="Owe: $ (Please Select Customer)", font=("arial", 12))
        self.cust_owe_label.place(x=5, y=180)
        self.cust_pay_label = Label(self.master, text="Paid: $", font=("arial", 12))
        self.cust_pay_label.place(x=5, y=205)
        self.cust_pay_entry = Entry(self.master, width=10, textvariable=pay)
        self.cust_pay_entry.place(x=60, y=205)

        #Submit button
        self.submit_btn = Button(self.master, text="Submit", command=lambda: self.submit(pay.get(), self.cust_id.get()))
        self.submit_btn.place(x=5, y=230)

        self.viewSales_btn = Button(self.master, text = "Total Sales", command= self.showTSales)
        self.viewSales_btn.place(x=5, y = 260)

    def update_data(self, cust_id):
        self.cust_id_label.destroy()
        self.cust_add_label.destroy()
        self.cust_owe_label.destroy()
        query = "SELECT * FROM customer WHERE name = \"" + cust_id + "\";"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        data = list(itertools.chain(*data))
        self.cust_code = data[0]
        self.cust_name = data[1]
        self.cust_address = data[2]
        self.cust_owe = float(data[3])
        cust_code = "Customer ID: " + self.cust_code
        addr = "Customer Address: " + self.cust_address
        owe = self.cust_owe
        owe = "{:0.2f}".format(owe)
        owe = "Owe: $" + owe
        self.cust_id_label = Label(self.master, text=cust_code, font=("arial", 12))
        self.cust_id_label.place(x=5, y=130)
        self.cust_add_label = Label(self.master, text=addr, font=("arial", 12))
        self.cust_add_label.place(x=5, y=155)
        self.cust_owe_label = Label(self.master, text=owe, font=("arial", 12, "bold"))
        self.cust_owe_label.place(x=5, y=180)

    def submit(self, amt_paid, cust):
        total = float(self.cust_owe) - float(amt_paid)
        self.totalSales = self.totalSales + float(amt_paid)
        print(self.totalSales)
        print("{:0.2f}".format(total))
        print(type(total))
        total = str(round(total, 2))
        print(total)
        query = "UPDATE customer SET owe = \"" + str(total) + "\" WHERE name = \"" + cust + "\";"
        self.cursor.execute(query)
        self.mydb.commit()
    
    def showTSales(self):      
        message = "$" + str("{:.2f}".format(self.totalSales))
        tkinter.messagebox.showinfo("Total Sales",message)

        # logout fucntion

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
    root.geometry("500x300")
    root.title("Accounting")
    close_window = Button(root, text="Close", command=root.quit)
    close_window.place(x=90, y=230)
    app = accounting(root, "0003")
    root.mainloop()
