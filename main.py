import tkinter
from tkinter import ttk
from Login import login
from selection import WOWindow

def main():
    dept = login()
    print(dept)
    if dept == "Receiving":
        receiving()
    elif dept == "Assembly":
        while(true):
            workorder = WOWindow(dept)
            assembly(workorder, workerID)
    elif dept == "Testing":
        while(true):
            workorder = WOWindow(dept)
            testing(workorder, workerID)
    elif dept == "Shipping":
        while(true):
            workorder = WOWindow(dept)
            shipping(workorder, workerID)

main()