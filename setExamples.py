# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 22:03:20 2020

@author: yagmurkaraman
"""

####################    DATA STRUCTURES - SETS    ####################
### out of order
### unique elements
### changeable
### performance

setEx = set() #creates a set

listEx = [1, "hello", "yagmur", 9]
setEx = set(listEx)
print(setEx) #prints {1, 'hello', 'yagmur', 9}

tupleEx = (1, "hello", "yagmur", 9)
setEx = set(tupleEx)
print(setEx) #prints {1, 'hello', 'yagmur', 9}

strEx = "hello world"
setEx = set(strEx)
print(setEx) #prints {'h', 'd', 'l', 'w', 'r', 'o', 'e', ' '}

listEx = ["hello", "world", "welcome", "hello", "apple", "world"]
setEx = set(listEx)
print(setEx) #prints {'hello', 'world', 'apple', 'welcome'}


###############   add & remove   ###############
listEx = ["hello", "world"]
setEx = set(listEx)

### add
setEx.add("welcome")
print(setEx) #prints {'hello', 'world', 'welcome'}

setEx.add("apple")
print(setEx) #prints {'hello', 'world', 'apple', 'welcome'}

setEx.add("welcome") #not added again because already exist
print(setEx) #prints {'hello', 'world', 'welcome'}


### add
setEx.remove("apple")
print(setEx) #prints {'hello', 'world', 'welcome'}

#setEx.remove("apple") #KeyError: 'apple' 
setEx.discard("apple") #not generated error although removed
print(setEx) #prints {'hello', 'world', 'welcome'}