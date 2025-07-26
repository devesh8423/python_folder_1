""""
Exception handling : study of handling Exception ie errors
Real Life projects dont stop if errors come/generates.

Exception handling gaves us a way,that how to manage any type of error in the program

We have 4 keyword in python Exception handling:

Python                  java
Try                     Try
except                  catch
Finally                 finally
raise                   Throw,throws                      
                        
                        
                        
"""
#New Program
# try:
#     a,b=3,4
#     s=a+b
#     print("Result",s)
# except:
#     print("There is some Error in the Program")


#New Program
# while(1):
# try:
#     a=int(input("Enter 1st no: "))
#     b=int(input("Enter 2nd no: "))
#     s=a+b
#     print("Result",s)
# except:
#     print("There is some Error in the Program")

#New Program
# while(True):
#     try:
#         a=int(input("Enter 1st no: "))
#         b=int(input("Enter 2nd no: "))
#         s=a/b
#         print("Result",s)
#         break
#     except:
#         print("There is some Error in the Program")

#New Program

# while(1):
#     # try:
#         a=int(input("Enter 1st no: "))
#         b=int(input("Enter 2nd no: "))
#         s=a/b
#         print("Result",s)
# a=4
# b=5
# print(a+b)


#New Program
# f=open("d://temp/cetpa6.txt","r") #FileNotFoundError: [Errno 2] No such file or directory: 'd://temp/cetpa6.txt'

# x="cetpa"
# print(x[3])    #IndexError: string index out of range


"""
In python for different type of errors ifferent error classes are
Created
1.indexerror
2.valueerror
3.typeerror
4.filenotfounderror
5.syntaxerror
6.indentationerror
7.modulenotfounderror
8.zerodivisonerror
9.attributeerror
And the parent of all error classes is Exceptionclass:


"""

# New Program
# while(True):
#     try:
#         a=int(input("Enter 1st no: "))
#         b=int(input("Enter 2nd no: "))
#         s=a/b
#         print("Result",s)
#         break
#     except ValueError:
#         print("Error! Enter Input In whole Numbers Only")
#     except ZeroDivisionError:
#         print("Error! Enter Nonzero second input only")
#     except Exception:
#         print("Error! There are some error in our program")

# New Program

# while(1):
#     try:

#         a=int(input("Enter no: "))
#         b=10
#         print(a+b)
#     except:
#         print("Error")

""""
Finally block of code always run
If there is some error or there is no error

Raise:
if you want to raise the Exception in the program
 Intentionally at some line of code.
 

"""
# New Program
# while(True):
#     try:
#         a=int(input("Enter 1st no: "))
#         b=int(input("Enter 2nd no: "))
#         s=a/b
#         print("Result",s)
#         break
#     except ValueError:
#         print("Error! Enter Input In whole Numbers Only")
#     except ZeroDivisionError:
#         print("Error! Enter Nonzero second input only")
#     except Exception:
#         print("Error! There are some error in our program")

#     finally:
#         print("I am in Finally block")

# New Program
# try:
#     int("a")
# except Exception as e:
#     print("Error:",e)