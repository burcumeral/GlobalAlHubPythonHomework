# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

myList=[]
Name=input("Your Name : ")
myList.append(Name)
Surname=input("Your Surname : ")
myList.append(Surname)
Age=int(input("Your Age : "))
myList.append(Age)
Birthyear=int(input("Your Birthyear : "))
myList.append(Birthyear)

for i in myList:
 print(i)

if myList[2]<0:
    print("Invalid Age")
else:
    if myList[2]<18:
        print("You can't go out because it's too dangerous")
    else:
        print("You can go out to the street")