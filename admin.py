
import mysql.connector
import sys
import tkinter as tk

myDb = mysql.connector.connect(host = "localhost", user = "root", passwd = "Razgriz!949", database = "inventory_system")


class Admin:
    # Order gets submitted to the database
    def onSubmit(self):
        myCursor = myDb.cursor()   

        empID = self.employeeIDInput.get()
        password = self.passwordInput.get()
        fName = self.firstNameInput.get()
        lName = self.lastNameInput.get()
        pNum = self.phoneNumberInput.get()
        department = self.deptInput.get()
        canReceive = self.canReceiveInput.get()
        canAssemble = self.canAssembleInput.get()
        canTest = self.canTestInput.get()
        canShip = self.canShipInput.get()
        isAdmin = self.isAdminInput.get()

        query = "INSERT INTO employees (employee_id, pass, first_name, last_name, phone_number, dept, can_receive, can_assemble, can_test, can_ship, is_admin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        myCursor.execute(query, (empID, password, fName, lName, pNum, department, canReceive, canAssemble, canTest, canShip, isAdmin))
        myDb.commit()

    def reset(self):
        self.employeeIDInput.set("")
        self.passwordInput.set("")
        self.firstNameInput.set("")
        self.lastNameInput.set("")
        self.phoneNumberInput.set("")
        self.deptInput.set("")
        self.canReceiveInput.set("")
        self.canAssembleInput.set("")
        self.canTestInput.set("")
        self.canShip.set("")
        self.isdminInput.set("")

    def __init__(self, root): 
        self.root = root

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
        self.deptEntry = tk.Entry(self.root, textvariable=self.deptInput, highlightbackground="light gray", width=25)
        self.deptLabel.place(x=40, y=220)
        self.deptEntry.place(x=150, y=220)

        # The following will be stored in the database and determine what each employee can do/has access to 
        self.canReceiveInput = tk.StringVar()
        self.canReceiveLabel = tk.Label(self.root, text="Can Receive:", bg="light gray")
        self.canReceiveEntry = tk.Entry(self.root, textvariable=self.canReceiveInput, highlightbackground="light gray", width=25)
        self.canReceiveLabel.place(x=40, y=260)
        self.canReceiveEntry.place(x=150, y=260)

        self.canAssembleInput = tk.StringVar()
        self.canAssembleLabel = tk.Label(self.root, text="Can Assemble:", bg="light gray")
        self.canAssembleEntry = tk.Entry(self.root, textvariable=self.canAssembleInput, highlightbackground="light gray", width=25)
        self.canAssembleLabel.place(x=40, y=300)
        self.canAssembleEntry.place(x=150, y=300)

        self.canTestInput = tk.StringVar()
        self.canTestLabel = tk.Label(self.root, text="Can Test:", bg="light gray")
        self.canTestEntry = tk.Entry(self.root, textvariable=self.canTestInput, highlightbackground="light gray", width=25)
        self.canTestLabel.place(x=40, y=340)
        self.canTestEntry.place(x=150, y=340)

        self.canShipInput = tk.StringVar()
        self.canShipLabel = tk.Label(self.root, text="Can Ship:", bg="light gray")
        self.canShipEntry = tk.Entry(self.root, textvariable=self.canShipInput, highlightbackground="light gray", width=25)
        self.canShipLabel.place(x=40, y=380)
        self.canShipEntry.place(x=150, y=380)

        self.isAdminInput = tk.StringVar()
        self.isAdminLabel = tk.Label(self.root, text="Is Admin:", bg="light gray")
        self.isAdminEntry = tk.Entry(self.root, textvariable=self.isAdminInput, highlightbackground="light gray", width=25)
        self.isAdminLabel.place(x=40, y=420)
        self.isAdminEntry.place(x=150, y=420)

        self.submit = tk.Button(self.root, text="Submit", bg='red', highlightbackground="light gray", command=self.onSubmit)
        self.submit.place(x=250, y=460)

        self.reset = tk.Button(self.root, text="Reset", bg='red', highlightbackground="light gray", command=self.reset)
        self.reset.place(x=200, y=460)

if __name__ == "__main__": 
    root = tk.Tk()
    root.geometry("600x500")
    root.title("Receiving")
    root.configure(bg="light gray")
    admin1 = Admin(root)
    root.mainloop()




