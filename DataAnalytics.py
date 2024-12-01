import tkinter as tk
import pymysql
import sys
import os
import io
import gc
from html.parser import HTMLParser
from tkinter.filedialog import askopenfile
from subprocess import Popen
from tkinter import messagebox
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import urllib.request
from subprocess import call
from bs4 import BeautifulSoup
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)
        
mydb=pymysql.connect(host="localhost",user="root",password="root",database="fraudapp_py")
mycursor=mydb.cursor()
top1=tk.Tk()
top1.title("Perform Analytics")

uid=""
#--------------------------Get Current User----------------------------
mycursor.execute("select * from currentuser")
myresult = mycursor.fetchall()
uid=""
for x in myresult:
    uid=x[2]

#--------------------------Get app anme----------------------------
mycursor.execute("select * from currentsearch")
myresult = mycursor.fetchall()
appname=""
for x in myresult:
    appname=x[1]



error1=tk.StringVar()
url= tk.StringVar()
result= tk.StringVar()

width = 500
height = 350
screen_width = top1.winfo_screenwidth()
screen_height = top1.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
top1.geometry("%dx%d+%d+%d" % (width, height, x, y))
top1.config(bg="grey")

with open("urldata.txt", "r+",errors="ignore") as f:
    data=f.read()
totalcount=0;
fraudcount=0
trustcount=0
violantcount=0
sexualcount=0
offensive=0
splittedword=data.split(" ")
for word1 in splittedword:
    totalcount=totalcount+1;
    mycursor.execute("select * from malword")
    myresult1 = mycursor.fetchall()
    for dbword in myresult1:
        wordcat=""
        if(dbword[1]==word1):
            print("Word Found")
            wordcat=dbword[2]
            if(wordcat=="Fraud"):
                fraudcount=fraudcount+1
            if(wordcat=="Trust"):
                trustcount=trustcount+1
                       
            
print(fraudcount)
result.set("Fraud Word TF: "+str(fraudcount)+"\n Trust Word TF : "+str(trustcount))

sql="insert into results(uid,app,fraudcount,trustcount,totalcount)values(%s,%s,%s,%s,%s)"
values=(uid,appname,fraudcount,trustcount,totalcount)
mycursor.execute(sql,values)
mydb.commit()    








#----------------------------Update data to table---------------------
#sql="update urldata set data=%s where uid=%s"
#values=(post_data,did)
#mycursor.execute(sql,values)
#mydb.commit()


def search():
    call('python Results.py', shell=True)
    #os.system("Results.py")
    
          
L= tk.Label(top1, width=30, font=('arial', 20),bg="black",fg="green", text = "   Fraud App Detction    ",bd=5)
L.grid(row=1,column=1)

L1= tk.Label(top1, width=30,bg="grey",fg="green", font=('arial', 20),text = "  TF Determination   ")
L1.grid(row=2,column=1)

L2= tk.Label(top1, width=30,bg="grey",fg="green", font=('arial', 15),text = "  Result  ",textvariable=result)
L2.grid(row=3,column=1)

ErL1=tk.Label(top1,text="",fg="white",justify=tk.LEFT,padx = 10,bg="grey",textvariable=error1)
ErL1.grid(row=4,column=1)



b6= tk.Button(top1,bg="black",fg="green",text=" Generate Result ",bd=8,command=search)
b6.config(width="30")  
b6.grid(row=5,column=1)

top1.mainloop()
