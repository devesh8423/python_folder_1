'''
Which data types are mutable in python
1.list
2.dict
3.set
Which data types are immutable in python
1.int
2.float
3.str
4.complex
5.tuple
6.frozenset
7.bool
8.Nonetype
'''

# so mutable means elements.
'''
in python to support dynmic nature ,everytime, 
we pass a new value to a variable,new value is stored at a
different location.
'''
# mutable..mutable means changes at the same location.

# change the first element of the strong
# s=input("Enter the string: ")
# ele=input("enter the new element: ")
# s=ele+s[1:]
# print("New string is:",s)

# LIST Method
'''if we try to modify the list elements using list methods
then same list is modified and new list is not created or new list is not returned 
why because of the list is mutable'''
# string method
'''if we try to modify the string elements using str methods
then same str is not modified and new string is created or new strring isreturned 
why because of the string  is immutable'''

x,y,z=10,10,10
# why  same id  for x,y and z 
'''All variables in python are of ref type
it means if we assign one variable to another then address of rhs variable
is assigned to lhs variable

But ideally in case of ref type variables 
if we change one variable then other variables is also changed
which is having same ref.but in python this nature of referenc+e type variable does not work'''

# l=[10,20,30,40,30,1,120,10,20]
# i=l.index(20,5) # that is start value if we did not gave this then it satrts with 0 and cout from 
#start index

# l=[10,20,30,40,30,1,120,10,20]  # repeted element index 
# ele=10
# for i in range(len(l)):
#     if ele==l[i]:
#         print(i)


'''Tuple is a hetrogenious data type in tuple,tuple is immutable only 2 methods are present
1.index
2.count

'''
# t=(10,20,30,40,50)
# id=20
# i=t.index(id)
# print(i)
# t=(10,20,30,40,20.0,20,50)
# id=20
# i=t.count(id)
# print(i)


'''
Whenever we call any function in programming
actual parameter are  passed to formal parameter.
formal parameter=actual parameter

'''
# def func1(l2):
#     l2[0]=50     #l2 address 10000
# l1=[10,20,30]    # l1 address 10000
# func1(l1)        #l2=l1  l2 address 10000
# print(l1)
# changing occur because of liost is mutable in nature..
# In functio we use assignment operator so new local variables are created



# # New proghram
# def add(u,v):
#     print(id(u),id(v))

# a,b=5,7
# r=add(a,b)           #u=a ,v=b  so id of a and u nd b and v are  same..
# print(id(a),id(b))
# print(u,v)        if i print outside function then it through an Error.

# id are same because of all variables in python are reference type


# if we want that no changes are occur so we use type cast in tuple 

# def func(t1):
#     l2=list(t1)
#     l2[0]=50
# l1=[10,20,30]
# t1=tuple(l1)
# func(t1)
# print(t1)

'''
Dictionary
1.Dictionary is a collection of hetrogeneous data type
2.Dictionary is collection of key value pairs. 
3.In Dictionary  elements are access by keys 
4.in Dictionary no indexing.
5.Dictionary is mutable in natureSyntax:
var={comma seperated key:value pairs}
var={key1:value1,key2:value2,....keyn:valuen}


Why Dictionary:
In list and tuple to access the elements we need iondex
But in real life applications,index are not known rather we know elements,
So to find the index through element is a very time consuming process.
So if we have big data in our application,then we can better use dictionary
rather list or tuple..
using Dictionary we can make dictionary key as the primary key as customer id.
and each value of dict can have complete customer data.

So if we know index in list or tuple even string then data can be accessed at a very fast speed
means like it will take no time to access the data..

dictionary also works on similar principle where keys of the dictionary are hashed which in 
background represents memory addresses and now if you know memory address,]
you can access dictionary value immediately.


Dictionary is an unordered collection of data , which can have only unique keys.
duplicate keys are not allowed in dictionary.

'''
#new program
# d={10:"cetpa",20:"abc",30:40,11:"devesh"}
# print(d[10])
# print(d[30])

# in dict how to access value 
# we access value by key

# l=[10,20,30,40,22,22,3,234,323,4,234,31,23,21,23123,1]
# for i in range(len(l)):
#     if l[i]==1:
#         print(i)

