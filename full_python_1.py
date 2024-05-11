#-----------------#
#Boolean 

# name = ""
# print(name.isspace())

# print(100>200)

# print(100>90)

# #true values
# print(bool("ghaith"))
# print(bool(10))
# print(bool(10.5))
# print(bool(True))

# #False values 
# print(bool(""))
# print(bool(0))
# print(bool(False))
# print(bool([]))

#-----------------#
#Boolean Operators 

# age = 20 
# country = "syria"
# rank = 15 

# #and
# print(age>15 and country == "syria" and rank >10) #True
# print(age>15 and country == "KSA" and rank >10) # False

# #or
# print(age>25 or country == "syria" ) #True
# print(age>50 or country == "KSA" or rank >10) # True 

# #not 
# print(age >15) 
# print(not age>15 )


#-------------------#
#assigment operators 

# x = 10 
# y = 20
# z = x - y 
# print(z)

# x += y 
# print(x)

# y -= x 
# print(y)

#---------------------#
# Type conversion

# a = 10 
# print(type(a))
# print(type(str(a)))

# print("#"*50)

# c = "GHAITH" #string
# d = [1 , 2 , 3 , 4 , 5] #list
# e = {"A" , "B" , "C"} #set
# f = {"A": 1 , "B" : 2} #dictionary 

# print(tuple(c))
# print(tuple(d))
# print(tuple(e))
# print(tuple(f))

# print("#"*50)

# c = "GHAITH" #string
# d = (1 , 2 , 3 , 4 , 5) #Tuple
# e = {"A" , "B" , "C"} #set
# f = {"A": 1 , "B" : 2} #dictionary 

# print(list(c))
# print(list(d))
# print(list(e))
# print(list(f))

#--------------------#
#User input

#input("HELLO PYTHON")

# Fname = input ("what is your first name ? ")
# Mname = input ("what is your middle name ? ")
# Lname = input ("what is your last name ? ")

# # for delete spaece and capital first letter 
# Fname = Fname.strip().capitalize() 
# Lname = Lname.strip().capitalize()

# print(f'Hello {Fname} {Mname.strip().capitalize():.1s} {Lname} Happy to see you ')

# #--------------------#

# theName = input("what is your name ?   ")
# theEmail = input("what is your Email ?   ")

# theUserName = theEmail[:theEmail.index("@")]
# theWibsite = theEmail[theEmail.index("@") +1 :]

# print(f"Hello {theName} your Email is {theEmail}")
# print(f"your user name is {theUserName}")
# print(f"your Wibsite is {theWibsite}")

# Email = "muhbanifuture@gmail.com"
# print(Email[0:Email.index("@")])

#----------------------------------------------------#

#if , else , elif : 

# uName = "Ghaith"
# uCountry = "Syria"
# cName = "python"
# cPrice = 100 
# cDiscount = 30 

# if uCountry == "Egypt" : 

    

#     print(f"Hello {uName} because you are from {uCountry} ")
#     print(f"the course \"{cName} \" price is:  {cPrice - 60}$")

# elif uCountry == "Syria" :
#     print(f"Hello {uName} because you are from {uCountry} ")
#     print(f"the course \"{cName} \" price is:  {cPrice - 80}$")


# else :
#     print(f"Hello {uName} because you are from {uCountry} ")
#     print(f"the course \"{cName} \" price is:  {cPrice - 20}$")

#----------------------#

#practical membership control 

# List contains Admins 

# admin = ["Ghaith" , "Ahmad" , "Osama" , "Zayd" , ]

# # Login
# name = input("Please type your name :").strip().capitalize() 

# if name in admin : 
#     print(f"Hello {name} welcome back admin  ")

#     option = input("Delete or update your name ? ").capitalize().strip()

#     if option == "Update"  :
#         theNewName = input("please write your new name :")
#         admin[admin.index(name)] = theNewName
#         print("name updated ")
#         print(admin)

#     elif option == "Delete" :
#         admin.remove(name)
#         print("your name deleted")
#         print(admin)

#     else : 
#         print("Wrong option")    

# else : 
#     status  = input("you are not Admin , add you Y , N ? ").strip().capitalize()
#     if status == "Y" or status == "Yes":
#         print("you have been Admin ")
#         admin.append(name)
#         print(admin)
    
#     else :
#         print("you aer not Added.")

#---------------------------------------------------#
# Loop While and else  Trainng  

