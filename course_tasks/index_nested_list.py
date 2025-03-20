# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:37:19 2024

@author: anekl
"""

#Exercise 2.15 
#Index a nested list 

q = [["a","b","c"],["d","e","f"], ["g","h"]]

#extract a 
#simplest way: 
a = q[0][0]
print(a)

#With a for loop:        
for index, element in enumerate(q): 
    for subindex, subelement in enumerate(element): 
        if index == 0 and subindex == 0:  # Check if it's the first element
            verdi = subelement  # Extract the element
            print(verdi) 


#extract the list d,e,f: 
for index, element in enumerate(q): 
    for subindex, subelement in enumerate(element): 
        if index == 1:
            verdi = subelement 
            print(verdi)
#alternative (simple): 
for item in q[1]: 
    print(item)


#extract h (simple): 
for item in q[2][1]: 
    print(item)
    
#more complex way: 
for index, element in enumerate(q): 
    for subindex, subelement in enumerate(element): 
        if index == 2 and subindex == 1: 
            verdi = subelement 
            print(verdi)

q[-1][-2] 
#index -1 = the last index 
#subindex -2 = the second last subindex with the value g 
#you have to count backwards. 


for i in q: 
    for j in range(len(i)): 
        print(i[j])
        
#i = represents each sublist in q 
#j = an index that iterates over the length of every sublist 
#the loop effectively prints each element of each sublist in q.  




             