# # New program
# cus={10:["devesh",22,"123"],20:["sarvesh",23,"8957"],30:["ramesh",25,"9889"]}
# id=int(input("Enter cust Id: "))
# print("Customer Data:",cus[id])
# print("Customer name:",cus[id][0])
# print("Customer Age:",cus[id][1])
# print("Customer Mob:",cus[id][2])

#New program
'''for loop on dictionary: then directly keys will be accessed in loop.
'''
# d={1:10,2:20,3:30,4:40}
# for i in d:
#     print(i)


# to access key and value both in dictionary we use this method..

# d={1:10,2:20,3:30,4:40}
# for i in d:
#     print("key:",i,"value:",d[i])

# we did this similarly in list 
# l=[2,3,5,8,9,11,12]
# for i in range(len(l)):
#     print("index:",i,"value",l[i])

# duplicate keys are not allowed in python
# d={1:10,2:20,3:30,4:40,2:20}
# print(d)
# print(len(d))

# d={1:10,2:20,3:30,4:40,2:20}
# ky=d.keys()
# print(ky)
# val=d.values()
# print(val)

# New program
# cus={10:["devesh",22,"123"],20:["sarvesh",23,"8957"],30:["ramesh",25,"9889"]}
# id=int(input("Enter cust Id: "))
# name=input("Enter updated Name:")
# cus[id][0]=name
# print(cus)

# New program for add elements in dict

# # To add new key and value in dict ...
# d={1:10,0.0:20,3:30,4:40,2:20}
# d[4]=50
# print(d)


# To add new key and value in dict by using dict method is d.update().
# d={1:10,0.0:20,3:30,4:40,2:20}
# d.update({5:40})
# print(d)

# To add new key and value in dict by using dict method is d.setdefault().
# d={1:10,0.0:20,3:30,4:40,2:20}
# d.setdefault(7,70)
# print(d)


# DIFFEREnce in set default and update 
# update in this existing element or value is change if key is same

# d={1:10,0.0:20,3:30,4:40,2:20}
# d.update({2:30,1:100,7:70})
# print(d)

# # set default in this existing element or value is not  change if key is same.
# d={1:10,0.0:20,3:30,4:40,2:20}
# d.setdefault(1,00)
# print(d)

# add elements in empty dict
# cus_dict={}
# id=input("Enter Cust Id:")
# name=input("Enter Cust Name:")
# age=input("Enter Cust Age:")
# mob=input("Enter Cust mob:")
# cus_dict.update({id:[name,age,mob]})
# # cus_dict.setdefault(id,[name,age,mob])
#cust_dict[id]=[name,age,mob]
# print(cus_dict)




'''
1.Set is also unordered collection  of data..
2.We can not accesss set element using index..
3.Set only holds unique values

'''

# remove all duplicates of this list

# l1=[10,20,30,40,50,10,20,40,50,10]
# s1=set(l1)
# print(s1)
# l1=list(s1)
# print(l1)

# Union means 2 table ki saari values 1 baaar ayengi.not duplicate
# intersection means 2 table ki common elements ..common


# for frozen set no ready made symbal to
# create frozenset so we use typecasting to create frozensets
# frozen set is immutable
# s={10,20,30}
# f=frozenset(s)
# print(f)
# print(type(f))

# create your own account on github and publish the crm software on it 
#world biggest website  is for general question answer:Quora..

# world biggest website for technical question answer is: stackoverflow

'''
There can be few packages which can have subpackages inside it:
Syntax:
import package_name
import package_name.subpackage_name

'''
# New  program
# d={"id":10,"name":"devesh","age":23,"mob":123}
# i=d.items()
# print(i)
# print(type(i))
# for e in i:
#     print(e,e[0],e[1])



'''
Whenever we access a module, the complete module is executed automatically
But generally we want that if we are accessing a module from outside then its bll should only be called because
pl is made local for that module only.

'''





# s={2,3,4,5,5,6,7,1,2,3,3,5,12,"k",23432,34}
# d=frozenset(s)
# print(s)
# print(type(s))