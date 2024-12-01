import tkinter as tk
top=tk.Tk()
top.geometry("400x400")
showerr1=tk.StringVar()
showerr2=tk.StringVar()
def click():
    #-------------Name validation-------
    username=name.get().strip()
    if(len(username)==0):
        showerr1.set("Enter Valid Name")
    else:
        showerr1.set(" ")
    if(username.isalpha()):
        showerr1.set(" ")
    else:
        showerr1.set("Enter Valid Name")

    #-------------Contact Number----------
    getcontact=contact.get()
    print(len(getcontact))
    if(len(getcontact)!=10):
        showerr2.set("Enter Valid Number")    
    else:
        if(getcontact.isdigit()):
            showerr2.set("")
        else:
            showerr2.set("Enter Valid Number")
            
        
            
            
#--------------Name --------------------------------
L1=tk.Label(top,text="Enter your name")
L1.grid(row=0,column=1)

name=tk.Entry(top)
name.grid(row=0,column=2)

err1=tk.Label(top,fg="red",textvariable=showerr1)
err1.grid(row=1,column=2)

#----------------------Contact Number--------------
L2=tk.Label(top,text="Enter Your Contact Number")
L2.grid(row=2,column=1)

contact=tk.Entry(top)
contact.grid(row=2,column=2)

err2=tk.Label(top,fg="red",textvariable=showerr2)
err2.grid(row=3,column=2)



b1=tk.Button(top,text="submit",command=click)
b1.grid(row=4,column=2)

top.mainloop()
