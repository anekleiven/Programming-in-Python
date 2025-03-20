# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 10:52:06 2024

@author: anekl
"""

#Exercise 2.13 
#Simulate a program by hand 

initial_amount = 100 
p = 5.5 #interest rate 
amount = initial_amount
years = 0 

while amount <= 1.5*initial_amount:    #<= 150 
    amount += p/100*amount 
    years += 1
    print(years)
    
#105.5, 1 år 
#111, 2 år 
#116.5, 3 år 
#122, 4 år 
#127.5, 5 år 
#133, 6 år 
#138.5, 7 år 
#144, 8 år 
#149.5, 9 år 

#The program calculates how many years it takes, for the amount to reach 150.

