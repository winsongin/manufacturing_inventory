from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
import mysql.connector
import itertools

class Assembly:
    def __init__(self, master, emp_id):
        self.master = master
        self.wo = ""
        self.wonum = "Work Order: " + self.wo
        self.emp_id = "Worker ID: " + emp_id
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Razgriz!949",
            database="inventory_system"
        )
        self.cursor = self.mydb.cursor(buffered=True)
        self.assyWindow()


    def assyWindow(self):
        chassis_query = "SELECT part_no FROM inventory WHERE part_type = \"Chassis\";"
        engine_query = "SELECT part_no FROM inventory WHERE part_type = \"Engine\";"
        wheel_query = "SELECT part_no FROM inventory WHERE part_type = \"Wheel\";"

        self.cursor.execute(chassis_query)
        chassis_list = self.cursor.fetchall()
        chassis_list = list(itertools.chain(*chassis_list))

        self.cursor.execute(engine_query)
        engine_list = self.cursor.fetchall()
        engine_list = list(itertools.chain(*engine_list))

        self.cursor.execute(wheel_query)
        wheel_list = self.cursor.fetchall()
        wheel_list = list(itertools.chain(*wheel_list))

        chassis = StringVar()
        chassis.set(chassis_list[0])

        engine = StringVar()
        engine.set(engine_list[0])

        wheel = StringVar()
        wheel.set(wheel_list[0])

        # Instantiating text variables
        self.partNum1 = StringVar()
        self.partNum2 = StringVar()
        self.partNum3 = StringVar()
        self.partNum1Qty = StringVar()
        self.partNum2Qty = StringVar()
        self.partNum3Qty = StringVar()
        self.partNum1Stock = StringVar()
        self.partNum2Stock = StringVar()
        self.partNum3Stock = StringVar()

        # Instantiates style for ttk buttons
        style = Style()

        #orderNumber_label = Label(self.master, text="Work Order Number: ", font=("arial", 12, "bold"))
        #workerID_label = Label(self.master, text="Worker ID: ", font=("arial", 12, "bold"))


        qty_label = Label(self.master, text="Qty", font=("arial", 13, "bold"))
        stock_label = Label(self.master, text="Stock", font=("arial", 13, "bold"))
        partNum1_label = Label(self.master, text="Chassis: ", font=("arial", 13, "bold"))
        partNum2_label = Label(self.master, text="Engine: ", font=("arial", 13, "bold"))
        partNum3_label = Label(self.master, text="Wheel:  ", font=("arial", 13, "bold"))
        self.part1Stock_label = Label(self.master, text="", font=("arial", 13, "bold"))
        self.part2Stock_label = Label(self.master, text="", font=("arial", 13, "bold"))
        self.part3Stock_label = Label(self.master, text="", font=("arial", 13, "bold"))

        style.configure('C.TButton', padding=0, font=("arial", 12), background='gray',
                        foreground='Green')
        enter_button = Button(self.master, text="Enter",
                              command=lambda: self.onClick(tree, chassis.get(), partNum1_qty.get(), engine.get(),
                                                           partNum2_qty.get(),
                                                           wheel.get(), partNum3_qty.get()), style='C.TButton')
        reset_button = Button(self.master, text="Reset", command=self.reset, style='C.TButton')
        stock_button = Button(self.master, text="Stock",
                              command=lambda: self.stock(chassis.get(), engine.get(), wheel.get()), style='C.TButton')

        partNum1_entry = OptionMenu(self.master, chassis, *chassis_list)
        partNum2_entry = OptionMenu(self.master, engine, *engine_list)
        partNum3_entry = OptionMenu(self.master, wheel, *wheel_list)
        partNum1_qty = Entry(self.master, width=5, textvariable=self.partNum1Qty)
        partNum2_qty = Entry(self.master, width=5, textvariable=self.partNum2Qty)
        partNum3_qty = Entry(self.master, width=5, textvariable=self.partNum3Qty)

        id = Label(self.master, text=self.emp_id, font=("arial", 12, "bold"))
        id.place(x=5, y=5)

        qty_label.place(x=205, y=55)
        stock_label.place(x=265, y=55)

        partNum1_label.place(x=5, y=80)
        partNum2_label.place(x=5, y=105)
        partNum3_label.place(x=5, y=130)

        reset_button.place(x=480, y=35, width=80)
        enter_button.place(x=480, y=65, width=80)
        stock_button.place(x=480, y=95, width=80)

        partNum1_entry.place(x=85, y=80)
        partNum2_entry.place(x=85, y=105)
        partNum3_entry.place(x=85, y=130)
        partNum1_qty.place(x=205, y=80)
        partNum2_qty.place(x=205, y=105)
        partNum3_qty.place(x=205, y=130)

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
        tree.place(x=7, y=180)

        printAll = "SELECT * FROM work_in_progress WHERE status = \"" + "Assembly" + "\""
        cursor = self.mydb.cursor()
        cursor.execute(printAll)
        records = cursor.fetchall()

        counter = 0
        for row in records:
            tree.insert('', 'end', values=
            (row[0], row[1], row[2], row[3], row[4]))
            counter += 1

    def reset(self):
        self.partNum1.set("")
        self.partNum2.set("")
        self.partNum3.set("")
        self.partNum1Qty.set("")
        self.partNum2Qty.set("")
        self.partNum3Qty.set("")
        return

    def onClick(self, tree, chassisNum, chassisQty, engNum, engQty, whlNum, whlQty):
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
        update_status = "UPDATE work_in_progress SET status = \"Testing\" WHERE wo_number = \"" + self.wo + "\";"
        if answer == "yes":
            self.cursor.execute(chas_query)
            self.cursor.execute(eng_query)
            self.cursor.execute(whl_query)
            self.cursor.execute(update_status)
            self.mydb.commit()
            tkinter.messagebox.showinfo("Confirmation", "Changes made")


        printAll = "SELECT * FROM work_in_progress WHERE status = \"" + "Assembly" + "\""
        cursor = self.mydb.cursor()
        cursor.execute(printAll)
        records = cursor.fetchall()

        counter = 0

        for i in tree.get_children():
            tree.delete(i)

        for row in records:
            tree.insert('', 'end', values=
            (row[0], row[1], row[2], row[3], row[4]))
            counter += 1

    def stock(self, chassis, engine, wheel):
        part1_query = "SELECT qty FROM inventory WHERE part_no = \"" + chassis + "\";"
        part2_query = "SELECT qty FROM inventory WHERE part_no = \"" + engine + "\";"
        part3_query = "SELECT qty FROM inventory WHERE part_no = \"" + wheel + "\";"
        self.cursor.execute(part1_query)
        part1_qty = self.cursor.fetchone()
        self.cursor.execute(part2_query)
        part2_qty = self.cursor.fetchone()
        self.cursor.execute(part3_query)
        part3_qty = self.cursor.fetchone()

        self.part1Stock_label.destroy()
        self.part2Stock_label.destroy()
        self.part3Stock_label.destroy()
        self.part1Stock_label = Label(self.master, text=part1_qty, font=("arial", 13, "bold"))
        self.part2Stock_label = Label(self.master, text=part2_qty, font=("arial", 13, "bold"))
        self.part3Stock_label = Label(self.master, text=part3_qty, font=("arial", 13, "bold"))
        self.part1Stock_label.place(x=260, y=75)
        self.part2Stock_label.place(x=260, y=100)
        self.part3Stock_label.place(x=260, y=125)

    def sort_column(self, tree, col, department, reverse):
        tree.delete(*tree.get_children())

        connection = mysql.connector.connect(host="localhost",
                                             user="root", password="Razgriz!949",
                                             auth_plugin="mysql_native_password", database="inventory_system")
        db_Info = connection.get_server_info()
        cursor = connection.cursor()
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
        connection.close()
        print("MySQL connection closed.")

    def select(self, wo):
        self.wonum = "Work Order: " + wo
        self.wo = wo
        number = Label(self.master, text=self.wonum, font=("arial", 12, "bold"))
        number.place(x=0, y=25)



if __name__ == "__main__":
    root = Tk()
    root.geometry("665x340")
    root.title("Assembly")
    app = Assembly(root, "0001")
    root.mainloop()