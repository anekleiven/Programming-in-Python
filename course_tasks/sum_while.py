# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 10:21:55 2024

@author: anekl
"""

#Exercise 2.11 
#Compute a mathematical sum 


s = 0
k = 1
M = 5

while k < M:            #will calculate the sum as long as k < M (100)
    s = s + (1 / k)     #the sum is updated (=s+= 1/k)
    k = k + 1           #k is incremented by 1 after each iteration (=k+=1)
print(s)                #when the loop finishes, the sum is printed


#MANUAL CODE when M = 5 
#s = 0 + 1
#1 
#s = 1 + 1/2 
#1.5 
#s = 1.5 + 1/3 
#1.833 
#s = 1.833 + 1/4 
#s = 2.08