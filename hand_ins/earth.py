# -*- coding: utf-8 -*-
"""Created on Fri Sep 13 09:19:09 2024"""
__author__ = "Ane Kleiven"
__email__ = "ane.kleiven@nmbu.no"
"""                                   """
#Del 1: Jordens volum 

import math

r_km = 6371                    #jordens radius i km 
r_m = r_km*1000                #jordens radius i m 
pi = math.pi                   #pi

V = 4/3 * pi * r_m**3          #formelen for jordens volum 

print(f"Jordens volum er omtrent {V:.3e} m^3")


#Del 2: Jordens tetthet 

m = 5.9737*10**24              #jordens masse i kg 
V = 4/3 * pi * r_m**3          #formelen for jordens volum 
rho = m/V                      #jordens tetthet målt i kg/m^3 

print(f"Jordens tetthet er {rho:.2f} kg/m^3")



