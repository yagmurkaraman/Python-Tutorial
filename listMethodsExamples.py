# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 23:35:53 2020

@author: yagmurkaraman
"""

###############   add & change & delete   ###############
list = ["apple", "orange", "banana", "peach"]
print(list) #prints ['apple', 'orange', 'banana', 'peach']

### change ###
list[1] = "mango" #change index 1 as mango
print(list) #prints ['apple', 'mango', 'banana', 'peach']

list[0:3] = "pear", "lemon", "berry" #change index 0, 1, 2
print(list) #prints ['pear', 'lemon', 'berry', 'peach']

### add ###
list = list + ["melon"] #adds "melon" to last element
print(list) #prints ['pear', 'lemon', 'berry', 'peach', 'melon']

### delete ###
del list[2] #deletes index 2, "berry"
print(list) #prints ['pear', 'lemon', 'peach', 'melon']


###############  append & remove methods   ###############
list = ["apple", "orange", "banana", "peach"]
print(dir(list)) #prints avaliable list methods

list.append("pear") #appends "pear" to last of list
list.remove("pear") #removes "pear" element


###############  insert & pop methods   ###############
list = ["apple", "orange", "banana", "peach"]
list.insert(0, "pear") #inserts "pear" to index 0
print(list) #prints ['pear', 'apple', 'orange', 'banana', 'peach']

list.insert(3, "melon") #inserts "melon" to index 3
print(list) #prints ['pear', 'apple', 'orange', 'melon', 'banana', 'peach']

list.insert(len(list), "berry") #inserts "berry" to last index of list
print(list) #prints ['pear', 'apple', 'orange', 'melon', 'banana', 'peach', 'berry']

list.pop(0) #deletes index 0
print(list) #prints ['apple', 'orange', 'melon', 'banana', 'peach', 'berry']

list.pop(4) #deletes index 4
print(list) #prints ['apple', 'orange', 'melon', 'banana', 'berry']


###############  other common methods   ###############
list = ["apple", "orange", "banana", "peach"]

#count
print(list.count("apple")) #prints 1
print(list.count("banana")) #prints 1 
print(list.count("orange")) #prints 1
print(list.count("melon")) #prints 0

#copy
copyList = list.copy()
print(copyList) #prints ['apple', 'orange', 'banana', 'peach']

#extend
list.extend(["melon", "berry", 32]) #add end of the list
print(list) #prints ['apple', 'orange', 'banana', 'peach', 'melon', 'berry', 32]

#index
print(list.index("banana")) #prints 2
print(list.index("orange")) #prints 1

#reverse
list.reverse() #reverse the list
print(list) #prints [32, 'berry', 'melon', 'peach', 'banana', 'orange', 'apple']

#sort
list = [43, 12, 26, 34, 5]
list.sort()
print(list) #prints [5, 12, 26, 34, 43]

#clear
list.clear()
print(list) #prints []


#END OF FILE