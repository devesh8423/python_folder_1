"""
Object : Is an instance of class..

All variable outside class are static variables.
Inside class ,we can have two types of variables
And two types of methods(functions)



# Inside class variables:

1.Static variable/class variable ..> these variable are fixed for the complete class.

Static variables are created inside class same as ouside class by passing the value.
Static variables are accessed outside class by class name.
class_name.variable_name

variable_name=value

2.Object variable/Instance variable ..> These variables are different variables for different objects

Instance variables are created inside class with object name.
Inside class object name is self.

Syntax to create Instancr variable.
Self.variable_name=value
How to access instance variables outside class
obj_name.variable_name

# Inside class methods:

1.Static method/class method ..>
Static method are created inside class by writing  @staticmethod decorator
before function name.  rest functions is created like outside class.


To access them outside class:
class_name.method_name(Aeguments)

2.Object method/Instance method ..> 

Instance method are created inside class like we create functions 
outside class.

..> first argument inside instance method is self.
To access them outside class:
class_name.method_name(Aeguments)


"""

# Decorator: Decorate the functionality of  functions are also functions:



# How to decide,a method inside class to make static method or instance method:
'''
In static method,objects are not passed inside class.
when in a method ,we dont have a need of object inside class or inside method ,
Then we create static methods.

Still we can access static methods and static variables outside class
using object name(instance name) but we should avoid it.
'''

# New program
# class c1:
#     def myMethod(self):
#         print("inside Instance method",self)
#     @staticmethod
#     def func1():
#         print("inside static method")
# ob=c1()
# ob.myMethod()
# c1.func1()

# New program

# class c1:
#     a,b=5,4                 # Two static variables
#     def  __init__(self):
#         self.a=10           # Instance variables
#         self.b=None          # Instance variables
# print(c1.a,c1.b)
# ob1=c1()
# ob2=c1()
# ob1.a=12
# ob2.a=13
# ob1.b=14
# # ob2.b=15
# print(ob1.a,ob2.a)
# print(ob1.b,ob2.b)


# New program

# Still we can access static methods and static variables outside class
# using object name(instance name) but we should avoid it.

# class c1:
#     def myMethod(self):
#         print("inside Instance method",self)
#     @staticmethod
#     def func1():
#         print("inside static method")
# ob=c1()
# ob.myMethod()
# c1.func1()
# ob.func1()   # it means that sttaic method har ek variable ke liye common chalengee..
#              # so unko hum class name aur object name dono se access kr skte hain.



'''
Static method and static variables behaves like normal functions and normal variables outside class.

Generally developer community says atatic variables and static methods are not property of class
and they class staticmethods as functions.

ie static function inside class ie preferred to be called as functions.
while instance function inside class ie preferred to be called as methods.


Till now whatever methods(functions) we studies in list class,tuple class dict class all were instance methods. 
'''
# # New program

# def add(a,b):
#     return a+b

# class c1:
#     @staticmethod
#     def add(a,b):
#         return a+b
    
# r1=add(4,5)
# r2=c1.add(4,5)
# print(r1,r2)

# in dono me kuch diffeence nhi hai agr class ke bahar to var_name=function_name(arguments)
# aur age class ke and bne hai to var_name.claas_name=function_name(arguments)
# jaha object aati hai waha oops ka koi role hai jaha object aya hi nhi waha oops ka koi role hi nhi.


# # New program
# class c1:
#     x,y=4,5
# o=c1()
# p=c1()
# c1.x=33
# print(o.x,p.x)

# New program
# class c1:
#     a=1
#     def __init__(self):
#         self.b=1
#     def increment(self):
#         c1.a+=1
#         self.b+=1
#         print(c1.a,self.b)
# o=c1()
# o.increment()
# p=c1()
# p.increment()
# q=c1()
# q.increment()




'''Wap to make object counter.the moment a new object is created inside class,
object counter should be printed '''


#New program

# class c1:
#     a=0
#     def __init__(self):
#         c1.a+=1
#         print(c1.a)

# o=c1()
# q=c1()
# a=c1()

#New program


# class c1:
#      c=0
#      def __init__(self):
#             c1.c+=1
#             print("object created by user",c1.c)

# a=c1()
# a=c1()
# a=c1()





