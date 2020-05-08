from tkinter import *
from tkinter.ttk import *
import mysql.connector
import sys
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import assembly_class
import login
import shipping
import testing
import receiving
import accounting
import admin
import selection
# myDb = mysql.connector.connect(host = "localhost", user = "root", passwd = "Razgriz!949", database = "inventory_system")

myDb = mysql.connector.connect(host = "localhost", user = "root", passwd = "Razgriz!949", database = "inventory_system")


class Admin:
    # Order gets submitted to the database
    def onSubmit(self, tree):
        myCursor = myDb.cursor()   

        empID = self.employeeIDInput.get()
        password = self.passwordInput.get()
        fName = self.firstNameInput.get()
        lName = self.lastNameInput.get()
        pNum = self.phoneNumberInput.get()
        department = self.deptInput.get()
        # New feature: changing department that the employee works in
        changeDepartment = self.changeDeptInput.get()

        canReceive = "N"
        canAssemble = "N"
        canTest = "N"
        canShip = "N" 
        isAdmin = "N"
        isAccountant = "N"

        
        # canReceive = self.canReceiveInput.get()
        # canAssemble = self.canAssembleInput.get()
        # canTest = self.canTestInput.get()
        # canShip = self.canShipInput.get()
        # isAdmin = self.isAdminInput.get()

        # For creating first-time employees
        if self.checkBoxInput.get() == 0:
            if department == "Receiving": 
                canReceive = "Y"

            elif department == "Assembly": 
                canAssemble = "Y"

            elif department == "Testing": 
                canTest = "Y"

            elif department == "Shipping": 
                canShip = "Y"

            elif department == "Admin": 
                isAdmin = "Y"

            elif department == "Accounting": 
                isAccountant = "Y"

            query = "INSERT INTO employees (employee_id, pass, first_name, last_name, phone_number, dept, can_receive, can_assemble, can_test, can_ship, is_admin, is_accountant) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            myCursor.execute(query, (empID, password, fName, lName, pNum, department, canReceive, canAssemble, canTest, canShip, isAdmin, isAccountant))
            myDb.commit()

        # If the employees' department is being changed, the database is updated to reflect that
        else: 

            if changeDepartment == "Receiving": 
                canReceive = "Y"

            elif changeDepartment == "Assembly": 
                canAssemble = "Y"

            elif changeDepartment == "Testing": 
                canTest = "Y"

            elif changeDepartment == "Shipping": 
                canShip = "Y"

            elif changeDepartment == "Admin": 
                isAdmin = "Y"

            elif changeDepartment == "Accounting": 
                isAccountant = "Y"

            # query = "INSERT INTO employees (employee_id, pass, first_name, last_name, phone_number, dept, can_receive, can_assemble,can_test, can_ship, is_admin, is_accountant) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            query = "UPDATE employees SET pass = %s, first_name = %s, last_name = %s, phone_number = %s, dept = %s, can_receive = %s, can_assemble = %s, can_test = %s, can_ship = %s, is_admin = %s, is_accountant = %s WHERE employee_id = %s"
            myCursor.execute(query, (password, fName, lName, pNum, changeDepartment, canReceive, canAssemble, canTest, canShip, isAdmin, isAccountant, empID))

            # myCursor.execute(query, (empID, password, fName, lName, pNum, department, canReceive, canAssemble, canTest, canShip, isAdmin, isAccounting))
            myDb.commit()

            for i in tree.get_children():
                tree.delete(i)

            printAll = "SELECT * FROM employees"
            cursor = myDb.cursor()
            cursor.execute(printAll)
            records = cursor.fetchall()

            for row in records:
                tree.insert('', 'end', values=
                (row[0], row[1]))

    # Logout function
    def Logoff(self):
        answer = tkinter.messagebox.askquestion("Logout", "Are you sure you want to logout? ")

        if answer == "yes":
            tkinter.messagebox.showinfo("Logout", "Goodbye")
            self.root.destroy()

            master = tk.Tk()
            root.geometry("350x200")
            login1 = login.Login(master)
            master.mainloop()
            if login1.dept == "Receiving":
                master = tk.Tk()
                master.geometry("650x500")
                master.configure(bg="light gray")
                receiving1 = receiving.Receiving(master)
                master.mainloop()
            elif login1.dept == "Assembly":
                workorder = selection.WOWindow(login1.dept)
                master = tk.Tk()
                master.geometry("665x340")
                master.title("Assembly")
                app = assembly_class.Assembly(master, "0002")
                master.mainloop()
            elif login1.dept == "Testing":
                workorder = selection.WOWindow(login1.dept)
                master = tk.Tk()
                master.geometry("680x500")
                master.title("Testing")
                app = testing.TestingWindow(master, "0003")
                master.mainloop()
            elif login1.dept == "Shipping":
                workorder = selection.WOWindow(login1.dept)
                master = tk.Tk()
                master.geometry("680x400")
                app = shipping.Shipping(master, "0004")
                master.mainloop()
            elif login1.dept == "Accounting":
                master = tk.Tk()
                master.geometry("500x300")
                master.title("Accounting")
                close_window = tk.Button(master, text="Close", command=master.quit)
                close_window.place(x=90, y=230)
                app = accounting(root, "0005")

            elif login1.dept == "Admin":
                master = tk.Tk()
                master.geometry("600x500")
                master.title("New User")
                master.configure(bg="light gray")
                admin1 = admin.Admin(master)
                master.mainloop()

    def reset(self):
        self.employeeIDInput.set("")
        self.passwordInput.set("")
        self.firstNameInput.set("")
        self.lastNameInput.set("")
        self.phoneNumberInput.set("")
        self.deptInput.set("")
        self.changeDeptInput.set("")
        self.checkBox.deselect()
        # self.canReceiveInput.set("")
        # self.canAssembleInput.set("")
        # self.canTestInput.set("")
        # self.canShip.set("")
        # self.isdminInput.set("")

    def __init__(self, root): 
        self.root = root

        self.FileMenu = tk.Menu(root)
        self.root.config(menu=self.FileMenu)

        self.subMenu = tk.Menu(self.FileMenu)
        self.subMenu2 = tk.Menu(self.FileMenu)
        self.FileMenu.add_cascade(label="File", menu=self.subMenu)
        self.subMenu.add_command(label="Exit", command=self.root.destroy)
        self.subMenu.add_command(label="Logout", command=self.Logoff)

        # Prompts the user for the employee ID
        self.employeeIDInput = tk.StringVar()
        self.employeeIDLabel = tk.Label(self.root, text="Employee ID:", bg="light gray")
        self.employeeIDEntry = tk.Entry(self.root, textvariable=self.employeeIDInput, highlightbackground="light gray", width=25)
        self.employeeIDLabel.place(x=40, y=20)
        self.employeeIDEntry.place(x=150, y=20)

        # Prompts the user for the employee password
        self.passwordInput = tk.StringVar()
        self.passwordLabel = tk.Label(self.root, text="Password:", bg="light gray")
        self.passwordEntry = tk.Entry(self.root, textvariable=self.passwordInput, highlightbackground="light gray", width=25)
        self.passwordLabel.place(x=40, y=60)
        self.passwordEntry.place(x=150, y=60)

        # Prompts the user for the employee's first name
        self.firstNameInput = tk.StringVar()
        self.firstNameLabel = tk.Label(self.root, text="First Name:", bg="light gray")
        self.firstNameEntry = tk.Entry(self.root, textvariable=self.firstNameInput, highlightbackground="light gray", width=25)
        self.firstNameLabel.place(x=40, y=100)
        self.firstNameEntry.place(x=150, y=100)

        # Prompts the user for the employee's last name
        self.lastNameInput = tk.StringVar()
        self.lastNameLabel = tk.Label(self.root, text="Last Name:", bg="light gray")
        self.lastNameEntry = tk.Entry(self.root, textvariable=self.lastNameInput, highlightbackground="light gray", width=25)
        self.lastNameLabel.place(x=40, y=140)
        self.lastNameEntry.place(x=150, y=140)

        # Prompts the user for the employee's phone number
        self.phoneNumberInput = tk.StringVar()
        self.phoneNumberLabel = tk.Label(self.root, text="Phone Number:", bg="light gray")
        self.phoneNumberEntry = tk.Entry(self.root, textvariable=self.phoneNumberInput, highlightbackground="light gray", width=25)
        self.phoneNumberLabel.place(x=40, y=180)
        self.phoneNumberEntry.place(x=150, y=180)

        # Prompts the user for the employee's department
        self.deptInput = tk.StringVar()
        self.deptLabel = tk.Label(self.root, text="Department:", bg="light gray")
        # self.deptEntry = tk.Entry(self.root, textvariable=self.deptInput, highlightbackground="light gray", width=25)
        self.deptDropDown = ttk.Combobox(self.root, state="readonly", textvariable=self.deptInput, width=25)
        self.deptDropDown["values"] = ("Receiving", "Assembly", "Testing", "Shipping", "Admin", "Accounting")
        self.deptLabel.place(x=40, y=220)
        # self.deptEntry.place(x=150, y=220)
        self.deptDropDown.place(x=150, y=220)


        # Prompts the user to change departments if desired ==============================================================
        self.changeDeptInput = tk.StringVar()
        self.checkBoxInput = tk.IntVar()
        self.checkBox = tk.Checkbutton(self.root, text="Change department to:", variable=self.checkBoxInput, onvalue=1, offvalue=0, bg="light gray")
        self.changeDropDown = ttk.Combobox(self.root, state="readonly", textvariable=self.changeDeptInput, width=25)
        self.changeDropDown["values"] = ("Receiving", "Assembly", "Testing", "Shipping", "Admin", "Accounting")
        self.checkBox.place(x=150, y=260)
        self.changeDropDown.place(x=150, y=300)
        # ================================================================================================================

        # # The following will be stored in the database and determine what each employee can do/has access to 
        # self.canReceiveInput = tk.StringVar()
        # self.canReceiveLabel = tk.Label(self.root, text="Can Receive:", bg="light gray")
        # self.canReceiveEntry = tk.Entry(self.root, textvariable=self.canReceiveInput, highlightbackground="light gray", width=25)
        # self.canReceiveLabel.place(x=40, y=340)
        # self.canReceiveEntry.place(x=150, y=340)

        # self.canAssembleInput = tk.StringVar()
        # self.canAssembleLabel = tk.Label(self.root, text="Can Assemble:", bg="light gray")
        # self.canAssembleEntry = tk.Entry(self.root, textvariable=self.canAssembleInput, highlightbackground="light gray", width=25)
        # self.canAssembleLabel.place(x=40, y=400)
        # self.canAssembleEntry.place(x=150, y=400)

        # self.canTestInput = tk.StringVar()
        # self.canTestLabel = tk.Label(self.root, text="Can Test:", bg="light gray")
        # self.canTestEntry = tk.Entry(self.root, textvariable=self.canTestInput, highlightbackground="light gray", width=25)
        # self.canTestLabel.place(x=40, y=440)
        # self.canTestEntry.place(x=150, y=440)

        # self.canShipInput = tk.StringVar()
        # self.canShipLabel = tk.Label(self.root, text="Can Ship:", bg="light gray")
        # self.canShipEntry = tk.Entry(self.root, textvariable=self.canShipInput, highlightbackground="light gray", width=25)
        # self.canShipLabel.place(x=40, y=480)
        # self.canShipEntry.place(x=150, y=480)

        # self.isAdminInput = tk.StringVar()
        # self.isAdminLabel = tk.Label(self.root, text="Is Admin:", bg="light gray")
        # self.isAdminEntry = tk.Entry(self.root, textvariable=self.isAdminInput, highlightbackground="light gray", width=25)
        # self.isAdminLabel.place(x=40, y=520)
        # self.isAdminEntry.place(x=150, y=520)

        # Selection Grid
        tree = Treeview(self.root, column=("column", "column1"))
        searchQuery = StringVar()
        selection = StringVar()

        load_button = Button(self.root, text="Select Employee", command=lambda: self.select(selection.get()),
                             style='C.TButton')
        selection_entry = Entry(self.root, width=15, textvariable=selection)

        selection_entry.place(x=330, y=180)
        load_button.place(x=430, y=180)

        tree.column("#0", minwidth=0, width=0, stretch=False)
        tree.heading("#1", text="Employee ID")
        tree.column("#1", minwidth=0, width=100, stretch=False)
        tree.heading("#2", text="Name")
        tree.column("#2", minwidth=0, width=100, stretch=False)


        tree.configure(height=5)
        tree.place(x=330, y=20)

        printAll = "SELECT * FROM employees"
        cursor = myDb.cursor()
        cursor.execute(printAll)
        records = cursor.fetchall()

        for row in records:
            tree.insert('', 'end', values=
            (row[0], row[1]))

        self.submit = tk.Button(self.root, text="Submit", bg='red', highlightbackground="light gray", command=lambda: self.onSubmit(tree))
        self.submit.place(x=250, y=350)

        self.reset = tk.Button(self.root, text="Reset", bg='red', highlightbackground="light gray", command=self.reset)
        self.reset.place(x=200, y=350)

    def select(self, emp_id):
        query = "SELECT * FROM employees WHERE employee_id = \'" + emp_id + "\'"
        cursor = myDb.cursor()
        cursor.execute(query)
        result = cursor.fetchone()

        self.employeeIDInput.set(result[0])
        self.passwordInput.set(result[5])
        self.firstNameInput.set(result[1])
        self.lastNameInput.set(result[2])
        self.phoneNumberInput.set(result[3])

if __name__ == "__main__": 
    root = tk.Tk()
    root.geometry("600x450")
    root.title("Receiving")
    root.configure(bg="light gray")
    admin1 = Admin(root)
    root.mainloop()




