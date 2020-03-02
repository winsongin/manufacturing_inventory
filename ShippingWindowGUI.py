#########Auther: Xinyi Niu############
#########Last edit: 2/28/2020#########

#-------CPSC362 GROUP PROJECT---------#
#-------Inventory system--------------#
#------Shipping Window GUI------------#
#-------First sprint------------------#
from tkinter import *
import tkinter.messagebox
root = Tk()

root.title('Inventory')
root.geometry('600x440')


Label(root, text='W/O #:').grid(row=0, column=0)

Label(root, text='Worker ID:').grid(row=1, column=0)
Label(root, text='Customer:').grid(row=2, column=0)
Label(root, text='Address:').grid(row=3, column=0)
Label(root, text='QTY').grid(row=4, column=0)
Label(root, text='Tracking Number:').grid(row=5, column=0)
Label(root, text='Price:').grid(row=6, column=0)


e1 = Entry(root)

e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)
e5 = Entry(root)
e6 = Entry(root)
e7 = Entry(root)


e1.grid(row=0, column=1, padx=10, pady=5)

e2.grid(row=1, column=1, padx=10, pady=5)
e3.grid(row=2, column=1, padx=10, pady=5)
e4.grid(row=3, column=1, padx=10, pady=5)
e5.grid(row=4, column=1, padx=10, pady=5)
e6.grid(row=5, column=1, padx=10, pady=5)
e7.grid(row=6, column=1, padx=10, pady=5)

def show():#hit print button will display 
    print('W/O #：%s' % e1.get())
    print('Worker ID：%s' % e2.get())
    print('Customer：%s' % e3.get())
    print('Address：%s' % e4.get())
    print('Qty：%s' % e5.get())
    print('Shipping：%s' % e6.get())
    print('Pricce：%s' % e7.get())

on_hit= False
def hit_me():
    tkinter.messagebox.showinfo(title='shipping message', message=" The order is shipping out")
    global on_hit
    if on_hit == False:
        on_hit= True
        var.set('The order is shipping out')
    else:
            on_hit = False
            var.set('')

Button(root, text='Print', width=10, command=show) \
             .grid(row=7, column=0, sticky=W, padx=10, pady=5)


Button(root, text='Ship', width=10, command=hit_me)\
             .grid(row=7, column=1, sticky=E, padx=10, pady=5)

#
mainloop()
