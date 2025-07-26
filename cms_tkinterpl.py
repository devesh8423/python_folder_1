#presentation layer
from  CRM_oops import *
from tkinter import *
from tkinter import messagebox

def add_handler():
    cus=Customer()
    cus.id=var_id.get()
    cus.name=var_name.get()
    cus.age=var_age.get()
    cus.mob=var_mob.get()
    cus.addCustomer()
    messagebox.showinfo("CMS","Customer Added Successfully")
    var_id.set("")
    var_name.set("")
    var_age.set("")
    var_mob.set("")

def search_handler():
    cus=Customer()
    cus.id=var_id.get()
    cus.searchCustomer()
    var_name.set(cus.name)
    var_age.set(cus.age)
    var_mob.set(cus.mob)
    
def delete_handler():
    cus=Customer()
    cus.id=var_id.get()
    cus.deleteCustomer()
    messagebox.showinfo("CMS","Customer Deleted Successfully")
    var_id.set("")

def modify_handler():
    cus=Customer()
    cus.id=var_id.get()
    cus.name=var_name.get()
    cus.age=var_age.get()
    cus.mob=var_mob.get()
    cus.modifyCustomer()
    messagebox.showinfo("CMS","Customer Modified Successfully")
    var_id.set("")
    var_name.set("")
    var_age.set("")
    var_mob.set("")
    

def display_handler():
    root_all_customer=Tk()
    id_all_customer=Label(root_all_customer,text="customer ID",font=1,bg="orange",width=20,height=2)
    id_all_customer.grid(row=0,column=0)

    name_all_customer=Label(root_all_customer,text="customer NAME",font=1,bg="orange",width=20,height=2)
    name_all_customer.grid(row=0,column=1)

    age_all_customer=Label(root_all_customer,text="customer AGE",font=1,bg="orange",width=20,height=2)
    age_all_customer.grid(row=0,column=2)
    
    mob_all_customer=Label(root_all_customer,text="customer MOB",font=1,bg="orange",width=20,height=2)
    mob_all_customer.grid(row=0,column=3)
    e=0
    for i in Customer.cus_list:
        e+=1
        lbl_id_cust=Label(root_all_customer,text=i.id,font=1,bg="Yellow",width=20,height=2)
        lbl_id_cust.grid(row=e,column=0)

        lbl_name_cust=Label(root_all_customer,text=i.name,font=1,bg="Yellow",width=20,height=2)
        lbl_name_cust.grid(row=e,column=1)

        lbl_age_cust=Label(root_all_customer,text=i.age,font=1,bg="Yellow",width=20,height=2)
        lbl_age_cust.grid(row=e,column=2)

        lbl_mob_cust=Label(root_all_customer,text=i.mob,font=1,bg="Yellow",width=20,height=2)
        lbl_mob_cust.grid(row=e,column=3)


    
def save_handler():
    Customer.saveTopickle()
    messagebox.showinfo("CMS","Data Added Successfully")

def load_handler():
    Customer.loadFromPickle()
    messagebox.showinfo("CMS","Data Load Successfully")

root=Tk()
lbl_id=Label(root,text="Cust Id",font=1)
lbl_id.grid(row=0,column=0)
lbl_name=Label(root,text="Cust Name",font=1)
lbl_name.grid(row=1,column=0)
lbl_age=Label(root,text="Cust Age",font=1)
lbl_age.grid(row=2,column=0)
lbl_mob=Label(root,text="Cust Mob",font=1)
lbl_mob.grid(row=3,column=0)

var_id=StringVar()
entr1=Entry(root,textvariable=var_id,font=1)
entr1.grid(row=0,column=1)

var_name=StringVar()
entr2=Entry(root,textvariable=var_name,font=1)
entr2.grid(row=1,column=1)

var_age=StringVar()
entr3=Entry(root,textvariable=var_age,font=1)
entr3.grid(row=2,column=1)

var_mob=StringVar()
entr4=Entry(root,textvariable=var_mob,font=1)
entr4.grid(row=3,column=1)

btn_add=Button(text="Add Cust",font=1,command=add_handler,width=15,height=2)
btn_add.grid(row=4,column=0)

btn_search=Button(text="Search Cust",font=1,command=search_handler,width=15,height=2)
btn_search.grid(row=4,column=1)

btn_delete=Button(text="Delete Cust",font=1,command=delete_handler,width=15,height=2)
btn_delete.grid(row=4,column=2)

btn_modify=Button(text="Modify Cust",font=1,command=modify_handler,width=15,height=2)
btn_modify.grid(row=5,column=0)

btn_display=Button(text="DisplayAll Cust",font=1,command=display_handler,width=15,height=2)
btn_display.grid(row=5,column=1)

btn_save=Button(text="Save Data",font=1,command=save_handler,width=15,height=2)
btn_save.grid(row=5,column=2)

btn_load=Button(text="Load Data",font=1,command=load_handler,width=15,height=2)
btn_load.grid(row=6,column=0)

root.mainloop()

"""This is called perfect layered architecture Which we design  in Cms using oops and tkinter"""