# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 13:01:13 2024

@author: anekl
"""

print(27 == 42)
print("Pizza with ham and cheese".replace("ham","pepperoni"))
print("The best mirror is an old friend.".split()[-3:-1])
print("house".upper() in "The house is in on fire") 
print("Always remember: it is never too late".split(":")[0].split()[0][0:-3])

[e + f for e, f in [[4, 2], [4, 3]]]
[sum([n, m, o]) for n, m, o in zip([2, 1, 4], [0, 3, 4], [0, 6, 2])]
[name[-2:] for name in ['Ida', 'Olav', 'Kristin'] if 'a' not in name]
[z + z * z for z in range(1, 6, 2)] 


# oppgave 3 

def multiplier(tall1, tall2, tall3) :
    produkt = tall1*tall2*tall3
    return produkt 

multiplier(1,2,3)


# oppgave 4 


def adder(a, b = 2): 
    return a+b 

adder(5)


# oppgave 5 


navn = ["Jensen", "Olsen", "Svendsen"] 

def title_adder(navn):
   titles = [("Dr." + name) for name in navn] 
   return titles

title_adder(navn)


# oppgave 6 

dic = {} 
for x in range(1,6) :
    dic[x] = x**2 
print(dic)


# oppgave 7 

myList = [4, "The", 3, "dog", "ate", 1, 18, "my", "homework"]

def extractor(the_list): 
    newlist = [] 
    for element in the_list: 
        try: 
            int(element) 
        except (ValueError, TypeError): 
            newlist.append(element)

    return newlist

extractor(myList)



# oppgave 8 


def max_of_three(a,b,c) :
    if a > b and a > c :
        return a 
    elif b > a and b > c: 
        return b 
    else: 
        return c 
    
max_of_three(1, 2, 3)

    

# oppgave 9 

k = [1,2,3]

from math import sqrt

def stand_dev(liste):
    n = len(liste) 
    gj_snitt = sum(liste) / n 
    summer = sum((x - gj_snitt)**2 for x in liste)
    st_dev = sqrt(1/n * summer)
    return st_dev

stand_dev(k)



# oppgave 10 

import random as rd 

k = 10000 

ball = [1, 2]
farge = ["rød", "grønn", "blå"]

# Generate all combinations of ball and color
hatt1 = [(b, f) for b in ball for f in farge]
hatt2 = [(b,f) for b in ball for f in farge]

# Initialize success counter
grønne_baller = 0 
suksess = 0 

for _ in range(k): 
    balls1 =  [rd.choice(hatt1) for _ in range(2)]
    balls2 = [rd.choice(hatt2) for _ in range(2)]
    grønne_baller = sum(ball[1] == "grønn" for ball in balls1) + sum(ball[1] == "grønn" for ball in balls2)

    if grønne_baller == 4: 
        suksess += 1 
        
sannsynlighet = suksess/k 
print(sannsynlighet)


# oppgave 11

def get_info(filename, continent, coastline, desert): 
    with open(filename,"r") as file: 
        header = file.readline() 
        data = file.readlines() 
            
        populations = []
        countries = [] 
        for line in data: 
            res = line.split(";") 
            
            if res[2] == continent and res[3] == coastline and res[4] == desert: 
                populations.append(int(res[5]))
                countries.append(res[0]) 
                
        print(f"Countries: {countries}")
        print(f"Populations: {populations}")
    

get_info("data\\byer.txt", continent = "Asia", coastline = "yes", desert = "no")


# oppgave 12 

import math 

class Murstein: 
    
    def __init__(self, a, b, c): 
        self.a = a 
        self.b = b 
        self.c = c
        self.diagonal = None

    def compute_diagonal(self): 
        self.diagonal = sqrt(self.a**2 + self.b**2 + self.c**2)
        return self.diagonal 
    
    def printResult(self): 
        if self.diagonal == None: 
            return "Diagonal not computed yet. Need some input"
        else: 
            return f"Length of diagonal is {self.diagonal:.3f}"

Diagonal = Murstein(5, 4, 3)
Diagonal.compute_diagonal()
Diagonal.printResult()

#%% 

# oppgave 1 

print(27 == 42)
# False 

print('Pizza with ham and cheese.'.replace('ham', 'pepperoni'))
# Pizza with pepperoni and cheese 

print('The best mirror is an old friend.'.split()[-3:-1])
# ['The', 'best', 'mirror', 'is', 'an', 'old', 'friend']
# ['an', 'old']

print('house'.upper() in 'The house is in on fire')
# False 

print('Always remember: it is never too late'.split(':')[0].split()[0][0:-3])
# Always remember: 
# 'Always', 'remember' 
# 'Always' 
# Alw
    

# oppgave 2

[e + f for e, f in [[4, 2], [4, 3]]]
# [6,7]

[sum([n, m, o]) for n, m, o in zip([2, 1, 4], [0, 3, 4], [0, 6, 2])]
# [2,10,10]

[name[-2:] for name in ['Ida', 'Olav', 'Kristin'] if 'a' not in name]
# ['in']

[z + z * z for z in range(1, 6, 2)]
# [2,12,30]






































