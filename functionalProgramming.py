# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 17:25:28 2020

@author: yagmurkaraman
"""

##############   Functional Programming with Python    ##############

#example 1: side-effect, impure function
globalVariable = 7

def impureSumFunction(number):
    return number + globalVariable

def pureSumFunction(numberFirst, numberSecond):
    return numberFirst + numberSecond

print(impureSumFunction(5)) #prints depends on globalVariable value, side-effect
print(pureSumFunction(5, 6)) #prints 11 always


###OOP Example
class LineCounter():
    def __init__(self, fileName):
        self.fileName = open(fileName, "r")
        self.lines = []
    def readFile(self):
        self.lines = [line for line in self.file]
    def countLines(self):
        return len(self.lines)
    
lineCounter = LineCounter("example.txt")

print(lineCounter.lines) #prints []
print(lineCounter.countLines()) #prints 0
 
lineCounter.readFile() #this changes the instances, so dangerous

print(lineCounter.lines) #prints lines of file
print(lineCounter.countLines()) #prints count of lines

#line counts and lines changed -> impure

###FP Example
def readFile(fileName):
    with open(fileName, "r") as file:
        return [line for line in file]
    
def countLines(lines):
    return len(lines)

fileLines = readFile("example.txt")
lineCount = countLines(fileLines) 
print(lineCount)
    
#line counts and lines do not change, if file content do not -> pure     

### ENF OF FILE ###