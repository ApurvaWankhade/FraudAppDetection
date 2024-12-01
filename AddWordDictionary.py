import tkinter as tk
import pymysql
from tkinter import messagebox  
import gc
import os
gc.collect()
mydb=pymysql.connect(host="localhost",user="root",password="root",database="fraudapp_py")
mycursor=mydb.cursor()
top=tk.Tk()
top.title("Add Word Here")
width = 500
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
     word = tk.StringVar()
     category= tk.StringVar()
    
     word=E1.get()
     category=E2.get()
    
     a=0

     if(a==0):
         sql="insert into malword (word,category)values(%s,%s)"
         values=(word,category)
         mycursor.execute(sql,values)
         mydb.commit()
         messagebox.showinfo("Word","Word Added Sucessfully")
         #os.system("index.py")
         #top.destroy()
    


L1=tk.Label(top,text="Enter Training",bg="black")
L1.grid(row=1, column=1)

L2=tk.Label(top,text="Enter Word    :",fg="green",bg="black", font=('arial', 14), bd=5)
L2.grid(row=2, column=1)

E1=tk.Entry(top,font=(14),bd=5)
E1.grid(row=2,column=2)

ErL1=tk.Label(top,text="",fg="red",bg="black",textvariable=error1)
ErL1.grid(row=3,column=2)



L3=tk.Label(top,text="Enter Word Category :",fg="green",bg="black", font=('arial', 14), bd=5)
L3.grid(row=4, column=1)

E2=tk.Entry(top,font=(14),bd=5)
E2.grid(row=4,column=2)

ErL2=tk.Label(top,text="",fg="red",bg="black",textvariable=error2)
ErL2.grid(row=5,column=2)


b1=tk.Button(top,text="Submit",command=reg)
b1.grid(row=10,column=2)


top.mainloop()
