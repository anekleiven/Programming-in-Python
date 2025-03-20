# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:17:08 2024

@author: anekl
@purpose: enkle funksjoner for multiplikasjoner 
"""

def double(x): 
    return 2 * x 

def tripple(x): 
    return 3 * x 

def quadruple(x): 
    return 4 * x 

def test_double(): 
    a1 = double(2)
    assert a1 == 4, "Something wrong with double"


# two underscores before and after name and main 
if __name__ == "__main__": 
    print("Here we go")
    test_double()
    r1 = double(2)
    r2 = tripple(2)
    r3 = quadruple(2)
    
    
