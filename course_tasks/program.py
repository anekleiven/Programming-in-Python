# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 08:21:29 2024

@author: anekl
"""

# import libraries needed in the code 
import math 


# define functions 
def f(x): 
    """docstring for function f(x)"""
    e = math.exp(-0.1 * x) 
    s = math.sin(6 * math.pi * x) 
    return e * s 

x = 2 
# call f to calculate y 
y = f(x) 

print(f"({x}) = {y:g}")


# test functions 
# the name should start with test_ 

def double(x) :
    return x*2 

def test_double(): 
    x = 4
    exact = 9 
    computed = double(x) 
    
    msg = 'computed {0}, expected {1}'.format(computed,exact)
    assert(computed == exact), msg 

#msg = a string message that should be used if the test fails
# assert checks whether computed == exact. 
# if true nothing happens 
# if false msg message is printed
# use more asserts to test different things in a function 
test_double()

#%% assert in a function 

def KelvintoFahrenheit(Temperature): 
    assert(Temperature >= 0), "Colder than absolute zero!"
    return((Temperature - 273)*1.8) + 32 

# gives assertionerror if temp >= 0 

#%% Rekursjon 

# make a function that calls it self 

#example with iterative solution 

def factorial_iterative(n): 
    product = 1 
    
    for i in range(n): 
        product = product * (i + 1) 
        
    return product 



# example with recursion 

def factorial_recursive(n):
    if n == 1 :
        return 1 
    else: 
        return n * factorial_recursive(n-1)
    
# in recursion you need to program an ending
# here ending = if n =1 -> return 1 


#%% numeric derivation 

def g(t): 
    return t**(-6) 

def diff2(f,x, h = 1E-6) :
    r = (f(x-h) - 2*f(x) + f(x+h)) / h**2 
    return r 

# h = 1E-6 er satt som default verdi 
   


y = diff2(g, 1)
print(y)

for k in range(2,15) :
    h = 10**-k 
    y = diff2(g, 1,h)
    print(f'h = {h:.0e}: {y:.5f}')

#vi forventer mer eksakte verdier ved liten h. 
# begrensning i python: numerisk presisjon og avrundingsfeil
# ved h > 1*10**-6 blir tallet helt feil
# Når du velger h for numeriske derivasjoner, må du finne en balanse mellom å velge h lite nok til å få en nøyaktig tilnærming, men ikke så lite at numeriske feil forstyrrer beregningene. 
# For små h fører til numeriske problemer på grunn av begrensningene i flyttallsaritmetikken.



#%%  if test med flere forgreninger 

import math 

def f(x):
    if 0 <= x <= math.pi: 
        return math.sin(x) 
    else: 
        return 0 


def N(x): 
    if x < 0: 
        return 0 
    elif 0 <= x < 1: 
        return x 
    elif 1 <= x < 2: 
        return 2 - x 
    elif x >= 2: 
        return 2 
    
N(1)


















