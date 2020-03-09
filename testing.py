from tkinter import * #importing the tkinter class.
import tkinter.messagebox #Able to create pop-up Messages.
import mysql.connector#connecting Python with Mysql

mydb = mysql.connector.connect(
  host= "localhost",
  user= "root",
  passwd= "Omar131997",
    database = "employees"
)

mydb2 = mysql.connector.connect(
  host= "localhost",
  user= "root",
  passwd= "Omar131997",
    database = "work_orders"
)


################################# Python/Mysql Connection above #####################################################

mainWindow = Tk() #creating a blank window. Top is = to blank window.
mainWindow.geometry("600x500")#Resizing window
mainWindow.configure(bg="light blue")
mainWindow.title("Testing") #giving window a title

#Creating a menu bar
FileMenu = Menu(mainWindow)
mainWindow.config(menu = FileMenu)

subMenu = Menu(FileMenu)
subMenu2 = Menu(FileMenu)
FileMenu.add_cascade(label = "File", menu = subMenu)
subMenu.add_command(label = "New Test")
subMenu.add_command(label = "Exit", command = mainWindow.destroy)
FileMenu.add_cascade(label = "Edit", menu = subMenu2)
subMenu2.add_command(label = "New Order")

#Function will output Testing results
def onClick():
    answer = tkinter.messagebox.askquestion("RESULT", "Are these tests correct? ")
    if answer == "yes" and 5 <= int(entry3.get()) <= 12 and 98 <= int(entry4.get()) <= 100 and \
            2 <= int(entry5.get()) <= 4 and 98 <= int(entry6.get()) <= 100:
        tkinter.messagebox.showinfo("RESULT", "ALL TEST PASS!")
    else:
        tkinter.messagebox.showinfo("RESULT", "TESTS FAILED!")

#Function will display order number
def orderNumber():
    cursor1 = mydb2.cursor()
    cursor1.execute("SELECT wo_number  FROM work_in_progress WHERE company = 'Best Buy' ")
    order = cursor1.fetchall()
    return order

#Function will display Worker ID
def workerID():
    mycursor2 = mydb.cursor()
    mycursor2.execute("SELECT employee_id  FROM employees WHERE first_name = 'Jane' " )
    myresult = mycursor2.fetchall()
    return myresult

#function will display Order Status
def getStatus():
    cursor3 = mydb2.cursor()
    cursor3.execute("SELECT status  FROM work_in_progress WHERE status = 'Testing' " )
    stat = cursor3.fetchall()
    return stat

#Function will Reset all Testing inputs
def reset():
    E3.set(' ')
    E4.set(' ')
    E5.set(' ')
    E6.set(' ')

#creating labels here:
testing_label = Label(mainWindow, text = "TESTING PROCESS", relief = "solid", width = 18, font = ("arial", 25, "bold"))

#Displaying work order number.
orderNumber_label = Label(mainWindow, text = "Work Order Number: ", bg = "yellow", font = ("arial", 15, "bold"))
work_number = StringVar()
number = Label(mainWindow, textvariable = work_number, font = ("arial", 15, "bold"))
work_number.set(orderNumber())
number.place(x = 225, y = 80)

#displaying worker ID:
workerID_label = Label(mainWindow, text = "Worker ID: ", bg = "yellow", font = ("arial", 15, "bold"))
id = StringVar()
id_label = Label(mainWindow, textvariable = id , font=("arial", 15, "bold"))
id.set(workerID())
id_label.place(x=225, y=110)

#displaying Order Status:
status_label = Label(mainWindow, text = "Order Status: ", bg = "yellow", font = ("arial", 15, "bold"))
status = StringVar()
stat_label = Label(mainWindow, textvariable = status , font=("arial", 15, "bold"))
status.set(getStatus())
stat_label.place(x=225, y=140)

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
E3 = IntVar()
entry3 = Entry(mainWindow, textvariable = E3)
E4 = IntVar()
entry4 = Entry(mainWindow, textvariable = E4)
E5 = IntVar()
entry5 = Entry(mainWindow, textvariable = E5)
E6 = IntVar()
entry6 = Entry(mainWindow, textvariable = E6)

#Placing all Labels and Buttons on to window.
testing_label.place(x = 130, y = 10)
orderNumber_label.place(x = 10, y = 80)
workerID_label.place(x = 10, y = 110)
status_label.place(x = 10, y = 140)
parameters_label.place(x = 480, y = 190)

test1_label.place(x = 50, y = 220)
test2_label.place(x = 50, y = 250)
test3_label.place(x = 50, y = 280)
test4_label.place(x = 50, y = 310)

p1.place(x = 480, y = 220)
p2.place(x = 480, y = 250)
p3.place(x = 480, y = 280)
p4.place(x = 480, y = 310)
enter_button.place(x = 400, y = 340 )
reset_button.place(x = 320, y = 340 )

entry3.place(x = 310, y = 220)
entry4.place(x = 310, y = 250)
entry5.place(x = 310, y = 280)
entry6.place(x = 310, y = 310)

mainWindow.mainloop()
