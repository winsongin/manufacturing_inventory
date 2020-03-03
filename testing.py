from tkinter import * #importing the tkinter class.
import tkinter.messagebox #Able to create pop-up Messages.
import mysql.connector#connecting Python with Mysql

mydb = mysql.connector.connect(
  host= "localhost",
  user= "root",
  passwd= "Omar131997",
    database = "employees"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT employee_id  FROM employees ")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#################### Python/Mysql Connection above #####################################################

mainWindow = Tk() #creating a blank window. Top is = to blank window.
mainWindow.geometry("600x500")#Resizing window

mainWindow.title("Testing") #giving window a title


def onClick():#funcion to out
    a = 5
    b = 12
    answer = tkinter.messagebox.askquestion("Results", "Are these tests correct? ")
    if answer == "yes" and a >= int(entry3.get()) >= b:
        tkinter.messagebox.showinfo("Results", "All Test Pass")
    else:
        tkinter.messagebox.showinfo("Results", "All Test Failed")

def orderNumber():
    number = Label(mainWindow, text = 123456789, font = ("arial", 15, "bold"))
    number.place(x = 225, y = 80)

def workerID():
    id = Label(mainWindow, text = 123456, font = ("arial", 15, "bold"))
    id.place(x = 225, y = 110 )

def reset():
    entry3.set(0)
    entry4.set(0)
    entry5.set(0)
    entry6.set(0)
    return

#creating labels here:
testing_label = Label(mainWindow, text = "TESTING PROCESS", relief = "solid", width = 18, font = ("arial", 25, "bold"))
orderNumber_label = Label(mainWindow, text = "Work Order Number: ", bg = "yellow", command = orderNumber(), font = ("arial", 15, "bold"))
workerID_label = Label(mainWindow, text = "Worker ID: ", bg = "yellow", command = workerID(), font = ("arial", 15, "bold"))
test1_label = Label(mainWindow, text = "Test 1: Speed ", bg = "red", font = ("arial", 13, "bold"))
test2_label = Label(mainWindow, text = "Test 2: Durability ", bg = "red", font = ("arial", 13, "bold"))
test3_label = Label(mainWindow, text = "Test 3: Battery Efficiency  ", bg = "red", font = ("arial", 13, "bold"))
test4_label = Label(mainWindow, text = "Test 4: Remote Signal Range ", bg = "red", font = ("arial", 13, "bold"))
parameters_label = Label(mainWindow, text = "Parameters", relief = "solid", width = 10, font = ("araial", 12, "bold"))
p1 = Label(mainWindow, text = "[5-12 MPH]", font = ("araial", 12, "bold"))
p2 = Label(mainWindow, text = "[98% or >]", font = ("araial", 12, "bold"))
p3 = Label(mainWindow, text = "[2-4 Hours]", font = ("araial", 12, "bold"))
p4 = Label(mainWindow, text = "[98% or >]", font = ("araial", 12, "bold"))

#Creating butoons here:
enter_button = Button(mainWindow, text = "Enter", bg = "blue", fg = "white",  command = onClick, font = ("arial", 13, "bold"))#Command is binding to fuction.
reset_button = Button(mainWindow, text = "Reset", command = reset, bg = "blue", fg = "white", font = ("arial", 13, "bold"))
#User input
entry3 = Entry(mainWindow)
# entry4 = Entry(mainWindow)
# entry5 = Entry(mainWindow)
# entry6 = Entry(mainWindow)

#Placing all Labels and Buttons on to window.
testing_label.place(x = 130, y = 10)
orderNumber_label.place(x = 10, y = 80)
workerID_label.place(x = 10, y = 110)
parameters_label.place(x = 480, y = 120)

test1_label.place(x = 50, y = 160)
test2_label.place(x = 50, y = 190)
test3_label.place(x = 50, y = 220)
test4_label.place(x = 50, y = 250)

p1.place(x = 480, y = 160)
p2.place(x = 480, y = 190)
p3.place(x = 480, y = 220)
p4.place(x = 480, y = 250)
enter_button.place(x = 400, y = 315 )
reset_button.place(x = 320, y = 315 )

entry3.place(x = 310, y = 160)
# entry4.place(x = 310, y = 190)
# entry5.place(x = 310, y = 220)
# entry6.place(x = 310, y = 250)

mainWindow.mainloop()
