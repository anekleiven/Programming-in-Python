# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:21:34 2024

@author: anekl
"""

#Exercise 2.1 
#Make a Fahrenheit-Celsius conversion table 
"""
C = 0
delta_t = 10 

grader_c = [0,10,20,30,40,50,60,70,80,90,100]

while C<=100:                                           #while loop
   F = (9/5*C) + 32
   print(f"{C:5d},{F:5.1f}")
   C = C + delta_t
   

for C in grader_c                                       #for loop 
    F = (9/5*C) + 32
    print(f"{C:5d},{F:5.1f}")
"""

#Exercise 2.2 
#Generate an approximate Fahrenheit-Celsius conversion table 

C = 0
delta_t = 10 

grader_c = [0,10,20,30,40,50,60,70,80,90,100]

while C<=100:                                           #while loop
   F = (9/5*C) + 32
   C_est = (F-30)/2 
   print(f"{C:5d},{F:5.1f},{C_est:5.1f}")
   C = C + delta_t
   

for C in grader_c:                                       #for loop 
    F = (9/5*C) + 32
    C_est = (F-30)/2 
    print(f"{C:5d},{F:5.1f},{C_est:5.1f}")