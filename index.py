import tkinter as tk
import pymysql
import sys
import os
import gc
from tkinter import messagebox
from subprocess import Popen
import subprocess
from subprocess import call
gc.collect()
#-------------------------db connection---------------------------------------
mydb=pymysql.connect(host="localhost",user="root",password="root",database="fraudapp_py")
mycursor=mydb.cursor()

top1=tk.Tk()
top1.title("Login Here")
width = 600
height = 350
screen_width = top1.winfo_screenwidth()
screen_height = top1.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
top1.geometry("%dx%d+%d+%d" % (width, height, x, y))
top1.config(bg="grey")
error1=tk.StringVar()
error2=tk.StringVar()
def login():
     uname= tk.StringVar()
     password= tk.StringVar()
     uname=E11.get()
     password=E12.get()
     a=0
     if(len(uname)==0):
         error1.set("Enter Email")
         a=1
     else:
          error1.set("")

     if(len(password)==0):
         error2.set("Enter Password")
         a=1
     else:
         error2.set("")
     if(a==0):
          a1="0"
          mycursor.execute("select * from user where cardplay=%s and playernum=%s",(E11.get(), E12.get()))
          myresult = mycursor.fetchall()
          uname=""
          username=""
          uid=""
          
          for x in myresult:
                uid=x[0]
                uname=x[1]
                a1="1"
                
          mycursor.execute("delete from currentuser")
          mydb.commit()
          
          ql="insert into currentuser (username,userid)values(%s,%s)"
          values=(uname,uid)
          mycursor.execute(ql,values)
          mydb.commit()
          #print("Valid")
          if(a1=="1"):
               jum()
          else:
               #print("Uname "+E11.get())
               #print("PAss "+E12.get())
               
               if(E11.get()=="admin" and E12.get()=="admin"):
                    top1.destroy()
                    call('python AdminDashboard.py', shell=True)
                    
                    #os.system("AdminDashboard.py")
                    #os.close()
               else:
                    messagebox.showinfo("Alert","Invalid Username or Password")
                    
          
          #exec(open("UserDashboard.py").read())
         #top1.quit

def jum():
     #exec(open("NewRegistration.py").read())
     try:
          top1.destroy()
          #os.system("UserDashboard.py")
          call('python UserDashboard.py', shell=True)
          #os.close()
          
     except IOError:
           print('Problem reading: ' + filename) 
          
     
     #top1.destroy()   
     
def reg1():
     top1.destroy()
     call('python NewRegistration.py', shell=True)
     #os.system("NewRegistration.py")
     
    


L1=tk.Label(top1,text="   Fraud App Detection    ",font=('arial', 24),bg="black",fg="green")
L1.grid(row=1, column=2)

L2=tk.Label(top1,text="Enter Email    :",fg="green",bg="grey", font=('arial', 14), bd=5)
L2.grid(row=2, column=1)

E11=tk.Entry(top1,font=(14),bd=5)
E11.grid(row=2,column=2)

ErL1=tk.Label(top1,text="",fg="red",bg="grey",textvariable=error1)
ErL1.grid(row=3,column=2)



L3=tk.Label(top1,text="Enter Password :",fg="green",bg="grey", font=('arial', 14), bd=5)
L3.grid(row=4, column=1)

E12=tk.Entry(top1,show="*",font=(14),bd=5)
E12.grid(row=4,column=2)


ErL2=tk.Label(top1,text="",fg="red",bg="grey",textvariable=error2)
ErL2.grid(row=5,column=2)



b1=tk.Button(top1,bg="grey",fg="green",text="Login",bd=8,width=30,command=login)
b1.grid(row=10,column=2)

b2=tk.Button(top1,bg="grey",fg="green",text="New Registration",width=30,bd=8,command=reg1)
b2.grid(row=11,column=2)

top1.mainloop()




