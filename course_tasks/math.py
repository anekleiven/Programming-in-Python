# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:02:25 2024

@author: anekl
"""

#Regn ut normalfordelingen ved x

from math import pi, exp, sqrt 

m = 0   #gjennomsnitt
s = 2   #standardavvik 
x = 0.5 #evalueringspunkt 

f=1/(sqrt(2*pi)*s) * exp(-0.5*((x-m)/s)**2)

print(f)





