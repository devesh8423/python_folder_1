# # ques..> 
# # Create a program capable of displaying to user like KBC..
# # use list data type to store type to store the questions and their correct answers..
# # displaying the final amount the person is taking home after playing the game..
# print("welcome to KBC!")
# questions=[
# ["1.which language was used to create facebook?","python","jawa","php","c++","none",3],
# ["2.which one is not a web browser?","chrome","linux","safari","firefox","edge",2],
# ["3.what is HTTP used for?","email","gaming","coding","browsing","calling",4],
# ["4.which is a social media plateform?","facebook","python","chatgpt","excel","powerbi",1],
# ["5.which company own youtube?","meta","apple","google","microsoft","none",3],
# ["6.what does vpn protect?","ads","privacy","speed","virus","user",2],
# ["7.what does firewall so?","boost speed","delete file","block access","open sites","burn data",3],
# ["8.which is a search engine?","bing","google","photoshop","discard","copicut",2],
# ["9.what is WWW short for?","world wide web","web world wibe",'web wide world',"wide web world","world web wide",1],
# ["10.which keyword key is used to refresh?","f1","f5","alt+f4","f3","none",2],
# ["11.which device is connected to wifi?","router","printer","cpu","dvd","tv",1],
# ["12.what is google known as?","search engine","social media","operating system","chatbot","photoeditor",1],
# ["13.which is a file  type of image ?","pdf","jpg","mp4","txt","none",2],
# ["14.which is a datatye of python?","collection","infinite","finite","None","file",4],
# ["15.how many command usedin sql?","3","4","5","2","7",3],
# ]
# levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]

# money=0
# for i in range(0,len(questions)):
#     question=questions[i]
#     print(f"\nQuestion for Rs.{levels[i]}\n{question[0]}\n")
#     print(f"1.{question[1]}      2.{question[2]}")
#     print(f"3.{question[3]}      4.{question[4]}")
#     reply =int(input("Enter your Answer Or Press 0 to quit: "  ))
#     if (reply==0):
#         money=levels[i-1]
#         break
    
#     if (reply==question[-1]):
#         print(f"\nCorrect Answer you have won Rs.{levels[i]}\n")
#         if(i==4):
#             money=10000
#         elif(i==9):
#             money=320000
#         elif (i==14):
#             money=10000000
#     else:
#         print("Wrong Answer !")
#         break
# if money==10000000:
#     Name=input("please Enter your Name: ").upper()
#     print(f"\nCongratulation {Name} You Won Rs.{money}\n🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
# elif money==320000:
#     Name=input("please Enter your Name: ")
#     print(f"\nCongratulation {Name} You Won Rs.{money}\n🎉🎉🎉🎉")
    
# elif money==10000:
#     Name=input("please Enter your Name: ")
#     print(f"\nCongratulation {Name} You Won Rs.{money}\n🎉")


# print(f"Your Take Home Money is: {money}")



# print("welcome to KBC!")
# questions=[
# ["1.which language was used to create facebook?","python","jawa","php","c++","none",3],
# ["2.which one is not a web browser?","chrome","linux","safari","firefox","edge",2],
# ["3.what is HTTP used for?","email","gaming","coding","browsing","calling",4],
# ["4.which is a social media plateform?","facebook","python","chatgpt","excel","powerbi",1],
# ["5.which company own youtube?","meta","apple","google","microsoft","none",3],
# ["6.what does vpn protect?","ads","privacy","speed","virus","user",2],
# ["7.what does firewall so?","boost speed","delete file","block access","open sites","burn data",3],
# ["8.which is a search engine?","bing","google","photoshop","discard","copicut",2],
# ["9.what is WWW short for?","world wide web","web world wibe",'web wide world',"wide web world","world web wide",1],
# ["10.which keyword key is used to refresh?","f1","f5","alt+f4","f3","none",2],
# ["11.which device is connected to wifi?","router","printer","cpu","dvd","tv",1],
# ["12.what is google known as?","search engine","social media","operating system","chatbot","photoeditor",1],
# ["13.which is a file  type of image ?","pdf","jpg","mp4","txt","none",2],
# ["14.which is a datatye of python?","collection","infinite","finite","None","file",4],
# ["15.how many command usedin sql?","3","4","5","2","7",3],
# ]


