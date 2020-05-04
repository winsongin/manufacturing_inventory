from tkinter import * #importing the tkinter class.
import tkinter.messagebox #Able to create pop-up Messages.
import mysql.connector

import assembly_class
import login
import testing
import shipping_connector
import receiving
import accounting
import admin
import selection

#class Decleration
class TestingWindow:
    def __init__(self, master, wo, emp_id):
        self.master = master
        self.wo = wo
        self.emp_id = emp_id
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Omar131997",
            database="inventory_system"
        )

        self.FileMenu = Menu(master)
        self.master.config(menu= self.FileMenu)

        self.subMenu = Menu(self.FileMenu)
        self.subMenu2 = Menu(self.FileMenu)
        self.FileMenu.add_cascade(label="File", menu=self.subMenu)
        self.subMenu.add_command(label="Exit", command=self.master.destroy)
        self.subMenu.add_command(label = "Logout", command=self.Logoff)
        self.FileMenu.add_cascade(label="Edit", menu=self.subMenu2)

        # creating labels here:
        self.testing_label = Label(master, text="TESTING PROCESS", relief="solid", width=18, font=("arial", 25, "bold"))

        # Displaying work order number.
        self.orderNumber_label = Label(master, text="Work Order Number: ", bg="yellow", font=("arial", 15, "bold"))
        self.work_number = StringVar()
        self.number = Label(master, text=self.wo, font=("arial", 15, "bold"))
        self.number.place(x=225, y=80)

        # displaying worker ID:
        self.workerID_label = Label(master, text="Worker ID: ", bg="yellow", font=("arial", 15, "bold"))
        self.id = StringVar()
        self.id_label = Label(master, text=self.emp_id, font=("arial", 15, "bold"))
        self.id_label.place(x=225, y=110)

        # displaying Order Status:
        self.status_label = Label(master, text="Order Status: ", bg="yellow", font=("arial", 15, "bold"))
        self.stat = StringVar()
        self.orderStatusEntry = Label(self.master, text="Testing", font=("arial", 15, "bold"))

        self.test1_label = Label(master, text="Test 1: Speed ", bg="red", font=("arial", 13, "bold"))
        self.test2_label = Label(master, text="Test 2: Durability ", bg="red", font=("arial", 13, "bold"))
        self.test3_label = Label(master, text="Test 3: Battery Efficiency  ", bg="red", font=("arial", 13, "bold"))
        self.test4_label = Label(master, text="Test 4: Remote Signal Range ", bg="red", font=("arial", 13, "bold"))
        self.parameters_label = Label(master, text="Parameters", relief="solid", width=10, font=("arial", 12, "bold"))

        self.p1 = Label(master, text="[5-12 MPH]", font=("arial", 12, "bold"))
        self.p2 = Label(master, text="[98% or >]", font=("arial", 12, "bold"))
        self.p3 = Label(master, text="[2-4 Hours]", font=("arial", 12, "bold"))
        self.p4 = Label(master, text="[98% or >]", font=("arial", 12, "bold"))

        # Creating buttons here:
        self.enter_button = Button(master, text="Enter", bg="blue", fg="white", command=lambda: self.onClick(),
                                   font=("arial", 13, "bold"))  # Command is binding to fuction.
        self.reset_button = Button(master, text="Reset", command=self.reset, bg="blue", fg="white",
                                   font=("arial", 13, "bold"))

        # User input
        self.E3 = IntVar()
        self.entry3 = Entry(master, textvariable=self.E3)
        self.E4 = IntVar()
        self.entry4 = Entry(master, textvariable=self.E4)
        self.E5 = IntVar()
        self.entry5 = Entry(master, textvariable=self.E5)
        self.E6 = IntVar()
        self.entry6 = Entry(master, textvariable=self.E6)

        # Placing all Labels and Buttons on to window.
        self.testing_label.place(x=130, y=10)
        self.orderNumber_label.place(x=10, y=80)
        self.workerID_label.place(x=10, y=110)
        self.status_label.place(x=10, y=140)
        self.orderStatusEntry.place(x=225, y=140)
        self.parameters_label.place(x=480, y=190)

        # placing items here on master
        self.test1_label.place(x=50, y=220)
        self.test2_label.place(x=50, y=250)
        self.test3_label.place(x=50, y=280)
        self.test4_label.place(x=50, y=310)

        self.p1.place(x=480, y=220)
        self.p2.place(x=480, y=250)
        self.p3.place(x=480, y=280)
        self.p4.place(x=480, y=310)
        self.enter_button.place(x=400, y=340)
        self.reset_button.place(x=320, y=340)

        self.entry3.place(x=310, y=220)
        self.entry4.place(x=310, y=250)
        self.entry5.place(x=310, y=280)
        self.entry6.place(x=310, y=310)

    # Logof function will let user logout.
    def Logoff(self):
        answer = tkinter.messagebox.askquestion("Logout", "Are you sure you want to logout? ")

        if answer == "yes":
            tkinter.messagebox.showinfo("Logout", "Goodbye")
            self.master.destroy()

            root = Tk()
            root.geometry("650x500")
            login1 = login.Login(root)
            root.mainloop()
            if login1.dept == "Receiving":
                root = Tk()
                root.geometry("650x500")
                root.configure(bg="light gray")
                receiving1 = receiving.Receiving(root)
                root.mainloop()
            elif login1.dept == "Assembly":
                workorder = selection.WOWindow(login1.dept)
                root = Tk()
                root.geometry("600x500")
                root.title("Assembly")
                app = assembly_class.assembly(root, "0002", workorder)
                root.mainloop()
            elif login1.dept == "Testing":
                workorder = selection.WOWindow(login1.dept)
                root = Tk()
                root.geometry("600x500")
                root.title("Testing")
                app = testing.TestingWindow(root, workorder, "0003")
                root.mainloop()
            elif login1.dept == "Shipping":
                workorder = selection.WOWindow(login1.dept)
                root = Tk()
                app = shipping_connector.Interface(root, workorder, "0004")
                shipping_connector(workorder, workerID)
                root.mainloop()
            elif login1.dept == "Accounting":
                root = Tk()
                root.geometry("500x300")
                root.title("Accounting")
                close_window = tk.Button(root, text="Close", command=master.quit)
                close_window.place(x=90, y=230)
                app = accounting(root, "0005")

            elif login1.dept == "Admin":
                root = Tk()
                root.geometry("600x500")
                root.title("New User")
                root.configure(bg="light gray")
                admin1 = admin.Admin(root)
                root.mainloop()


    def onClick(self):
        answer = tkinter.messagebox.askquestion("RESULT", "Are these tests correct? ")
        cursor = self.mydb.cursor()
        if answer == "yes" and 5 <= int(self.entry3.get()) <= 12 and 98 <= int(self.entry4.get()) <= 100 and \
                2 <= int(self.entry5.get()) <= 4 and 98 <= int(self.entry6.get()) <= 100:
            tkinter.messagebox.showinfo("RESULT", "ALL TEST PASS!")
            cursor = self.mydb.cursor()
            cursor.execute("UPDATE work_in_progress SET status = 'Shipping' ")
            self.mydb.commit()

        else:
            tkinter.messagebox.showinfo("RESULT", "TESTS FAILED!")
            cursor.execute("UPDATE work_in_progress SET status = 'Assembly' ")
            self.mydb.commit()
            
    #gets status of order
    def getStatus(self):
        cursor3 = self.mydb.cursor()
        statement = "SELECT status  FROM work_in_progress WHERE status = '{}' "
        cursor3.execute(statement)
        stat = cursor3.fetchall()
        return stat

    # Function will Reset all Testing inputs
    def reset(self):
        self.E3.set(' ')
        self.E4.set(' ')
        self.E5.set(' ')
        self.E6.set(' ')


if __name__ == "__main__":
    master = Tk()
    master.geometry("600x500")  # Resizing window
    master.configure(bg="light gray")
    master.title("Testing")  # giving window a title
    window = TestingWindow(master,"1", "0003")
    master.mainloop()
