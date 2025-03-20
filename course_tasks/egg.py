# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:58:21 2024

@author: anekl
"""

#Exercise 1.12 

m_small = 47
m_large = 67 
p = 1.038 
c = 3.7 
K = 5.4*10**(-3)
tw = 100 
ty = 70
t0_fridge = 4 
t0_room = 20 

import math

egg_fridge = ((m_large**(2/3)*c*p**(1/3))/(K*3.14**(2)*(4*3.14/3)**(2/3)))*(math.log((0.76*(t0_fridge-tw))/(ty-tw)))
egg_room = ((m_large**(2/3)*c*p**(1/3))/(K*3.14**(2)*(4*3.14/3)**(2/3)))*(math.log((0.76*(t0_room-tw))/(ty-tw)))

round_egg_fridge = round(egg_fridge,0)
round_egg_room = round(egg_room,0)

egg_minutes_fridge = round_egg_fridge/60 
egg_minutes_room = round_egg_room/60

