import tkinter as tk
import pymysql
import sys
import os
import gc
from html.parser import HTMLParser
from tkinter.filedialog import askopenfile
from subprocess import Popen
from tkinter import messagebox
import urllib.request
from bs4 import BeautifulSoup
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)
        
mydb=pymysql.connect(host="localhost",user="root",password="root",database="maliciousurl")
mycursor=mydb.cursor()
top1=tk.Tk()
top1.title("Admin Dashboard")

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


mycursor.execute("select * from currentuser")
myresult = mycursor.fetchall()
uid=""
for x in myresult:
    uid=x[2]


Lb1 = tk.Listbox(top1,width=50,bd=3,font=("arial",12))
sql="select * from usersearches where uid=%s"

mycursor.execute("select * from results where uid=%s",uid)
data=""
myresult = mycursor.fetchall()
k=1
for x in myresult:
    data=x[2]+" | Sex Count : "+x[3]+" | Off Count : "+x[4]+" |  Vio Count : "+x[5]
    Lb1.insert(k, data)

Lb1.grid(row=12, column=1)




def search():
    os.system("UserDashboard.py")
    top1.destroy()
    
          
L= tk.Label(top1, width=30, font=('arial', 20),bg="black",fg="green", text = "   Malicious Url Detction    ",bd=5)
L.grid(row=1,column=1)

L1= tk.Label(top1, width=30,bg="grey",fg="green", text = "  Extraxted Data from URL   ")
L1.grid(row=2,column=1)



ErL1=tk.Label(top1,text="",fg="white",justify=tk.LEFT,padx = 10,bg="grey",textvariable=error1)
ErL1.grid(row=4,column=1)



b6= tk.Button(top1,bg="black",fg="green",text="Exit",bd=8,command=search)
b6.config(width="30")  
b6.grid(row=5,column=1)

top1.mainloop()
