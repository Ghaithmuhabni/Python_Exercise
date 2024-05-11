# def power (n,p):
#     if p == 0: 
#         return 1
#     return (n*power(n,p-1))
# print(power(10,3))

#############################

# def factorial(n):
#     if (n==1 or n==0):
#         return 1 
#     return(n*factorial(n-1))
# print(factorial(6))
##############################

# def Cift_Sayilar(**Cift):
#     Cift = {"a":2,
#             "b":8,
#             "c":3,
#             "d":15
#     }
#     cift = []
#     tek = []
#     for elements in Cift.values():
#         if elements%2==0 :
#             cift.append(elements)
#         else: tek.append(elements)
#     print(f"cift sayilar {cift}\ntek sayilar {tek}")
# Cift_Sayilar()
################################

# a = [1,2,3]
# b=a 
# print(a is b , a==b)
#################################

# k = int(input("bir rakam giriniz : "))
# test_list = [(4,4) , (5,6) , (1,3) , (0,0) , (7,7) , (6,3) , (5,5)] 
# for i in (test_list):
#     for j in range (len(i)-1):
#         if k == i[j] and k == i[j+1] :
#             test_list.remove(i)
# print(test_list)
#################################

# x = [1,2,3]
# for i in range (len(x)) :
#     for j in range (len(x)) :
#         for k in range (len(x)) :
#             if(i!=j and i!=k and j!=k) : 
#                 print(x[i],x[j],x[k])
#################################

# list  = [["c",1983,"a"],
#         ["pythn",1987,"c"],
#         ["java",1990,"d"],
#         ["html",1957,"b"]]
# print (sorted(list, key = lambda i: i[1]))
#################################

# R = int(input("Enter the number of rows:"))
# C = int(input("Enter the number of columns:"))

# matrix = []
# print("Enter the entries rowwise:")

# for i in range(R):
# 	a =[]
# 	for j in range(C):
# 		a.append(int(input()))
# 	matrix.append(a)

# for i in range(R):
# 	for j in range(C):
# 		print(matrix[i][j], end = " ")
# 	print()
################################

# test_list = [["6gh",3],['best',1]]
# cus = [1,2]
# test_list[0].append(cus[0])
# test_list[1].append(cus[1])
# print(test_list)

# x = zip(test_list,cus)
# print(list(x))
################################

# giris = [1,1,2,2,3,3,4,4,5,5,5]
# cikis = []
# coppy=[]

# for i in range(len(giris)):
#     s=str(giris[i])
#     coppy.append(s)
    
# for i in range(len(coppy)):
#     if coppy[i] not in cikis:
#        tmp=list(coppy[i])
#        cikis.append(tmp*coppy.count(coppy[i]))
#        print()
# print(cikis)
# yeni=[]
# for z in cikis:
#     if z  not in yeni:
#         yeni.append(z)
#     else:
#         continue

# print(yeni)
# yenn=[]
# for i in range(len(yeni)):
#    yenn.append([int(yeni[i][j])for j in range(len(yeni[i]))])
# print(yenn)
#############################3

# m = int(input("Enter the number of rows:"))
# n = int(input("Enter the number of columns:"))
# val = [0] * n
# for x in range (n):
#     val[x] = [0] * m
# print(val)

###########################

# sutun = int(input("Enter size of column: "))
# satir = int(input("Enter size of row: "))

# a = []
# b = []
# for j in range(0, sutun):
#     b.append(0)
# for i in range(0, satir):
#     a.append(b)
# print(a)
###################################

# import random as rand
# # matres rasgele sayilar atiyor 
# m = int(input("satir : "))
# n = int(input("sutun : "))
# Mat = []
# toplam = []
# max_sayi = 0 

# for i in range(0,m):
#     Mat.append([])
#     for j in range(0,n):
#         Mat[i].append(j)
#         Mat[i][j] = rand.randint(1,100)
# print(Mat)

# # max sayi 
# for i in range(0,m):
#     for j in range(0,n):
#         if Mat[i][j]>max_sayi:
#             max_sayi = Mat[i][j]
# print(f"en buyuk sayi = {max_sayi}")
# # aritmatik ort.
# for i in range(m) : 
#     for j in range(n) :
#         toplam.append(Mat[i][j])
# x=(sum(toplam))/(len(toplam))
# print(f"aritmatik ort. = {x}")
###############################

# import cv2
# min = 999
# s = []
# im = cv2.imread(r"c:\Users\mouhb\OneDrive\Desktop\liner\10e278a6-7ecd-4918-ab43-022f2a6c3b12.jpg")
# cv2.imshow('Al 5ra',im)
# cv2.waitKey()
# image = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# r , c = image.shape
# print(c)
# print(r)

# for i in range(r):
# 	for j in range(c):
# 		if image[i][j] < min:
# 			min = image[i][j]
# 			a=[i,j]
# 			s.append(a)
# print(s)

# print("en az seyah noktasinda ",min)