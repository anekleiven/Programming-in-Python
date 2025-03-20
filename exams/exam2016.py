# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 07:50:39 2024

@author: anekl
"""

#%%

print('Ice Cream'.upper())
print('John' in 'John is a great bloke.')
print('They call it a Royale with cheese.'[-7:-1]) # exludes period (-1)
print('A list of cities: {2}, {1}, {3}, {0}'.format('Quito', 'Rio', 'Oslo', 'Perth'))

        
#%% 

x = 4 
y = -2 

x < 0 and y > 0
x > 0 or y < 0
x >= 4 or y != -2
not(x < 0) and y >= -2
not(x < 10 or y < 1)


#%%

# Spørsmål 3: funksjon 

a = [1,2,3,4]
b = [5,6,7,8] 
c = [2,1,4,3]



def sum_index(liste1,liste2,liste3) :
    sum_liste = [] 
    return [liste1[i] + liste2[i] + liste3[i] for i in range(len(liste1))]
    sum_liste.append() 

sum_index(a,b,c)


#%% 

# Spørsmål 4: bruk av sets 

c = ["Larvik", "Oslo", "Bodø", "Larvik", "Oslo"]
d = ["Larvik", "Arendal", "Hamar", "Arendal"]

# Sets cannot have two items with the same value.
# Sets cannot be changed or indexed 

set(c) # returns all items once, no duplicates 
set(c) - set(d) # returns the elements that are present in c but not in d
set(c) & set(d) # returns items in both lists (Larvik)
set(c) | set(d) # all unique elements from c and d 


#%% 

# spørsmål 5: Les data fra en fil inn i en dictionary 


def read_txt(filnavn): 
    kilo = {}
    
    with open(filnavn,"r") as fil: 
        linjer = fil.readlines()
        
    for linje in linjer[1:]:
        data = linje.strip().split(",")
        navn = data[0] 
        vekt = int(data[2])
    
        kilo[navn] = vekt 
    
    return kilo 


read_txt("data/data2.txt")


#%% 
import numpy as np 

# spørsmål 6

array_a = np.array([
    [0,1,2,3,4,5],
    [10, 11, 12, 13, 14, 15],
    [20, 21, 22, 23, 24, 25],
    [30, 31, 32, 33, 34, 35],
    [40, 41, 42, 43, 44, 45],
    [50, 51, 52, 53, 54, 55]
])

# a) 
array_a[3,0:5]

# b) 
array_a[2:5,1:4]

# c) 
array_a[0:,1::2]

# d)
b = [[8, 7], [2, 8], [4, 5], [8, 1]]

B = np.vstack(b)

print(B)

# e) 

# sets all negative values to zero 

C = np.array([[241, -14, 88],
[-30, 127, 39],
[-22, -51, -7],
[155, 61, 172]])

C[C < 0] = 0

# f) 

# lager en array fra 1 til 2, med 5 tall. jevnt fordelt. 

np.linspace(1,2,5) 

# g) lager en array som starter på 0 og øker med 3 hver gang. maks grense er 11. 
# step size er definert, men ikke antall tall 
np.arange(0,11,3)

'''
    np.arange() is useful when you know the step size 
    and need an array of evenly spaced numbers based on
    that step.
    
    np.linspace() is useful when you know how many points
    you want between two values, and it will automatically 
    calculate the step size to fit those points evenly between
    the start and stop values.
    
''' 
    
#%% 

# spørsmål 7: random tall 

import random as rd
import numpy.random as npr  

def simuler_terning(): 
    kast = npr.randint(1,6,10)
    return kast

def estimer_sannsynlighet(simuleringer = 100000): 
    suksess = 0 
    
    for _ in range(simuleringer): 
        kast = simuler_terning()
        
        toere = np.sum(kast ==2) 
        femmere = np.sum(kast == 5) 
        
        if toere == 2 and femmere == 0: 
            suksess += 1 
        
    sannsynlighet = suksess/simuleringer 
    return sannsynlighet

sannsynlighet = estimer_sannsynlighet()
print(f"Based on 10000 simulations, the chance of getting exactly two eyes and not 5 eyes from 10 throws is about {sannsynlighet}")


# b) jo flere forsøk, jo nærmere den sanne sannsynligheten


#%% 

# spørsmål 8: hva skrives ut på skjerrmen med følgende kode 
# list comprehension 

# a) liste med 0,2,4,6,8
[2 * x for x in range(5)]

# b) [5,7,9]
[x + y for x, y in zip([1, 2, 3], [4, 5, 6])]

# c) output: alle ord som starter på s. fra 2. bokstav tom. nest siste
[k[1:-1] for k in ['story', 'light', 'sun'] if k[0] == 's']


#%%

# spørsmål 9: try except 

a = [99, 'Peter', [5, 12, 1], 1.7]

def listExtractor(liste, index): 
    try: 
        element = liste[index] 
        print(f"Element at index {index} has value {element} and is a {type(element)}.")
    except IndexError:  
            print(f"Need an index between 0 and {len(a)-1} but got {index}")



listExtractor(a, 2)
listExtractor(a, 4)
listExtractor(a, 1)
listExtractor(a, 0)


#%% 

# spørsmål 10: klasser 

import math 

class Triangle:
    
    def __init__(self, a,b,c): 
        self.a = a
        self.b = b
        self.c = c
        self.s = 1/2 * (self.a + self.b + self.c)
        self.area_computed = False

    def compute_area(self): 
        area = math.sqrt(self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c))
        self.area_computed = True
        return area 
    
    def printResult(self): 
        if not self.area_computed:
            print("Area not computed yet.")
        else: 
            area = self.compute_area()
            print(f"Area = {area:.2f} and s = {self.s:.2f} using Heron's formula")
    

tr1 = Triangle(4,5,6) 
tr1.printResult()
tr1.compute_area()
tr1.printResult()


#%% oppgave 1 

print('A list of cities: {2}, {1}, {3}, {0}'.format('Quito', 'Rio', 'Oslo', 'Perth'))
# A list of cities: Oslo, Rio, Perth, Quito 

print('They call it a Royale with cheese.'[-7:-1])
# cheese 

print('John' in 'John is a great bloke.') 
# True 

print('Ice Cream'.upper())
# ICE CREAM

print(int(6 / 3))
# 2
    
# oppgave 2 
x = 4; y = - 2

x < 0 and y > 0
# False

x > 0 or y < 0 
# True 

x >= 4 or y != -2
# True 

not(x < 0) and y >= -2
# True 

not(x < 10 or y < 1) 
# False 
    

# oppgave 3

''' 
Programmer en funksjon som tar tre lister med tall som input. Listene skal være like lange.
I funksjonen beregnes summen av tall for hver indeks i listene. 
For listene a, b og c betyr dette 1 + 5 + 2 (første tall i hver liste), 
2 + 6 + 1 (andre tall i hver liste), etc. 
Funksjonen skal returnere summene samlet i en liste. 
For listene a, b og c skal funksjonen returnere følgende resultat: [8, 9, 14, 15].
''' 

a = [1, 2, 3, 4]; b = [5, 6, 7, 8]; c = [2, 1, 4, 3]

def sum_ind(a,b,c): 
    sumlist = [] 
    return [(a[index] + b[index] + c[index]) for index in range(len(a))]
    sumlist.append()

sum_ind(a, b, c)

        
#%%      
# oppgave 4 

# a collection of items without duplicates 


c = ['Larvik', 'Oslo', 'Bodø', 'Larvik', 'Oslo']
d = ['Larvik', 'Arendal', 'Hamar', 'Arendal']

set(c)
# {'Larvik', 'Oslo', 'Bodø'} 

set(c) | set(d)
# {'Larvik', 'Oslo', 'Bodø', 'Arendal', 'Hamar'}

set(c) - set(d)
# {'Oslo', 'Bodø'} 

set(c) & set(d)
# {'Larvik'}



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
