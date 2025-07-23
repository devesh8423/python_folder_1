# 2 nd class object oriented programming ....oops
'''oops concept'''

# class MyClass:
#     def MyFunction(self):
#         print("cetpa",self)

# obj1=MyClass()  # obj1 address 1000
# obj2=MyClass()   # obj2 address 2000
# print(obj1)                                                                
# print(obj2)                                                             
# obj1.MyFunction()
# obj2.MyFunction()


# New program
# How to creates variables inside class..
'''
So there are two types of functions(methods) and two types of variables which can we defined inside class.
..>Till now,we have discussed instance methods./object methods.these
   methods are made like functions we make outside class.

   
..> Now we are talking about instance/object variables.
...> How to create instance variables inside class: like we were making dictionary,if we want to make
    one dictionary for 1 customer similarly we can makeone object for 1 customer..
    One dictionary of one customer may look like
cust1_dict={"id:10,"name":"devesh",age:39,"mobile":1234}


Another cust:

cust2_dict={"id:20,"name":"sarvesh",age:30,"mobile":6234}

How to access a particular data of a particular/customer from dictionary
cust1_dict["id"] ie by passing key to dictionary variable or dictionary object..


Now similar concept happen in oops also , but syntax is slightly 
different.till now how variables were define in python..?
by assigning the value..

BUt in oops to create variables, firstly we need to create the objects.


Like cust1_dict and cust2_dict are representing two different customers
similarly two objects of user defined customer class or any class will represent two different customers.

To create instance variables inside customer class,then we firstly create a constructur.

constructor: is a method inside class, which is called automatically every time we create a new object of the class.
In python the name of constructor is fixed ie__init__ .so all instance variables generally we create inside a constructor..

Syntax to create variables with objects :
obj_name.variable_name=default_value

obj_name inside class is self.

How to access a variable
obj_name.var_name

#All user defined classes are mutable 



# How to modify a variable.
obj_name.var_name=updated_value
# mutable data types: list dict set and all user defined classes

Class calculatoe:
    pass When we create our cal using functional programming the 4 variables are present no1,no2,choice,output
'''
# #New program
# class Class1:
#     def __init__(self):     # self=obj1
#         self.id=0
#         self.name="" 
#         self.age=0
#         self.mob=0
# obj1=Class1()       # self=obj1
# print(obj1.id,obj1.name,obj1.age,obj1.mob)
# obj1=Class1()       # self=obj2,obj2 address 2000

# a="cetpa"
# a=list(a)
# print(a)

# def func1(self):
#     self.append(10)
#     self.append(12)
#     self.append(12)

# # l1=list()
# # func1(l1)
# # print(l1)
# # x=complex()
# # print(type(x))
# NEw program
import math
class Calculator:

    def __init__(self):
        self.no1=0
        self.no2=0
        self.choice=0
        self.res=0
    def add(self):
        self.res=self.no1+self.no2
    def sub(self):
        self.res=self.no1-self.no2
    def mul(self):
        self.res=self.no1*self.no2
    def div(self):
        self.res=self.no1/self.no2
    def mod(self):
        self.res=self.no1 % self.no2
    def pow(self):
        self.res=self.no1**self.no2


# while(1):
    
cal1=Calculator()    #cal1=self,cal1.no1=0,cal1.no2=0,cal1.choice=0,cal1.res=0
cal1.no1=int(input("Enter first no: "))
cal1.no2=int(input("Enter second no: "))
cal1.choice=input("Enter your choice +,-,*,/,%,pow,log: ")
if (cal1.choice=="+"):
    cal1.add()
    print("result:",cal1.res)
elif (cal1.choice=="-"):
    cal1.sub()
    print("result:",cal1.res)
elif (cal1.choice=="*"):
    cal1.mul()
    print("result:",cal1.res)
elif (cal1.choice=="/"):
    cal1.div()
    print("result:",cal1.res)
elif (cal1.choice=="log"):
    cal1.res=math.log(cal1.no1,cal1.no2)
    print("result:",cal1.res)
elif (cal1.choice=="%"):
    cal1.mod()
    print("result:",cal1.res)
elif (cal1.choice=="pow"):
    cal1.pow()
    print("result:",cal1.res)






# class C1:
#     def __init__(self):  # self addr 1000
#         self.a=1            # 1000.a=1
#         self.b=2            #1000.b=2
#     def myMethod1(self):                # self=1000,self.a=10,self.b=2
#         print(self.a,self.b)              # 10,2
#         self.a+=1                          # self.a=11
#         self.b=20                           # self.b=20
#         print(self.a,self.b)                # 11,20
# obj1=C1()                        # obj1 address 1000 obj1.a=1,obj1.b=2
# obj1.a=10                        # obj1 address 1000
# obj1.myMethod1()
# print(obj1.a,obj1.b)          #11,20



# New program
# class cll1:
#     def __init__(self):
#         print("Object is created")
# obj1=cll1()
# obj2=cll1()
# obj3=cll1()
# obj4=cll1()
# obj5=cll1()