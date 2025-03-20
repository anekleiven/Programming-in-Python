# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:43:01 2024

@author: anekl
"""

#Exercise 2.22: Interpret a code 

import time              #import functions from time
t0 = time.time()         #Get the current time (in seconds since the epoch)
while time.time() - t0 > 10: # Loop until 10 seconds have passed
    print("....I like while loops!")  #Print message 
    time.sleep(2)         #insert 2 seconds pause 
print("Oh no - the loop is over") #print when loop is over 


#if t0 > 10, the loop will not start, since time.time() - t(0) is not higher than 10 

