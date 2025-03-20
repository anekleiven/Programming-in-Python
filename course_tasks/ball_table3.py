# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 12:09:42 2024

@author: anekl
"""

#Exercise 2.17 
#Store data in nested list 

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
  


#create nested list of t and y  
#list where each column contain t and y values 

ty = [[t_values], [y_values]]

for index in range(len(t_values)): 
    print(f"{t_values[index]:5.2f}, {y_values[index]:7.2f}")

#create a list where each row contain t and y values 
ty2 = list(zip(t_values,y_values))   
     
for t_value, y_value in ty2: 
    print(f"{t_value:.2f} {y_value:.2f}")
