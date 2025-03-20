# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 17:05:02 2024

@author: anekl
"""
"""
#Exercise 2.7 
#Generate equally spaced coordinates 

a = 0  # Start of interval
b = 10  # End of interval
n = 5  # Number of intervals

# Calculate the step size
h = (b - a) / n

# Initialize an empty list to store the coordinates
x_coords = []

# Use a for loop to generate the coordinates and append them to the list
for i in range(n + 1):
    x = a + i * h  # Calculate each coordinate
    x_coords.append(x)  # Append to the list

# Output the list of coordinates
print(x_coords)
"""
#With list comprehension 

a = 5  # Start of interval
b = 20  # End of interval
n = 5  # Number of intervals

h = (b - a) / n


x_coords = [a + i*h for i in range (n+1)]           #koordinatene til x = a+ i*h for i in range n+1 
print(x_coords)

