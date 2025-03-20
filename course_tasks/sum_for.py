# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 10:41:14 2024

@author: anekl
"""

#Exercise 2.12
#Replace a while loop with a for loop 

  
s = 0
M = 5  # Set the upper limit

for k in range(1, M):  # Loop from k = 1 to M-1. M is not included. 
    s = s + (1 / k)    # Update the sum
print(s)  # Print the result

