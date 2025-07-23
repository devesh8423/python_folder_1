#function: A block of code designed to perform a specific task
# why functions?
# To make the code reusable
# functions are basic building blocks of modular approach of programming
# functions are the basic building blocks of multi threading..
# functions are the basic building block of layerd architecture
# presentation layer
# business logic layer
# data link layer
# data access layer
# function make the code scalable.

'''
syntax to call a function

function_name(arguments)

synatax to create a function:udf user defined function
def function name(arguments):
    block of code
    return arguments    # return is optional

# if function does not return anything then in puthon

# automatically none type is none is returned

# while calling a function 
# argument passed are called actual parameters

# while creating a function the arguments mentioned inside function are called formal parameters..




'''
# def add(a,b):
#     return (a+b)
# a,b=3,4
# c=add(a,b)
# print(c)

# wap to check whether a no is even number or not

# def even(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# n=int(input("enter any number: "))
# b=even(n)
# print("The entered number is even",b)


# new program for addition of two no
'''
1. presentation layer

2.business logic layer
'''
# ..> write a program for adition of two numbers

# 2.business logic layer

# def add(a,b):
#     return a+b

# 1. presentation layer

# no1=int(input("Enter first number: "))
# no2=int(input("Enter second number: "))
# r=add(no1,no2)
# print("The sum of numbers is :",r)

# how above program will be executed..
'''
1st.. function defintion 
2nd..no1
3rd..no2
4th...r
5th..add function call hoga fir hum function me jayege


'''
'''
1..> use as much comments as possible in your program
2..> minimum #bl,pl,#wht functionality going to implement

3..> use logical identifiers users defined names..
4..>


'''
'''
1, the variables which are defined inside function are local variable..

1, the variables which are defined  outside function are global variable..

global variables...> means these variables can access globally  that is outside function and inside function.
'''
# def fun1():
#     a=5

# new  : these are required argument function..
# iska matlb jitna formal parameter de rhe ho utna actual parameter me dena padta hai..

# def add():
#     r=a+b
#     return r
# a,b=9,8
# r=add()
# print(r)


# two important thing that is 

#business logic layer # approach 1 without passing arguments
# def add():
#     r=a+b
#     return r
# #presentation layer
# a,b=2,3
# r=add()
# print(r)

# # another function is same 

# #business logic layer   # approach 2 with passing arguments
# def add(a,b):
#     r=a+b 
#     return r
# #presentation layer
# c,b=2,3
# r=add(a,b)
# print(r)


# approach 2 with passing arguments is better because it makes the code reusable
# 2nd approch can be used with different different parameter..


# add function
#business logic layer
# def add(a,b):
#     r=a+b
#     return r
# a,b,c,d,e,f=1,2,3,4,5,6
# a1=add(a,b)
# a2=add(c,d)
# a3=add(e,f)
# print(a1,a2,a3)

'''if local and global variables have same name then the priority is gave to local variable.'''
# def fun():
#     a=5
#     print(a)
# a=6
# print(a)
# fun()
# print(a)

# if we want to ccess and modify global variable inside function then we need to use global keyword

# def fun():
#     global a
#     a=5
#     print(a)
# a=6
# print(a)
# fun()
# print(a)

# new program

# def fun():
#     global a
#     a=5
#     print(a)

# fun()
# print(a)

# new program


# wap check whether fst character and last character of string is same or not

# business logic layer

# def check(n):
#     if (n[0]==n[-1]):
#         return "yes"
#     else:
#         return "false"


# # presentation layer

# a=input("Enter any string: ")
# res=check(a)
# print("fst and last character are same :",res)

# 

# LOOPS: loops Are use to run the block of code repeatdly..
# To run the code again and again for finite number of times or infinite number of times..

# types of loops

# for loop

# while loop
'''
main syntax for loop:
for element in iterator:
    set of statements

another varient that is set of main syntax for lop:
    for index in range():
    set of staements

'''
# multi element data types are iterators
# s="welcome"
# for i in s:   
#     print(i)
# print("End of loop")

