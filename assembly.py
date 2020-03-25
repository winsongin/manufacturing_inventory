from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
import mysql.connector
import itertools


def AssyWindow(workOrder, workerID):
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
    worker = "0002"
    minusQty = ""
    partNum = ""

    chassis_query = "SELECT part_no FROM inventory WHERE part_type = \"Chassis\";"
    engine_query = "SELECT part_no FROM inventory WHERE part_type = \"Engine\";"
    wheel_query = "SELECT part_no FROM inventory WHERE part_type = \"Wheel\";"

    cursor.execute(chassis_query)
    chassis_list = cursor.fetchall()
    chassis_list = list(itertools.chain(*chassis_list))

    cursor.execute(engine_query)
    engine_list = cursor.fetchall()
    engine_list = list(itertools.chain(*engine_list))

    cursor.execute(wheel_query)
    wheel_list = cursor.fetchall()
    wheel_list = list(itertools.chain(*wheel_list))
    # print(query)

    mainWindow = Tk()
    mainWindow.geometry("600x500")

    mainWindow.title("Assembly")

    def onClick(chassisNum, chassisQty, engNum, engQty, whlNum, whlQty):
        print(partNum)
        if chassisNum == "" or chassisQty == "" or engNum == "" or engQty == "" or whlNum == "" or whlQty == "":
            tkinter.messagebox.showinfo("Failed", "Fields are required")
            return

        answer = tkinter.messagebox.askquestion("Confirmation", "Assembly completed? ")
        chas_query = "UPDATE INVENTORY SET qty = qty - " + str(
            chassisQty) + " WHERE part_no = \"" + chassisNum + "\";"
        eng_query = "UPDATE INVENTORY SET qty = qty - " + str(
            engQty) + " WHERE part_no = \"" + engNum + "\";"
        whl_query = "UPDATE INVENTORY SET qty = qty - " + str(
            whlQty) + " WHERE part_no = \"" + whlNum + "\";"
        if answer == "yes":
            cursor.execute(chas_query)
            cursor.execute(eng_query)
            cursor.execute(whl_query)
            mydb.commit()
            tkinter.messagebox.showinfo("Confirmation", "Changes made")

    #def orderNumber():



    def reset():
        partNum1.set("")
        partNum2.set("")
        partNum3.set("")
        partNum1Qty.set("")
        partNum2Qty.set("")
        partNum3Qty.set("")
        return

    chassis = StringVar(mainWindow)
    chassis.set(chassis_list[0])

    engine = StringVar(mainWindow)
    engine.set(engine_list[0])

    wheel = StringVar(mainWindow)
    wheel.set(wheel_list[0])

    #Instantiating text variables
    partNum1 = StringVar()
    partNum2 = StringVar()
    partNum3 = StringVar()
    partNum1Qty = StringVar()
    partNum2Qty = StringVar()
    partNum3Qty = StringVar()

    #Instantiates style for ttk buttons
    style = Style()

    orderNumber_label = Label(mainWindow, text="Work Order Number: ", font=("arial", 12, "bold"))
    workerID_label = Label(mainWindow, text="Worker ID: ", font=("arial", 12, "bold"))
    id = Label(mainWindow, text=workerID, font=("arial", 12, "bold"))
    id.place(x=95, y=35)
    number = Label(mainWindow, text=workOrder, font=("arial", 12, "bold"))
    number.place(x=175, y=10)

    qty_label = Label(mainWindow, text="Qty", font=("arial", 13, "bold"))
    partNum1_label = Label(mainWindow, text="Chassis: ", font=("arial", 13, "bold"))
    partNum2_label = Label(mainWindow, text="Engine: ", font=("arial", 13, "bold"))
    partNum3_label = Label(mainWindow, text="Wheel:  ", font=("arial", 13, "bold"))

    style.configure('C.TButton', padding=3, font=("arial", 13, "bold"), background='blue',
                    foreground='blue')
    enter_button = Button(mainWindow, text="Enter",
                          command=lambda: onClick(chassis.get(), partNum1_qty.get(), engine.get(), partNum2_qty.get(),
                                                  wheel.get(), partNum3_qty.get()), style='C.TButton')
    reset_button = Button(mainWindow, text="Reset", command=reset, style='C.TButton')

    partNum1_entry = OptionMenu(mainWindow, chassis, *chassis_list)
    partNum2_entry = OptionMenu(mainWindow, engine, *engine_list)
    partNum3_entry = OptionMenu(mainWindow, wheel, *wheel_list)
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

    #Test code to show the difference in quantities
    cursor.execute("SELECT * FROM inventory WHERE part_no = \"0X1233\";")
    txt = cursor.fetchall()
    print(txt)
    mydb.commit()
    print(txt)
    #Closes cursor and mydb
    cursor.close()
    mydb.close()
