# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:06:20 2024

@author: anekl
"""

#Exercise 2.19 
#Explore round-off errors from a large number of inverse operations 

from math import sqrt
for n in range(1,150):                               #for n mellom 1 og 60
    r = 2.0                                         #r starter med 2
    for i in range(n):                              #for i mellom 1 og 60
        r= sqrt(r)                                  #r = roten av r 
    for i in range(n):                              #for i mellom 1 og 60 
        r = r**2                                    #r = r^2 
print("%d times sqrt and **2: %.16f" % (n, r))

#etter 59 ganger med roten av 2 og 2^2, r = 1 
#for every round of sqrt and ^2, r gets a bit smaller. 
#round off errors are destroying the calculations when n is big enough. 
#the number will never go below 1, since sqrt(1) = 1 



