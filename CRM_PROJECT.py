'''why crm or cms:
client relationship management
customer management system
World,s biggest ready made CRM product company:
Salesforce

'''
'''Whenever we create any management system then we have minimum crud
operation in that system 
crud ..>create ,read, update,delete'''

'''
how to add customer
how to fetch customer/Search customer
how to update/modify customer
how to delete customer
'''

#BLL Business Logic layer
import random
id_list=[]
name_list=[]
age_list=[]
mob_list=[]

def getSystemId(): # 7 digit unique number
    while(1):
        id=random.randint(1,9999999)  #1300,1300,1200
        if(id not in id_list):
            return id

def addCustomer(id,name,age,mob):
    id_list.append(id)
    name_list.append(name)
    age_list.append(age)
    mob_list.append(mob)

def searchCustomer(id):
    index=id_list.index(id)
    return index

def deleteCustomer(id):
    i=id_list.index(id)
    id_list.pop(i)
    name_list.pop(i)
    age_list.pop(i)
    mob_list.pop(i)
def modifyCustomer(id,name,age,mob):
    i=id_list.index(id)
    name_list[i]=name
    age_list[i]=age
    mob_list[i]=mob

#PL Presentation layer
def showCustomer(i):
    print("Custome Id:",id_list[i],"Custome name:",name_list[i],"Custome age:",age_list[i],"Custome mob:",mob_list[i])

def getId():
    while(1):
        id=input("Enter Customer Id: ")
        if(id in id_list):
            print("Warning! Duplicate Id")
        else:
            return id


print("Welcome CMS Management System")
while(1):
    choice=input("Enter choice:1 add ,2 Search,3 Delete,4 Modify ,5 Display all,6 Exit:")
    if(choice=="1"):    # Addd ne customer

        id=getSystemId()
        name=input("Enter Cust name :")
        age=input("Enter Cust Age :")
        mob=input("Enter Cust Mob :")
        addCustomer(id,name,age,mob)
        print("Customer added Successfully")
    
    elif(choice=="2"):    # Search Customer
        id=input("Enter Cust ID to Search the customer :")
        i=searchCustomer(id)

        showCustomer(i)

    elif(choice=="3"):  #Delete Customer detail
        id=input("Enter Cust ID to Delete: ")
        deleteCustomer(id)
        print("Customer Deleted Successfully")
    elif(choice=="4"): #Modify customer
        id=input("Enter Customer ID to Modify: ")
        name=input("Enter Cust Updated Name: ")
        age=input("Enter Cust Updated Age: ")
        mob=input("Enter Cust Updated Mobile No: ")
        modifyCustomer(id,name,age,mob)
        print("Customer Modified successfully")
    elif(choice=="5"):  # Display all customers
        for i in range(len(id_list)):
            showCustomer(i)
    elif(choice=="6"):    #Exit
        print("Thanks for using CRM")
        break
    else:
        print("Incorrect Choice")

'''
What more feature we can add in CRM:
1.Duplicate id detect
2.mobile number should be of 10 digit only
3.Can add more features of the customer:
Add Email,Address,Pin code,City,State,DOB....
4.System Generated ID.(Can be in A Sequence OR can be Random ID  as well as non-duplicate
id of 7 Digit or 10igit Also)
5.If User enter incorrect id .Takle
6.Searching can be basis of the mob as well on name
7.Selected data change in Modify Customer.
8.sort the data on some criteria
9.Count the customers
10.ban a customer


'''

# make this crm by sing dictionary
# create your own account on github and publish the crm software on it 
#world biggest website Quora..
# world biggest website for technical question answer is stackoverflow

# on your resume mention your github id and stackoverflow id, also mention you are an active contributor to stackflow.
# worlds biggest website for information wikipedia
# create your account on hackerEarth.com
#select your favorite programming language as python
# Start solving python problems
# creAte a good work
# Hacker rank:
# Hacker earth:
# Code chef: