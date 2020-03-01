# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 14:40:00 2020

@author: Francisco
"""
import mysql.connector as sql

mydb = sql.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'P@nchito14',
        database = 'inventory_manager'
        )

cur = mydb.cursor()

def finddept(uid):
    d = []
    statement = ("select dept from employees where employee_id= '{}'").format(uid)
    cur.execute(statement)
    results = cur.fetchall()
    for x in results:
        ts= ''.join(x)
        d.append(ts)
    switch(d[0]) 

def switch(d):
    print(d)
        
