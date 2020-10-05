# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 21:33:13 2020

@author: yagmurkaraman
"""

### print() function ###
print(9) #prints '9'
print(9.2) #prints '9.2'
print(9+9) #prints '18'
print(9*9) #prints '81'
print("HELLO AI ERA") #prints "HELLO AI ERA" 
print('HELLO AI ERA') #prints 'HELLO AI ERA' /you can write strings with "" or ''


### type() function ###
print(type(9)) #prints 'int'
print(type(9.2)) #prints 'float'
print(type(9+9)) #prints 'int'
print(type(9*9)) #prints 'int'
print(type("HELLO AI ERA")) #prints 'str'


####################    STRINGS    ####################
print("lorem " + "ipsum") #prints 'lorem ipsum'
print("yagmur " * 3) #prints 'yagmur yagmur yagmur '

### len() method ###
exampleStr = "lorem_ipsum"
len(exampleStr) #len() method, finds length of given string
print(len(exampleStr)) #prints '11'

### upper() and lower() methods ###
#upper() converts all of the characters uppercase
#lower() converts all of the characters lowercase
exampleStr = "lorem_ipsum"
print(exampleStr.upper()) #prints 'LOREM_IPSUM'

exampleStr = "LOREM_IPSUM"
print(exampleStr.lower()) #prints 'lorem_ipsum'

print(exampleStr.islower()) #prints False because lenStr is 'LOREM_IPSUM' now
exampleStr = exampleStr.lower() #converts all of the characters lowercase and assigns to lenStr 
print(exampleStr.islower()) #prints True because lenStr is 'lorem_ipsum' now

### replace() method ###
exampleStr = exampleStr.replace("m", "n") #replace m letters as n, and assign to lenStr
print(exampleStr) #prints 'loren_ipsun'

### strip() method ###
exampleStr = "  lorem_ipsum  "
print(exampleStr.strip()) #prints 'lorem_ipsum', removes whitespaces as default

exampleStr = "**lorem_ipsum**"
print(exampleStr.strip("*")) #prints 'lorem_ipsum', removes '*' characters

exampleStr = "lorem_ipsum"
print(exampleStr.strip("lore")) #prints 'm_ipsum', removes 'lore' 

### type methods ###
print(dir(str)) #prints all str methods like contains, strip, swapcase, translate...
print(dir(int)) #prints all int methods like ceil, floor, round, sizeof...



####################    SUBSTRINGS    ####################
exampleStr = "lorem_ipsum"
print(exampleStr[0]) #print 0. index, 'l'
#print(exampleStr[15]) #IndexError: string index out of range
print(exampleStr[0:3]) #print 'lor': first 3 characters
print(exampleStr[3:12]) #print 'em_ipsum'


#### ENF OF FILE ####