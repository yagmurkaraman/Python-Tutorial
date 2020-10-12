# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 22:52:56 2020

@author: yagmurkaraman
"""

####################    DATA STRUCTURES    ####################

###    []     ###
###  list()   ###
grades = [80, 90, 60, 70]
print(type(grades))  #prints 'list'

exList = ['a', 13, 8.2, grades]
print(exList) #prints exList with grades array
print(len(exList)) #prints 4


### types of list ###
print(exList[0]) #prints 'a'
print(exList[1]) #prints 13
print(exList[2]) #prints 8.2
print(exList[3]) #prints [80, 90, 60, 70, 65, 87, 93, 74]

print(type(exList[0])) #prints 'str'
print(type(exList[1])) #prints 'int'
print(type(exList[2])) #prints 'float'
print(type(exList[3])) #prints 'list'


### list in list ###
allList = [grades, exList]
print(allList)

del allList #deletes allList
#print(allList) #NameError: name 'allList' is not defined


### access to list elements ###
grades = [50, 60, 70, 80, 90]
print(grades[0]) #prints 50
print(grades[1]) #prints 60
print(grades[0:2]) #prints 50, 60
print(grades[:2]) #prints 50, 60 --> same grades[0:2]
print(grades[2:]) #prints 70, 80, 90

grades = ['a', 40, [50, 60, 70, 80, 90]]
#print(grades[3]) #IndexError: list index out of range
print(grades[2]) #prints [50, 60, 70, 80, 90]
print(grades[0:2]) #prints ['a', 40]
print(grades[2][3]) #prints 80, 2d list


### END OF FILE ###