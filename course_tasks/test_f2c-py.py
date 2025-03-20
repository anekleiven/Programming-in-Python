# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 11:09:22 2024

@author: anekl
"""

# exercise 3.5 

def convC2F(C): 
    return (9/5)*C + 32 

convC2F(5) 

def convF2C(F): 
    return 5/9*(F-32) 

convF2C(41)



#test function for convC2F

def test_convC2F(): 
    C = 5 
    exact = 42
    computed = convC2F(C)
    
    msg = f'computed {computed}, expected {exact}'.format(computed,exact)
    assert(computed == exact),msg 

test_convC2F()



#test function for convF2C

def test_convF2C(): 
    F = 41 
    exact = 5 
    computed = convF2C(F) 
    
    msg = f'computed {computed}, expected{exact}'.format(computed,exact)
    assert(computed == exact),msg 
    
test_convF2C()
