# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 11:49:20 2024

@author: anekl
"""

#numpy library 

import numpy as np 

def f(x): 
    return x**3

n = 5
# delta x: x increments
dx = 1 / (n-1) 
x1 = [i*dx for i in range(n)]
y1 = [f(x) for x in x1] 
pairs = [[x,y] for x,y in zip (x1,y1)]


x2 = np.array(x1) 
y2 = np.array(y1) 


# create numpy array directly 
x3 = np.linspace(0,1,n)   #tilsvarer: x1 = [i*dx for i in range(n)]
y3 = np.zeros(n) 

for i in range(n): y3[i] = f(x3[i])

# create array directly with list comprehension 
y4 = np.array([f(xi) for xi in x3])

