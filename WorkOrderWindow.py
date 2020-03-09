import tkinter
from tkinter import ttk
import mysql.connector

def WOWindow(department):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Razgriz!949",
        database="inventory_system"
    )

