from tkinter import *
from tkinter import ttk
from login import Login
from assembly_class import assembly
from testing import TestingWindow
from shipping import Interface
from selection import WOWindow


def main():
    root = Tk()
    root.geometry("650x500")
    login1 = Login(root)
    root.mainloop()
    if login1.dept == "Receiving":
        return
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
        Interface(interface, workorder, "0004")
        shipping(workorder, workerID)

main()