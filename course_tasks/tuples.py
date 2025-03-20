# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 08:58:29 2024

@author: anekl
"""

#Eksamensrelevant: forståelse mellom lister og tuples 
#Tuples: lister som ikke kan endres 
#Konstante lister 
#Bruker parentes istedenfor [] 

tuple1 = (1,2,"tuples",5) 
tuple2 = 1,2,"tuples",5             #trenger ikke parentes

#kan gjøre mye av det samme som lister: 
    
tuple3 = tuple1 + tuple2            #lage ny tuple3 
print(tuple3[3:])                   #inkluderer index 3 
print(5 in tuple3)                  #true. sjekke om 5 er i tuple3. 

#Tuples er beskyttet mot ufrivillige endringer 
#Tuples er raskere enn lister. Bruker mindre strøm. Bærekraftig. 
#Tuples kan brukes som 'nøkkelord' i ordlister (dictionaries), det kan ikke lister 




