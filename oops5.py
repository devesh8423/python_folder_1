# # New program
# class c1:
#     def __init__(self):
#         self.a=1
#         self.b=2

#     def showdata(self):
#         print(self.a,self.b)

# class c2(c1):
#     def __init__(self):
#         self.c=3
#         self.d=4

# ob=c2()
# ob.showdata() # Error 

# New program

#Overriding is allowed ie same function name in both parent and child.
# IF we are calling the function through child object then priority 
# will we givven to child function or method.
# class c1:
#     def myMethod(self):
#         print("I am in class c1:")
# class c2(c1):
#     def myMethod(self):
#         print("I am in class c2:")

# ob=c2()
# ob.myMethod()

'''This is concept of overriding'''
# New program

# class c1:
#     def myMethod(self):
#         print("I am in class c1:")
# class c2(c1):
#     pass

# ob=c2()
# ob.myMethod()


# New program
'''Complete Inheritance..>Accessing the properties of parent class'''

# Till now we have discuss,
'''
Syntax to coll a Instance method..
obj_name.method_name()

#There is another syntax to coll a instance method..

clas_name.method_name(object,other arguments)


'''
# New program
# class c1:
#     def myMethod(self):
#         print("I am in class c1:")
# obj=c1()
# obj.myMethod()
# c1.myMethod(obj)

# New program

# class c1:
#     def myMethod(self):
#         print("I am in class c1:")
# class c2(c1):
#     def myMethod(self):
#         print("I am in class c2:")

# ob=c2()
# ob.myMethod()
# c1.myMethod(ob)
# c2.myMethod(ob)


# New program
# class c1:
#     def __init__(self):
#         self.a=1
#         self.b=2
# class c2(c1):               # incomplete inheritance only access methods not variables           
#     def __init__(self):
#         self.c=3
#         self.d=4
# ob=c2()
# print(ob.a)                  #AttributeError: 'c2' object has no attribute 'a'

# New program

# class c1:
#     def __init__(self):
#         self.a=1
#         self.b=2
# class c2(c1):                     
#     def __init__(self):
#         self.c=3
#         self.d=4
#         super().__init__()                     # represent immidiate parent{() lagane se object bn jayega .__init__()
# ob=c2()
# print(ob.a,ob.b,ob.c,ob.d)                      #Complete inheritance


# To Achieve inheritance in python ,
# 1.Mention prent class name in  bracket of child class name
# 2.call parent constructor inside child constructor 
#  super().__init__()
# parent_class.__init__(self)

# New program
# class c1:
#     def __init__(self):
#         self.a=1
#         self.b=3
# class c2(c1):
#     pass
# obj=c2()
# print(obj.a)

# New program

# class c1:
#     def __init__(self):
#         self.a=1
#         self.b=3
# class c2(c1):
#     def __init__(self):
#         self.c=3
#         self.d=4
#         # super().__init__()
#         c1.__init__(self)
# obj=c2()
# print(obj.a)

# New program
# class c1:
#     def myMethod(self):
#         print("I Am in class C1")
# class c2(c1):
#     def myMethod(self):
#         print("I Am in class C2")
#         super().myMethod()
# ob=c2()
# ob.myMethod()


# New program:
# class c1:
#     def __init__(self,a,m):
#         self.a=a
#         self.b=m

        
# ob=c1()  #ob.__init__() ob=self
# TypeError: c1.__init__() missing 2 required positional arguments: 'a' and 'm'

# New program:

# class c1:
#     def __init__(self,a,m):     # parameterised constructor
#         self.a=a
#         self.b=m

        
# ob=c1(2,3)
# print(ob.a,ob.b) 

# x="5"
# x=int(x)  # calling a parameterised constructor
# c=2
# print(list(c))

# # New program:

# class c1:
#     def __init__(self,a=1,m=2):     #Default  parameterised constructor
#         self.a=a
#         self.b=m
#         # print(self.a,self.b)
        
# ob=c1(2,3)
# print(ob.a,ob.b) 
# ob1=c1()
# print(ob1.a,ob1.b)

# # x="5"
# # x=int(x)  # calling a parameterised constructor
# # c=2
# # print(list(c))

# New program:
"""
Syntax to create object of a class
obj_name=class_name(parameter for constructor)

"""


'''
TYPES OF Inheritance:
1.Single level Inheritance
2.Multi level Inheritance
3.Multiple Inheritance
4.Hierarichal Inheritance
5.Hybrid  Inheritance

'''

'''

1.Single level Inheritance..>One child having one parent..


2.Multi level Inheritance...> One parent having one  child,child having another child,another child having another child..


3.Hierarchial  Inheritance..> One parent multiple childeren


4.Multiple Inheritance..> One child multiple parent (In java this is called Dimond Problem)
                        Java does not support multiple inheritance due to ambiguity in java interface concepts are build..
                        But in python method reolution order/method resolution operator/variable is designed which suggest that which method 
                         will called  in case of ambiguity.
                         MRO  

                # If we have multiple parent at same level, then first parent method will be given priority which is mention
                in bracket of child class.
                        


5.Hybrid Inheritance..> Hybrid inheritance where two are more inheritance are combined


# In python all predefined and even user defined classes have one common parent class ie 
object class.


# In python whenever we interact with the user ie in print function or input function , data is travelled in string format only..

print(500) # here 500 will be firstly converted to str

ie whenever we print any arguments using print  function all the arguments are firstly  passed to __str__method,
this method convert the input in str format and then These string are printd uusing print method on screen. 

Due to this method when we print different types of data then values are printed in different formats 

# har class ke ek bydefault class hai jo hai parent class
'''
#New program