# new program
# s=[11,22,33,44]
# for i in s:   
#     print(i,end="")
#     print("*")
# print("End of loop")
# new program
# s=[11,22,33,44]
# for i in s:   
#     print(i,end="")
#     print("*",end="")
# print("End of loop")

# on which for loop will be executed is an iterator

# new program:


# loops program level 1:  print a series that isaccess elements of an iterator..
# :ex1:
# for i in range(2,21,2):
#     print(i) 

# print a table where input by user
# n=int(input("Enter no: "))
# for i in range(1,11):
#     print(f"{n} X {i}={i*n}")

# # another way
# n=int(input("Enter no: "))
# for i in range(n,(n*10+1),n):
#     print(i)

# another way
# n=int(input("Enter no: "))
# for i in range(10):
#     t=(i+1)*n
#     print(t)

#print cube
# for i in range(2,14):
    # t=i**3
    # print(t)

# for i in range(-9,-1,1): # no error because of slicing
    # print(i)
# print square of the element of the list
# l=[10,20,30,40,50]
# for i in l:
    # print(i**2) # or print(i*i)


# for i in range(1,1.4,0.1): # eroor because the index are integer values 
    # print(i)

# Access the elements of a string and convert them into capital letter
 # without using string methods
# s="ceTpa123"
# for i in s:
#  code=ord(i)
#  if code>=97 and code<=122:
#   code=code-32
#  ch=chr(code)
#  print(ch)

# Access the elements of a string and convert them into small letter
 # without using string methods..

# s="CetpA"
# for i in s:
#     c=ord(i)
#     if c>=97 and c<=122:
#         c=c-32
#     c=chr(c)
#     print(c)
#another way
# s="cetpa"
# for i in s:
#     code=ord(i)
#     if i in "abcdefghijklmnopqrstuvwxyz":
#         code=code-32
#     code=chr(code)
#     print(code)

'''To convert a capital letter to small letter, add 32 in the ascii value of the code.'''
#level 2: perform some operation on all elements or selected elements of an iterator and display the final result..

'''
1..> very important concept of program of loops ios to sum the elements of an iterator

1. run the loop/iterae the loop on iterator..
2. create the table: find the relationship between  term and index/element..
3.write the expression result=result + term..
4. mention step0: initiate the result outside the loop before the start of the loop in such a way that first time 
  the loopruns, result should get the value of first term..
5.terminate the loop by coming out of indentation and print the result..


'''
#simple way
# l=[10,20,30,50]
# for i in l:
#     print(i)
# print("total sum of l",i+i)

# another way.....>

# l=[10,20,30,40,50]
# c=0
# for i in l:
#     c=c+i
# print(c)

# new program..>
# business logic layer
# def myUpper(n):
#     res=""
#     for i in n:
#         i=ord(i)
#         if (i>=97 and i<=122):
#             i=i-32
#         i=chr(i)
#         res=res+i
#     return res
# #presentation layer
# s=input("Enter string: ")
# res=myUpper(s)
# print("String in upper case: ",res)


# new program: sum only even digit of a number input by user
# n=input("Enter any number: ")
# res=0
# for i in n:
#     t=int(i)
#     if t%2==0:
#         res=res+t
# print(res)

# new program: sum only even digit of a number input by user
# BY function   

# BUSINESS LOGIC LAYER
# def sumEven(n): 
#     res=0                         # formal parameter
#     for i in n:
#         t=int(i)
#         if (t%2==0):
#             res=res+t
#     return res


# # PRESENTATION LAYER
# n=input("Enter number: ")
# res=sumEven(n)                            # actual parameter
# print("Sum of even numbers are",res)

# wap to swap commas and in a string..
# sample:"127.0.34,1"
#output:"127,0,34.1"

# s="127.0.34,1"
# s=s.replace(".","*")
# s=s.replace(",",".")
# s=s.replace("*",",")
# print(s)

# new program

# s="22.0,0,9.0,9.9"
# s=s.replace(".","*")
# s=s.replace(",",".")
# s=s.replace("*",",")
# print(s)

# new program
# find all occurences of substring in a given string by ignoring the case.
# str="""welcome to cetpa i am learning python from cetpa. join cetpa for successful career ahead"""" 

