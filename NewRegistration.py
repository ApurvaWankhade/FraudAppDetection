import tkinter as tk
import pymysql
from tkinter import messagebox  
import gc
import os
gc.collect()
mydb=pymysql.connect(host="localhost",user="root",password="root",database="fraudapp_py")
mycursor=mydb.cursor()
top=tk.Tk()
top.title("Register Here")
width = 400
height = 350
screen_width = top.winfo_screenwidth()
screen_height = top.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
top.geometry("%dx%d+%d+%d" % (width, height, x, y))
top.config(bg="black")

error1=tk.StringVar()
error2=tk.StringVar()
error3=tk.StringVar()
error4=tk.StringVar()
def reg():
     NAME = tk.StringVar()
     CONTACT= tk.StringVar()
     EMAIL= tk.StringVar()
     PASSWORD= tk.StringVar()
     NAME=E1.get()
     CONTACT=E2.get()
     EMAIL=E3.get()
     PASSWORD=E4.get()
     a=0
#------------------------NAME VALIDATION-----------------------------------------
     NAME=NAME.replace(" ","")
     if(len(NAME)==0):
         error1.set("Please Enter Valid Name")    
         a=1
     else:
          
          #print(NAME)
          if(NAME.isalpha()==False ):
              error1.set("Please Enter Valid Name")
              a=1
          else:
               error1.set("")
#--------------------------------Number Validation-------------------------        
     if(len(CONTACT)!=10 ):

         error2.set("Please Enter valid Contact Number")
         a=1
     else:
          if(CONTACT.isdigit()==True):
               error2.set("")
               num=["98","78","88","80","89","70","95","82","80","84","92","96","75","76"]
               numtwo=CONTACT[:2]
               print(numtwo)
               if numtwo in num:
                    error2.set("")
               else:
                    error2.set("Please Enter valid Contact Number")
                    a=1
                    
          else:
                error2.set("Please Enter valid Contact Number")
                a=1

#----------------------------Email Validation----------------------------------------------
     if(len(EMAIL)==0):
         error3.set("Please Enter Valid Email")
         a=1
     else:
         #print(EMAIL.find("@"))
         if(EMAIL.find("@")<0 or EMAIL.find(".")<0 ):
              error3.set("Please Enter Valid Email")
              a=1
         else:
              error3.set("")
              
#---------------------------Password Validation-----------------------------------------------
         
     if(len(PASSWORD)==0):
         error4.set("Please Enter Valid Password")
         a=1
     else:
          print(PASSWORD.find("@"))
          if(PASSWORD.find("@")<0 and PASSWORD.find("!")<0 and PASSWORD.find("_")<0):
               error4.set("password must contain one"+"\n"+"special symbol from @ or ! or _")
               a=1
          else:
               error4.set("")
                
          
                    
              
               
     if(a==0):
         sql="insert into user (name,contact,email,password)values(%s,%s,%s,%s)"
         values=(NAME,CONTACT,EMAIL,PASSWORD)
         mycursor.execute(sql,values)
         mydb.commit()
         messagebox.showinfo("Registration","Registration Done Sucessfully")
         os.system("index.py")
         top.destroy()
    


L1=tk.Label(top,text="   Fraud App Detection    ",font=('arial', 10),bg="black",fg="green")
L1.grid(row=1, column=1)

L2=tk.Label(top,text="Name    :",fg="green",bg="black", font=('arial', 14), bd=5)
L2.grid(row=2, column=1)

E1=tk.Entry(top,font=(14),bd=5)
E1.grid(row=2,column=2)

ErL1=tk.Label(top,text="",fg="red",bg="black",textvariable=error1)
ErL1.grid(row=3,column=2)



L3=tk.Label(top,text="Contact :",fg="green",bg="black", font=('arial', 14), bd=5)
L3.grid(row=4, column=1)

E2=tk.Entry(top,font=(14),bd=5)
E2.grid(row=4,column=2)

ErL2=tk.Label(top,text="",fg="red",bg="black",textvariable=error2)
ErL2.grid(row=5,column=2)


L4=tk.Label(top,text="Enter Email",fg="green",bg="black", font=('arial', 14), bd=5)
L4.grid(row=6, column=1)

E3=tk.Entry(top,font=(14),bd=5)
E3.grid(row=6,column=2)

ErL3=tk.Label(top,text="",fg="red",bg="black",textvariable=error3)
ErL3.grid(row=7,column=2)


L4=tk.Label(top,text="Enter Password",fg="green",bg="black", font=('arial', 14), bd=5)
L4.grid(row=8, column=1)

E4=tk.Entry(top,show="*",font=(14),bd=5)
E4.grid(row=8,column=2)

ErL4=tk.Label(top,text="",fg="red",bg="black",textvariable=error4)
ErL4.grid(row=9,column=2)






b1=tk.Button(top,text="Submit",command=reg)
b1.grid(row=10,column=2)


top.mainloop()
