"""scientific calculator"""
import operator
import math
while(1):
    try:
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
            raise NotImplementedError("Incorrect Choice")
         
    except ValueError:
        print("Error! Enter whole numbers")
    except ZeroDivisionError:
        print("Error! Enter nonZero Second input")
    except Exception:
        print("Error! Try again")

    except NotImplementedError as err:
        print("Error",err)
    finally:
        ch=input("Wana Continue? y/N :")
        if(ch=="n" or ch=="N"):
            break

""""
Raise keyword is generally used in bll
"""