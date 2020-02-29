from datetime import datetime, timedelta
import mysql.connector
import sys
import random
import tkinter as tk

root = tk.Tk()
root.geometry("600x500")
root.title("Receiving")
root.configure(bg="light gray")

# Prompts the user for the Date/Time
dateTimeInput = tk.StringVar()
dateTimeLabel = tk.Label(root, text="Date/Time", bg="light gray")
dateTimeEntry = tk.Entry(root, textvariable=dateTimeInput, highlightbackground="light gray")
dateTimeLabel.place(x=40, y= 20)
dateTimeEntry.place(x=150, y= 20)

# Prompts the user for the Work Order
workOrderInput = tk.StringVar()
workOrderLabel = tk.Label(root, text="Work Order #", bg="light gray")
workOrderEntry = tk.Entry(root, textvariable=workOrderInput, highlightbackground="light gray")
workOrderLabel.place(x=40, y=100)
workOrderEntry.place(x=150, y=100)

# Prompts the user for ETA
ETAInput = tk.StringVar()
ETALabel = tk.Label(root, text="ETA", bg="light gray")
ETAEntry = tk.Entry(root, textvariable=ETAInput, highlightbackground="light gray")
ETALabel.place(x=40, y=200)
ETAEntry.place(x=150, y=200)

# Prompts the user for Worker ID
workerIDInput = tk.StringVar()
workerIDLabel = tk.Label(root, text="Worker ID", bg="light gray")
workerIDEntry = tk.Entry(root, textvariable=workerIDInput, highlightbackground="light gray")
workerIDLabel.place(x=40, y=300)
workerIDEntry.place(x=150, y=300)

# Submit Button
submit = tk.Button(root, text="Submit", bg='red', highlightbackground="light gray")
submit.place(x=250, y=400)

root.mainloop()

# myDb = mysql.connector.connect(host = "localhost", user = "root", passwd = "ForSchoolUse", database = userInput)

# Generate the current time that the Work Order is being put in order to reflect real time
def dateTime():
    now = datetime.now()
    # myCursor = myDb.cursor()

    # Time is printed in 24-hour format
    currentTime = now.strftime("%H:%M:%S")
    print("Current Time: ", currentTime)
    
# TODO: workerId should be checked in the database to ensure that it is an authorized user/employee
def workerId(): 
    workerId = input("Enter your workerId: ") 
    while(len(workerId) != 5):
        print("WorkerId is 5 digits. Please try again.")
        workerId = input("Enter your workerId: ")
    # print(workerId) # for testing purposes

# Produce a random workOrder number
# TODO: need to ensure that the number generated doesn't already exists in the database
def workOrder(): 
    workOrder = random.randint(1, 100)
    print("Work Order #: ", workOrder)


# ETA of manufacturing a product is roughly 2 hours after the work order is received
def estimatedTimeOfArrival(): 
    eta = (datetime.now() + timedelta(hours=2))
    print("Estimated Time of Arrival: ", eta.strftime("%H:%M:%S"))






