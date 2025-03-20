# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:30:49 2024

@author: anekl
@purpose: import myfuncs 
"""
#%%
#alternative 1

import myfuncs as my                    #forkorter myFuncs til my 

comp1 = my.double(2)
comp2 = my.tripple(2)
comp3 = my.quadruple(2)

print(comp1,comp2,comp3)

#%%
#alternative 2

import myfuncs                     #forkorter myFuncs til my 

comp1 = myfuncs.double(2)
comp2 = myfuncs.tripple(2)
comp3 = myfuncs.quadruple(2)

print(comp1,comp2,comp3)

#%%
#alternative 3 

from myfuncs import double, tripple, quadruple

comp1 = double(2)
comp2 = tripple(2)
comp3 = quadruple(2) 

print(comp1,comp2,comp3)