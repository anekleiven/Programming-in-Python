# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 07:48:18 2024

@author: anekl
"""

#doc strings 

def C2F(C) :
    """Convert Celsius degrees (C) to Fahrenheit (f). """ 
    return (9/5)*C + 32 



#doc string for å dokumentere en funksjon 
#forklarer hva funksjonen gjør 
#doc strings gjør at du kan ha tekst over flere linjer med """ 
#første linje etter definisjonen av funksjonen 
#kan brukes til å be om hjelp om funksjonen help(funksjon) 

def line(x0,y0,x1,y1): 
    """
    Compute the coeffisients a and b in the mathematical expression 
    for a straight line y = a*x + b that goes through 
    two positions (x0, y0) and (x1,y1). 
    x0,y0: a point on the line (float) 
    x1,y1: another point on the line (float) 
    return: a,b (floats) for the line (y = a*x + b) 
    
    """
    a = (y1-y0) / (x1-x0) 
    b = y0 - a*x0 
    return a,b 


