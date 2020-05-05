#Change these as needed
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
import mysql.connector
import itertools


class Department:# Change Department to your department
    def __init__(self, master, emp_id):
        self.master = master
        self.wo = ""
        self.wonum = "Work Order: " + self.wo
        self.emp_id = "Worker ID: " + emp_id
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="XXX",
            database="inventory_system"
        )
        self.cursor = self.mydb.cursor(buffered=True)
        self.MyWindow() # Change MyWindow to your window name

    # Change MyWindow to your window name
    def MyWindow(self):

        # Worker ID Label. Do Not Move
        id = Label(self.master, text=self.emp_id, font=("arial", 12, "bold"))
        id.place(x=5, y=5)

        # Instantiates style for ttk buttons. Please use this for your buttons
        style = Style()
        style.configure('C.TButton', padding=0, font=("arial", 12), background='gray',
                        foreground='Green')


        # INSERT CODE HERE YOU CAN BASICALLY COPY AND PASTE








        # BELOW IS THE CODE FOR THE SELECTION WINDOW

        #Selection Grid
        tree = Treeview(self.master, column=("column", "column1", "column2", "column3", "column4"))
        searchQuery = StringVar()
        selection = StringVar()

        load_button = Button(self.master, text="Select Work Order", command=lambda: self.select(selection.get()), style='C.TButton')
        selection_entry = Entry(self.master, width=15, textvariable=selection)

        selection_entry.place(x=400, y=8)
        load_button.place(x=500, y=7)

        tree.column("#0", minwidth=0, width=0, stretch=False)
        tree.heading("#1", text="Work Order", command=lambda: self.sort_column(tree, 0, "Assembly", False))
        tree.column("#1", minwidth=0, width=100, stretch=False)
        tree.heading("#2", text="Department", command=lambda: self.sort_column(tree, 1, "Assembly", False))
        tree.column("#2", minwidth=0, width=100, stretch=False)
        tree.heading("#3", text="Customer", command=lambda: self.sort_column(tree, 2, "Assembly", False))
        tree.column("#3", minwidth=0, width=150, stretch=False)
        tree.heading("#4", text="Received Date", command=lambda: self.sort_column(tree, 3, "Assembly", False))
        tree.column("#4", minwidth=0, width=150, stretch=False)
        tree.heading("#5", text="Estimated Ship", command=lambda: self.sort_column(tree, 4, "Assembly", False))
        tree.column("#5", minwidth=0, width=150, stretch=False)

        tree.configure(height=5)
        tree.place(x=7, y=180) # You may need to increase y's value to fit your form

        printAll = "SELECT * FROM work_in_progress WHERE status = \"" + "Assembly" + "\"" # CHANGE "ASSEMBLY" TO YOUR DEPARTMENT
        cursor = self.mydb.cursor()
        cursor.execute(printAll)
        records = cursor.fetchall()

        counter = 0
        for row in records:
            tree.insert('', 'end', values=
            (row[0], row[1], row[2], row[3], row[4]))
            counter += 1


    # INSERT FUNCTIONS BELOW




    # BELOW IS CODE FOR THE TREE. DO NOT CHANGE

    def sort_column(self, tree, col, department, reverse):
        tree.delete(*tree.get_children())
        db_Info = self.mydb.get_server_info()
        cursor = self.mydb.cursor()
        cursor.execute("select database()")
        records = cursor.fetchone()

        if (col == 0):
            querySort = "SELECT * FROM work_in_progress WHERE status = \"" + department + "\" ORDER BY wo_number"
        elif (col == 1):
            querySort = "SELECT * FROM work_in_progress WHERE status = \"" + department + "\" ORDER BY status"
        elif (col == 2):
            querySort = "SELECT * FROM work_in_progress WHERE status = \"" + department + "\" ORDER BY date_recv"
        elif (col == 3):
            querySort = "SELECT * FROM work_in_progress WHERE status = \"" + department + "\" ORDER BY eta"
        elif (col == 4):
            querySort = "SELECT * FROM work_in_progress WHERE status = \"" + department + "\" ORDER BY cust_id"

        cursor.execute(querySort)
        records = cursor.fetchall()
        for row in records:
            print("Work Number: ", row[0])
            print("Status: ", row[1])
            print("Date Received: ", row[2])
            print("ETA: ", row[3])
            print("Customer ID: ", row[4])

        counter = 0
        for row in records:
            tree.insert('', 'end', values=
            (row[0], row[1], row[2], row[3], row[4]))
            counter += 1

        cursor.close()
        self.mydb.close()
        print("MySQL connection closed.")

    def select(self, wo):
        self.wonum = "Work Order: " + wo
        self.wo = wo
        number = Label(self.master, text=self.wonum, font=("arial", 12, "bold"))
        number.place(x=0, y=25)



if __name__ == "__main__":
    root = Tk()
    root.geometry("665x340") #You may need to change this to fit your window
    root.title("Department") # Change to your department
    app = MyWindow(root, "0001") #Change to your window name
    root.mainloop()