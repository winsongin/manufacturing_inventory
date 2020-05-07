from tkinter import *
from login import Login
from assembly_class import Assembly
from testing import TestingWindow
from shipping import Shipping
from receiving import Receiving
from accounting import accounting
from admin import Admin


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
        root = Tk()
        root.geometry("665x340")
        root.title("Assembly")
        app = Assembly(root, "0002")
        root.mainloop()
    elif login1.dept == "Testing":
        root = Tk()
        root.geometry("680x500")
        root.title("Testing")
        app = TestingWindow(root, "0003")
        root.mainloop()
    elif login1.dept == "Shipping":
        root = Tk()
        root.geometry("665x340")
        root.title("Shipping")
        Shipping(root)
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

main()