# s="""welcome to cetpa i am learning python from cetpa. join cetpa for successful career ahead"""
# substr="cetpa"
# sub="cetpa"
# s=s.lower()
# n=s.count(substr)
# print(n)


#new program for count program

# #  business logic layer
# def count(n):
#     res=0
#     for i in l:
#         res+=1
#     return res




# # presentation layer
# l=[10,20,30,30,40]
# res=count(l)
# print(res)


#new program for count program

#  business logic layer
# def myCount(l,d):
#     c=0
#     for i in l:
#         if (i==d):
#             c+=1
#     return c

# # presentation layer
# l=[10,20,30,30,40,20,80]
# d=10
# res=myCount(l,d)
# print(res)

# new program
# s="cetpa cleients list includes Fiserv,Candence,Samsung,IGT"
# s=s.title()
# print(s)
# s=s.swapcase()
# print(s)

# # new program
# l=[10,20,30,40,50]
# for i in range(len(l)):
#     print(i,l[i])

# new program
# s="Devesh"
# for i in range(len(s)):
#     print(s[i])

# New program
# l=[10,20,30,40,50]
# output=10+20=30 ,20+30=50

# l=[10,20,30,40,50]
# for i in range(len(l)-1):
#     e=l[i]+l[i+1]
#     print(e)


'''
1.nested loops...>
outer loop ntime run, inner loop m times
final statement inside inner loop will be n*m

# '''
# for i in range(3):
#     for j in range(4):
#         print(i,j)
# print("End of loop")

# New program

# l=[1,2,3,4]
# l1=[6,7,8,9]
# for i in l:
#     for j in l1:
#         print(i,j)



# s="devesh is a good boy but some time he is  not good boy he is very bad"
# s=s.title()
# s=s.swapcase()
# print(s)

# l=[10,20,30,40,50]
# for i in range(len(l)):
# 
    # print(i,l[i])

# l=[10,20,30,40,50]
# for i in range(len(l)-1):
#     e=l[i]+l[i+1]
#     print(e)


# l=[1,2,3,4,5]
# l1=[4,5,6,7,1]
# for i in l:
#     for j in l1:
#         print(i,j)

# In function definition jo function kuch return nhi krte hai vo none return krte hai..

'''PATTERN PRINTING'''
'''
*
**
***
****
*****
'''
# MOST IMPORTANT IN LOOPS 

# for i in range(2):
#     print(end="\n")
#     print()    # dono ka matlb same hai chahe hum end="\n" kre ya simple dono new linedete hain..

# n=int(input("Enter number:"))
# for i in range(n):
#     for j in range(n-i):
#         print("*",end="")

#     print()



# l=[22,33,44,55,66,20,30,39]
# for i in range(len(l)-1):
#     a=l[i]+l[i+1]
#     print(a)

# NESTED LOOP
# for i in range(3):
#     for j in range(4):
#         print(i,j)


'''PATTERN PRINTING'''
# print * 5 times'

# for i in range(5):
#     print("**")


# for i in range(5):
    # print("*",end="")

"""
*
**
***
****
*****
"""
# for i in range(5):                # i=0,1,2,3,4
#     for j in range(i+1):          #j=1,2,3,4,5
#         print("*",end="")
#     print()



# n=int(input("Enter number of rows: "))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# a,b,c,d="1234"
# print(b,d)

# l=[[1,2,3,6],[4,5,6,6],[7,7,8,9]]
# for a,b,c,d in l:
#     print(a,b,c,d)

# n=int(input("enter number: "))
# for i in range(n):
#     for j in range(n-i):
#         print("*",end="")    
#     print()



# n=int(input("enter number: "))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print()

'''
     *
    **
   ***
  ****
 *****
******
'''

# n=int(input("Enter number of lines: "))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(i+1):
#         print("*",end="")
#     print()



'''
*        *
**      **
***    ***
****  ****
**********
'''
# n=int(input("Enter no of lines:"))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     for k in range(n+3-i*2):
#         print(" ",end="")
#     for l in range(i+1):
#         print("*",end="")
#     print()

# ANOTHE WAY TO WRITE THIS CODE 

