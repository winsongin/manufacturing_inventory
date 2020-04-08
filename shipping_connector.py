# import pymysql
# import mysql
from tkinter import *
import tkinter.messagebox
import mysql.connector


def get_data(wo):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Razgriz!949",
        database="inventory_system"
    )

    cursor = db.cursor()
    form_name = "customer"
    select_word = "wo,worker_id,customer,address,qty,tracking,price,order_status"
    sql = "SELECT cust_id FROM work_in_progress WHERE wo_number = {wo}".format(select_word=select_word, form_name=form_name, wo=wo)
    print(sql)
    cursor.execute(sql)
    result = cursor.fetchone()
    result = result[0]
    select_word = "cust_id,name,address,owe"
    new_query = "SELECT {select_word} FROM customer WHERE cust_id = {wo}".format(select_word=select_word, form_name=form_name, wo=result)
    cursor.execute(new_query)
    result = cursor.fetchone()
    print(result)

    if result is not None:
        result = {
            "cust_id": str(result[0]),
            "name": str(result[1]),
            "address": str(result[2]),
            "owe": str(result[3])
        }
    db.close()
    return result


def get_update_sql(data):
    form_name = "work_in_progress"
    line = "status = \"Shipped\""
    wo = data['wo']
    sql = """update {form_name} set {line} where wo_number = {wo}""".format(form_name=form_name, line=line, wo=wo)
    return sql


def execute_update_sql(update_data):
    data = {
        "host": "39.106.219.251",
        "user": "root",
        "password": "admin",
        "db": "goods",
        "charset": "utf8"
    }

    # db = pymysql.connect(**data)
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Razgriz!949",
        database="inventory_system"
    )

    cursor = db.cursor()
    sql = get_update_sql(update_data)
    cursor.execute(sql)
    db.commit()
    db.close()


class Interface:
    def __init__(self, interface, wo, emp_id):
        self.interface = interface
        self.wo = wo
        self.emp_id = emp_id
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Razgriz!949",
            database="inventory_system"
        )
        self.cursor = self.mydb.cursor(buffered=True)
        self._init()


    def _init(self):
        self.worker_id = StringVar('')
        self.customer = StringVar('')
        self.address = StringVar('')
        self.qty = StringVar('')
        self.tracking = StringVar('')
        self.price = StringVar('')

        query = "SELECT cust_id FROM work_in_progress WHERE wo_number = {wo}".format(wo=self.wo)
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        result = result[0]
        query2 = "SELECT * FROM customer WHERE cust_id = {cust_id}".format(cust_id=result)
        self.cursor.execute(query2)
        selection = self.cursor.fetchone()

        #Label(self.interface, text='W/O #:').grid(row=0, column=0)
        #Label(self.interface, text='Worker ID:').grid(row=1, column=0)
        #Label(self.interface, text='Customer:').grid(row=2, column=0)
        #Label(self.interface, text='Address:').grid(row=3, column=0)
        #Label(self.interface, text='QTY').grid(row=4, column=0)
        Label(self.interface, text='Tracking Number:').grid(sticky='w',row=5, column=0, padx=10, pady=5)
        #Label(self.interface, text='Price:').grid(sticky='w',row=6, column=0, padx=10, pady=5)

        #self.e1 = Entry(self.interface)
        work_order = "W/O #: " + self.wo
        worker = "Worker ID: " + self.emp_id
        cust_name = "Customer: " + selection[1]
        cust_addr = "Address: " + selection[2]
        cust_owe = "Price: " + selection[3]
        Label(self.interface, text=work_order).grid(sticky='w', row=0, column=0, padx=10, pady=5)
        Label(self.interface, text=worker).grid(sticky='w', row=1, column=0, padx=10, pady=5)
        Label(self.interface, text=cust_name).grid(sticky='w', row=2, column=0, padx=10, pady=5)
        Label(self.interface, text=cust_addr).grid(sticky='w', row=3, column=0, padx=10, pady=5)
        #Label(self.interface, textvariable=self.qty).grid(row=4, column=1, padx=10, pady=5)
        self.tracking = Entry(self.interface)
        self.tracking.place(x=120, y=130)
        Label(self.interface, text=cust_owe).grid(sticky='w', row=6, column=0, padx=10, pady=5)

        #self.e1.grid(row=0, column=1, padx=10, pady=5)

        Button(self.interface, text='Print', width=10, command=self.show).grid(row=9, column=0, sticky=W, padx=10, pady=5)
        Button(self.interface, text='Submit', width=10, command=self.submit).grid(row=8, column=0, sticky=W, padx=10, pady=5)
        Button(self.interface, text='Ship', width=10, command=self.ship).place(x=120, y=190)

    def show(self):
        """
        1.获得当前wo的值 get the wo data
        2.清空所有输入框 clean the input
        3.查询数据库数据 search database data
        4.将数据进行显示 print the data
        """

        status = self.is_exist()
        if status:
            wo = self.wo
            print(wo)
            data = get_data(wo)
            self.clear()
            self.set_value(data)
        else:
            # 未查询到数据  not find the data
            tkinter.messagebox.showinfo(title='shipping message', message="no found data")
            self.clear()

    def submit(self):
        status = self.is_exist()
        if status:
            data = self.get_all_input()
            execute_update_sql(data)
        else:
            # 未查询到数据  not find the data
            tkinter.messagebox.showinfo(title='shipping message', message="no found data")

    def ship(self):
        status = self.is_exist()

        if status:
            data = {
                "wo": self.wo,
                "order_status": "shipped",
            }
            execute_update_sql(data)
            tkinter.messagebox.showinfo(title='shipping message', message=" The order is shipping out")
        else:
            tkinter.messagebox.showinfo(title='shipping message', message="no found data")

    def is_exist(self):
        """
        检查这条数据是否存在 check if the data in the database
        """
        wo = self.wo
        print(wo)
        data = get_data(wo)
        if data is None:
            return False
        else:
            return True

    def clear(self):
        """
        清空所有Entry  clean all the entry
        """
        #self.e1.delete(0, END)
        self.worker_id.set("")
        self.customer.set("")
        self.address.set("")
        self.qty.set("")
        self.tracking.delete(0, END)
        self.price.set("")

    def set_value(self, data):
        """
        把查询到的放到input中  input the data
        """
        #self.e1.insert(0, data["wo"])
        #self.worker_id.set(data["worker_id"])
        self.customer.set(data["name"])
        self.address.set(data["address"])
        #self.qty.set(data["qty"])
        self.tracking.insert(0, self.tracking.get())
        self.price.set(data["owe"])

    def get_all_input(self):
        """
        获得所有已经录入的信息 get all the saved data
        """
        data = {
            "wo": self.wo,
            "tracking": self.tracking.get(),
        }
        return data


if __name__ == "__main__":
    interface = Tk()
    interface.configure()
    interface.title("Inventory")
    interface.geometry("600x440")
    Interface(interface, "1", "0004")
    interface.mainloop()
