from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
import mysql.connector

def AssyWindow():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Razgriz!949",
        database="inventory_system"
    )

    cursor = mydb.cursor()

    # This section will serve as a temp login
    # workerID = str(input("Enter worker ID: "))
    # woNumber = str(input("Enter work order number: "))
    workerID = "0001"
    minusQty = ""
    partNum = ""

    login_query = "SELECT * FROM employees WHERE employee_id = \"" + workerID + "\";"


    # print(query)

    cursor.execute(login_query)
    query_list = cursor.fetchall()
    records = []

    for each in query_list[0]:
        records.append(each)

    print("User: ", records[0])

    mainWindow = Tk()
    mainWindow.geometry("600x500")

    mainWindow.title("Assembly")

    def onClick(partNum, minusQty):
        answer = tkinter.messagebox.askquestion("Confirmation", "Assembly completed? ")
        update_query = "UPDATE INVENTORY SET qty = qty - " + str(minusQty) + " WHERE part_no = \"" + partNum + "\";"
        if answer == "yes":
            cursor.execute(update_query)
            tkinter.messagebox.showinfo("Confirmation", "Changes made")

    def orderNumber():
        number = Label(mainWindow, text=123456789, font=("arial", 12, "bold"))
        number.place(x=175, y=10)

    def workerID():
        id = Label(mainWindow, text=123456, font=("arial", 12, "bold"))
        id.place(x=95, y=35)

    def reset():
        partNum1.set("")
        partNum2.set("")
        partNum3.set("")
        partNum1Qty.set("")
        partNum2Qty.set("")
        partNum3Qty.set("")
        return

    partNum1 = StringVar()
    partNum2 = StringVar()
    partNum3 = StringVar()
    partNum1Qty = StringVar()
    partNum2Qty = StringVar()
    partNum3Qty = StringVar()
    style = Style()
    orderNumber_label = Label(mainWindow, text="Work Order Number: ", command=orderNumber(), font=("arial", 12, "bold"))
    workerID_label = Label(mainWindow, text="Worker ID: ", command=workerID(), font=("arial", 12, "bold"))

    qty_label = Label(mainWindow, text="Qty", font=("arial", 13, "bold"))
    partNum1_label = Label(mainWindow, text="Chassis: ", font=("arial", 13, "bold"))
    partNum2_label = Label(mainWindow, text="Wheels: ", font=("arial", 13, "bold"))
    partNum3_label = Label(mainWindow, text="Antenna:  ", font=("arial", 13, "bold"))

    style.configure('C.TButton', padding=3, font=("arial", 13, "bold"), background='blue',
                    foreground='blue')
    enter_button = Button(mainWindow, text="Enter", command=lambda: onClick(partNum1_entry.get(), partNum1_qty.get()), style='C.TButton')
    reset_button = Button(mainWindow, text="Reset", command=reset, style='C.TButton')

    partNum1_entry = Entry(mainWindow, textvariable=partNum1)
    partNum2_entry = Entry(mainWindow, textvariable=partNum2)
    partNum3_entry = Entry(mainWindow, textvariable=partNum3)
    partNum1_qty = Entry(mainWindow, width=5, textvariable=partNum1Qty)
    partNum2_qty = Entry(mainWindow, width=5, textvariable=partNum2Qty)
    partNum3_qty = Entry(mainWindow, width=5, textvariable=partNum3Qty)

    orderNumber_label.place(x=10, y=10)
    workerID_label.place(x=10, y=35)

    qty_label.place(x=360, y=130)
    partNum1_label.place(x=110, y=160)
    partNum2_label.place(x=110, y=190)
    partNum3_label.place(x=110, y=220)

    enter_button.place(x=300, y=315, width=80)
    reset_button.place(x=210, y=315, width=80)

    partNum1_entry.place(x=215, y=160)
    partNum2_entry.place(x=215, y=190)
    partNum3_entry.place(x=215, y=220)
    partNum1_qty.place(x=360, y=160)
    partNum2_qty.place(x=360, y=190)
    partNum3_qty.place(x=360, y=220)

    mainWindow.mainloop()

    cursor.execute("SELECT * FROM inventory WHERE part_no = \"01-444\";")
    print(cursor.fetchall())
    mydb.commit()
    cursor.close()
    mydb.close()




AssyWindow()