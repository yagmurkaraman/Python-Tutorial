# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 17:58:44 2020

@author: yagmurkaraman
"""

##############   Anonymous Functions    ##############
sumOperation = lambda number1, number2 : number1 + number2
print(sumOperation(6, 8)) #prints 

unorderedList = [('b', 3), ('a', 8), ('d', 12), ('c', 1)]
unorderedList = sorted(unorderedList, key = lambda x : x[1])
print(unorderedList) #prints [('c', 1), ('b', 3), ('a', 8), ('d', 12)]


##############   Vectorel Operations    ##############
### OOP
listA = [1, 2, 3, 4, 5] # -> vector
listB = [2, 3, 4, 5, 6] # -> vector
listAB = []

#multiply vectors items
for index in range(0, len(listA)):
    listAB.append(listA[index] * listB[index])
    
print(listAB) #prints [2, 6, 12, 20, 30]


### Functional Programming 
#easy operations
#less side-effect
#less problems
import numpy as np

listA = np.array([1, 2, 3, 4, 5])
listB = np.array([2, 3, 4, 5, 6])

listAB = listA*listB # -> vectorel operation
print(listAB) #prints [ 2  6 12 20 30]


##############   map & filter & reduce    ##############
#map: results after applying the given function to each item of a given iterable
listA = [1, 2, 3, 4, 5]
listA = list(map(lambda x: x + 10, listA)) #add 10 to each item
print(listA) #prints [11, 12, 13, 14, 15]


#filter: filters the given sequence with the help of a function that tests each element in the sequence to be true or not
listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listA = list(filter(lambda x: x % 2 == 0, listA)) #find even elements
print(listA) #prints [2, 4, 6, 8, 10]


#reduce: used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along
#This function is defined in “functools” module.
from functools import reduce
listA = [1, 2, 3, 4, 5]
listA = reduce(lambda x, y : x + y, listA) #sum all items
print(listA) #prints 15

### ENF OF FILE ###