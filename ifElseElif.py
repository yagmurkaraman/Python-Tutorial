# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 23:09:13 2020

@author: yagmurkaraman
"""

####################    True & False Conditions   ####################

### if & else
limit = 50000
income = 40000

if income < limit:
    print("income is less than limit")
else:
    print("income is greater than limit")
    
    
### elif
limit = 50000
income1 = 60000
income2 = 50000
income3 = 40000

if income1 > limit:
    print("congratulations, you win") #prints this message
elif income1 < limit:
    print("warning!")
else:
    print("continue...")
    
##############################    
if income2 > limit:
    print("congratulations, you win") 
elif income2 < limit:
    print("warning!") 
else:
    print("continue...") #prints this message
    
##############################    
if income3 > limit:
    print("congratulations, you win") 
elif income3 < limit:
    print("warning!") #prints this message
else:
    print("continue...")
    

####################    simple application   ####################
limit = 50000
storeName = input("enter store name: ")
income = int(input("enter your income: "))

if income > limit:
    print("congratulations: " + storeName + ", you won a promotion!") 
elif income < limit:
    print("warning! low income: " + str(income))
else:
    print("continue...")