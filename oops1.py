'''
OBJECT ORIENTED PROGRAMMING(OOPS)

OOPS CONCEPT : 
Till now we have discussed procedural way of programming.

procedural  programming: function oriented 

Now we are going to discuss object oriented programming.

object oriented programming.developed through classes
object oriented programming: classes oriented

There is nothing in special and new in  oops ,just its a mind game.
In actual our target is to divide the programs in different structure..

So that we can reduce the complexity in the program.
and make the project scalable so that in future we can easiley make the changes .
in the program..

If we have a small project having 1 lakh lines of codes and we want to make the changes in it,then
it is easily posible only if our program is divided into small structures, small layers,small modules..

Small size structure : functions
Medium size structure : Classes
Big  size structure : Modules

# Class:
    1. Blueprint of objects
    2.Is a data type
    3.logical entity having attributes and methoods ie
    4.Class is a collection of properties,ie collection of methods and variables
    5.We can represent real time entity through class
    6.Clss defines structure and behavior of an object.
    7.Class is a collection of hetrogeneous data types.

We can understand class like a dictionary ,just syntax is different
Customer is coleection of id,name,age,mob,city, state,gender
id int
name str
age int
mob int
city str
state str
gender str

# How to access methods(functions) of list:
l=[10,20,30]
l.append(200)
Syntax is
variable_name.method_name(arguments)
object_name.method_name(arguments)

Syntax to create a class:

Class Class_name:
    collection of methods and variables

    
Syntax to create aobject of a class:
obj_name=Class_name(arguments)

How variables are created in python ?
By assigning the values.
There is one  more syntax to create default variables
with default values
obj_name=Class_name(arguments)

When we print  variables general predefined data types int,float str ,tuple dict etc
Then its values are printed but if we print objects of user defined data types.then its addresses are printed.
'''
# x=5
# print(x,type(x))
# x=int()
# print(x,type(x))
# x=list()
# print(x,type(x))
# x=list("Cetpa      getpa")
# # print(x,type(x),len(x))

# class C2:
#     pass
# x=C2()
# print(type(x))




'''most important thing in opps jo hum likhne ja rhe hai..

l1=[10,20,30]
l2=[10,20,30]
l1.append(33)
print(l1)
:..Is program me l1 append hoga ya l2 append hoga ..
To anwer hai l1 append hoga ..
matlab jaha pr append method ja rha hai (list class ke andr) to yaha
se us append method me kya kya ja rha hai to answr is l1 and 33.
to waha pr 2 argument pahuch rhe hai, jaha actual append method bna hoga uske braket me 2 argument hone chahiye,
pahle argument me l1 aur dusre me 33 (komn sa function hua ye required argument function)
To jb methods bante hai class ke andr to waha pr agr 2 argument hai to calling ke time pr hum 1 argument bhejte hai,,
Ek to object khud ja rha hota haipahle argument ke saath..



# '''
# l1=[10,20,30]
# l2=[10,20,30]
# l1.append()
# print(l1)

# l1=[10,20,30]
# l1.clear()
# print(l1)

# class MyClass:
#     def myMethod(a):
#         print("Hello oops bhai")
#         print("Hello oops bhai")
#         print("Hello oops bhai")
#         print("Hello oops bhai")
#         print("Hello oops bhai")

# object1=MyClass()
# object1.myMethod() # yha pr bracket me kitne argument dene hai 0 kuki object1 hai vo pahle argument ke pass jayega 
                    # (pahle ke paas address jata hai) 
                    # jb bhi hum kisi method ko coll krenge to pahle argument ke paas object jayega aur rest of 
                    # argument aage apke braket me pass ho jayenge)
                    #python recommend jo class ke andr method bna rhe ho pahle argument ka name self do
                    # lekin vo convencial hai rule nhi hai



class MyClass:
    def myMethod(self,a,b):
        print(self,a,b)
        

object1=MyClass()
object1.myMethod(3,5)   # self=object1,a=3,b=5 in background formal parameter=actual parameter
print(object1)          # object1 print krenge to whi address print hoga jo self me hoga
                        # jo 3 print krne pr hoga wahi a print krne pr hoga
                        # jo 5 print krne pr hoga wahi b print krne pr hoga
                        # to int print krne pr value print hoti hai
                        # to int print krne pr value print hoti hai
                        # Aur userdefined class ke object print krne pr uski address print hoti hai

# print(self)           # Eroor ,self is a local (object ) value is only in the class not outside class..

"""
..>Class is a collection of proprerties or attributes which means variables and methods (functions).


Syntax to create a class:


Class Class_name:

    set of statements( variables and methods)

Syntax to create a class:

obj_name=Class_name(arguments)

Syntax to call a method(function) developed inside class:


obj_name.method_name(arguments)


"""
#when we call a method then object is pas to first argument of method.
# python recommends the name of 1st argument ie first formal parameter inside a method should be self.
# once we call a method then object of class is pass to self.
# so if there are n arguments as formal parameter inside a methods ,then 1st argument shi=ould be self.
#At time of  calling this method , in actual parameters in bracket of method calling,we pass n-1 actual parameters.

