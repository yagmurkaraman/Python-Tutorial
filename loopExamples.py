# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 14:15:55 2020

@author: yagmurkaraman
"""

####################    FOR & WHILE Loops    ####################
fruits = ["apple", "orange", "strawberry", "melon"]

print(fruits[0]) #prints apple
print(fruits[1]) #prints orange
print(fruits[2]) #prints strawberry
print(fruits[3]) #prints melon

for item in fruits: #item -> represents each item in fruits list
    print(item) #prints each item in fruits list
    

#function example with for loop
salaries = [1000, 2000, 3000, 4000, 5000]    

def calculateNewSalary(salary):
    newSalary = salary + salary * 0.2
    return newSalary
    
def findNewSalaries():
    for item in salaries:
        print(calculateNewSalary(item)) #prints 1200, 2400, 3600, 4800, 6000
    
findNewSalaries()


#an example with if, for, function 
salaries = [1000, 2000, 3000, 4000, 5000]    

def salaryForLow(item):
    return item + item*0.2

def salaryForHigh(item):
    return item + item*0.1

def findNewSalaries():
    for item in salaries:
        #print(item)
        if item >= 3000:
            print(salaryForHigh(item))
        else:
            print(salaryForLow(item))
            
findNewSalaries() #new salaries: 1200, 2400, 3300, 4400, 5500


# break & continue
salaries = [8000, 5000, 2000, 1000, 3000, 7000, 1500]
salaries.sort() #sorted salaries as ascending

#prints 1000, 1500, 2000
for item in salaries:
    if item == 3000:
        print("exit")
        break #exit from for loop
    print(item)

#prints 1000, 1500, 2000, 5000, 7000, 8000
for item in salaries:
    if item == 3000:
        continue #skip print and return beginning of for
    print(item)
    

# while
number = 1
#prints 2, 3, 4, 5, 6, 7, 8, 9, 10
while number < 10:
    number += 1
    print(number)
    
number = 1
#prints 1, 2, 3, 4, 5, 6, 7, 8, 9
while number < 10:
    print(number)
    number += 1