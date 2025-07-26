
'''
Delegation model..>
JSON..>
Regular expression..>


'''

'''
File Handling: Till now we save the data temprorarily in variables are stored in  ram(volatile memory).
To save the data permanently in hard disk files we learn about file handling.

In file Handling , when  we interact with our  hard disk then  data is transferred in the form of data streams
ie data bundles..


In file handling , how to interact with the harddisk: How to read and write  data in files.


Step one:
First thing first: File type object : TextIOWrapper class
file_obj_name=open(file_path,mode)

'''
# New program

# import time
# for i in range(5):
#     print("Cetpa")
#     time.sleep(1)
#     print("Welcome")
#     time.sleep(2)

# New program
# import time
# for i in range(5):
#     print("*",end="")
#     time.sleep(2)

# New program

# f=open("D://temp/dev.txt","r")
# print(type(f))
# data=f.read()
# print(data)
# f.close()

# New program
# f=open("D://temp/dev.txt","r")
# data=f.read(5)
# print(data)
# # f.close()
# data=f.read(2)
# print(data)


# New program
# '''Another syntax is with open'''
# with open("d://Temp/dev.txt","r") as f:
#     data=f.read(5)
#     print(data)
# data=f.read(2)              #ValueError: I/O operation on closed file. yha kya hota hai jb hum with open krte hai to us heading se bahr close ho jata hai
                                # matlb yaha pr close nhi likhna oadta hai .usi indentation me rahoge to open nhi to close.

# f=open("c://temperory/devesh.txt","r")
# d=f.read()
# print(d)
# f.close()
# with open("c://temperory/devesh.txt","r") as f:
#     d=f.read()
#     print(d)

# # New program
# f=open("d://temp/dev2.txt","w")
# d="Welcome to devesh file handling system"
# f.write(d)
# f.close()

# # New program

# f=open("d://temp/dev2.txt","a")
# d="\nElvish bhai ke agge koi bol skta hai kya\n kya haal hai bhai ke"
# f.write(d)
# f.close()

# s=b"devesh"
# print(type(s))
# print(s)

'''
Advanced file handling :

pickle format..>

pickle format:python internal partial encrypted format ,where class objects data can we 
Directly retrives to files and can be Directly retrives from files .This format is used only
TO trasfer data python to python.

pickling of data..>



IF you want to transfer data any other programming language then there is world's most popular
data trasfer standard format which is json format..

'''
# pickle format: Supports only binary data transfer
# import pickle
# data=[10,20,30]
# f=open("d://temp/dev3.txt","wb")
# pickle.dump(data,f)
# f.close()

# import pickle
# data=[10,20,30]

# f=open("d://temp/dev3.txt","rb")
# d=pickle.load(f)
# print(d)

