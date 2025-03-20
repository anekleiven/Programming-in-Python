# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 10:05:26 2024

@author: anekl
"""

import f2c_py

try: 
    C = float(input("Enter temperature in degrees Celsius: "))
    F = f2c_py.convC2F(C)
    print(f"{C}°C is equivalent to {F}°F.")
except ValueError:
        print("Invalid input. Please enter a valid number")

        
        