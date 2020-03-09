# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk
import mysql.connector
from login_mechanic import finddept

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Razgriz!949",
        database="inventory_system"
        )

cur = mydb.cursor()
uid = []
p = []
statement = "select employee_id from employees"
cur.execute(statement)
results = cur.fetchall()
for x in results:
    uid.append(x)
statement = "select pass from employees"
cur.execute(statement)
results = cur.fetchall()
for x in results:
    p.append(x)
    
#Login Screen 

def login():
    lock = True
    found = False
    name = eUsername.get()
    for x in uid:
        ts = ''.join(x)
        if ts == name:
            found_user = ts
            found = True
    password = ePassword.get()
    for x in p:
        ts = ''.join(x)
        if ts == password:
            found_pass = ts
            lock = False
    if found == True and lock == False:
        print('Logged in')
        return(finddept(found_user))


#Window Creation
win = tk.Tk()

win.title("Inventory Manager")
win.geometry("600x500") #width and height

frmHome = tk.Frame(win, height = 400)
frmHome.pack()

frmA = tk.Frame(win)


#Label object 

lUsername = tk.Label(frmHome, text = 'Username')
lPassword = tk.Label(frmHome, text = 'Password')


#Variables to Store Data

user = tk.StringVar()
passwd = tk.StringVar()


#Entry object

eUsername = tk.Entry(frmHome, textvariable = user)
ePassword = tk.Entry(frmHome, textvariable = passwd, show ='*')


#Button

bLogin = tk.Button(frmHome, text = 'Login', command = login)


#placing in GUI

lUsername.pack(side= tk.TOP, anchor = 'w', expand = 'true')
eUsername.pack(side= tk.TOP, anchor = 'center', expand = 'true', fill = 'x')
lPassword.pack(side= tk.TOP, anchor = 'w', expand = 'true')
ePassword.pack(side= tk.TOP, anchor = 'center', expand = 'true', fill = 'x')
bLogin.pack(side = tk.BOTTOM, anchor = 'center')

win.mainloop()
