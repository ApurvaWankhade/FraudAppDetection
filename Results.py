import tkinter as tk
import random
import pymysql
import sys
import os
import gc
from html.parser import HTMLParser
from tkinter.filedialog import askopenfile
from subprocess import Popen
from tkinter import messagebox
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import urllib.request
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

offensivecount=tk.StringVar()
sexualcount=tk.StringVar()
violantcount=tk.StringVar()
maliciousness=tk.StringVar()
rating=tk.StringVar()

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


#---------------------Get Current Url-----------------------------------------
mycursor.execute("select * from currentsearch")
myresult = mycursor.fetchall()
k=1
for x in myresult:
    appname=x[1]
    print(appname)

    
sql="select * from results"
values=(appname)
mycursor.execute(sql)
trustcount=0
fraudcount=0;
totalcount=0;
myresult = mycursor.fetchall()
for x in myresult:
    if(x[1]==appname):
        print(x[2])
        fraudcount=int(x[2])
        trustcount=int(x[5])
        totalcount=int(x[6])
    
fraudcount=fraudcount/totalcount
fraudcount=fraudcount*100
trustcount=trustcount/totalcount
trustcount=trustcount*100
url.set(appname)
violantcount.set("Fraud Count : "+str(fraudcount)+"%")
sexualcount.set("Trust Count : "+str(trustcount)+"%")
offensivecount.set("Total Count "+str(totalcount))

#total=int(viocount)+int(sexcount)+int(offcount)
#malcount=total/3

malcount=0
if(fraudcount>=trustcount):
    result.set("Fraud App Detected")
    #sql="insert into blacklinks(url,ration)values(%s,%s)"
    #values=(geturl,malcount)
    #mycursor.execute(sql,values)
    #mydb.commit() 
else:
    result.set("Fraud App Not Detected")
#-------------------------------------Update Malicious Ness----------------------------
#sql="update results set malration=%s where url=%s"
#values=(str(malcount),geturl)
#mycursor.execute(sql,values)
word1="score"
count=0;
isfound=False
ratings=""
with open('urldata.txt','r',errors="ignore") as file:
    # reading each line    
    for line in file:
        # reading each word        
        for word in line.split():
            if word1 in word:
                #print(word)
                isfound=True
            ratings=word
            if(isfound):
                count=count+1;
            if(count==2):
                break;
#ratings1=float(ratings)
#ratings2=ratings+0.5;
#secure_random = random.SystemRandom()
#ratings11 = secure_random.uniform(ratings1, ratings)
#print(randomfloat)
rating.set("Ratings:"+ratings)
    
L= tk.Label(top1, width=30, font=('arial', 20),bg="black",fg="green", text = "   Fraud App Detection    ",bd=5)
L.grid(row=1,column=1)

L1= tk.Label(top1, width=30,bg="grey",fg="green", text = "  Extraxted reviews    ")
L1.grid(row=2,column=1)

L2= tk.Label(top1, width=30,bg="grey",fg="red",font=('arial', 20), text = "  Result  ",textvariable=result)
L2.grid(row=3,column=1)

L3=tk.Label(top1,text="",fg="white",justify=tk.LEFT,font=('arial', 15),padx = 10,bg="grey",textvariable=url)
L3.grid(row=4,column=1)

L3=tk.Label(top1,text="",fg="white",justify=tk.LEFT,font=('arial', 15),padx = 10,bg="grey",textvariable=violantcount)
L3.grid(row=5,column=1)

L4=tk.Label(top1,text="",fg="white",justify=tk.LEFT,font=('arial', 15),padx = 10,bg="grey",textvariable=sexualcount)
L4.grid(row=6,column=1)


L5=tk.Label(top1,text="",fg="white",justify=tk.LEFT,font=('arial', 15),padx = 10,bg="grey",textvariable=offensivecount)
L5.grid(row=7,column=1)

L5=tk.Label(top1,text="",fg="white",justify=tk.LEFT,padx = 10,bg="grey",font=('arial', 15),textvariable=maliciousness)
L5.grid(row=8,column=1)

L6=tk.Label(top1,text="",fg="white",justify=tk.LEFT,padx = 10,bg="grey",font=('arial', 15),textvariable=rating)
L6.grid(row=9,column=1)


top1.mainloop()
