# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 21:19:58 2020

@author: yagmurkaraman
"""

####################    DATA STRUCTURES - TUPLE    ####################
### difference from list -> unchangeable
### tuple()

exTuple = ("yagmur", "karaman", 1995, 14.2, [1, 2, 3, 4]) #contains different types, like list
exTuple = "yagmur", "karaman", 1995, 14.2, [1, 2, 3, 4] #contains different types, like list

exTuple = ("yagmur",) #if single, put a comma end of element
print(type(exTuple)) #prints 'tuple'


###############   access to elements   ###############
### same as list

exTuple = ("yagmur", "karaman", 1995, 14.2, [1, 2, 3, 4]) 

print(exTuple[2]) #prints 1995
print(exTuple[0:2]) #prints 'yagmur', 'karaman'

exTuple[3] = 23 #TypeError: 'tuple' object does not support item assignment