# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:59:25 2024

@author: anekl
"""

#Exercise 2.16 
#Store data in lists 
C = 0
delta_t = 10 

grader_c = [0,10,20,30,40,50,60,70,80,90,100]
grader_c_approx = []
grader_F = []

while C<=100:                                           #while loop
   F = (9/5*C) + 32
   C_est = (F-30)/2 
   grader_F.append(F)
   grader_c_approx.append(C_est)
   print(f"{C:5d},{F:5.1f},{C_est:5.1f}")
   C = C + delta_t
   
conversion = [[grader_c], [grader_F], [grader_c_approx]]

for index, element in enumerate(conversion):
    for subindex, subelement in enumerate(element): 
        verdi = subelement 
        print(verdi)
        
