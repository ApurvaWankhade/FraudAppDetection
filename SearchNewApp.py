import tkinter as tk
import pymysql
import sys
import os
import io
import re
import gc
from html.parser import HTMLParser
from tkinter.filedialog import askopenfile
from subprocess import Popen
from tkinter import messagebox
import urllib.request
from subprocess import call
from bs4 import BeautifulSoup
from google_play_scraper import app
        
mydb=pymysql.connect(host="localhost",user="root",password="root",database="fraudapp_py")
mycursor=mydb.cursor()
top1=tk.Tk()
top1.title("User Dashboard")

error1=tk.StringVar()
url= tk.StringVar()

width = 500
height = 350
screen_width = top1.winfo_screenwidth()
screen_height = top1.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
top1.geometry("%dx%d+%d+%d" % (width, height, x, y))
top1.config(bg="grey")

def search():
    urldata=" "
    uname=""
    url=e1.get()
    if(len(url)==0):
        error1.set("Enter Valid App Name")
    else:
        mycursor.execute("select * from currentuser")
        myresult = mycursor.fetchall()
        uid=""
        for x in myresult:
            uid=x[2]
            uname=x[1]

        #---------------------------------insert in usersearches----------------
        sql="insert into usersearches(appname,uid,uname)values(%s,%s,%s)"
        values=(url,uid,uname)
        mycursor.execute(sql,values)
        mydb.commit()
       #-----------------------clear current searches--------------------------
        sql3="delete from currentsearch"
        mycursor.execute(sql3)
       #-----------------------insert in current searches------------------------
        sql2="insert into currentsearch(app,uid)values(%s,%s)"
        values2=(url,uid)
        mycursor.execute(sql2,values2)
        mydb.commit()
       #-----------------------------Review Extraction--------------------
       # result = app(
        # url,
        # lang='en', # defaults to 'en'
         # country='us' # defaults to 'us'
        #)

        result = app(
             url,
             lang='en', # defaults to 'en'
            country='us' # defaults to 'us'
        )
        
        #f=open("guru99.txt", "w+")
        #f.write(""+str(result))
        #print(result)
        #for x in result:
           # print(x[0])

        with open("urldata.txt", "w", encoding="utf-8") as f:
                
        
        #print(urldata)
        #call('python ViewExtractedData.py', shell=True)
        #os.system("ViewExtractedData.py")
          
L= tk.Label(top1, width=30, font=('arial', 20),bg="black",fg="green", text = "   Fraud App Detection    ",bd=5)
L.grid(row=1,column=1)

L1= tk.Label(top1, width=30,bg="grey",fg="green", text = "  Enter App Package Name    ")
L1.grid(row=2,column=1)


e1= tk.Entry(top1,bg="white",fg="green",text="Search For New Link",bd=8)  
e1.config(width="60")
e1.grid(row=3,column=1)


ErL1=tk.Label(top1,text="",fg="red",bg="grey",textvariable=error1)
ErL1.grid(row=4,column=1)



b6= tk.Button(top1,bg="black",fg="green",text="Search",bd=8,command=search)
b6.config(width="30")  
b6.grid(row=5,column=1)

top1.mainloop()
