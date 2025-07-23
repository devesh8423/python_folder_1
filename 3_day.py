#operators in python
# arithmetic .>+,-,*,/,%,//,**
# assignment..>
# logical..> and or not
# membership
# identity
# comparison..True and False,==,!=,>=,<=,,<,> used to compare
# bitwise


# a=7
# b=3
# print(a/b)


# a,b=5,3
# print(a/b)
# print(a//b)
# a,b=-5,3
# print(a/b)
# print(a//b)


# lower int deta hai floor division


# user_id=input("Enter user id")
# pwd=input("Enter the pwd")
# print(user_id=="devesh" and pwd=="upadhyay")

# x=5
# y=7
# print(y and x)

# when we used logical operators on  non bool values
# for and 

#logical condition: generaly works on bool values..
#when we used logical operator :if 1st value is false output will be 1st value else output will be second value

# which values ae false values
# 0
# none
# empty
# false

# print(not(False))
# print(not(0))
# print(not(None))
# print(not[])

# x=0
# y=7
# print(x and y)

#AND CASE

# agr first value false hai to output me fst value hi aayega
# ag first value false nhi hai to second value output me ayega


# OR CASE
# x=99
# y=788
# print(x or y)
# agr first value true hai to output me fst value hi aayega
# agr first value true nhi hai to second value output me ayega



# # Bitwise operator
# &   bitwise and  : both inputs bits  1 then output 1
# |   bitwise or   :one inputs bits 1 then output 1
# ~   bitwise not  : toggle. input 1 output 0
# ^   bitwise xor  : both inputs are different then output 1 else output is 0
# <<  bitwise shift left with 0 
# >>  bitwise shift right with sign

# a=5
# b=3
# print(a<<b)

# a=13
# b=3
# print(a<<b)

# assignment operator
# # there are 14 assignment operators

# =  equal to
# +=  plus equal to
# -= minus equal to
# *=  multiply equal to
# %= modulas equal to
# /= divide equal to
# **= exponential equal to
# //= floor divison equal to
# &= and equal to
# |= or equal to
# ^= exor equal to
# <<= shift left equal to
# >>= shift right equal to
# := walrus equal to  pahle inner ko karega fir outer ko  PYTHON 3.8 ME LAUNCH HUA HAI

# print(a:=3) #  yaha pahle inner chala fir outer chalegaa
# pahle expression chalega fir function chalega

# in python all variables are reference type when we assign one variable to another then address of rhs variables is assigned to lhs variable

# a=7
# b=a
# print(a)

# IDENTITY OPERATOR
# IS   RETURNS TRUE IF SAME ADDRESS ELSE FALSE

# IS NOT  RETURNS FALSE IF SAME ADDRESS ELSE FALSE

# ALL VARIABLE IN PYTON ARE REFERENCE TYPE/


# a=4
# b=a
# print(a is b)
# print(id(a),id(b))

# a=4
# b=a
# print(a is not  b)
# print(id(a),id(b))

# membership operator :check whether the element / sub data is part of the main-data or main iterator.
# in  : if member then true else false
# not in :if member then false else true
# l=[10,20,23,44]
# print(10 in l)
# print(10 not in l)

# a,b,c,d,e=1,2,3,4,7
# print(d,end="\t\t")
# print(e)

# a=9
# b=7

# a=3
# b=8
# print(a,b)
# x=a
# a=b
# b=x

# print(a,b)

# till now we have discussed:
'''
1.Operators
2.introduction to data types
3.all variable in python are of reference type
4.input and print function in details
5.why python

'''
# conditional 
'''
1.if
2.elif
3.else

'''
'''
1.in python the styatements haing some sub statements inside it are called headings..at the end of heading we use columns:

and 1 group of statement is called block
.(block of code)
2.all statement inside a block are or inside a heading are indented statements that they are  placed at a fixed space with respect to heading

if (condition):
    statement 1
    statement 2
    .
    .
    statement n

elif(condition):
    statement 1
    statement 2
    .
    .
    statement n
else:
    statement 1
    statement 2
    .
    .
    .
    statement n

'''
# a=99
# if a==99:
#     print("hi")

# else:
#     print('L')

# if(False):
#     print("cetpa")
# else:
#     print("g")

#New program
'''
small project: scientific calculator

python library/package/...framework

library is a collection of  .predefined variables functions classes and methods.

the libary 
'''
# print("cetpa")

# print(int(2.9))

# find the biggest no in 3 numbers
'''
no1=int(input("Enter number"))
no2=int(input("Enter number"))
no3=int(input("Enter number"))

if (no1>no2 and no1>no3):
    print("The biggest number is",no1)

# elif me tb ayege jb sure ho jayega ki n01 sbse  bda nhi hai.>
# agr aap elif me aye ho to pahla condition true nhi hai
elif( no2>no3):
    print("The biggest number is",no2)
else:
    print("The biggest number is",no3)

'''

