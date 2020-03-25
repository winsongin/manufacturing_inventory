import tkinter
from tkinter import ttk
from Login import login
from assembly import AssyWindow
from selection import WOWindow
from testing import TestWindow


def main():
    dept = login()
    print(dept)
    if dept == "Receiving":
        return
    elif dept == "Assembly":
        workorder = WOWindow(dept)
        print(workorder)
        AssyWindow(workorder, "0002")
    elif dept == "Testing":
        workorder = WOWindow(dept)
        TestWindow(workorder, "0003")
    elif dept == "Shipping":
        while(True):
            break
            #workorder = WOWindow(dept)
            #shipping(workorder, workerID)

main()