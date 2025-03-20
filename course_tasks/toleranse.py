# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:01:55 2024

@author: anekl
"""

#Toleranse

v1 = (1/49) * 49
v2 = (1/51) * 51

print(f"{v1:.16f} {v2:.16f}")

toleranse = 1e-18                    #Sier noe om hvilken presisjon vi kan forvente for disse operasjonene. 

print(abs(v1-1) < toleranse) 
print(abs(v2-1) < toleranse)

#True = presisjonen er god nok, false = presisjonen er ikke god nok 



