# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 16:00:15 2020

@author: yagmurkaraman
"""

####################    OOP With Python    ####################
#Python is an object oriented programming language.
#Almost everything in Python is an object, with its properties and methods.
#A Class is like an object constructor, or a "blueprint" for creating objects.

# class attributes
class DataScientist():
    #attributes
    department = ""
    sqlKnowledge = "yes"
    experienceYear = 0
    programmingLanguages = []
    
# access to class attributes
print(DataScientist.department)
print(DataScientist.sqlKnowledge)
print(DataScientist.experienceYear)
print(DataScientist.programmingLanguages)

# change class attributes
DataScientist.sqlKnowledge = "no"
print(DataScientist.sqlKnowledge) #prints 'no'

# class instantiation
dataScientist1 = DataScientist()
print(dataScientist1.sqlKnowledge) #prints 'no'

dataScientist1.programmingLanguages.append("Python")
dataScientist1.programmingLanguages.append("Java")
print(dataScientist1.programmingLanguages) #prints ['Python', 'Java']

dataScientist2 = DataScientist()
#prints ['Python', 'Java'], changed class attributes, wrong!
print(dataScientist2.programmingLanguages) 

print(DataScientist.programmingLanguages) #prints ['Python', 'Java'], WRONG!

# instance attributes
# __init__(self)
class DataScientist():
    #default class attributes
    programmingLanguages = ["R", "PYTHON"]
    department = ""
    sqlKnowledge = "yes"
    experienceYear = 0
    # self represents each class instance attributes
    def __init__(self): #this means, each instance attributes
        self.programmingLanguages = []
        self.department = ""
        
dataScientist1 = DataScientist()
print(dataScientist1.programmingLanguages) #prints []

dataScientist2 = DataScientist()
print(dataScientist2.programmingLanguages) #prints []

dataScientist1.programmingLanguages.append("Python")
print(dataScientist1.programmingLanguages) #prints ['Python']

dataScientist2.programmingLanguages.append("Java")
print(dataScientist2.programmingLanguages) #prints ['Java']

print(DataScientist.programmingLanguages) #prints ['R', 'PYTHON'], class own attribute

dataScientist1.department = "Math"
dataScientist2.department = "Engineer"

print(dataScientist1.department) #prints Math
print(dataScientist2.department) #prints Engineer
print(DataScientist.department) #prints nothing


# instance methods
class DataScientist():
    #attributes
    workers = []
    def __init__(self):
        self.department = ""
        self.programmingLanguages = []
    def addLanguage(self, newLanguage): #instance method, self represents each instance, belong to class
        self.programmingLanguages.append(newLanguage)
   
dataScientist1 = DataScientist()
print(dataScientist1.department) #prints nothing
print(dataScientist1.programmingLanguages) #prints [] 

dataScientist2 = DataScientist()
print(dataScientist2.department) #prints nothing
print(dataScientist2.programmingLanguages) #prints []

#DataScientist.addLanguage("R") #TypeError: addLanguage() missing 1 required positional argument: 'newLanguage'
dataScientist1.addLanguage("R")
print(dataScientist1.programmingLanguages) #prints ['R'] 

dataScientist2.addLanguage("Python")
print(dataScientist2.programmingLanguages) #prints ['Python']


# inheritance structure
# Inheritance allows us to define a class that inherits all the methods and properties from another class
class Employees():
    def __init__(self, FirstName, LastName, Address):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Address = Address
        
class DataScience(Employees):
    def __init__(self):
        self.Programming = ""

class Marketing(Employees):
    def __init__(self):
        self.StoryTelling = ""

dataScientist = DataScience() 
dataScientist.FirstName = "yagmur" #inherits from Employees class
print(dataScientist.FirstName) #prints 'yagmur'

employee = Employees("yagmur", "karaman", "turkey")
print(employee.Address) #prints 'turkey'

### ENF OF FILE ###