# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 22:55:18 2020

@author: yagmurkaraman
"""

####################    Exceptions    ####################
#The try block lets you test a block of code for errors.
#The except block lets you handle the error.

#ZeroDivisionError
numberA = 10
numberB = 0

try: #try to run
    print(numberA/numberB) #waits throw to exception for numberB is zero
except ZeroDivisionError:
    print("denominator cannot be zero")
    

#TypeError
numberA = 10
numberB = "2"

try:
    print(numberA/numberB)
except TypeError:
    print("calculate with numbers")
    
### ENF OF FILE ###