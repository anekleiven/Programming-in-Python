# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 12:32:08 2024

@author: anekl
"""
#Exercise 2.9 
#Store values from a formula in lists 

g = 9.81 
v0 = 40
n = 10

t_max = 2 * v0 / g
h = t_max/n 
t = 0 

t_values = [] 
y_values = [] 

print(f"{'t':>5} {'y(t)':>7}")                      #table header        
while t <= t_max + 1e-10:
    y = v0*t - (1/2*g*t**2) 
    t += h
    
    t_values.append(t)
    y_values.append(y) 
  
 
for t,y in zip(t_values,y_values):
    print(f"{t:5.2f},{y:7.2f}")
    
for index, item in enumerate(t_values):
    print(f"{t_values[index]:5.2f}, {y_values[index]:7.2f}")

for index in range(n+1): 
    print(f"{t_values[index]:5.2f}, {y_values[index]:7.2f}")
    

