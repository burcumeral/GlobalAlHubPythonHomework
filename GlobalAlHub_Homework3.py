# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 02:55:47 2020

@author: Burcum
"""


import random
guess_words=["python","intelligence","artificial","machine","learning"]

def choose_word(guess_words):
    word=(random.choice(guess_words)).upper()
    return word

word=choose_word(guess_words)
right=len(word)-1 #rule1
myList=list(word)
#print(myList)

name=input("To start the game, please enter your name or nickname: ")
print("Welcome "+ name + ". Let's play Hangman. You have " + str(right) + " guesses")


for i in range(0,right):
 letter=input("Enter a letter : ").upper()
 right-=1
 if letter in myList:
        print("Congratulations.There is " + letter + " is in this word")
 else:
        print("Wrong letter")
        print("you have " + str(right) + " right.")
        #print(right)
final=(input("You have no right left.Guess What is the word?")).upper()
if final==word:
    print("Congratulations, You win.Game over.")
else:
    print("Sorry buddy, You lost.Game over.")


