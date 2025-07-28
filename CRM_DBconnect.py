"Customer management system using oops:"

# Business logic layer:
import pickle
import pymysql
class Customer:
    cus_list=[]
    con=pymysql.connect(host="localhost",user="root",password="devesh@2425",database="cus1")
    Cur=con.cursor()
    def __init__(self):
        self.id=0
        self.name=0
        self.age=0
        self.mob=0
    def addCustomer(self):
        Customer.cus_list.append(self)
        Customer.Cur.execute(f"insert into custb values({self.id},'{self.name}',{self.age},'{self.mob}')")
        Customer.con.commit()
    def searchCustomer(self):
        # for i in Customer.cus_list:
        #     if i.id==self.id:
        #         self.name=i.name
        #         self.age=i.age
        #         self.mob=i.mob
        #         return
        qry=f"select * from custb where id={self.id}"
        Customer.Cur.execute(qry)
        data=Customer.Cur.fetchone()
        self.name=data[1] 
        self.age=data[2] 
        self.mob=data[3] 
    def deleteCustomer(self):
        # for i in Customer.cus_list:
        #     if i.id==self.id:
        #         Customer.cus_list.remove(i)
        #         return
        qry=f"Delete from custb where id={self.id}"
        Customer.Cur.execute(qry)
        Customer.con.commit()
    def modifyCustomer(self):
        # for i in Customer.cus_list:
        #     if i.id==self.id:
        #         i.name=self.name
        #         i.age=self.age
        #         i.mob=self.mob
        #         return
        qry=f"update custb set name='{self.name}',age={self.age},mob='{self.mob}' where id={self.id}"
        Customer.Cur.execute(qry)
        Customer.con.commit()
    @staticmethod
    def saveTopickle():
        f=open("d://temp/cmsdata.txt","wb")
        pickle.dump(Customer.cus_list,f)
        f.close()
    
    @staticmethod
    def loadFromPickle():
        f=open("d://temp/cmsdata.txt","rb")
        Customer.cus_list=pickle.load(f)
        f.close()





# presentation layer
if(__name__=="__main__"):
    print("Welcome to Customer management system")


    def showCustomer(cus):
        print("Customer Id :",cus.id,"Customer Name :",cus.name,"Customer Age:",cus.age,"Customer Mob:",cus.mob)

    # def getMob():
    #     while(1):
    #         mob=input("Enter Mob No: ")
    #         if (mob.isdecimal()):
    #             if len(mob)==10:
    #                 return mob
    #             else:
    #                 print("Enter Mob 10 digit Only")

    #         else:
    #             print("Enter Mob No with digits only!")        
    
    while(1):
        cus=Customer()
        ch=input("""Enter Choice: 1 Add, 2 Search, 3 Delete, 4 modify, 5 Display, 6 Exit 
    7 save, 8 Load: """)
        if ch=="1":
            cus.id=input("Enter cust Id: ")
            cus.name=input("Enter cust Name: ")
            cus.age=input("Enter cust Age: ")
            cus.mob=input("Enter Mob:")
            cus.addCustomer()
            print("Customer Added successfully !")
        elif(ch=="2"):      #search customer
            cus=Customer()
            cus.id=input("Enter cust Id to search: ")
            cus.searchCustomer()
            showCustomer(cus)
        elif(ch=="3"):  # Delete customer
            cus=Customer()
            cus.id=input("Enter cust Id: ")
            cus.deleteCustomer()
            print("Customer Deleted successfully !")
        
        elif(ch=="4"):  # Modify customer
            cus=Customer()
            cus.id=input("Enter cust Id: ")
            cus.name=input("Enter cust updated Name: ")
            cus.age=input("Enter cust updated Age: ")
            cus.mob=input("Enter cust updated Mob: ")
            cus.modifyCustomer()
            print("Customer modified successfully !")

        elif ch=="5":  # Display all customer
            for i in Customer.cus_list:
                showCustomer(i)
        elif ch=="6":
            print("Thanks for using Customer management system !")
            break

        elif(ch=="7"):   # save to pickle format 
            Customer.saveTopickle()

        elif(ch=="8"):
            Customer.loadFromPickle()


        else:
            print("Incorrect choice !")