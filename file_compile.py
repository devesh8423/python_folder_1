def add(a,b):
    return a+b
def sub(a,b):
    return a-b
import py_compile
py_compile.compile("file_compile.py")


"""
Compiled file: Intermediate code,Which is not human understandable
If we comlipe our program on one os anf the compiled file can we executed on other os also 
then we say our language or technology is plateform independent:Cora : comile  once run anywhere.
java and Python are plateform independent 

A language can be  plateform independent for a particular os ,only if the virtual machine for that particular os 
is already developed

"""

import file_compile
r=file_compile.add(5,3)
print(r)