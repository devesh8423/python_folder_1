'''Database Connectivity:

1...>Till now we save the datat in ram using variables or hard disk files for permanent storage.
2..> Now we have to save the data into database.

Types of Database
1.Relational Database :Sql Based
Related means data entries (rows+) are associated or realated based on some fields generally primary key.
Data is in the form of tables (Rows(Entries) and columns(Field))
SQL:Structured query language
Ezxamples: MySQLserver,Oracle,My-SQLserver,postgre SQl,MariDB,SQLite,IBM_DB2

1.Nonrelational Database : No sql
MONGoDB,Cassendra Server


MySQL Server:Relation Database:install,at the time od=f installed,default user create:root and we need to mention the password of this root user:

Once you open mysql,it will ask pwd of root user
if you will enter wrong password,databse server will be closed automatically without any warning.

MySQL:SQl Queries.
Tabular format database.
CRUD Operation.
C:UPDATE
D:DELETE
select insert delete update are data related queries and rest create is for creation of database and table

Datatabse server is collection of databases.Database is a Collection of Tables.Table is a collectiomn Of row(entries) or collection
of columns(Fields) 
'''
# QUERIES..>   MULTIPLE TYPES

'''
DML:DATA MANiPULATION Language(data modifiaction)like insert ,update, delete
DDL:Data DEFINITION LANGUAGE:CREATE, DROP,TRUNCATE,ALTER
DQL:DATA QUERY LANGUAGE:LIKE SELECT

BENIFITS OF USING DATABSE OVER EXCEL:
FAST ACCESS ,CAN STORE LARGE DATA,MORE RELIABLE,

Primary Key:Is one of the field of table which is unique and not null key.


Now our target is to access database in python.
step 1 : install pymysql package
step 2:Make connection with thw database.
con=pymysql.connect(host="localhost",user="root",password="root123",database="db1")

host:ipaddress:
id database server in your own computer then ip address of your computer if you access locally:(127.0.0.1)
Which can we represented by "localhost "
step 3 : create a cursor on connection (con) object
cur=cun.cursor()
step 4: start excecuting queries on cursor:
cur.excute(insert into table_name values(50,"sonu",45)")
step 5: after writing SQL DML queries , we need to commit the database
with
con.commit()
After commiting modification will take place in table.

step 6: con.close()

'''

# Database Connectivity 

# import pymysql
# con=pymysql.connect(host="127.0.0.1",user="root",passwd="devesh@2425",database="db1")
# cur=con.cursor()
# query="insert into tb1 values(50,'Ayush',16)"
# cur.execute(query)
# con.commit()
# con.close()

# Database Connectivity 
# import pymysql
# con=pymysql.connect(host="localhost",user="root",passwd="devesh@2425",database="db1")
# cur=con.cursor()
# qry="insert into tb1 values (60,'aditya',18)"
# cur.execute(qry)
# cur.execute("insert into tb1 values(70,'Abhi',8) ")
# con.commit()
# con.close()
'''New program'''
# import pymysql
# con=pymysql.connect(host="127.0.0.1",user="root",password="devesh@2425")
# cur=con.cursor()
# cur.execute("use db1")
# cur.execute("select * from tb1")
# data=cur.fetchall()
# print(data)
# con.close()

'''New program'''
# import pymysql
# con=pymysql.connect(host="127.0.0.1",user="root",password="devesh@2425")
# cur=con.cursor()
# cur.execute("use db1")
# cur.execute("select * from tb1")
# data=cur.fetchall()
# for i in data:
#     print("cus Id:",i[0],"cus Name:",i[1],"cus Age:",i[2])
# con.close()

'''New program'''
