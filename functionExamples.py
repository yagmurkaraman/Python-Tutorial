# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 21:50:04 2020

@author: yagmurkaraman
"""

####################    INTRODUCTION TO FUNCTIONS   ####################

#?print #gets function documentation
print("a", "b", sep = "_") #prints a_b

### create & call function
def takeSquare(number): 
    print(number**2)
    
takeSquare(3) #prints 9
takeSquare(6) #prints 36


### print result with output message
def takeSquare(number): 
    print("Square of the given number: " + str(number**2))
    
takeSquare(3) #prints Square of the given number: 9
takeSquare(6) #prints Square of the given number: 36

def takeSquare(number): 
    print("Given number: " + str(number) + ", Square of the given number: " + str(number**2))
    
takeSquare(3) #prints Given number: 3, Square of the given number: 9
takeSquare(6) #prints Given number: 6, Square of the given number: 36


### two-parameter function
def multiply(firstNumber, secondNumber):
    print(firstNumber * secondNumber)
    
multiply(4, 6) #prints 24


### predefined functions
def multiply(firstNumber, secondNumber):
    print(firstNumber * secondNumber)
    
multiply(4) #prints TypeError: multiply() missing 1 required positional argument: 'secondNumber'

def multiply(firstNumber, secondNumber = 6):
    print(firstNumber * secondNumber)
    
multiply(4) #prints 24

def multiply(firstNumber, secondNumber = 6):
    print(firstNumber * secondNumber)
    
multiply(4, 5) #prints 20


### keep output of function
def operation(firstParam, secondParam, thirdParam):
    return (firstParam + secondParam) / thirdParam

result = operation(25, 30, 40)
print(result)
