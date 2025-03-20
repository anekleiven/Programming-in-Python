# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 11:23:38 2024

@author: anekl
"""

def double(x) :
    return x*2 

def test_double():
    x = 4 
    exact = 8 
    computed = double(x) 
    
    msg = f'computed{computed},expected{exact}'
    assert(exact == computed), msg 
    
"""
def test_double():
    assert double(2)==4
    assert abs(double(0.1) - 0.2) < 1E-15
    assert double([1, 2]) == [1, 2, 1, 2]
    assert double((1, 2)) == (1, 2, 1, 2)
    assert double(3+4j) == 6+8j
    assert double("hello") == "hellohello"
    

test_double()


double(2)
double("hello")
double(abs(double(0.1) - 0.2) < 1E-15)

"""


