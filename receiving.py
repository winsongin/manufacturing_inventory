from datetime import datetime, timedelta
# import time as tm
import mysql.connector
import sys
import random
import tkinter as tk

myDb = mysql.connector.connect(host = "localhost", user = "root", passwd = "winsongin", database = inventory_system)

root = tk.Tk()
root.geometry("600x500")
root.title("Receiving")
root.configure(bg="light gray")

def dateTime():
    now = datetime.now()
    return now

# ETA of manufacturing a product is roughly 2 hours after the work order is received
def estimatedTimeOfArrival(): 
    eta = (datetime.now() + timedelta(hours=2))
    return eta

# TODO: need to ensure that the number generated doesn't already exists in the database
# def workOrder(): 
#     workOrder = random.randint(1, 100)
#     print("Work Order #: ", workOrder)

# Prints the Date/Time
dateTimeInput = tk.StringVar()
dateTimeLabel = tk.Label(root, text="Date/Time:", bg="light gray")
dateTimeEntry = tk.Entry(root, textvariable=dateTimeInput, highlightbackground="light gray", width=25)
dateTimeInput.set(dateTime())
dateTimeLabel.place(x=40, y= 20)
dateTimeEntry.place(x=150, y= 20)

# Prompts the user for the Work Order
workOrderInput = tk.StringVar()
workOrderLabel = tk.Label(root, text="Work Order #:", bg="light gray")
workOrderEntry = tk.Entry(root, textvariable=workOrderInput, highlightbackground="light gray", width=25)
workOrderLabel.place(x=40, y=100)
workOrderEntry.place(x=150, y=100)

# Prompts the user for ETA
ETAInput = tk.StringVar()
ETALabel = tk.Label(root, text="ETA:", bg="light gray")
ETAEntry = tk.Entry(root, textvariable=ETAInput, highlightbackground="light gray", width=25)
ETAInput.set(estimatedTimeOfArrival())
ETALabel.place(x=40, y=200)
ETAEntry.place(x=150, y=200)

# Prompts the user for Worker ID
workerIDInput = tk.StringVar()
workerIDLabel = tk.Label(root, text="Employee ID:", bg="light gray")
workerIDEntry = tk.Entry(root, textvariable=workerIDInput, highlightbackground="light gray", width=25)
workerIDLabel.place(x=40, y=300)
workerIDEntry.place(x=150, y=300)

# myDb = mysql.connector.connect(host = "localhost", user = "root", passwd = "winsongin", database = inventory_system)
    
# # TODO: workerId should be checked in the database to ensure that it is an authorized user/employee
# def workerId(): 
#     workerIDInput.get()
#     print(workerIDInput)
#     workerId = input("Enter your workerId: ") 
#     while(len(workerId) != 5):
#         print("WorkerId is 5 digits. Please try again.")
#         workerId = input("Enter your workerId: ")

def onSubmit():
    myCursor = myDb.cursor()
    workOrder = workOrderEntry.get()
    dateTime = dateTime()
    eta = estimatedTimeOfArrival()
    querydateTime = "INSERT INTO work_in_progress (wo_number, date_recv, eta) VALUES (%s, %s, %s)"
    val = (workOrder, dateTime, eta)
    myCursor.execute(querydateTime, val)

myDb.commit()


submit = tk.Button(root, text="Submit", bg='red', highlightbackground="light gray", command=onSubmit)
submit.place(x=250, y=400)

root.mainloop()




