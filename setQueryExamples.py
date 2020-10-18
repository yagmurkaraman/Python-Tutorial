# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 21:32:18 2020

@author: yagmurkaraman
"""
# =============================================================================
# ####################    DATA STRUCTURES - SETS    ####################
# =============================================================================

#########   difference() & symmetric_difference()   #########

### difference
setEx1 = set([1, 3, 5])
setEx2 = set([1, 2, 3])

setExDiff = setEx1.difference(setEx2) #set1 has but set2 not
print(setExDiff) #prints {5}

setExDiff = setEx2.difference(setEx1) #set2 has but set1 not
print(setExDiff) #prints {2}

### symmetric_difference
setExSymmDiff = setEx1.symmetric_difference(setEx2) #elements not in both
print(setExSymmDiff) #prints {2, 5}


#########   intersection & union   #########
setEx1 = set([1, 3, 5])
setEx2 = set([1, 2, 3])

### intersection
setExInter = setEx1.intersection(setEx2)
print(setExInter) #prints {1, 3}

setExInter = setEx1 & setEx2
print(setExInter) #prints {1, 3}

### union
setExUnion = setEx1.union(setEx2)
print(setExUnion) #prints {1, 2, 3, 5}

### intersection_update
setEx1.intersection_update(setEx2) #update first set
print(setEx1) #prints {1, 3}


#########   some query operations   #########
setEx1 = set([7, 8, 9])
setEx2 = set([5, 6, 7, 8, 9, 10])

isInterEmpty = setEx1.isdisjoint(setEx2) #is intersection set empty control
print(isInterEmpty) #prints False

isSubSet = setEx1.issubset(setEx2) #is set1 subset of set2
print(isSubSet) #prints True

isSuperSet = setEx2.issuperset(setEx1) #is set2 superset of set1
print(isSuperSet) #prints True