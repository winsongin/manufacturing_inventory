from datetime import datetime, timedelta
import time as tm
import mysql.connector
import sys
import random
import tkinter as tk

myDb = mysql.connector.connect(host = "localhost", user = "root", passwd = "winsongin", database = "inventory_system")

root = tk.Tk()
root.geometry("650x500")
root.title("Receiving")
root.configure(bg="light gray")


def datentime():
    now = datetime.now()
    now = now.strftime("%m/%d/%Y, %H:%M:%S")
    return now

def workOrderNumber(): 
    myCursor = myDb.cursor()
    latestWorkOrder = "SELECT MAX(wo_number) FROM work_in_progress"
    myCursor.execute(latestWorkOrder)
    result = myCursor.fetchall()
    myDb.commit()
    list = [x[0] for x in result]
    lastWorkOrder = str(list[0])
    if(lastWorkOrder == 'None'):
        nextWorkOrder = "1"
        print(nextWorkOrder)
        return nextWorkOrder
    nextWorkOrder = int(lastWorkOrder) + 1 
    return nextWorkOrder

# ETA of manufacturing a product is roughly 2 hours after the work order is received
def estimatedTimeOfArrival(): 
    eta = (datetime.now() + timedelta(hours=2))
    eta = eta.strftime("%m/%d/%Y, %H:%M:%S")
    return eta

def owe():
    myCursor = myDb.cursor()
    custWorkOrders = "SELECT (price) FROM work_in_progress WHERE cust_id = {}"
    myCursor.execute(custWorkOrders.format(customerIDEntry.get()))
    result = myCursor.fetchall()
    myDb.commit()

    owed = 0 
    for i in result:
        owed = owed + i[0]
    print(owed)
    return owed

def reset(): 
    dateTimeInput.set(datentime())
    workOrderInput.set(workOrderNumber())
    ETAInput.set(estimatedTimeOfArrival())
    priceInput.set("")
    customerNameInput.set("")
    customerIDInput.set("")
    addressInput.set("")
    return


# Order gets submitted to the database
def onSubmit():
    myCursor = myDb.cursor() 

    orderNumber = workOrderNumber()
    stat = "Assembly" 
    dateTime = datentime()
    estTimeArrv = estimatedTimeOfArrival()
    orderPrice = priceEntry.get()
    orderQuantity = quantityEntry.get()
    custName = customerNameEntry.get()
    custID = customerIDEntry.get()
    trackingNum = trackingNumberEntry.get()
    orderStat = orderStatusEntry.get()
    custAddr = addressEntry.get()
    custOwe = owe()

    query = "INSERT INTO work_in_progress (wo_number, status, date_recv, eta, price, cust_id, address) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    myCursor.execute(query, (orderNumber, stat, dateTime, estTimeArrv, orderPrice, custID, custAddr))
    myDb.commit()

    query2 = "INSERT INTO customer (cust_id, name, address, owe, quantity, tracking_number, order_status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    myCursor.execute(query2, (custID, custName, custAddr, custOwe, orderQuantity, trackingNum, orderStat))
    myDb.commit()

# Prints the Date/Time
dateTimeInput = tk.StringVar()
dateTimeLabel = tk.Label(root, text="Date/Time:", bg="light gray")
dateTimeEntry = tk.Entry(root, textvariable=dateTimeInput, highlightbackground="light gray", width=25)
dateTimeInput.set(datentime())
dateTimeLabel.place(x=40, y= 20)
dateTimeEntry.place(x=150, y= 20)

# Auto-increments the last Work Order Number and displays it to the user
workOrderInput = tk.StringVar()
workOrderLabel = tk.Label(root, text="Work Order #:", bg="light gray")
workOrderEntry = tk.Entry(root, textvariable=workOrderInput, highlightbackground="light gray", width=25)
workOrderInput.set(workOrderNumber())
workOrderLabel.place(x=40, y=60)
workOrderEntry.place(x=150, y=60)

# ETA is computed and displayed to the user
ETAInput = tk.StringVar()
ETALabel = tk.Label(root, text="ETA:", bg="light gray")
ETAEntry = tk.Entry(root, textvariable=ETAInput, highlightbackground="light gray", width=25)
ETAInput.set(estimatedTimeOfArrival())
ETALabel.place(x=40, y=100)
ETAEntry.place(x=150, y=100)

# Prompts the user for the price of the product
priceInput = tk.StringVar()
priceLabel = tk.Label(root, text="Price:", bg="light gray")
priceEntry = tk.Entry(root, textvariable=priceInput, highlightbackground="light gray", width=25)
priceLabel.place(x=40, y=140)
priceEntry.place(x=150, y=140)

# Prompts the user for the quantity
quantityInput = tk.StringVar()
quantityLabel = tk.Label(root, text="Address:", bg="light gray")
quantityEntry = tk.Entry(root, textvariable=quantityInput, highlightbackground="light gray", width=25)
quantityLabel.place(x=40, y=200)
quantityEntry.place(x=150, y=200)

# Prompts the user for the customer's name
customerNameInput = tk.StringVar()
customerNameLabel = tk.Label(root, text="Name:", bg="light gray")
customerNameEntry = tk.Entry(root, textvariable=customerNameInput, highlightbackground="light gray", width=25)
customerNameLabel.place(x=40, y=240)
customerNameEntry.place(x=150, y=240)

# Prompts the user for the customer's ID
customerIDInput = tk.StringVar()
customerIDLabel = tk.Label(root, text="Customer ID:", bg="light gray")
customerIDEntry = tk.Entry(root, textvariable=customerIDInput, highlightbackground="light gray", width=25)
customerIDLabel.place(x=40, y=280)
customerIDEntry.place(x=150, y=280)

# Prompts the user for the tracking number
trackingNumberInput = tk.StringVar()
trackingNumberLabel = tk.Label(root, text="Address:", bg="light gray")
trackingNumberEntry = tk.Entry(root, textvariable=trackingNumberInput, highlightbackground="light gray", width=25)
trackingNumberLabel.place(x=40, y=320)
trackingNumberEntry.place(x=150, y=320)

# Prompts the user for the order status
orderStatusInput = tk.StringVar()
orderStatusLabel = tk.Label(root, text="Address:", bg="light gray")
orderStatusEntry = tk.Entry(root, textvariable=orderStatusInput, highlightbackground="light gray", width=25)
orderStatusLabel.place(x=40, y=360)
orderStatusEntry.place(x=150, y=360)

# Prompts the user for the customer's address
addressInput = tk.StringVar()
addressLabel = tk.Label(root, text="Address:", bg="light gray")
addressEntry = tk.Entry(root, textvariable=addressInput, highlightbackground="light gray", width=25)
addressLabel.place(x=40, y=400)
addressEntry.place(x=150, y=400)

submit = tk.Button(root, text="Submit", bg='red', highlightbackground="light gray", command=onSubmit)
submit.place(x=250, y=450)

reset = tk.Button(root, text="Reset", bg='red', highlightbackground="light gray", command=reset)
reset.place(x=200, y=450)

root.mainloop()




