# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 14:04:02 2024

@author: anekl
"""

#Exercise 2.25 
#Investigate a for loop over a changing list 

numbers = range(10)
print(numbers)                  #prints range(0,10) = 0-9 

for n in numbers: 
    i = len(numbers)/2 
    del numbers[i] 
    print("n = %d, del %d" % (n,i), numbers)

#i første runde: 
#for hver n i numbers: 
    #i er lengden på numbers/2 = 5 
    #slett numbers index 5 = tallet 5 
    #print n=0, del 5, [0,1,2,3,4,6,7,8,9]
#loopen fortsetter sånn og sletter tall. 

#Warning: never modify a list we are looping over. 
