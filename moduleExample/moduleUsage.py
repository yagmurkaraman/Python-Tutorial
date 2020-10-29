# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 22:38:22 2020

@author: yagmurkaraman
"""

##############   module/library/package    ##############
# three different usage way
import ModuleSalary
ModuleSalary.newSalaryCalculate(1000)
ModuleSalary.newSalaryCalculate(2000)


import ModuleSalary as ms
ms.newSalaryCalculate(1000)
ms.newSalaryCalculate(2000)


from ModuleSalary import newSalaryCalculate
newSalaryCalculate(1000)
newSalaryCalculate(2000)


import ModuleSalary as ms
print(ms.salaries) #prints [1000, 2000, 3000, 4000, 5000]

### ENF OF FILE ###