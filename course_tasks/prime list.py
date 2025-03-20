# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:50:36 2024

@author: anekl
"""

#Exercise 2.3 
#Work with a list 

primes = [2,3,5,7,11,13]                #list primes 

for prime in primes:                    #make a for loop to print list primes 
    print(prime) 
    
p = 17                                  #a new prime 

primes.append(p)                        #add prime to the list primes 

for prime in primes:                    #write the list incl. new value 
    print(prime)
    

