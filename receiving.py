from datetime import datetime, timedelta
import mysql.connector
import sys
import random

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

# Calling all functions
dateTime()
workerId()
workOrder()
estimatedTimeOfArrival()






