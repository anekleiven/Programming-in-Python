# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 15:32:53 2024

@author: anekl
"""

#Exercise 2.8 
#Make a table of values from a formula
"""
g = 9.81 
v0 = 40
n = 10

t_max = 2 * v0 / g
h = t_max/n 

for i in range(n+1): 
    t = i * h 
    y = v0*t - (1/2*g*t**2) 
    print(f"{t:5.2f},{y:7.2f}")
"""

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
    print(f"{t:5.2f},{y:7.2f}")
    t += h
    
    t_values.append(t)
    y_values.append(y) 
  
 



    
    
    