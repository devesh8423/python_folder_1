"Customer management system using oops:"

# Business logic layer:

# class Customer:
#     cus_list=[]
#     def __init__(self):
#         self.id=0
#         self.name=0
#         self.age=0
#         self.mob=0

# # presentation layer
# print("Welcome to Customer management system")
# while(1):
#     cus=Customer()
#     ch=input("Enter Choice: 1 Add, 2 Search, 3 Delete, 4 modify, 5 Display, 6 Exit")
#     if ch=="1":
#         cus.id=input("Enter cust Id: ")
#         cus.name=input("Enter cust Name: ")
#         cus.age=input("Enter cust Age: ")
#         cus.mob=input("Enter cust Mob: ")
        
# New program

# class Customer:
#     cus_list=[]
#     def __init__(self):
#         self.id=0
#         self.name=0
#         self.age=0
#         self.mob=0
# cus=Customer()
# cus.id=input("Enter cust Id: ")
# cus.name=input("Enter cust Name: ")
# cus.age=input("Enter cust Age: ")
# cus.mob=input("Enter cust Mob: ")
# Customer.cus_list.append(cus)
# print(Customer.cus_list[0].id)
# print(Customer.cus_list[0].name)
# print(Customer.cus_list[0].age)
# print(Customer.cus_list[0].mob)

# cus=Customer()
# # print(cus.id)
# print(type(cus))


# New program
# class customer:
#     cs_ls=[]
# cus=customer()
# customer.cs_ls.append(cus)
# print(customer.cs_ls)
# print(customer.cs_ls[0])

# New program
# class customer:
#     pass
# cus=customer()
# cus.name="devesh"
# print(cus.name)
# cus1=customer()
# cus1.name="sarvesh"
# print(cus1.name)

# # New program
# class Customer:
#     cus_list=[]
#     def __init__(self):
#         self.id=0
#         self.name=0
#         self.age=0
#         self.mob=0
# cu=Customer()    #cus.__init__() formal=actual
# print(cu.id)
# Customer.cus_list.append(cu)
# cu.id=10
# print(Customer.cus_list[0].id)
# print(Customer.cus_list[0].name)
# print(Customer.cus_list[0].age)
# print(Customer.cus_list[0].mob)

# cu1=Customer()
# Customer.cus_list.append(cu1)
# cu1.id=30
# cu1.age=30
# print(Customer.cus_list[1].id)
# print(Customer.cus_list[1].name)
# print(Customer.cus_list[1].age)
# print(Customer.cus_list[1].mob)


"""
OOPS :
Abstraction and Encapsulation

Abstraction: Hiding information..
Encapsulation: Methods and Objects in Single Unit..
Inheritance: InInheriting the properties of parent class by child class..
Why inheritance:To make code reusable

Polymorphism: poly means many morph means form,Polymorphism means many forms.
Twpo types of Polymorphism:
Overloading ..>>Same function name ,with different arguments in same class.
                .python doesnot support python overloading.
                why because. In python everything is at runtime,
                once we define a new function with same name  then previous function is deleted by garbadge collector and
                make its memory free
overriding  ..>> same function name ,with same different arguments in inherited  class or child class.


"""
# New program

# def add(a,b):
#     return a+b
# def add(a,b,c):
#     return a+b+c

# s=add(5,78)
# print(s)

# # New program
# class c1:
#     def myMethod(self):
#         print("My Method1")
# class c2:
#     pass
# obj=c2()
# obj.myMethod()
# # obj=c2()

# # New program

# this is half inheritance ..

# class c1:
#     def myMethod(self):
#         print("My Method1")
# class c2(c1): # c2 child ,c1 parent 
#     pass
# obj=c2()
# obj.myMethod()
# # obj=c2()

# # New program
class c1:
    def __init__(self):
        self.a=1
        self.b=2

    def showdata(self):
        print(self.a,self.b)

class c2(c1):
    def __init__(self):
        self.c=3
        self.d=4

ob=c2()
ob.showdata()  # error