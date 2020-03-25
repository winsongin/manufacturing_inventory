# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk
import mysql.connector as sql

def login():
    
    mydb = sql.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'Razgriz!949',
            database = 'inventory_system'
            )
    
    cur = mydb.cursor()
    #gets Usernames from Database
    def getUser(u):
        #try:
        statement = ("select employee_id from employees where employee_id = '{}'").format(u)
        cur.execute(statement)
        result = cur.fetchone()
        if result == None:
            return True
    
        result = ''.join(result)
        if result == u:
            return True


    #gets Passwords from Database
    def getPass(p):
        statement = ("select pass from employees where pass = '{}'").format(p)
        cur.execute(statement)
        result = cur.fetchone()
        #if not in database return Lock is True
        if result == None:
            return True
    
        result = ''.join(result)
   
        #if in database return false
        if result == p:
            return False


    #Find Department For User
    def finddept(uid):
        d = []
        statement = ("select dept from employees where employee_id= '{}'").format(uid)
        cur.execute(statement)
        results = cur.fetchone()
        for x in results:
            ts = ''.join(x)
            d.append(ts)
            return (d[0])     

    #Login Function
    def execute(u,p):
        global temp
        lock = True                                                  
        found = False                                                
        name = u
        found = getUser(name)
        password = p
        lock = getPass(password)
        if found == True and lock == False:
            dept = finddept(name)
            temp = dept
            win.destroy()
            return
        else:
            tmp = tk.Label(frmHome, text = "Password/EmployeeID Incorrect, Try Again")
            tmp.pack()
    
        #Window Creation
    win = tk.Tk()

    win.title("Login")
    win.geometry("600x500") #width and height
    
    frmHome = tk.Frame(win, height = 400)
    frmHome.pack()
    
    
    #Label object 
    
    lUsername = tk.Label(frmHome, text = 'Employee ID')
    
    lPassword = tk.Label(frmHome, text = 'Password')
    
    #Variables to Store Data

    user = tk.StringVar()

    passwd = tk.StringVar()

    #Entry object

    eUsername = tk.Entry(frmHome, textvariable = user)

    ePassword = tk.Entry(frmHome, textvariable = passwd, show ='*')
    
    #Button

    bLogin = tk.Button(frmHome, text = 'Login', command = lambda: execute(eUsername.get(),ePassword.get()))

    #placing in GUI

    lUsername.pack(side= tk.TOP, anchor = 'w', expand = 'true')

    eUsername.pack(side= tk.TOP, anchor = 'center', expand = 'true', fill = 'x')

    lPassword.pack(side= tk.TOP, anchor = 'w', expand = 'true')

    ePassword.pack(side= tk.TOP, anchor = 'center', expand = 'true', fill = 'x')

    bLogin.pack(side = tk.BOTTOM, anchor = 'center')
      
    win.mainloop()
    
    return temp
