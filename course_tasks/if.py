# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 09:57:02 2024

@author: anekl
"""

import math 

def f(x): 
    if 0 <= x <= math.pi :      #python expects a true/false statement 
        return math.sin(x) 
    else:                       #else er frivillig, same output 
        return 0 


# several if tests in one function; use if and elif 

def N(x): 
    if x < 0: 
        return 0 
    elif 0 <= x < 1:
        return x 
    elif 1 <= x < 2:
        return 2-x 
    elif x >= 2: 
        return 2 
   
    
   
#if else in one line 

def m(x): 
    return (math.sin(x) if 0 <= x < 2*math.pi else 0)