# # project one .....>>> SNAKE WATER GUN GAME
# import random
# '''
# 1 for snake
# -1 for water
# 0 for gun
# '''
# computer=random.choice([-1,1,0])
# yourstring=input("enter your choice: ")
# yourdict={"s":1,"w":-1,"g":0}
# reversedict={1:"snake",-1:"water",0:"gun"}

# you=yourdict[yourstring]
# # by now we have 2 numbers (variables), you and computer..
# print(f"you chose: {reversedict[you]}\nComputer chose: {reversedict[computer]} ")
# if computer==you:
#     print("ITS a Draw ")


# else:
#     if computer==-1 and you==1 :
#         print("you win")
#     elif computer==-1 and you==0 :
#         print("you lose!")
#     elif computer==1 and you==-1 :
#         print("you lose!")
#     elif computer==1 and you==0 :
#         print("you win")
#     elif computer==0 and you==-1 :
#         print("you win")
#     elif computer==0 and you==1 :
#         print("you loose!")
#     else:
#         print("Something went wrong!")

# project one .....>>> SNAKE WATER GUN GAME


'''
1 for snake
-1 for water
0 for gun
# # '''
import random
# comp=random.choice([-1,1,0])
# # print(comp)
# n=input("enter your choice: ")
# d={"s":1,"w":-1,"g":0}
# rd={1:"snake",-1:"water",0:"gun"}
# y=d[n]
# print(f"you choose:{rd[y]}\ncomputer choose:{rd[comp]}")



# computer=random.choice([-1,1,0])
# yourstring=input("enter your choice: ")
# yourdict={"s":1,"w":-1,"g":0}
# reversedict={1:"snake",-1:"water",0:"gun"}

# you=yourdict[yourstring]
# # by now we have 2 numbers (variables), you and computer..
# print(f"you chose: {reversedict[you]}\nComputer chose: {reversedict[computer]} ")

# computer=random.choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26])
# n=(input("\nEnter your choice: ")).lower()
# dic={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,
#      "n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
# revdic={1:"apple",2:"boy",3:"cat",4:"dog",5:"elephant",6:"fish",7:"goat",8:"horsh",9:"incp",10:"joker",11:"king",12:"lion",13:"mango"
#         ,14:"nose",15:"orange",16:"pecoke",17:"queen",18:"rose",19:"souce",20:"teeth",21:"umbrella",22:"van",23:"world",24:"xmustree",25:"yellow",26:"zebra"}

# you=dic[n]
# print(f"\nThe value of computer is:{revdic[computer]}\nThe value of user is:{revdic[you]}")


# '''
# o-d-devesh
# 1-s-sarvesh
# -1=r-ramesh

# '''
# n=input("Enter name:").lower()
# dic={'d':0,"s":1,"r":-1}
# rd={0:"devesh",1:"sarvesh",-1:"ramesh"}
# n=dic[n]
# print(f"my name is {rd[n]}")


'''
o--devesh
1--sarvesh
-1=-ramesh

'''
n=int(input("Enter number:"))
rd={0:"devesh",1:"sarvesh",-1:"ramesh"}
print(f"my name is {rd[n]}")



















































# print("Welcome to KD CLUB \nJaha hote hai Sawal Jawab\n ")
# sawals=[
# ["1.devesh upadhyay ke ghar ka name kyaa hai?", "Deepanshu","Himanshu","Dipyanshu","Inme se koi nahee",1],
# ["2.Sarvesh upadhyay ke ghar ka name kyaa hai ?", "Deepanshu","Himanshu","Dipyanshu","Inme se koi nahee",2],
# ["3.ramesh upadhyay ke ghar ka name kyaa hai ?", "Deepanshu","Himanshu","Dipyanshu","Inme se koi nahee",4],
# ["4.Mahesh upadhyay ke ghar ka name kyaa hai ?", "Deepanshu","Himanshu","Dipyanshu","Inme se koi nahee",4],
# ]

# level=[100,200,300,400]
# money=0
# for i in range(len(sawals)):
#     sawal=sawals[i]
#     print(f"Question for Rs.{level[i]}\n{sawal[0]}")
#     print(f"A.{sawal[1]}    B.{sawal[2]} ")
#     print(f"C.{sawal[3]}    D.{sawal[4]} ")
#     reply=int(input("Choose your answer Or 0 to Quit: "))
#     if reply==0:
#         money=level[i-1]
#         break
#     if reply==sawal[-1]:
#         print(f"Correct Answer ! you won Rs.{level[i]}")
#     else:
#         print("Wrong Answer")
# print(f"Your Take home Money is {money}")