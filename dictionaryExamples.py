# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 21:34:28 2020

@author: yagmurkaraman
"""

####################    DATA STRUCTURES - DICTIONARY    ####################
### contains different types, like list and tuple
### unchangeable
### out of order
### key, value

dictionary = {"REG": "Regresyon Modeli",
              "LOJ": "Lojistik Regresyon",
              "CART": "Classification and Reg"}

print(len(dictionary)) #prints 3

#value can be list
dictionary = {"REG": ["RMSE", 10],
              "LOJ": ["MSE", 20],
              "CART": ["SSE", 30]}

print(len(dictionary)) #prints 3


### access to dictionary elements ###
### can be access to elements with key, rather than index like list and tuple
dictionary = {"REG": ["RMSE", 10],
              "LOJ": ["MSE", 20],
              "CART": ["SSE", 30]}

dictionary["REG"] #returns 10 (value)

### dictionary in dictionary element
dictionary = {"REG": {"RMSE": 10,
                      "MSE": 20,
                      "SSE": 30},
              
              "LOJ": {"RMSE": 10,
                      "MSE": 20,
                      "SSE": 30},
              
              "CART": {"RMSE": 10,
                      "MSE": 20,
                      "SSE": 30}}

dictionary["REG"]["RMSE"] #returns 10


###############   add & change   ###############
dictionary = {"REG": "Regresyon Modeli",
              "LOJ": "Lojistik Regresyon",
              "CART": "Classification and Reg"}

### add
dictionary["GBM"] = "Gradient Boosting Mac" #add new element

### change
dictionary["REG"] = "Coklu Dogrusal Regresyon" #change exist elements value

### may contains differen types
dictionary[1] = "Yapay Sinir Aglari" #added

typeList = [1]
dictionary[typeList] = "new element" #TypeError: unhashable type: 'list', because list is changeable

typeTuple = (1)
dictionary[typeTuple] = "new element" #tuple can be assigned as key