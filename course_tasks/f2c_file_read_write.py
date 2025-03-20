# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 12:50:57 2024

@author: anekl
"""
F = [] 

with open("data/Fdeg.dat") as Fdat: 
    for _ in range(3):
        Fdat.readline()
    for line in Fdat: 
        words = line.split(":")
        n = float(words[1])
        F.append(n)
       
import f2c_py
import pandas as pd

C = [f2c_py.convF2C(temp) for temp in F] 

Temp = pd.DataFrame({"Fahrenheit": [f"{f:.2f}" for f in F],"Celsius": [f"{c:.2f}" for c in C]})

with open("data/temp.txt","w") as temp: 
    temp.write("Fahrenheit\tCelsius\n")
    for index, row in Temp.iterrows():
       temp.write(f"{row['Fahrenheit']}\t\t{row['Celsius']}\n")
            