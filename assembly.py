from tkinter import * #importing the tkinter class.
import tkinter.messagebox #Able to create pop-up Messages.
import mysql.connector#connecting Python with Mysql

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Test",
    database="inventory_system"
)

cursor = mydb.cursor()

#This section will serve as a temp login
#workerID = str(input("Enter worker ID: "))
workerID = "0001"

query = "SELECT * FROM employees WHERE employee_id = \"" + workerID + "\";"

print(query)

cursor.execute(query)
query_list = cursor.fetchall()
records = []

for each in query_list[0]:
    records.append(each)

print("User: ", records[0])