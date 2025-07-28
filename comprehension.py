'''List Comprehension:
When we want to use particular operation on all elements or selected elements of an iterator and want to create
a new list then we can use  list comprehension. or even want to create some series of elements in a list we can use 

Partial Syntax:
list_var=[result element for creating/ accessing_element using for loop ]

Complete Syntax:
list_var=[result element for creating/ accessing_element using for loop condition_on_elements ]

'''


''' create a list having square value of element  of an integer data string.'''

#New program

# s="12345678"
# l=[ i**2 for i in s] #TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
# print(l)
# l=[int (i)**2 for i in s]
# print(l)

#New program

# x='2'
# l=[int(x)]
# print(l[0],type(l[0]))

#New program

# x='2'
# l=[ int(i)for i in x]
# print(l)

# using loop
# s="12345678"
# l=[]
# for i in s:
#     t=int(i)**2
#     l.append(t)
# print(l)

#New program

# create a list having square value of even index element  of an integer data string"

#New program

# List Comprehension:

# s="12345678"
# l=[int(i)**2 for i in s if int(i)%2==0]
# print(l)

#New program

# using loop

# s="12345678"
# l=[]
# for i in s:
#     if int(i) % 2==0:
#         l.append(int(i)**2)
# print(l)
#New program

# create a even list..
# l=[1,2,3,3,43,45,44,45,55,5,5556,43,5,23,23,3,34,3434,34,23,2,333,33,343,]
# a=[i for i in l if i%2==0]
# print(a)

#New program

# l=[1,2,3,3,43,45,44,45,55,5,5556,43,5,23,23,3,34,3434,34,23,2,333,33,343,]
# a=[int(i)%2==0 for i in l]
# print(a)

'''Find all of the numbers from 1-1000 that have a 3 in them'''
# l=[i for i in range(1,1001) if '3' in str(i)]
# print(l)

'''Find all of the numbers from 1-1000 that have a 3 in them'''
# l=[i for i in range(1,1001) if "0" in str(i)]
# print(l,len(l))

