"""scientific calculator"""
import operator
import math
no1=int(input("Enter first no: "))
no2=int(input("Enter first no: "))
ch=input("Enter your choice +,-,*,/,pow,log:")
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

else:
    print("Incorrect Choice")