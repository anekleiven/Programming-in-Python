# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:34:38 2024

@author: anekl
"""

#Exercise 2.21 
#Compare two real numbers with a tolerance 

a = 1/947.0 * 947
b = 1
if a != b: 
    print("wrong result")

#round off errors make two identical numbers different on a computer. 


abs(a-b) < 0.000000000000001

#the difference between a and b is smaller than 0.0000000000001
#1 * 10^-15 

