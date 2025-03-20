# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 12:46:40 2024

@author: anekl
"""
#exercise 2.10 

a = [1,3,5,7,11]                #print list A
b = [13,17]                     #print list B
c = a + b                       #a new list C = A + B 
#print c                        #no output, missing parentheses 
b[0] = -1                       #changes index 0 to -1 
d = [e+1 for e in a]            #new list d where e values = a+1  
d.append(b[0] + 1)              #adding (index b + 1 = 0) to d 
d.append(b[-1] + 1)             #adding the last number in b + 1 to d = 17+1. 
                                #index[-1] = the last element in a list
#print(d[-2])                    #prints the second last number in d = 0 

for e1 in a:                    #for each element in list a 
    for e2 in b:                #for each element in list b 
        print(e1 + e2)          #print the sum of e1 and e2 
            