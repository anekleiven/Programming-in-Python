# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:25:54 2024

@author: anekl
"""

formula = input('Write a formula involving x:')

code = f""" 
def f(x): 
    return {formula} 
"""
exec(code) 

x = 0               #settes til 0 for å sikre at den ikke er none (kommer aldri inn i løkka) 
while x is not None: 
    x = eval(input("Provide x (or type None to quit): "))

    if x is not None: 
        y = f(x) 
        print(f"f({x}) = {y}")
    

# \n betyr linjeskift 
