# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 13:31:56 2024

@author: anekl
"""

# Exercise 4.5 Use exceptions to handle wrong input 

import f2c_py

try: 
    C = float(input("Enter temperature in degrees Celsius: "))
    F = f2c_py.convC2F(C)
    print(f"{C}°C is equivalent to {F}°F.")
except ValueError:
        print("Invalid input. Please enter a valid number")

        
        