# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 23:06:08 2020

@author: Burcum
"""


def calc():
    calc_grade=grades["midterm"]*0.30+grades["final"]*0.50+grades["project"]*0.20
    return calc_grade
    
myList=["Ali Veli","Hatice Netice"]
right=2

for i in range(3):
 name=input("enter your name please: ").capitalize()
 surname=input("Enter your surname please: ").capitalize()
 full_name=str(name)+str(" ")+str(surname)
 #print(full_name)
 NameList=[]
 NameList=full_name.split("~")
 #print(NameList)
 compare=list(set(NameList).intersection(set(myList)))
 if list(set(NameList).intersection(set(myList))):
     print("Welcome")
     break
 else:
     print("Incorrect information.You have " + str(right)+" right left.")
 if right == 0:
     print("Please try again later.")
 right -=1
 
if list(set(NameList).intersection(set(myList))):
 courses=["Math","Computer","Science","Music","Cebir"]
 for i in range(len(courses)):
    print(courses[i])
 select_courses=input("Please select at least 3 courses on the list: ").title()
 newList=select_courses.split()
 match_courses=list(set(newList).intersection(set(courses)))
 #print(match_courses)
 if len(match_courses)>=3 and len(match_courses)<=5:
       print("Your courses are: " + select_courses)
       grades={"midterm":100, "final":50, "project":50}
       if calc()>90:
           print("Grade:AA")
       elif 70 <calc()<90:
           print("Grade:BB")
       elif 50 <calc()<70:
           print("Grade:CC")
       elif 30 <calc()<50:
           print("Grade:DD")
       elif calc()<30:
           print("Grade:FF" + "You failed.Take the course again.")
 else:
    print( "You failed in class")





