import tkinter as tk
import pymysql
import sys
import os
import gc
from tkinter.filedialog import askopenfile
from subprocess import Popen
from tkinter import messagebox
from subprocess import call
mydb=pymysql.connect(host="localhost",user="root",password="root",database="fraudapp_py")
mycursor=mydb.cursor()

top1=tk.Tk()
top1.title("Admin Dashboard")
width = 1300
height = 700
screen_width = top1.winfo_screenwidth()
screen_height = top1.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
top1.geometry("%dx%d+%d+%d" % (width, height, x, y))
top1.config(bg="grey") 
def viewusers():
    call('python ViewUsers.py', shell=True)
    #os.system("ViewUsers.py")
def viewkeywords():
    call('python viewkeywords.py', shell=True)
    #os.system("ViewUsers.py")
def mysearches():
    call('python ViewAllSearches.py', shell=True)
    #os.system("ViewAllSearches.py")
def addkeyword():
    call('python AddWordDictionary.py', shell=True)
    #os.system("AddWordDictionary.py")
def blacklink():
    call('python BlackListedLink.py', shell=True)
    #os.system("BlackListedLink.py")
def logout():
    top1.destroy()
    call('python index.py', shell=True)
    #os.system("index.py")
    
L= tk.Label(top1, width=30, font=('arial', 20),bg="black",fg="green", text = "   Fraud App Detection",bd=5)
L.grid(row=1,column=1)
L= tk.Label(top1, width=30, font=('arial', 20),bg="black",fg="red", text = "--Helps to Detect Malicious  APP",bd=5)
L.grid(row=1,column=2)
L= tk.Label(top1, width=30, font=('arial', 20),bg="black",fg="green", text = "",bd=5)
L.grid(row=1,column=3)

photo = tk.PhotoImage(file = r"D:\Abstract and Details 2017\Malicious URL detection System Python\images\viewuser.png")
photoimage = photo.subsample(4, 4) 
b2= tk.Button(top1,bg="white",fg="green",text="View Users",bd=8,command=viewusers,image = photoimage,compound ="top")  
b2.config(width="100")
b2.config(height="100")
b2.grid(row=2,column=1,padx=30,pady=30)


photo2 = tk.PhotoImage(file = r"D:\Abstract and Details 2017\Malicious URL detection System Python\images\searches.png")
photoimage2 = photo2.subsample(4, 4) 
b3= tk.Button(top1,bg="white",fg="green",text="View All Searches",bd=8,command=mysearches,image = photoimage2,compound ="top" )
b3.config(width="100")
b3.config(height="100")  
b3.grid(row=2,column=2)


photo3 = tk.PhotoImage(file = r"D:\Abstract and Details 2017\Malicious URL detection System Python\images\addword.png")
photoimage3 = photo3.subsample(4, 4) 
b4= tk.Button(top1,bg="white",fg="green",text=" Add Keyword",bd=8,command=addkeyword,image = photoimage3,compound ="top")
b4.config(width="100")
b4.config(height="100") 
b4.grid(row=4,column=1)


photo4 = tk.PhotoImage(file = r"D:\Abstract and Details 2017\Malicious URL detection System Python\images\blacklink.png")
photoimage4 = photo4.subsample(4, 4)
b5= tk.Button(top1,bg="white",fg="green",text="Black Listed App",bd=8,command=blacklink,image = photoimage4,compound ="top" )
b5.config(width="100")
b5.config(height="100")   
b5.grid(row=4,column=2)


photo5 = tk.PhotoImage(file = r"D:\Abstract and Details 2017\Malicious URL detection System Python\images\showword.png")
photoimage5 = photo5.subsample(4, 4)
b6= tk.Button(top1,bg="white",fg="green",text="View Keywords",bd=8,command=viewkeywords,image = photoimage5,compound ="top"  )
b6.config(width="100")
b6.config(height="100")  
b6.grid(row=2,column=3)

photo6 = tk.PhotoImage(file = r"D:\Abstract and Details 2017\Malicious URL detection System Python\images\logout.png")
photoimage6 = photo6.subsample(4, 4)
b7= tk.Button(top1,bg="white",fg="green",text="Log Out",bd=8,command=logout,image = photoimage6,compound ="top"  )
b7.config(width="100")
b7.config(height="100")  
b7.grid(row=4,column=3)

top1.mainloop()
