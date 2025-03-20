# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 14:54:17 2024
__author__ = "Ane Kleiven"
__email__ = "ane.kleiven@nmbu.no"
"""
# make an empty dictionary 
julehandel = {}

# read the julehandel file 
file = open("data\julehandel.txt","r")

# skip the two first line 
file.readline()
file.readline()

# read each line and split by tabulator
# add keys and values to dictionary 
for line in file:  
    beskrivelse, antall, pris = line.split("\t")
    antall = int(antall) 
    pris = float(pris) 
    kostnad = antall*pris 
    julehandel[beskrivelse] = kostnad
    
# calculate the total sum    
totalkostnad = sum(julehandel.values())

# print results using f-strings 
print("-----------------------------------------")
for beskrivelse, kostnad in sorted(julehandel.items()):
    print(f"{beskrivelse:27}   {kostnad:7.2f} kr")
print("-----------------------------------------")
print(f"Sum{' ' * 17}          {totalkostnad:7.1f} kr")


