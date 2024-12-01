import tkinter as tk
import pymysql
import sys
import os
import io
import textwrap
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
top1.title("Stop Word Removal")

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
k=0
data=""
with open("urldata.txt", "r+",errors="ignore") as f:
    data=f.read()



did=""
Lb1 = tk.Listbox(top1,width=50,bd=3,font=("arial",12))
example_sent=data
#----------------------------------Stop WOrd Removal--------------------------------------
post_data=""
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(example_sent)
filtered_sentence = [w for w in word_tokens if not w in stop_words]
filtered_sentence = []
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
for x in filtered_sentence:
    post_data=post_data+" "+x
    
#print(filtered_sentence)
print("Filtered Data"+post_data)
stopworddata=""

wrapper = textwrap.TextWrapper(width=50)
word_list = wrapper.wrap(text=post_data)
for element in word_list:
    Lb1.insert(k, element)
    stopworddata=stopworddata+element
    k=k+1


#---------------------------Updating to text file-------------------------------
with open("urldata.txt", "w",errors="ignore") as f:
    f.write(stopworddata)
    

Lb1.insert(k, stopworddata)

#mycursor.execute("select * from urldata")
#myresult = mycursor.fetchall()
k=1
#for x in myresult:
    #Lb1.insert(k, data)
     #k=k+1
Lb1.grid(row=12, column=1)

def search():
    #top1.destroy()
    call('python DataAnalytics.py', shell=True)
    #os.system("DataAnalytics.py")
    
          
L= tk.Label(top1, width=30, font=('arial', 20),bg="black",fg="green", text = "   Fraud App Detection    ",bd=5)
L.grid(row=1,column=1)

L1= tk.Label(top1, width=30,bg="grey",fg="green", font=('arial', 20),text = "  Data after Stopword Removed   ")
L1.grid(row=2,column=1)



ErL1=tk.Label(top1,text="",fg="white",justify=tk.LEFT,padx = 10,bg="grey",textvariable=error1)
ErL1.grid(row=4,column=1)



b6= tk.Button(top1,bg="black",fg="green",text="Perform Analytics",bd=8,command=search)
b6.config(width="30")  
b6.grid(row=5,column=1)

top1.mainloop()