# n=int(input("Enter lines:"))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     for k in range(2*(n-i-1)):
#         print(" ",end="")
#     for l in range(i+1):
#         print("*",end="")

#     print()
'''
A
BB
CCC
DDDD
EEEEE
'''
code=65
# n=int(input("Enter numbers:"))
# for i in range(n):
#     ch=chr(code)
#     for j in range(i+1):
#         print(ch,end="")
#     code+=1
#     print()


# n=int(input("Enter no of lines:"))
# code=65
# for i in range(n):
    
#     for j in range(i+1):
#         ch=chr(code)
#         print(ch,end="")
#     code+=1
#     print()

#NEW PROGRAM
#while loop is exactly similar in functionality to for loop,
# while loop is generally to develop infinite loop
# while loop will only run till the time ,value inside while loop is a true value.
#FALSE VALUE
'''
NONE
0
EMPTY
FALSE
'''
# To exit from for or while loop on some particular condition we can use break key.
# To skip some particular iteration of  loop, we can use continue keyword.
'''
import operator
import math
import operator
import math
while(1):
    no1=int(input("Enter first no: "))
    no2=int(input("Enter first no: "))
    ch=input("Enter your choice +,-,*,/,pow,log,exit:")
    if(ch=="+"):
        print("Result:",no1+no2)

    elif(ch=="-"):
        print("Result:",no1-no2)

    elif(ch=="*"):
        m=no1*no2
        print("Result:",m)

    elif(ch=="/"):
        print("Result:",no1/no2)

    elif(ch=="pow"):

        print("Result:",no1**no2)

    elif(ch=="log"):
        m=math.log(no1,no2)
        print("Result:",m)

    elif(ch=="exit"):
        break
    else:
        print("Incorrect Choice")

'''
#New program: print all element square.don,t want to print element of index 2.
# l=[10,20,30,40,50]
# for i in range(len(l)):
#     if i==2:
#         continue
#     print(l[i]**2)

# New program
# i=0             # lower bound
# while(i<5):     # while(i<upper bound)
#     print(i)
#     i+=1           # increment by step size


# step to make while loop
# 1.initialize the index/variable with lower bound
#2.while(condition)     :index<upper bound or index>upper bound or any condition

#3.inside loop,set of statements,which need to be executed repeatedly
#4.increment or decrement index by step size


# for i in range(2,21,2):
#     print(i)


# i=2
# while(i<21):
#     print(i)
#     i+=2





# def append_len(lst=[]):
#     lst.append(len(lst))
#     return lst

# # print(append_len())
# print(append_len([1, 2, 3]))
# print(append_len())
# print(append_len())

# def append_len(lst=None):
#     if lst is None:
#         lst = []
#     lst.append(len(lst))
#     return lst
# print(append_len([1, 2, 3]))
# print(append_len())
# print(append_len())


# create a function that check the first alnd last item is same or not

# def same(x):
#     if x[0]==x[-1]:
#         return True
#     else:
#         return False
# c=input("Enter Value:")
# print(same(c))

# s=[10,20,30,40,50,60,70]
# for i in s:
#     print(i,end="")
#     print("*")
# print("End of loop")

# Iterator ..> on which loop will be executed is eterator..
# for i in range(1,7,2):
#     print(i)
# range is eterator

# x=range(8)
# print(x)

# y=list(x)
# print(y)

# a=ord("a")
# z=ord("z")
# print(a)
# print(z)
# A=ord("A")
# Z=ord("Z")
# print(A)
# print(Z)

# def myUpper(x):
#     res=''
#     for i in x:
#         t=ord(i)
#         if (t>=97 and t<=122):
#             t=t-32
#         t=chr(t)
#         res=res+t
#     return res
# x="devesh"
# print(myUpper(x))

#Business logic layer
# def myLower(x):
#     r=""
#     for i in x:
#         t=ord(i)
#         if (t>=65 and t<=90):
#             t=t+32
#         t=chr(t)
#         r=r+t
#     return r


# # presentation layer
# x="DEVESH UPADHYAY"
# z=myLower(x)
# print("String in lower case: ",z)