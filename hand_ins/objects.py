# -*- coding: utf-8 -*-
"""Created on <dagens dato>"""
__author__ = "Ane Kleiven"
__email__ = "ane.kleiven@nmbu.no"
"""                        """

import random as rd

# lag klasser for katt, undulat og hund, hver med to attributer 
class katt:
    def __init__(self): 
        self.dyreslag = "katt" 
        self.antall_bein = 4 
    
    def __str__(self): 
        return f"Dyret er en {self.dyreslag} med {self.antall_bein} bein."


class undulat: 
    def __init__(self): 
        self.dyreslag = "undulat" 
        self.antall_bein = 2 
    
    def __str__(self): 
        return f"Dyret er en {self.dyreslag} med {self.antall_bein} bein."


class hund: 
    def __init__(self): 
        self.dyreslag = "hund" 
        self.antall_bein = 4 
    
    def __str__(self): 
        return f"Dyret er en {self.dyreslag} med {self.antall_bein} bein."


# lag funksjon for å returnere to tilfeldige familiedyr 
def lag_familiedyr(antall = 2): 
    dyr_klasser = [katt(), hund(), undulat()]
    familie = [] 
    for _ in range(antall): 
        dyr = rd.choice(dyr_klasser)
        familie.append(dyr)
    return familie


# kall funksjonen lag_familiedyr og print 
familiedyr = lag_familiedyr(2)
   
for i, dyr in enumerate(familiedyr):
    print(f'{i+1}: {dyr}')











