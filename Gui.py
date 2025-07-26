"""
Gui programming in python:

Till now we have discussed  about console programming.
For Gui programming we develop
1.desktop application: Framework:Tkinter
2.web application    : Django,
3.mobile application : Kivy
4.Hardware specific application like GUI in IOT Devices: 



Tkinter: GUI framework in python for desktop application developement.
"""

# import tkinter as tk
# root=tk.Tk()  # root object of tk class
# root.mainloop() # infinite loop

# import tkinter as tk
# root=tk.Tk()
# root.geometry("400x500")

# root.mainloop()
'''
Now we haveto create Widgets on root window 
Widgets like 
Buttton
Entery
Text
Menu
Slider

widgets Geometry: Layout : 3 option
widget .pack() :pack(side)
widget.place()  : place(x,y) in form of pixels
widget.grid()   : grow(row,column) in numbers

pack: side=left right ,bottom,default top


'''
#New program
# import tkinter as tk
# root=tk.Tk()
# root.geometry("400x500")
# btn1=tk.Button(root,text="Button1",bg="red",fg="yellow")
# btn1.place(x=100,y=200)
# btn2=tk.Button(root,text="Button2",bg="Green",fg="Yellow")
# btn2.place(x=150,y=250)

# root.mainloop()

# New program
# import tkinter as tk
# root=tk.Tk()
# root.geometry("400x500")
# btn1=tk.Button(root,text="Button1",bg="red",fg="yellow")
# btn1.pack(side="right")
# btn2=tk.Button(root,text="Button2",bg="Green",fg="Yellow")
# btn2.pack(side="left")

# root.mainloop()

# import tkinter as tk
# root=tk.Tk()
# root.geometry("400x500")  # here the x is small not capital
# btn1=tk.Button(root,text="Button1",bg="red",fg="yellow")
# btn1.grid(row=0,column=0)
# btn2=tk.Button(root,text="Button2",bg="green",fg="yellow")
# btn2.grid(row=1,column=1)
# root.mainloop()

# import tkinter as tk
# root=tk.Tk()
# root.geometry("400x500")
# btn1=tk.Button(root,text="Button1",bg="red",fg="yellow")
# btn1.grid(row=0,column=0)
# btn2=tk.Button(root,text="Button2",bg="Green",fg="Yellow")
# btn2.grid(row=1,column=1)

# root.mainloop()


# import tkinter as tk
# root=tk.Tk()
# root.geometry("400x500")  # here the x is small not capital
# btn1=tk.Button(root,text="Button1",bg="red",fg="yellow",width=15,height=3,row=0,column=0)
# btn1.grid(row=0,column=0)
# btn2=tk.Button(root,text="Button2",bg="green",fg="yellow")
# btn2.grid(row=1,column=1)
# root.mainloop()

'''GUI programming is an event basd programming
EVENT: An Action .action performed.
Events are the input provide by users of machines
How we create event Handlers:sung functions:
Events in GUI programming:
mouse:
left click
left double click
left Triple click
left click Release
.
right
.
middle click...
.
left clicked and mouse move.
.
without click mouse move

keyword Events:
Any key or combination of keys pressed single or multiple
times can have different events.

Important events for our program are where we call the handler(function )
Once the event occurs,where we want to perform some particular action if event fires.
+

'''
'''
GUI programming is a event based programming ,where actions take place one an important event is fired.
Actions against events are handled by/managed by handlers.
Event handlers are also called sub-routine or call-back functions
or also called handlers.
# '''
# #New program
# import tkinter as tk
# def handler1():
#     print("Cetpa")
# root=tk.Tk()
# root.geometry("500x400")  # here the x is small not capital
# btn=tk.Button(root,text="Submit",height=3,width=20,font=1,bg="yellow",command=handler1)
# btn.pack()
# root.mainloop()

#New program

# import tkinter as tk
# def handler1():
#     print("Button one is clicked")
# def handler2():
#     print("Button TWO is clicked")
# def handler3():
#     print("Button Three is clicked")
# root=tk.Tk()
# root.geometry("500x400")  # here the x is small not capital
# btn1=tk.Button(root,text="Submit1",height=3,width=20,font=1,bg="yellow",command=handler1)
# btn1.grid(row=0,column=0)
# btn2=tk.Button(root,text="Submit2",height=3,width=20,font=1,bg="orange",command=handler2)
# btn2.grid(row=0,column=1)
# btn3=tk.Button(root,text="Submit3",height=3,width=20,font=1,bg="yellow",command=handler3)
# btn3.grid(row=0,column=2)
# root.mainloop()

'''Label widget: Like print functionie to display some text directly on scrren ie root window.'''

#New program
# import tkinter as tk
# root=tk.Tk()
# root.geometry("500x400")
# lb1=tk.Label(root,text="Good morning, how are you?",font=1,fg="blue")
# lb1.grid(row=0,column=0)
# root.mainloop()

'''Entry Widget: To take from user in text format in single line
Like input function of console. like input function we take data from
user and save it in some variable.

But in GUI programming , we can define the type of data , input by user.
ie till variable is define by passing value.
but in entry widgettkinter, we firstly need to define data type of variable like we define in c language and java.
 '''
# import tkinter as tk
# def handler():
#     # print(name) YE krne pr error ayega islie isko hum variable me rakh lenge string var class me get name ka variable hai jo data deta hai
#     n=name.get()
#     print(n)
# root=tk.Tk()
# root.geometry("500x400")
# name=tk.StringVar()
# entr1=tk.Entry(root,font=1,textvariable=name)
# entr1.grid(row=0,column=0)
# btn=tk.Button(root,text="Submit",font=1,command=handler)
# btn.grid(row=1,column=1)
# root.mainloop()


"""New program"""
# from tkinter import *
# def addCustomerhandler():
#     id=varid.get()
#     name=varname.get()
#     print(id,name)
# root=Tk()
# root.geometry("500x400")
# lblid=Label(root,text="Enter your ID",font=1)
# lblid.grid(row=0,column=0)
# lblname=Label(root,text="Enter your name",font=1)
# lblname.grid(row=1,column=0)
# varid=IntVar()
# entid=Entry(root,font=1,textvariable=varid)
# entid.grid(row=0,column=1)
# varname=StringVar()
# entname=Entry(root,font=1,textvariable=varname)
# entname.grid(row=1,column=1)
# btn_addcust=Button(root,text="Add Cust",font=1,command=addCustomerhandler)
# btn_addcust.grid(row=2,column=1)

# root.mainloop()
# path = r"C:\Users\deves\Desktop\Data analytics\mycsv1.csv"
# f = open(path, "r")
# d = f.read()
# print(d)
# f.close()

# f=open("d://temp/myexcel.xls","w")
# data="id\tname\tage\n10\tDevesh\t22\n20\tsarvesh\t24"
# f.write(data)
# f.close()
'''String formating'''
# a=input("Enter your name: ")
# b=input("Enter your age: ")
# print(f"my name is {a} and my age is {b}")

# from tkinter import *
# def handler():
#     print(var.get())
#     var.set("")
# root=Tk()
# root.geometry("500x400")
# lbl=Label(root,text="Enter Your Name",font=1)
# lbl.grid(row=0,column=0)

# var=StringVar()
# enr=Entry(root,textvariable=var,font=1)
# enr.grid(row=0,column=1)

# btn=Button(root,text="Submit",font=1,command=handler)
# btn.grid(row=1,column=0)

# root.mainloop()