"""2.Multi level Inheritance... One Parent having one child ,one child having another child And another having another child"""# class c1:
#     def __init__(self):
#         self.a=1
#     def myMethod(self):
#         print("I am in class c1")

# class c2(c1):
#     def __init__(self):
#         self.b=2
#         super().__init__()
#     def myMethod(self):
#         print("I am in class c2")
# class c3(c2):
#     def __init__(self):
#         self.c=3
#         super().__init__()
#     def myMethod(self):
#         print("I am in class c3")
# obj=c3()
# print(obj.a,obj.b,obj.c)
# obj.myMethod()

#New program

"""2.Multi level Inheritance... One Parent having one child ,one child having another child And another having another child"""

# class c1:
#     def __init__(self):
#         self.a=1
#     def myMethod(self):
#         print("I am in class c1")

# class c2(c1):
#     def __init__(self):
#         self.b=2
#         super().__init__()
#     # def myMethod(self):
#     #     print("I am in class c2")
# class c3(c2):
#     def __init__(self):
#         self.c=3
#         super().__init__()
#     # def myMethod(self):
#     #     print("I am in class c3")
# obj=c3()
# print(obj.a,obj.b,obj.c)
# obj.myMethod()

#New program

'''3.Hierarchical  Inheritance..> One Parent having Multiple Child'''
# class c1:
#     def __init__(self):
#         self.a=1
#     def myMethod(self):
#         print("I am in clas C1 !")
# class c2(c1):
#     def __init__(self):
#         self.b=2
#         super().__init__()
#     def myMethod(self):
#         print("I am in clas C2 !")
# class c3(c1):
#     def __init__(self):
#         self.c=3
#         super().__init__()
#     def myMethod(self):
#         print("I am in clas C3 !")
# class c4(c1):
#     def __init__(self):
#         self.d=4
#         super().__init__()
#     # def myMethod(self):
#         # print("I am in clas C4 !")
# obj=c4()   # yaha per 2 variable banenge ek parent aur ek child hai ek c4 bnega aur ek c1 ..
# print(obj.a,obj.d)
# obj.myMethod()

#New program
"""4.Multiple Inheritance..> one child having multiple parents (In java this is called dimond problem)"""
# class c1:
#     def __init__(self):
#         self.a=1
#     def myMethod(self):
#         print("I am in class c1")
# class c2:
#     def __init__(self):
#         self.b=2
#     def myMethod(self):
#         print("I am in class c2")
# class c3:
#     def __init__(self):
#         self.c=3
#     def myMethod(self):
#         print("I am in class c3")
# class c4(c1,c2,c3):                     # first priority ig given to the manner parents are writen (c1,c2,c3) in l to r priority is given
#     pass
#     def __init__(self):
#         self.d=4
#     def myMethod(self):
#         print("I am in class c4")
# ob=c4()
# # print(ob.b)
# ob.myMethod()                       # MRO: method resolution order

# print(c4.__mro__)

# New program

# class c1:
#     def __init__(self):
#         self.a=1
#     def myMethod(self):
#         print("I am in class c1")
# class c2:
#     def __init__(self):
#         self.b=2
#     def myMethod(self):
#         print("I am in class c2")
# class c3:
#     def __init__(self):
#         self.c=3
#     def myMethod(self):
#         print("I am in class c3")
# class c4(c1,c2,c3):                     # first priority ig given to the manner parents are writen (c1,c2,c3) in l to r priority is given
#     def __init__(self):
#         self.d=4
#         super().__init__()
#         c2.__init__(self)
#         c3.__init__(self)
#     def myMethod(self):
#         print("I am in class c4")
# ob=c4()
# # print(ob.b)
# ob.myMethod()                       # MRO: method resolution order
# print(ob.a,ob.d,ob.b,ob.c)
# # print(c4.__mro__)

# l=[10,22,23]
# s=str(l)
# print(s)
# print(len(s))
# l2=[10,22,23]
# print(len(l2))

# New program
# class customer:
#     def __init__(self,id,name,age,mob):  # this is parameterised constructor
#         self.id=id
#         self.name=name
#         self.age=age
#         self.mob=mob
# cus=customer(10,"Devesh",23,8957232425)
# print(cus.id,cus.name,cus.age,cus.mob)

# New program
# class customer:
#     def __init__(self,id,name,age,mob):  # this is parameterised constructor
#         self.id=id
#         self.name=name
#         self.age=age
#         self.mob=mob
#     def __str__(self):
#         id="Id:"+str(self.id)
#         name=" Name: "+str(self.name)
#         age=" Age: "+str(self.age)
#         mob=" Mob: "+str(self.mob)
#         r=id+name+age+mob
#         return r
# cus=customer(10,"Devesh",23,8957232425)
# # print(cus.id,cus.name,cus.age,cus.mob)
# print(cus)

# l1=[10,20,30]
# l2=l1.__str__()
# print(type(l2))
# print(len(l2))
# print(l2)

#New program
"""HRMs: Human resource management system
Employee properties:  id,name,age,mob

Designations: 
manager properties:  Id,name,age,mob,branch

Trainer : id,name,age,cource
Director :  id,name,age,mob,share

Add Employee method
Search employee method
delete employee method
modify employee method
display all employee method
exit

class :
employeee,init,variables,id,name,age,mob
manager,1 variable branch 

"""