# myF = ["Gh" , "Os" , "Sj" , "Zy" , "Ab" , "Am" ]
# a = 0

# while a < len(myF):
#     print(f'#{str(a+1).zfill(2)} {myF[a]}' )
#     a+= 1

# else :
#     print("All names printed to screen ")

#---------------#
# # WEbsites
# myFavouritWebs = []
# maximumWbsite = 5 

# while maximumWbsite > 0 : 
#     web = input("Add your website name without https://")
    
#     myFavouritWebs.append(f"https://{web.strip().lower()}  ")
#     maximumWbsite -= 1 
#     print(f"website added , {maximumWbsite} places left")

#     print(myFavouritWebs)

# else : 
#     print("Bookmark is full , you cant add more")


# if len(myFavouritWebs) > 0 :
#     myFavouritWebs.sort()
#     index = 0 
#     print("printing the list of websites in your bookmark ")
    
#     while index < len(myFavouritWebs):
    
#             print(myFavouritWebs[index])
#             index += 1 

#--------------------------------------------------------------#
# Password 

# trise = 4 

# mainPass = '12345' 

# inputPass = input("write your password:  ")

# while mainPass != inputPass : 

#     trise -= 1 

#     print(f"wrong Password , {'last' if trise == 0  else trise } chense left ")

#     inputPass = input("write your password agine :  ")

#     if trise == 0 : 
#         print("All tries is finished. ")

#         break


# else : 
#     print("corecte password welcome")

#----------------------------------------------#
# For loop 


# myNumber = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]

# for number in myNumber : 
#    # print(number)
    
#     if number %2 == 0 :
#         print(f"the number  { number }  is even number ")

#     else :
#         print(f"the number  { number }  is odd number ")

#----------------------------------------------------------#

# myRange = range(1 , 101)

# for i in myRange :
#     print(i)

# Dimention
# mySkills = {
#     "python" : "40%" , 
#     "c#" : "20%" , 
#     "c" : "50%" , 
#     "java" : "10%"
# }

# print(mySkills["c"])
# print(mySkills.get("c#"))

# for  i in mySkills : 
#     print(i) 
    # print(f"My progress in lang {i} is : {mySkills[i]}")

#--------------------------------------------------------------------#
# Nested loob (for)

# pepools = { "Ghaith" : {"c":"90%" , "c#" : "30%" , "python" : "40%"} ,
# "Osama" : {"Html":"60%" , "Css" : "50%" , "Sql" : "20%"} ,
# "sayed" : {"Js":"80%" , "R" : "10%" , "java" : "70%"} ,}

# print(pepools["Ghaith"])
# print(pepools["Osama"])
# print(pepools["sayed"])

# print(pepools["Ghaith"]['c'])
# print(pepools["Osama"]['Html'])
# print(pepools["sayed"]['Js'])

# for name in pepools :
#     print(f"Skills and progress for {name} is :")

#     for skill in  pepools[name] : 
#         print(f"{skill} => { pepools[name][skill]}")

#------------------------------------------------------#

# Break , Continue , Pass 

# MyNumber = [1 , 2 , 3 , 4 , 5 , 6 , 10 , 13 , 14 , 15 , 19 ]

# Continue 

# for number in MyNumber : 
#     if number == 13 : 
#         continue 
#     print(number)

# print("#"*50)

# # Break 

# for number in MyNumber:
#     print(number)
#     if number == 13 : 
#         break 

# print("#"*50)

# # Pass

# for number in MyNumber:
#     print(number)
#     if number == 13 :
#         pass 

#----------------------------------------#
# Loop Advanced Dictionary

# mySkills = {  
#     "c":"90%" ,
#     "c#" : "30%" ,
#     "python" : "40%"
# }

# print (mySkills.items())

# for skill in mySkills : 
#     print(f"{skill} => {mySkills[skill]}")

# for skill_key , skill_progress in mySkills.items():

#     print(f"{skill_key} => {skill_progress}")

# myUltimateSkills = { "Ghaith" : {
# "c":"90%" , "c#" : "30%" , "python" : "40%"} ,
# "Osama" : {
# "Html":"60%" , "Css" : "50%" , "Sql" : "20%"} 
# }

# for main_key , main_value in myUltimateSkills.items():
#     print(f"{main_key} => progress is :")

