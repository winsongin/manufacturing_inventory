
import mysql.connector
import sys
import tkinter as tk

myDb = mysql.connector.connect(host = "localhost", user = "root", passwd = "winsongin", database = "inventory_system")

root = tk.Tk()
root.geometry("600x500")
root.title("Receiving")
root.configure(bg="light gray")

# Order gets submitted to the database
def onSubmit():
    myCursor = myDb.cursor()   

    empID = employeeIDInput.get()
    fName = firstNameInput.get()
    lName = lastNameInput.get()
    pNum = phoneNumberInput.get()
    department = deptInput.get()
    canReceive = canReceiveInput.get()
    canAssemble = canAssembleInput.get()
    canTest = canTestInput.get()
    canShip = canShip.get()
    isAdmin = isAdminInput.get()


    query = "INSERT INTO employees (employee_id, first_name, last_name, phone_number, dept, can_receive, can_assemble, can_test, can_ship, is_admin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    myCursor.execute(query, (empID, fName, lName, pNum, department, canReceive, canAssemble, canTest, canShip, isAdmin))
    myDb.commit()

def reset():
    employeeIDInput.set("")
    firstNameInput.set("")
    lastNameInput.set("")
    phoneNumberInput.set("")
    deptInput.set("")
    canReceiveInput.set("")
    canAssembleInput.set("")
    canTestInput.set("")
    canShip.set("")
    isdminInput.set("")

# Prompts the user for the customer's name
employeeIDInput = tk.StringVar()
employeeIDLabel = tk.Label(root, text="Employee ID:", bg="light gray")
employeeIDEntry = tk.Entry(root, textvariable=employeeIDInput, highlightbackground="light gray", width=25)
employeeIDLabel.place(x=40, y=20)
employeeIDEntry.place(x=150, y=20)

# Prompts the user for the customer's name
firstNameInput = tk.StringVar()
firstNameLabel = tk.Label(root, text="First Name:", bg="light gray")
firstNameEntry = tk.Entry(root, textvariable=firstNameInput, highlightbackground="light gray", width=25)
firstNameLabel.place(x=40, y=60)
firstNameEntry.place(x=150, y=60)
# Prompts the user for the customer's name
lastNameInput = tk.StringVar()
lastNameLabel = tk.Label(root, text="Last Name:", bg="light gray")
lastNameEntry = tk.Entry(root, textvariable=lastNameInput, highlightbackground="light gray", width=25)
lastNameLabel.place(x=40, y=100)
lastNameEntry.place(x=150, y=100)
# Prompts the user for the customer's name
phoneNumberInput = tk.StringVar()
phoneNumberLabel = tk.Label(root, text="Phone Number:", bg="light gray")
phoneNumberEntry = tk.Entry(root, textvariable=phoneNumberInput, highlightbackground="light gray", width=25)
phoneNumberLabel.place(x=40, y=140)
phoneNumberEntry.place(x=150, y=140)
# Prompts the user for the customer's name
deptInput = tk.StringVar()
deptLabel = tk.Label(root, text="Department:", bg="light gray")
deptEntry = tk.Entry(root, textvariable=deptInput, highlightbackground="light gray", width=25)
deptLabel.place(x=40, y=180)
deptEntry.place(x=150, y=180)
# Prompts the user for the customer's name
canReceiveInput = tk.StringVar()
canReceiveLabel = tk.Label(root, text="Can Receive:", bg="light gray")
canReceiveEntry = tk.Entry(root, textvariable=canReceiveInput, highlightbackground="light gray", width=25)
canReceiveLabel.place(x=40, y=220)
canReceiveEntry.place(x=150, y=220)
# Prompts the user for the customer's name
canAssembleInput = tk.StringVar()
canAssembleLabel = tk.Label(root, text="Can Assemble:", bg="light gray")
canAssembleEntry = tk.Entry(root, textvariable=canAssembleInput, highlightbackground="light gray", width=25)
canAssembleLabel.place(x=40, y=260)
canAssembleEntry.place(x=150, y=260)
# Prompts the user for the customer's name
canTestInput = tk.StringVar()
canTestLabel = tk.Label(root, text="Can Test:", bg="light gray")
canTestEntry = tk.Entry(root, textvariable=canTestInput, highlightbackground="light gray", width=25)
canTestLabel.place(x=40, y=300)
canTestEntry.place(x=150, y=300)
# Prompts the user for the customer's name
canShipInput = tk.StringVar()
canShipLabel = tk.Label(root, text="Can Ship:", bg="light gray")
canShipEntry = tk.Entry(root, textvariable=canShipInput, highlightbackground="light gray", width=25)
canShipLabel.place(x=40, y=340)
canShipEntry.place(x=150, y=340)
# Prompts the user for the customer's name
isAdminInput = tk.StringVar()
isAdminLabel = tk.Label(root, text="Is Admin:", bg="light gray")
isAdminEntry = tk.Entry(root, textvariable=isAdminInput, highlightbackground="light gray", width=25)
isAdminLabel.place(x=40, y=380)
isAdminEntry.place(x=150, y=380)

submit = tk.Button(root, text="Submit", bg='red', highlightbackground="light gray", command=onSubmit)
submit.place(x=250, y=420)

reset = tk.Button(root, text="Reset", bg='red', highlightbackground="light gray", command=reset)
reset.place(x=200, y=420)

root.mainloop()




