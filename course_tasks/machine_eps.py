# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:21:48 2024

@author: anekl
"""

#Exercise 2.20 
#Explore what zero can be on a computer 

eps = 1.0
while 1.0 != 1.0 + eps:
    print("...................", eps)
    eps = eps/2.0
    print("final eps:", eps)
    
#the loop starts with eps = 1 
#the while loop goes on as long as 1 is not equal to 1 + eps 
#eps is then halfed 
#the loop starts over with the new value of eps 
#eps becomes smaller and smaller
#the loop stops when eps becomes becomes small such that 1.0 + eps is considered equal to 1.0.
#this is called the machine epsilon
#eps never becomes zero, but as close to zero that can be detected by the floating-point representation.


