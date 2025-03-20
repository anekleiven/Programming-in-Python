# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:01:20 2024

@author: anekl
"""

#Bruke løkker

#While løkke ("imens"løkke) 
#En while ufører repeterende utsagn så lenge den boolske betingelse er true.
#Alle utsagn i løkka må være intendert (4 mellomrom)

print("__________________________________")

C = -20                         #grader ce)lsius
delta_t = 5                     #hoppet mellom grader celsius

while C <= 40:                  #loop pluss betingelse
    F = 9/5 * C + 32 
    print(C,F)                      #skriv ut resultatet
    C = C + delta_t

print("__________________________________")


#Løkker: 
#Forskjell og likheter mellom for og while løkker. Viktig. 

#while condition:    
    #<block of statements> 

#for element in someList: 
    #<block of statements>



