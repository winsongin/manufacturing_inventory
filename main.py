import tkinter
from tkinter import ttk
from Login import login

def main():
    dept = login()
    if dept == "Receiving":
        WOWindow(dept)
    elif dept == "Assembly":
        WOWinwow(dept)
    elif dept == "Testing":
        WOWindow(dept)
    elif dept == "Shipping":
        WOWindow(dept)

main()