# chek character is english alphabet or not

# ch=input("Enter character: ")
# if (ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
#     print("character is upper case")
# elif(ch in "abcdefghijklmnopqrstuvwxyz"):
#     print("character in lower")
# elif(ch in "0123456789"):
#     print("character is a number")
# else:
#     print("Not a alphabet or number")

# another way is>>
# ch=input("Enter character: ")
# c=ord(ch)
# if (c>=65 and c<=90):
#     print("Entered character is in upper case")

# elif (c>=97 and c<=122):
#     print("Entered character is in lower case")

# elif (c>=48 and c<=57):
#     print("Entered character is in number case")

# else:
#     print("Not a alphabet or number")

'''Nested condition''' "consider inside condition"


# a,b,c,d=1,2,3,4
# if(a==1):
#     if(b==3):
#         if(c==3):
#             print("inside a,b,c")
#     elif(b==2):
#         print("hello")
#     else:
#         print("ABCD")

# else:
#     print("how are you")
# print("Program is complete")

# id=input("Enter the ID: ")
# if (id=="devesh"):
#     pwd=input("Enter password: ")
#     if (pwd=="1118"):
#         print("ID and password are correct")
#         print("you are welcome")
#     else:
#         print("Incorrect password")

# else:
#     print("The ID is in correct")


"""find the biggest of 3 numbers using nested condition"""

# no1=int(input("Enter number: "))
# no2=int(input("Enter number: "))
# no3=int(input("Enter number: "))
# if(no1>no2):
#     if(no1>no3):
#         print("biggest is",no1)
#     else:
#         print("biggest no is",no3)

# else:
#     if(no2>no3):
#         print("biggest no is",no2)
#     else:
#         print("biggest no is",no3)
    
# STRING : COLLECTION OG HOMOGENIUOUS DATA TYPE

# LIST : COLLECTION OG HETROGENEOUS DATA TYPE

# tuple : COLLECTION OG HETROGENEOUS DATA TYPE


#INDEXING AND SLICING
# s=[10,20,30,40,50,60,70]
# print(s[4:20:2])

# s="welcome"
# print(s[-2:-5:-1])

# s="welcome"
# print(s[-2:-5:1]) # empty


#ASSIGNMENT : Why indexing starts from 0
# l=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(l[0:2])


# how we create cariable in python?
#by assigning the value
# every data type in python is class
# class is a collection of variables and methods
# a=print("cetpa")
# print(a)

# in find method if element is not present the it gave -1
# in index method if element is not present the it throughs error
# a="Devesh upadhyay kha hai bhai"
# c=a.index(" ")
# print(c)


# remove c from the string
# s="welcome"
# s=s[:3]+s[4:] 
# print(s)

# s="12345678"
# s=s.replace("23456","****")
# print(s)

# s="welcome123"
# s=s.isalpha()  #only galphabets honi chahiye not numbers
# print(s)

# s="12346543"
# s=s.isnumeric()
# print(s)

# new program: wap to check the mobile number input by user is correct fomat or not

# n=input("Enter mobile number: ")
# if n.isnumeric():
#     if len(n)==10:
#         print("the is correct format")
#     else:
#         print("enter the number in 10 digit only")
# else:
#     print("enter only numbers in mobile")

#new program
# s="W"
# r=s.isupper()
# print(r)

# join method
# s="welcome"
# r=s.join("j")
# print(r)

#split
# s="devesh upadhyay " # by default split on the basis of spaces
# r=s.split()
# print(r)

#new program
# s="ABc* DEF*GHI" # character base er hum split karte hai
# r=s.split("*")
# print(r)

#new program
# s="devesh upadhyay" # character base er hum split karte hai
# r=s.split()
# print(r)  by defalt list me krta hai

# n=input("Enter number: ")
# print("numbers")
# j=n.split()
# print(len(j))

# join
# l="devesh"
# r="".join(l)
# print(r)


#strip
# s="deveshd"
# r=s.strip()
# print(r)


# n=input("enter number: ").split()
# print(n,len(n))

# s="**deveshd**"
# print(s,len(s))
# r=s.strip()
# r=s.strip("**")
# print(r,len(r))

# new rule humesa yaad rakho
# a=int(input("enter nu: ").strip()) 
# b=int(input("enter nu: ").strip())
# c=a+b
# print(c)

# new program
# s="         devesh           aaa   aaa aaa akha ho"
# r=s.replace(" aaa","")
# print(r)

e="Welcome"
r=e.swapcase()
print(r)

# write a code to reverse the input:
n=input("Enter Number: ")
s=''
for i in  n :
    s=i+s
if s.isdigit():
    print(int(s))
elif s.isalpha():
    print(s.upper())
else:
    print("Invalid Syntax please enter valid Syntax")
          
    

