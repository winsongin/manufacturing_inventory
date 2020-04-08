from tkinter import *
from tkinter import ttk
from login import Login
from assembly_class import assembly
from testing import TestingWindow
from shipping_connector import Interface
from receiving import Receiving
from accounting import accounting
from admin import Admin
from inventory_list import Inventory
from selection import WOWindow


def main():
    root = Tk()
    root.geometry("650x500")
    root.title("Login")
    login1 = Login(root)
    root.mainloop()
    if login1.dept == "Receiving":
        root = Tk()
        root.geometry("650x500")
        root.title("Receiving")
        root.configure(bg="light gray")
        receiving1 = Receiving(root)
        root.mainloop()
    elif login1.dept == "Assembly":
        workorder = WOWindow(login1.dept)
        root = Tk()
        root.geometry("600x500")
        root.title("Assembly")
        app = assembly(root, "0002", workorder)
        root.mainloop()
    elif login1.dept == "Testing":
        workorder = WOWindow(login1.dept)
        root = Tk()
        root.geometry("600x500")
        root.title("Testing")
        app = TestingWindow(root, workorder, "0003")
        root.mainloop()
    elif login1.dept == "Shipping":
        workorder = WOWindow(login1.dept)
        root = Tk()
        root.title("Shipping")
        Interface(root, workorder, "0004")
        #shipping(workorder, workerID)
        root.mainloop()
    elif login1.dept == "Accounting":
        root = Tk()
        root.geometry("500x300")
        root.title("Accounting")
        close_window = Button(root, text="Close", command=root.quit)
        close_window.place(x=90, y=230)
        app = accounting(root, "0005")
        root.mainloop()
    elif login1.dept == "Admin":
        root = Tk()
        root.geometry("600x500")
        root.title("New User")
        root.configure(bg="light gray")
        admin1 = Admin(root)
        root.mainloop()
    elif login1.dept == "Inventory":
        root = Tk()
        root.title("Inventory")
        app = Inventory(root)
        root.mainloop()

main()