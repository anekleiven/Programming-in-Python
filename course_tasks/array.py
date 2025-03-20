# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 07:17:55 2024

@author: anekl
"""

import numpy as np 
x = np.linspace(0,1,5) 
y1 = x**3
y2 = np.cos(x) 
y3 = x**3 + x*np.cos(x) 
y4 = x/3 + np.exp(-x*5) 


#%% example with bigger array - list versus array 

import time
# import timeit 
import math 
import numpy as np 

n = 1000000
dx = 1000 / n-1
# Python list with one million numbers 
x1 = [i*dx for i in range(n)] 
# NumPy array with one million numbers 
x2 = np.linspace(0,1000,1000000)


def fen(x) :                        #function f1
    return x**3 + x*math.cos(x) 

def fto(x): 
    return x**3 + x*np.cos(x)


ts1 = time.time()               #t0 = 1.jan 1970
y1 = [fen(x) for x in x1] 
td1 = time.time() - ts1 
print("Brukt tid for python liste", td1) 


ts2 = time.time() 
y2 = fto(x2) 
td2 = time.time() - ts2 
print("Brukt tid for numpy:", td2)


print("Numpy ganger raskere", td1/td2)


#%% compare numpy vector and python list 


import math 
import numpy as np 

def f1(x, omega): 
    return math.exp(-x) * math.sin(omega*x) 

omega = 2 * math.pi 
n = 51
dx = 5 / (n-1) 
xl = [i*dx for i in range(n)]

yl = [f1(xi, omega) for xi in xl] 


def f2(x,omega): 
    return np.exp(-x) * np.sin(omega*x) 

omega = 2 * np.pi 
# x vector 
xv = np.linspace(0,5,n) 
yv = f2(xv,omega)  


 