#     for childe_key , childe_value in main_value.items():
#         print(f"- {childe_key} => {childe_value}")

#------------------------------------------#

# print "*" tringel but have an error 

# n = int(input("bir sayi giriniz : "))
# i = 0 
# j = 0 

# for i in range (0 , n) :
#     if i < n :
#         i = i + 1  
#         for j in range (0 , i) :
#                 if j <= i :
#                     j = j + 1 
#                     print("*")



#----------------------------------------#
#? Function and Return #?

# def first_function() : 

#     return "Hello python form inside function"

# print(first_function())

#--------------------------------#
# Function parameters 

# # name                      => Parameter 
# # say_hello("GHAITh")       => Argument 


# a , b , c = "GHAITH" , "AHMAD" , "OSAMA"

# def say_hello(name): 
#     print(f"HEllo {name }")

# say_hello("GHAITh")

#---------------------------------#
# Function packing and unpaking Arguments " '*' for list or tuple"

# mylist = [1 , 2 , 3 , 4 ]
# print (mylist)
# print(*mylist)

# def say_Hello (n1 , n2 , n3 ):
#     peoples = [n1 , n2 , n3 ]

#     for name in peoples : 
#         print(f"Hello {name}")

# say_Hello("Ghaith" , "Amir" , "Zayd" )
# _______________________________________ # 

# def say_Hello (*peoples ): #   n1 , n2 , n3

#     for name in peoples : 
#         print(f"Hello {name}")

# say_Hello("Ghaith" , "Amir" , "Zayd" , "omer")

# def show_Skills (name , *Skills):
#     print(f"Hello {name} your Skills is : ")

#     for skill in Skills :
#         print (skill)


# show_Skills("GHaith" , "C" , "#C" , "Python")
# show_Skills("Ahmad" , "C" , "#C" , "Python")

#----------------------------------------------#
# Function Default Parameters 

# def Say_Hello(name = "Unknow" , age = "Unknow" , country = "Unknow"):
#     print(f"Hello {name} your age is {age} and your country is {country}")

# Say_Hello("ghaith" , 19 , "syria")   
# Say_Hello("zayd" , 10 ) 
# Say_Hello("Osama") 
# Say_Hello() 

#------------------------------------------------#
# Function packing , Unpacking keyword Arguments " '**' for dictionry"

# def show_Skills (*skills): 
#     print(type(skills))
#     for skill in skills :
#         print (f"{skill}")

# show_Skills("Python" , "C" , 'C#')        

# mySkills = {"Python" : "50%"  , "C" : "40%" , "Js" : "30%"}
# def show_Skills (**skills): 
#     print(type(skills))

#     for skill , value in skills.items() :
#         print (f"{skill} ==> {value}")

# show_Skills(Python = "50%"  , C = "40%" , Js = "30%")        
# show_Skills(**mySkills)

#-----------------------------------------------------#
# Function packing , unpacking Arguments trainings

# mySkills = {"Python" : "50%"  , "C" : "40%" , "Js" : "30%"}
# show_Skills = ("Python" , "C" , 'C#')

# def show_skills(name , *skills , **skillsWithprogres):
#     print(f"Hello {name}\n skills without progress is :")

#     for skill in skills:
#             print(f" - {skill}")

#     print ("skills with progress is : ")

#     for skill_key , skill_value in skillsWithprogres.items():

#         print(f"- {skill_key} => {skill_value}")

# show_skills("GHaith" , *show_Skills , **mySkills )

#---------------------------------#
# Function Scope

# x = 1 

# print(f"print variable {x}")

# def one() :
#     global x
#     x = 2 
#     print (f"print variable in function one {x}")


# def tow():
#     x = 4 
#     print (f"print variable in function tow {x}")


# one()
# print(f"print variable from global scope {x}")
# tow()

#----------------------------------------------------------#
#? Function Recursion #?


# def cleanWord(word) :
#     if len(word) == 1 :

#         return word 

#     if word[0] == word[1]: 

#         return cleanWord(word[1: ])

#     return word[0] + cleanWord(word[1:])

# print(cleanWord("wwwoooorrrldd"))

#--------------------------------------------------#
# Function => lambda 
# Anonymous Fucntion 

# def say_hello(name): return f"Hello {name}"

# hello = lambda name : f"Hello {name}"

# print(say_hello("GHAITH"))
# print(hello("GHAITH"))

#--------------------------------------------------#