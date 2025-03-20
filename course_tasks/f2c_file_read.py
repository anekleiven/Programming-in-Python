# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 11:13:47 2024

@author: anekl
"""

import f2c_py
filename = "Exercise 4.3.txt"
try: 
    with open(filename, "r") as file: 
        for _ in range(3): 
            next(file) 
        line = next(file).strip() 
        words = line.split()
        F = float(words[2])
            
        C = f2c_py.convC2F(F)
        print(f"{F}°F is equivalent to {C}°C.")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except ValueError:
    print("Invalid data format in the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

