import tkinter as tk
import mysql.connector as sql

mydb = sql.connect(host = 'localhost',user = 'root',passwd = 'Razgriz!949',database = 'inventory_system')
    
class Login:
    def __init__(self,root):

        self.root = root
        
        self.dept = ''

        #Label object 
        
        self.lUsername = tk.Label(self.root, text = 'Employee ID', font=("arial", 12))
        
        self.lPassword = tk.Label(self.root, text = 'Password', font=("arial", 12))
        
        self.wrong = tk.Label(self.root, text = 'Please Try Again', font=("arial", 12))
        
        #Variables to Store Data
    
        self.user = tk.StringVar()
    
        self.passwd = tk.StringVar()
    
        #Entry object
    
        self.eUsername = tk.Entry(self.root, textvariable = self.user,font=("arial", 12))
    
        self.ePassword = tk.Entry(self.root, textvariable = self.passwd, show ='*',font=("arial", 12))
        
        #Button
    
        self.bLogin = tk.Button(self.root, text = 'Login', command = self.execute, height = 1, width = 8,font=("arial", 12))
        
        self.root.bind('<Return>', self.buttonPressed)
        
        #placing in GUI
    
        self.lUsername.pack()
    
        self.eUsername.pack()
    
        self.lPassword.pack()
    
        self.ePassword.pack()
        
        self.bLogin.pack()
        
    def buttonPressed(self,event):
        self.execute()
          
    #gets Username from Database
    def getUser(self):
        cur = mydb.cursor()
        statement = ("select employee_id from employees where employee_id = '{}'").format(self.eUsername.get())
        cur.execute(statement)
        result = cur.fetchone()
        result = ''.join(result)
        if result == self.user.get():
            return True
        
        elif result == None:
            return True

    #gets Password from Database
    def getPass(self):
        cur = mydb.cursor()
        statement = ("select pass from employees where employee_id = '{}'").format(self.eUsername.get())
        cur.execute(statement)
        result = cur.fetchone()
        result = ''.join(result)
        #if not in database return Lock is True
        if result == self.passwd.get():
            return False    
        
        elif result == None:
            return True
        
        #if in database return false  
       
    #Find Department For User
    def findDept(self):
        cur = mydb.cursor()
        d = []
        statement = ("select dept from employees where employee_id= '{}'").format(self.eUsername.get())
        cur.execute(statement)
        results = cur.fetchone()
        for x in results:
            ts = ''.join(x)
            d.append(ts)

        return (d[0])
        
    #Login Function
    def execute(self):
        temp = ''
        lock = True                                                  
        found = False                                               
        found = self.getUser()
        lock = self.getPass() 
        if found == True and lock == False:
            temp = self.findDept()
            self.dept = temp
            self.root.destroy()
        else:
            if(self.wrong.winfo_ismapped() == True):
                self.wrong.pack_forget()
            self.wrong.pack()
       

            return temp, user

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("650x500")
    root.title("Login")
    result = Login(root)
    login1 = result[0]
    idNum = result[1]
    print(result)
    root.mainloop()
    if login1.dept == 'Receiving':
        print('working!')
