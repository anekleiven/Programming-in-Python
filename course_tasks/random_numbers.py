# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 08:44:25 2024

@author: anekl
"""

import random as rd
import matplotlib.pyplot as plt
import numpy.random as npr 


print(rd.random())

rd.random()
rd.uniform(100,102)

n = 1000
x = range(n) 
y = [rd.uniform(-1,1) for numbers in x]

plt.plot(x,y, 'bo')
plt.show()

"""
rand1 = rd.random()
rand2 = npr.random()
rand3 = npr.random(size = 1000)

"""

rand4 = rd.uniform(-1,10)
rand5 = npr.uniform(-10,10, size = 1000)


a = 1; b = 5; N = 10 

rand_1 = rd.randint(a,b)        # ikke myk parentes
print(rand_1) 

rand_2 = npr.randint(a,b+1,N)   # nb siste tall er ikke med, på ha med b+1 hvis vi vil ha tom 5 
print(rand_2)                   # myk parentes på numpy random numbers 



#%% eksempel kaste terning 

import time 

tid1 = time.time() 

N = 10000000
eyes = [rd.randint(1, 6) for i in range(N)]

seksere = 0 

for terningkast in eyes: 
    if terningkast == 6: 
        seksere +=1 
        
print(f"Fikk {seksere} seksere ved å rulle {N}")      

tid2 = time.time()  
print(f"det tok {tid2-tid1} sekunder")

#%% sannsynlighet for M seksere med N eksperimenter 
# monte carlo eksperiment - vektorisering - mye raskere enn for løkke 

import numpy as np 

tid1 = time.time()
N = 500000000
øyne = npr.randint(1,7,N)

seksere = (øyne == 6)
M = np.sum(seksere)             # går gjennom en stor array, vektorisert numpy summasjon

print(f"Fikk {M} seksere etter {N} terningkast")
sannsynlighet = M/N
print(f"Sannsynligheten for seksere er {sannsynlighet}")

tid2 = time.time() 


#%%     seed 

rd.seed(2); rd.random()     # gir samme random tall hver gang (med seed) 


 

print(f"Det tok {tid2-tid1} sekunder")
        

#%%

import numpy as np 
import numpy.random as npr 

rand_table = npr.rand(4,3)

mean = np.mean(rand_table)
st_dev = np.std(rand_table)

# zero is rows, one is columns
mean_col = np.mean(rand_table,axis=0)

mean_row = np.mean(rand_table, axis = 1)

st_dev_col = np.std(rand_table, axis = 0)

st_dev_row = np.std(rand_table, axis = 1)


#%% normalfordeling. sentrerer verdier jevnt rundt en middelverdi

import random 

rand = random.normalvariate(10, 1)

tester = np.random.normal(10,2,10)


#%% flere funksjoner i randombiblioteket 

import random 

awards = ["car", "computer", "ball", "boat", "computer"]

print(random.choice(awards))

index = random.randint(0, len(awards))
print(f"premie nummer to er {awards[index]}")

print(random.choice(awards))


#%% playing cards  

ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
colours = ["K","R","H","S"]

# function to make card deck 

def make_card_deck(): 
    ranks
    colours
    
    kortstokk = [] 
    for s in colours: 
        for r in ranks: 
            kortstokk.append(s+r) 
    
    random.shuffle(kortstokk) 
    
    return(kortstokk) 

kortstokk = make_card_deck()


# pick a card from the deck. remove from deck 

#kort = kortstokk[0] 
#del kortstokk[0]


# dele ut kort 

def del_ut(n, kortstokk) :
    hånd = [kortstokk[i] for i in range(n)]
    del kortstokk[:n]
    return hånd, kortstokk

#hånd1, kortstokk = del_ut(5, kortstokk)


# del ut kort til flere spillere 

def del_ut_flere(kort_per_spiller, spillere): 
    kortstokk = make_card_deck()
    hender = [] 
    
    for i in range(spillere):
        hånd, kortstokk = del_ut(kort_per_spiller, kortstokk)
        hender.append(hånd)
    
    return hender

spill = del_ut_flere(5, 6)

import pprint 

pprint.pprint(spill)


# hvor mange like (par, tre like etc.)

def same_rank(hånd,antall):
    verdier = [kort[1:] for kort in hånd]
    tell = 0 
    allerede_telt = [] 
    
    for verdi in verdier: 
        
        if verdi not in allerede_telt and verdier.count(verdi) == antall:
            tell += 1 
            allerede_telt.append(verdi)
            
        return tell 
    
hånd1, kortstokk = del_ut(10, kortstokk)   
    
print(same_rank(hånd1, 2))



# analyser antall kombinasjoner av samme slag 

# sjekk om vi har flush 

def samme_farge(hånd): 
    farger = [kort[0] for kort in hånd]
    teller = {}
    
    for farge in farger: 
        tell = farger.count(farge) 
        
        if tell >1: 
            teller[farge] = tell 
        
        return teller 
    

print(samme_farge(hånd1))


#%% Guess a number 


import random 

number = random.randint(1,100)
attempts = 0
guess = 0 

while guess != number: 
    guess = int(input("Guess a number: "))
    attempts += 1
    
    if guess == number: 
        print(f"Correct! You used {attempts} attempts.")
        
    elif guess < number: 
        print("Go higher!")
        
    else: 
        print("Go lower")
        
        
#%% trekke baller ut av en hatt 

# make a hat containing 12 different balls 

hat = []

for colour in "black", "red", "blue": 
    for i in range(4) :
        hat.append(colour) 


indeks = random.randint(0,len(hat) -1) 
ball1  = hat[indeks]
del hat[indeks]

random.shuffle(hat)
ball2 = hat.pop(0)  # removes the first element in list (same as del hat[indeks]) 


#%%     Monte Carlo experiment YATZY


kast = 1000000
M = 0 
verdi = 6

for i in range(kast): 
    sekser = 0 
    
    r1 = random.randint(1,6) 
    if r1 == verdi: 
        sekser +=1 
    r2 = random.randint(1,6)
    if r2 == verdi: 
        sekser +=1 
    r3 = random.randint(1,6)
    if r3 == verdi: 
        sekser +=1 
    r4 = random.randint(1,6)
    if r4 == verdi: 
        sekser +=1        
    r5 = random.randint(1,6)
    if r5 == verdi: 
        sekser +=1 
    
    if sekser == 5: 
        M +=1 
    
sannsynlighet = M/kast 
print(f"Sannsynligheten for yatzy er: {sannsynlighet}")

# den ekte sannsynligheten er: 1/(6*6*6*6*6) = 0.0001286


#%% sannsynligheten for å få 2 eller flere svarte baller 



def new_hat():
    colours = "black", "red", "blue"
    hat = [] 
    
    for colour in "black", "red", "blue": 
        for i in range(4) :
            hat.append(colour)
    
    return(hat) 


hat1 = new_hat()

def trekk_ball(hat): 
    indeks = random.randint(0,len(hat)-1)
    colour = hat.pop(indeks)
    return colour, hat 

n = 7 # antall baller vi trekker
N = 100000 #eksperimenter 

M = 0 

for e in range(N): 
    hat = new_hat()
    baller = [] 
    
    for i in range(n):
        farge, hat = trekk_ball(hat)
        baller.append(farge) 
        
    if baller.count("black") >=2: 
        M +=1 
    
sannsynlighet = M/N 
print(f"Sannsynligheten for to svarte: {sannsynlighet}") 

# sann sannsynlighet er 85% 



















      
        
        
    





























