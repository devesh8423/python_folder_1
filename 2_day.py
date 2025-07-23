# software :IDE: integrated developement environment
# popular ides in python
# 1: jupyter : anaconda framework: browser based
# 2: pycharm : jetbrains
# 3: vs code : microsoft :
# 4: google colab : limited free version:Deeplearning:AI
# 5: spyder  : anaconda framework


# Datatypes: Like in real world we have different kind of data,
# similarly in python we have different data type these are actually 
# values used in programming . to use these data types or values there 
# are some predefined rules: like int, to be saved directly. to save string, 
# we need to use quotes

# SINGLE ELEMENT /SINGLE VALUED
# INT 25,98987,-87
# FLOAT 0.077
# COMPLEX 3+4J
# BOOL True,False
# NON TYPE,None

# multi element/multi valued/iterators: Data can have multiple elements
# str
# list
# set
# dictionary
# tuple
# frozenset


# user interaction:

# console application: ON CONSOLE COLOR WINDOW, WE INTERACT THROUGH KEYBOARD, 
# DATA ONLY IN TEXT FORMAT.

# GUI APPLICATION: GRAPHICAL USER INTERFACE: WE INTERACT THROUGH KEYBOARD,
# MOUSE OR OTHER PERIPHERALS.

# IN CONSOLE: WE HAVE READY MADE FUNCTIONS TO INTERACT WITH USER: PRINT AND INPUT 
# PRINT: TO PRINT OR DISPLY THE DATA ON SCREEN
# INPUT: TO COLEECT OR INPUT THE DATA FROM SCREEN OR FROM USER

# PRINT BASIC VERSION:
# PRINT(VALUE/VARIABLES/EXPRESSIONS/CONDITIONS/FUNCTIONS....)


# IN PYTHON HOW TO SWAP TWO VARIABLES:
# PYTHON SUPPORT ASSIGNING VALUES VARIABLES IN SINGLE STATEMENT

# a,b=9,3
# print(a,b)
# a,b=b,a
# print(a,b)


# a,b,c=9,2,3
# print(a,b,c)
# a,b,c=c,a,b
# print(a,b,c)


# x=int()
# print(x,type(x))


# x=5 actual value in binary
# x="5" ascii value 

# ascii=american standard code for information interchange

# initialy ascii code was of 7 bits: total combinations:2 power n:128
# 8 bits:min value 0 , max value: 255: total combinations :2 power 8:256


# A: 65     a ascii code:97           
# B:66      b ascii code :98 
# C:69
# . .
# . .
# z=90      z ascii code: 122



#variable : data storing element: whose value vary in the program
# variable are stored in ram




# To check american standard code information interchange
# print(ord("a"))
# print(chr(97))




# python 3 started supporting unicodes

# input function: to take the data from user
# whenever we ineract with outer world using print or input
# function, data is transmitted in string format
# example==>
# a=input("Enter first number")
# b=input("Enter second number")
# c=a+b
# print(c)

# a=5
# b=7
# c=a+b
# print(c)


# a='5'
# b='7'
# c=a+b
# print(c)


# when we use +  operator on number, then data will be added
# when we use +  operator on strings, then data will be concatenated




# a=5
# print(a,type(a))
# a=input("enter a: ")
# print(a,type(a))
      

# str: collection of homogeneous data types that is characters or unicodes
# list: collection of hetrogeneous data types
# tupe: collection of hetrogeneous data types
#syntax
# var=[comma seperated values]


# l1=[11,22,33,44,55]
# l2=[111]
# l3=l1+l2    # both list are concatenated
# print(l3)


# t=(11,22,"dev",2.3)
# print(t)
# print(type(t))

# x=5
# print(len(x)) # work on iterators


# s="cetpa"
# l=list(s)
# print(l)


# print extended version
#oues:
# print 5 stars in single line using 5 points statements with printing one star every time using one print?


# we can pass few optional parameters in print: there are two default variable that is end and sep ...

# Default value of end is "\n"
# Default value of sep is ' '
# when we run print statement , end variable is printed at the end of the statement
# statement variable is printed whithin arguments(within every argyuments)
# we have multiple escape character in python which are escaped from the screen
# means they are not printed on the screen but they will leave a special functionlaity on the screen
# \t:Tab
# \n: new line character

# print("*")
# print("*")
# print("*")
# print("*")
# print("*")


#new line
# print("c\ncetpa")

# # tab space
# print("c\tcetpa")


# a,b,c,d=1,2,3,4
# print(a,b,c,d)
# print(a,b,c,d,sep="",end="\n")


# In print bydefault sep=" ",end="\n) are used 

# a,b,c,d=1,2,3,4
# print(a,b,c,d,sep="$$",end="kha")
# print("cetpa","ouick")


# a,b,c,d=1,2,3,4
# print(a,b,sep="*",end='#')

# a,b,c,d,e,f,g,h=1,2,3,4,5,6,7,8
# print(a,b,c,sep="*")
# print(d,e,sep="\t\t\t",end="**")
# print(f,g,h)


# 1*2*3
# 4            5**6 7 8            


# a,b,c,d,e,f=1,2,3,4,5,6
# print(a,b,sep="/n/n")
# print(c,sep="vikas")
# print(d,e,sep="kalra",end="##")


# 1/n/n2
# 3
# 4kalra5##

#values values are the values directly printed, taken by user as input or saved as variables
# values aere associated with some data types having their own rules like string is printed through quotes,list is printed through  bracket 
#  int is printed directly

# Identifiers: user defined names likes names of variables names of functions and name of classes
# keywords:  predefined names


# there are some few set of rules for identifiers:
# variables ko define krne ke liye humare pas identifiers hote hai..
# variables ke possible names ko skte hai identifiers batate hai..

# valid identifiers ..?

# 1....>english alphabets are allowed..

# 2...>numbers are allowed  but name should not start with number..

#3...> only one special symbal _ underscore is allowed..

#4...> other special symbal are not allowed.. space is also a special character so its not allowed

#5...> underscore se variable ka name start ho skta hai..

# 6...> python is a case sensitive language so identifiers are case sensitive 
# 7...> 
# invalid identifiers 


#coding principle: how to write neat and clean code
#1...> logicsl names given to identifiers 
#2...> 