from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
import mysql.connector
import itertools

class Inventory:
    def __init__(self, master):
        self.master = master
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Razgriz!949",
            database="inventory_system"
        )
        self.cursor = self.mydb.cursor(buffered=True)
        self.inventoryWindow()

    def inventoryWindow(self):
        inv_label = Label(self.master, text="Inventory", font=("arial", 16, "bold"))
        inv_label.place(x=280, y=5)

        tree = Treeview(self.master, column=("clm0", "clm1", "clm2", "clm3", "clm4"))
        tree.configure(height=15)
        tree.place(x=10, y=40)

        tree.column("#0", minwidth=0, width=0, stretch=False)
        tree.heading("#1", text="Part Name", command=lambda: self.sort_column(tree, 0))
        tree.column("#1", minwidth=0, width=100, stretch=False)
        tree.heading("#2", text="Part No.", command=lambda: self.sort_column(tree, 1))
        tree.column("#2", minwidth=0, width=100, stretch=False)
        tree.heading("#3", text="Manufacturer", command=lambda: self.sort_column(tree, 2))
        tree.column("#3", minwidth=0, width=150, stretch=False)
        tree.heading("#4", text="Quantity", command=lambda: self.sort_column(tree, 3))
        tree.column("#4", minwidth=0, width=100, stretch=False)
        tree.heading("#5", text="Part Type", command=lambda: self.sort_column(tree, 4))
        tree.column("#5", minwidth=0, width=150, stretch=False)

        loadQuery = "SELECT * FROM inventory"
        self.cursor.execute(loadQuery)
        records = self.cursor.fetchall()

        for each in records:
            tree.insert('', 'end', values=(each[0], each[1], each[2], each[3], each[4]))

        search = StringVar()
        editItem = StringVar()

        searchEntry = Entry(self.master, width=20, textvariable=search)
        searchBtn = Button(self.master, text="Search", command=lambda: self.search(tree, search.get()))
        resetBtn = Button(self.master, text="Reset", command=lambda: self.reset_window(tree))
        lowBtn = Button(self.master, text="Low Stock", command=lambda: self.view_low_stock(tree))
        addBtn = Button(self.master, text="Add New", command=self.add_inventory)
        editEntry = Entry(self.master, width=15, textvariable=editItem)
        editBtn = Button(self.master, text="Edit", command=lambda: self.edit_item(editItem.get()))

        searchEntry.place(x=10, y=380)
        searchBtn.place(x=150, y=380)
        resetBtn.place(x=230, y=380)
        lowBtn.place(x=310, y=380)
        editEntry.place(x=430, y=382)
        editBtn.place(x=537, y=380)
        addBtn.place(x=537, y=410)

    def sort_column(self, tree, col):
        # Delete all of the entries in the tree first.
        tree.delete(*tree.get_children())

        # Set the search command to a corresponding column according to number.
        if (col == 0):
            querySort = "SELECT * FROM inventory ORDER BY part_name"
        elif (col == 1):
            querySort = "SELECT * FROM inventory ORDER BY part_no"
        elif (col == 2):
            querySort = "SELECT * FROM inventory ORDER BY manufacturer"
        elif (col == 3):
            querySort = "SELECT * FROM inventory ORDER BY qty"
        elif (col == 4):
            querySort = "SELECT * FROM inventory ORDER BY part_type"

        # Print all the database records onto the GUI.
        self.cursor.execute(querySort)
        records = self.cursor.fetchall()

        for each in records:
            tree.insert('', 'end', values=(each[0], each[1], each[2], each[3], each[4]))

    def search_columns(self, tree, item):
        tree.delete(*tree.get_children())

        # Display all of the data if nothing is entered in the search box.
        if (len(item) == 0):
            # Print all the database records onto the GUI.
            querySearch = "SELECT * FROM inventory"
            self.cursor.execute(querySearch)
            records = self.cursor.fetchall()

            for each in records:
                tree.insert('', 'end', values=(each[0], each[1], each[2], each[3], each[4]))

        else:
            # Print all the database records onto the GUI.
            querySearch = ("SELECT * FROM inventory WHERE part_name LIKE '%{}%'").format(item)
            self.cursor.execute(querySearch)
            records = self.cursor.fetchall()

            for each in records:
                tree.insert('', 'end', values=(each[0], each[1], each[2], each[3], each[4]))

    def reset_window(self, tree):
        # Delete all of the entries in the tree first.
        tree.delete(*tree.get_children())

        # Print all the database records onto the GUI.
        querySearch = "SELECT * FROM inventory"
        self.cursor.execute(querySearch)
        records = self.cursor.fetchall()

        for each in records:
            tree.insert('', 'end', values=(each[0], each[1], each[2], each[3], each[4]))

    def view_low_stock(self, tree):
        # Delete all of the entries in the tree first.
        tree.delete(*tree.get_children())

        # Only display the list of items if the quantity is less than 50.
        quantSearch = "SELECT * FROM inventory where qty <= 50"

        # Print all the database records onto the GUI.
        self.cursor.execute(quantSearch)
        records = self.cursor.fetchall()

        for each in records:
            tree.insert('', 'end', values=(each[0], each[1], each[2], each[3], each[4]))

    def add_inventory(self):
        top = Toplevel()
        top.title("Add Inventory")
        top.geometry("400x400")

        mainLabel = Label(top, text="Add New Part", font=("arial", 16, "bold"))
        mainLabel.place(x=130, y=5)

        partNameLbl = Label(top, text="Part Name:", font=("arial", 13, "bold"))
        partNoLbl = Label(top, text="Part Number:", font=("arial", 13, "bold"))
        manuLbl = Label(top, text="Maunfacturer:", font=("arial", 13, "bold"))
        qtyLbl = Label(top, text="Quantity:", font=("arial", 13, "bold"))
        partTypeLbl = Label(top, text="Part Type:", font=("arial", 13, "bold"))

        partName = StringVar()
        partNo = StringVar()
        manu = StringVar()
        qty = StringVar()
        partType = StringVar()

        partNameEntry = Entry(top, width=30, textvariable=partName)
        partNoEntry = Entry(top, width=30, textvariable=partNo)
        manuEntry = Entry(top, width=30, textvariable=manu)
        qtyEntry = Entry(top, width=30, textvariable=qty)
        # partTypeEntry = Entry(top, width=30, textvariable=partType)
        partlist = ["Chassis", "Engine", "Wheel"]
        partTypeEntry = OptionMenu(top, partType, *partlist)

        partNameLbl.place(x=40, y=50)
        partNameEntry.place(x=180, y=50)
        partNoLbl.place(x=40, y=100)
        partNoEntry.place(x=180, y=100)
        manuLbl.place(x=40, y=150)
        manuEntry.place(x=180, y=150)
        qtyLbl.place(x=40, y=200)
        qtyEntry.place(x=180, y=200)
        partTypeLbl.place(x=40, y=250)
        partTypeEntry.place(x=180, y=250)

        addBtn = Button(top, text="Add", command=lambda: self.add_new(partName.get(), partNo.get(), manu.get(), qty.get(), partType.get()))
        closeBtn = Button(top, text="Close", command=top.destroy)

        addBtn.place(x=120, y=310)
        closeBtn.place(x=220, y=310)

    def add_new(self, partName, partNo, manu, qty, partType):
        quant = int(qty)

        checkQuery1 = "SELECT * FROM inventory WHERE part_name = %s"
        checkQuery2 = "SELECT * FROM inventory WHERE part_no = %s"
        self.cursor.execute(checkQuery1, [partName])
        result = self.cursor.rowcount
        self.cursor.execute(checkQuery2, [partNo])
        result2 = self.cursor.rowcount

        print(partName)
        print(result)
        print(result2)

        if (result > 0 and result2 > 0):
            tkinter.messagebox.showinfo("Error", "Part Name and Number already exist")
        elif (result > 0):
            tkinter.messagebox.showinfo("Error", "Part Name Already Exists")
        elif (result2 > 0):
            tkinter.messagebox.showinfo("Error", "Part Number Already Exists")
        else:
            addQuery = "INSERT INTO inventory (part_name, part_no, manufacturer, qty, part_type) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(addQuery, [partName, partNo, manu, quant, partType])
            self.mydb.commit()
            tkinter.messagebox.showinfo("Success", "Part Added")


    def edit_item(self, item):
        query = "SELECT * FROM inventory WHERE part_name = %s"
        self.cursor.execute(query, [item])
        rowcheck = self.cursor.rowcount

        if (rowcheck > 0):
            result = self.cursor.fetchone()
            top = Toplevel()
            top.title("Edit Item")
            top.geometry("400x400")

            mainLabel = Label(top, text="Edit Part", font=("arial", 16, "bold"))
            mainLabel.place(x=130, y=5)

            partNameLbl = Label(top, text="Part Name:", font=("arial", 13, "bold"))
            partNoLbl = Label(top, text="Part Number:", font=("arial", 13, "bold"))
            manuLbl = Label(top, text="Maunfacturer:", font=("arial", 13, "bold"))
            qtyLbl = Label(top, text="Quantity:", font=("arial", 13, "bold"))
            partTypeLbl = Label(top, text="Part Type:", font=("arial", 13, "bold"))

            partName = StringVar()
            partName.set(result[0])
            partNo = StringVar()
            partNo.set(result[1])
            manu = StringVar()
            manu.set(result[2])
            qty = StringVar()
            qty.set(result[3])
            partType = StringVar()
            partType.set(result[4])

            partNameEntry = Entry(top, width=30, textvariable=partName)
            partNoEntry = Entry(top, width=30, textvariable=partNo)
            manuEntry = Entry(top, width=30, textvariable=manu)
            qtyEntry = Entry(top, width=30, textvariable=qty)
            partlist = ["Chassis", "Engine", "Wheel"]
            partTypeEntry = OptionMenu(top, partType, *partlist)

            partNameLbl.place(x=40, y=50)
            partNameEntry.place(x=180, y=50)
            partNoLbl.place(x=40, y=100)
            partNoEntry.place(x=180, y=100)
            manuLbl.place(x=40, y=150)
            manuEntry.place(x=180, y=150)
            qtyLbl.place(x=40, y=200)
            qtyEntry.place(x=180, y=200)
            partTypeLbl.place(x=40, y=250)
            partTypeEntry.place(x=180, y=250)

            editBtn = Button(top, text="Edit",
                            command=lambda: self.edit_button(top, result[0], partName.get(), partNo.get(), manu.get(), qty.get(),
                                                         partType.get()))
            closeBtn = Button(top, text="Close", command=top.destroy)

            editBtn.place(x=120, y=310)
            closeBtn.place(x=220, y=310)
        else:
            tkinter.messagebox.showerror("Error", "No matching part name")

    def edit_button(self, top, oldpart, partName, partNo, manu, qty, partType):
        quant = int(qty)
        updateQuery = "UPDATE inventory SET part_name=%s, part_no=%s, manufacturer=%s, qty=%s, part_type=%s WHERE part_name = %s"
        updateQuery2 = "UPDATE inventory SET part_name=%s, part_no=%s, manufacturer=%s, qty=%d, part_type=%s WHERE part_name = %s"
        print(updateQuery2 % (partName, partNo, manu, quant, partType, oldpart))
        self.cursor.execute(updateQuery, [partName, partNo, manu, quant, partType, oldpart])
        self.mydb.commit()

        tkinter.messagebox.showinfo("Success", "Successfully Edited part")


if __name__ == "__main__":
    root = Tk()
    root.geometry("625x500")
    root.title("Inventory")
    app = Inventory(root)
    root.mainloop()