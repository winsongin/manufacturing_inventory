from tkinter import *  # importing the tkinter class.
from tkinter.ttk import *
import tkinter.messagebox  # Able to create pop-up Messages.
import mysql.connector  # connecting Python with Mysql
import itertools

class assembly:
    def __init__(self, master, emp_id, wonum):
        self.master = master
        self.emp_id = emp_id
        self.wonum = wonum
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Razgriz!949",
            database="inventory_system"
        )
        self.cursor = self.mydb.cursor(buffered=True)
        self.assembly_window()

    def assembly_window(self):

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

        # Instantiates style for ttk buttons
        style = Style()

        self.orderNumber_label = Label(self.master, text="Work Order Number: ", font=("arial", 12, "bold"))
        workerID_label = Label(self.master, text="Worker ID: ", font=("arial", 12, "bold"))
        id = Label(self.master, text=self.emp_id, font=("arial", 12, "bold"))
        id.place(x=95, y=35)
        number = Label(self.master, text=self.wonum, font=("arial", 12, "bold"))
        number.place(x=175, y=10)

        qty_label = Label(self.master, text="Qty", font=("arial", 13, "bold"))
        partNum1_label = Label(self.master, text="Chassis: ", font=("arial", 13, "bold"))
        partNum2_label = Label(self.master, text="Engine: ", font=("arial", 13, "bold"))
        partNum3_label = Label(self.master, text="Wheel:  ", font=("arial", 13, "bold"))

        style.configure('C.TButton', padding=3, font=("arial", 13, "bold"), background='blue',
                        foreground='blue')
        enter_button = Button(self.master, text="Enter",
                              command=lambda: self.onClick(chassis.get(), partNum1_qty.get(), engine.get(),
                                                      partNum2_qty.get(),
                                                      wheel.get(), partNum3_qty.get()), style='C.TButton')
        reset_button = Button(self.master, text="Reset", command=self.reset, style='C.TButton')

        partNum1_entry = OptionMenu(self.master, chassis, *chassis_list)
        partNum2_entry = OptionMenu(self.master, engine, *engine_list)
        partNum3_entry = OptionMenu(self.master, wheel, *wheel_list)
        partNum1_qty = Entry(self.master, width=5, textvariable=self.partNum1Qty)
        partNum2_qty = Entry(self.master, width=5, textvariable=self.partNum2Qty)
        partNum3_qty = Entry(self.master, width=5, textvariable=self.partNum3Qty)

        self.orderNumber_label.place(x=10, y=10)
        workerID_label.place(x=10, y=35)

        qty_label.place(x=360, y=130)
        partNum1_label.place(x=110, y=160)
        partNum2_label.place(x=110, y=190)
        partNum3_label.place(x=110, y=220)

        enter_button.place(x=300, y=315, width=80)
        reset_button.place(x=210, y=315, width=80)

        partNum1_entry.place(x=215, y=160)
        partNum2_entry.place(x=215, y=190)
        partNum3_entry.place(x=215, y=220)
        partNum1_qty.place(x=360, y=160)
        partNum2_qty.place(x=360, y=190)
        partNum3_qty.place(x=360, y=220)

    def onClick(self, chassisNum, chassisQty, engNum, engQty, whlNum, whlQty):
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
        update_status = "UPDATE work_in_progress SET status = \"Testing\" WHERE wo_number = \"" + self.wonum + "\";"
        if answer == "yes":
            self.cursor.execute(chas_query)
            self.cursor.execute(eng_query)
            self.cursor.execute(whl_query)
            self.cursor.execute(update_status)
            self.mydb.commit()
            tkinter.messagebox.showinfo("Confirmation", "Changes made")

    def reset(self):
        self.partNum1.set("")
        self.partNum2.set("")
        self.partNum3.set("")
        self.partNum1Qty.set("")
        self.partNum2Qty.set("")
        self.partNum3Qty.set("")
        return

root = Tk()
root.geometry("600x500")
root.title("Assembly")
app = assembly(root, "0002", "2")
root.mainloop()
