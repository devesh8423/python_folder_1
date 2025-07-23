


"""MODULE"""

'''
Whenever we access a module, the complete module is executed automatically
But generally we want that if we are accessing a module from outside then its bll should only be called because
pl is made local for that module only.

'''


'''
There can be few packages which can have subpackages inside it:
Syntax:
import package_name
import package_name.subpackage_name
import package name as alias_name
from package_name imort *
from package name import feature_name
from package name import feature_name as alias_name

'''

# import module1

'''When we want only call bll not pll then we pass in a condition
if(__name__=="__main__): 
now all the pll layer..

'''
# a=2
# b=9
# c=module1.func1(a,b)
# print(c)

# print(__name__)
# Here output is __main__
# import module1
# print(module1.__name__)
'''In all your future progam ,
YOU will add one extra statement in your pl that willl keep the complete pl code inside 
if(__name__=="__main__"):
pass
# '''
# import sys
# print(sys.path)
# print(len(sys.path))
# sys.path.append("D://temp")
# print(len(sys.path))
# import module9
# print(module9.func1(2,99))

# import sys
# print(sys.path)
# print(len(sys.path))
# sys.path.append("D.//temp")
# print(sys.path)
# print(len(sys.path))
# import module_name
# print(module_name.FUNCTIONNAME(VALUE1,VALUE2))

'''Category of functions 
1.Required argument functions..>

..Till now the different functions we created were required argument functions
..In this function actual and formal parameters are same..

2.Key word Argument function..>
Formal parameter becomes like keywords (keys) actual parameters becomes values,
In this category ,no of  arguments in formal and actual should be same.
Sequence not matters here..
While calling the function. we specify formal=actual parameter

3.Default argument function:
Where actual parameter is optional to pass. in this case we provide a default  value
to Formal parameters. at the time of calling.

At the time of calling ,if we pass value through actual then actual value is considered
otherwise  default value is considered..


4.Variable length arguments Function:
..> Length of arguments means no of arguments are not fixed..
For this we define one variable in formal and add * before it.

Python recommends that the name of the variable should be * args that is variable length arguments.
Here data will be received from actual in a tuple..
Taking variable name as args is recommendation / convention but not compulsion by python


5.Variable length Keyword arguments Function:
..> Length of arguments means no of arguments are not fixed..
For this we define one variable in formal and add ** before it.

Python recommends that the name of the variable should be **kwargs that is variable length Keyword arguments.
Here data will be received from actual in a Dictionary..
While calling, we can take any names for formal parameters to use as the keywords
Taking variable name as kwargs is recommendation / convention but not compulsion by python

6.Lambda Function:
..>Lambda Function are anonymous function written in single line or single expression..
..>To call a lambda function , we can pass or assign labda function to a variable..





'''

# 2.Key word Argument function..> Example
# def sub(a,b):
#     r=a-b
#     return r

# n01=20
# n02=15
# s=sub(a=n01,b=n02)
# print(s)

# 3.Default argument function..>Example

# def add(a=1,b=3):
#     c=a+b
#     return c
# v=12
# u=5
# r1=add(u,v)
# r2=add(v)
# r3=add(b=u)
# r4=add()
# print(r1,r2,r3,r4)

# 4.Variable length arguments:  Example *args 
# def Func1(*m):
#     return m
# u,v,w,x,y,z=1,2,3,4,5,6
# r1=Func1(u,v)
# r2=Func1()
# r3=Func1(u,v,w,x,y,z)
# print(r1)
# print(r2)
# print(r3)

#variable length add function..
# def add(*args):
#     c=0
#     for i in args:
#         c=c+i
#     return c

# c=9
# v=9
# x=9
# z=99
# s=90000
# r1=add(c,v,x,z,)
# print(r1)

# def mul(*args):
#     r=1
#     for i in args:
#         r=r*i
#     return r
# c=9
# x=8
# z=1
# r1=mul(90,0)
# print(r1)

# print(type(r1))

# def func1(**kwargs):
#     print(kwargs)
# fun=func1(id=12,name="Devesh",age=23,mob="8957")


# 6.Lambda Function: Example..
# lambda a,b:a+b

# print(lambda a,b:a+b)
# print(type(lambda a,b:a+b))
# x=5
# print(x)

# print(type(x))
# def add(a,b):
#     return a+b

# print(add)
# print(type(add))

# def add(a,b):
#     return a+b
# abc=add     # in python all variables are reference type 
# # print(abc)

# r=abc(4,5)
# print(r)
# r1=add(4,5)
# print(r1)

# add3=lambda a,b,c:a+b+c
# s=add3(3,4,50)
# print(s)





