# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 22:54:41 2020

@author: yagmurkaraman
"""

################    TYPE CONVERSATIONS    ################
firstNumber = input() #get input from user, example 8
secondNumber = input() #get input from user, example 6

print(type(firstNumber)) #prints 'str'

sumResult = firstNumber + secondNumber #concatenates two numbers
print(sumResult) #prints '86'

sumResult = int(firstNumber) + int(secondNumber) #adds two numbers
print(sumResult) #prints '14'

#######################################################
print(int(12.0)) #prints 12
print(float(12)) #prints 12.0

################     print() Function     ################
print("lorem", "ipsum") #prints 'lorem ipsum', default adds whitespace
print("lorem", "ipsum", sep = "_") #prints 'lorem_ipsum'

?print #lists all varieties of print method