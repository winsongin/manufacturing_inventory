import pymysql
from tkinter import *
import tkinter.messagebox


def get_data(wo):
    data = {
        "host": "39.106.219.251",
        "user": "root",
        "password": "admin",
        "db": "goods",
        "charset": "utf8"
    }
    db = pymysql.connect(**data)
    cursor = db.cursor()
    form_name = "customer"
    select_word = "wo,worker_id,customer,address,qty,tracking,price,order_status"
    sql = "SELECT {select_word} FROM customer WHERE wo = {wo}".format(select_word=select_word, form_name=form_name, wo=wo)
    cursor.execute(sql)
    result = cursor.fetchone()
    if result is not None:
        result = {
            "wo": result[0],
            "woriker_id": result[1],
            "customer": result[2],
            "address": result[3],
            "qty": result[4],
            "tracking": result[5],
            "price": result[6],
            "order_status": result[7],
        }
    db.close()
    return result


def get_update_sql(data):
    form_name = "customer"
    line = ""
    wo = data['wo']
    for d in data:
        key = d
        value = data[key]
        line += "{}='{}',".format(key, value)

    sql = """update {form_name} set {line} where wo = {wo}""".format(form_name=form_name, line=line[:-1], wo=wo)
    return sql


def execute_update_sql(update_data):
    data = {
        "host": "39.106.219.251",
        "user": "root",
        "password": "admin",
        "db": "goods",
        "charset": "utf8"
    }
    db = pymysql.connect(**data)
    cursor = db.cursor()
    sql = get_update_sql(update_data)
    cursor.execute(sql)
    db.commit()
    db.close()


class Interface:
    def __init__(self, interface):
        self.interface = interface
        self._init()

    def _init(self):
        self.worker_id = StringVar('')
        self.customer = StringVar('')
        self.address = StringVar('')
        self.qty = StringVar('')
        self.tracking = StringVar('')
        self.price = StringVar('')

        Label(self.interface, text='W/O #:').grid(row=0, column=0)
        Label(self.interface, text='Worker ID:').grid(row=1, column=0)
        Label(self.interface, text='Customer:').grid(row=2, column=0)
        Label(self.interface, text='Address:').grid(row=3, column=0)
        Label(self.interface, text='QTY').grid(row=4, column=0)
        Label(self.interface, text='Tracking Number:').grid(row=5, column=0)
        Label(self.interface, text='Price:').grid(row=6, column=0)

        self.e1 = Entry(self.interface)
        Label(self.interface, textvariable=self.worker_id).grid(row=1, column=1, padx=10, pady=5)
        Label(self.interface, textvariable=self.customer).grid(row=2, column=1, padx=10, pady=5)
        Label(self.interface, textvariable=self.address).grid(row=3, column=1, padx=10, pady=5)
        Label(self.interface, textvariable=self.qty).grid(row=4, column=1, padx=10, pady=5)
        self.tracking = Entry(self.interface)
        self.tracking.grid(row=5, column=1, padx=10, pady=5)
        Label(self.interface, textvariable=self.price).grid(row=6, column=1, padx=10, pady=5)

        self.e1.grid(row=0, column=1, padx=10, pady=5)

        Button(self.interface, text='Print', width=10, command=self.show).grid(row=7, column=0, sticky=W, padx=10, pady=5)
        Button(self.interface, text='Submit', width=10, command=self.submit).grid(row=8, column=0, sticky=W, padx=10, pady=5)
        Button(self.interface, text='Ship', width=10, command=self.ship).grid(row=8, column=1, sticky=W, padx=10, pady=5)

    def show(self):
        """
        1.获得当前wo的值
        2.清空所有输入框
        3.查询数据库数据
        4.将数据进行显示
        """

        status = self.is_exist()
        if status:
            wo = self.e1.get()
            data = get_data(wo)
            self.clear()
            self.set_value(data)
        else:
            # 未查询到数据
            tkinter.messagebox.showinfo(title='shipping message', message="no found data")
            self.clear()

    def submit(self):
        status = self.is_exist()
        if status:
            data = self.get_all_input()
            execute_update_sql(data)
        else:
            # 未查询到数据
            tkinter.messagebox.showinfo(title='shipping message', message="no found data")

    def ship(self):
        status = self.is_exist()

        if status:
            data = {
                "wo": self.e1.get(),
                "order_status": "shipped",
            }
            execute_update_sql(data)
            tkinter.messagebox.showinfo(title='shipping message', message=" The order is shipping out")
        else:
            tkinter.messagebox.showinfo(title='shipping message', message="no found data")

    def is_exist(self):
        """
        检查这条数据是否存在
        """
        wo = self.e1.get()
        data = get_data(wo)
        if data is None:
            return False
        else:
            return True

    def clear(self):
        """
        清空所有Entry
        """
        self.e1.delete(0, END)
        self.worker_id.set("")
        self.customer.set("")
        self.address.set("")
        self.qty.set("")
        self.tracking.delete(0, END)
        self.price.set("")

    def set_value(self, data):
        """
        把查询到的放到input中
        """
        self.e1.insert(0, data["wo"])
        self.worker_id.set(data["worker_id"])
        self.customer.set(data["customer"])
        self.address.set(data["address"])
        self.qty.set(data["qty"])
        self.tracking.insert(0, data["tracking"])
        self.price.set(data["price"])

    def get_all_input(self):
        """
        获得所有已经录入的信息
        """
        data = {
            "wo": self.e1.get(),
            "tracking": self.tracking.get(),
        }
        return data


if __name__ == "__main__":
    interface = Tk()
    interface.configure()
    interface.title("Inventory")
    interface.geometry("600x440")
    Interface(interface)
    interface.mainloop()
