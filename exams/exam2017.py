# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 17:50:29 2024

@author: anekl
"""
# Spørsmål 1: Hva skrives ut? 

print("The problem is not the problem"[4:11])
# problem 

print("The problem is you attitude about the problem".split())
# [The, problem, is, you, attitude, about, the, problem] 

print("Do or do not".find("do"))
# [6] 

print("There is no try".upper()) 
# THERE IS NO TRY 

print("My favourite courses: {2}, {0}, {3}, {1}".format("fys210","inf120","math112","stat100"))
# My favourite courses: math112, fys210, stat100, inf120



# Spørsmål 2: Boolske uttrykk 

x = 10
y = -1 

x < 0 and y > 0 
#FALSE 

x > 0 or y < 0 
#TRUE 

x >= 4 or y != -2 
#TRUE

not(x < 0) and y >= -2 
#TRUE 

not(x < 10 or y < 1) 
#FALSE



# Spørsmål 3: funksjon 

""" a) Skriv en funksjon som spør hvor gammel du er og som sjekker om du er 
gammel nok til å kjøre bil. Funksjonen tar inn to aldre som argument og leser
inn alderen fra brukeren. Dersom personen er over eller lik grense1 år 
skrives ’Velkommen til å kjøre opp’, dersom personene er mellom grense2 
og grense1 så skrives meldingen ’Du er velkommen til å ta kjøretime men må
vente litt før du kan kjøre opp’ og dersom personene er under grense2 år 
skrives meldingen ’Du må vente enda noen år’. """ 

"""b) Utvid funksjonen slik at du bruker en try – except for å sjekke 
om brukeren har skrevet inn et tall. Dersom det ikke er tall 
skal brukeren få melding om at kun et tall må skrives inn."""
     
    
def alder_bilkjøring(aldersgrense1=18, aldersgrense2=16):
    try:
        alder = int(input("Hvor gammel er du? "))  # Input-konvertering inni try-blokken
    except ValueError:
         raise ValueError("Ugyldig input. Skriv inn et tall.")  
    if alder >= aldersgrense1:
        print("Velkommen til å kjøre opp") 
    elif alder < aldersgrense1 and alder >= aldersgrense2: 
        print("Du er velkommen til å ta kjøretime, men må vente med oppkjøring") 
    else:
        print("Du må enda vente noen år") 
    

#alder_bilkjøring()


# Spørsmål 4: Bruk av sets 

l1 = ["banan", "eple", "appelsin", "eple", "kiwi"]
l2 = ["eple", "fersken", "drue", "fersken", "appelsin"]

set(l1) 
# vil oppgi objektene i listen i tilfeldig rekkefølge. ingen gjentakelser 

set(l2) - set(l1)
# fersken, drue

set(l2) & set(l1) 
# eple, appelsin 

set(l2) | set(l1) 
# alle objekter i begge set 



# Spørsmål 5: Dictionary 

dict = {"Temperature": 15.0, "Humidity": 68, "Precipitation": 3}

print('dict[’Humidity’]:', dict['Humidity'])
#dict["Humidity"]: 68

#print(dict[68])
#KeyError 68
# The Python KeyError is an exception that occurs when an attempt is made to
# access an item in a dictionary that does not exist.

# add and change dictionaries 
dict.update({"Location": "Ås"})
dict.update({"Temperature": 21.0})

# alternative: 
dict["Location"] = "Ål"
dict["Temperature"] = 34


# Spørsmål 6: numpy arrays 

import numpy as np 

a = np.array([[1,2,3,4,5,6,7],
              [8,9,10,11,12,13,14],
              [15,16,17,18,19,20,21],
              [22,23,24,25,26,27,28],
              [29,30,31,32,33,34,35],
              [36,37,38,39,40,41,42],
              [43,44,45,46,47,48,49]])
a[::4,:] 
a[1:-4,:]
a[::4,1:6]

C = np.array([[241, -14, 88],
[-30, 127, 39],
[-22, -51, -7],
[155, 61, 172]])

# setter alle verdier over 0 til 0 
C[C > 0] = 0 


np.linspace(1,5,9) 
# 9 tall mellom 1 og 5, jevnt fordelt 

np.arange(0,16,3) 
# tall mellom 0 og 16, intervall på 3
# 0,3,6,9,12,15

#%%

# Spørsmål 7: random tall 

"""
Vi har et spill med 5 terninger som viser øyne fra 1 til 6.
Skriv et program som bruker Monte Carlo-simulering til å regne ut 
sannsynligheten for å få eksakt 3 like når en kaster de 5 terningene. 
Programmet skal la brukeren få bestemme hvor mange 
eksperimenter som skal utføres. 
Husk nødvendig import.
"""

import random 

def montecarlosim_terning():
    try: 
        N = int(input("How many experiments do you want to do? "))
        terninger = 5
        antall_like = 3 
        suksess = 0 
    
        for _ in range(N): 
            kast = [random.randint(1,6) for _ in range(terninger)]
            counts = [kast.count(value) for value in range (1,7)]
        
            if counts.count(antall_like) == 1: 
                suksess += 1 
            
        sannsynlighet = suksess/N 
        print(f"The probability of getting {antall_like} equal numbers with {N} experiments is {sannsynlighet:.4f}")
    
    except ValueError: 
        print("Please choose an integer for number of experiments")
    
montecarlosim_terning()


#%% 

with open("data/temperatur.txt","r") as file: 
    lines = file.readlines() 
    temperature =  [] 
    
    for line in lines[2:]: 
        data = line.split() 
        days = int(data[0])
        temp2012 = float(data[1])
        temp2011 = float(data[2])
        temperature.append([days, temp2011, temp2012]) 
         
import matplotlib.pyplot as plt
import numpy as np 

temperature_arr = np.array(temperature)
temp2012 = temperature_arr[:,1]
temp2011 = temperature_arr[:,2]

mean2012 = np.mean(temp2012)
mean2011 = np.mean(temp2011)

plt.plot(temperature_arr[:,0], temperature_arr[:,1], label = f"Mean 2012: {mean2012:.2f}", marker ="o", color = "pink")
plt.plot(temperature_arr[:,0], temperature_arr[:,2], label = f"Mean 2011: {mean2011:.2f}", marker = "x", color = "royalblue")

plt.title("Mean temperatures in Aas in March 2011 and 2012")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")     
plt.legend(loc = "upper left") 

plt.show() 
  
        
        
#%% 

class Dog: 
    
    def __init__(self, name): 
        self.name = name
        self.tricks = []  
        
    def add_trick(self, trick): 
        self.tricks.append(trick) 
    
    def show_tricks(self): 
        print(f"{self.name} can do the following tricks: {', '.join(self.tricks)}")
    

Hund1 = Dog("Milo")
Hund2 = Dog("Jeppe")
Hund1.add_trick("Sit")
Hund1.add_trick("Play dead")
Hund1.add_trick("Roll over")  
Hund1.add_trick("Ligg")
Hund1.show_tricks()

Hund2.add_trick("Sit")
Hund2.show_tricks()
        
        
#%% 

def contains(sequence, subsequence): 
    if len(sequence) < len(subsequence):
        return False
    
    if sequence [: len(subsequence)] == subsequence: 
        return True
    
    return contains(sequence[1:], subsequence) 


print(contains("herremann", "mann"))
print(contains("hello world", "hello"))
        

#%% 
import numpy as np 

tall = [1,3,4,6,7,8,9,0]       
        
tall[0] 
tall[0:3]
tall[-3:-1]   
tall[2:4]
        
a = [[1,2,3,4],[5,6,7,8], [9,10,11,12], [13,14,15,16]]
a_arr = np.array(a)

a_arr[1:,1:]
a_arr[3,::2]
a_arr[1::2,1:]
a_arr[:-1,:-3]


#%% 

# oppgave 1 

print('The problem is not the problem'[4:11])
# problem 

print('The problem is you attitude about the problem'.split())
# ['The', 'problem', 'is', 'you', 'attitude', 'about', 'the', 'problem']

print('Do or do not'.find('do')) 
# 6 - husk at første er index 0 

print('There is no try'.upper())
# THERE IS NO TRY

print('My favourite courses: {2}, {0}, {3}, {1}'.format('fys230', 'inf120', 'math112','stat100'))
# My favourite courses: math112, fys230, stat100, inf120 
                                                           
                                                           
# oppgave 2 

x = 10; y = - 1

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


# oppgave 3 og 4

def bilkjøring(grense1, grense2) :
    try: 
        alder = int(input("How old are you? ")) 
        if alder >= grense1 and alder < grense2: 
            return "velkommen på kjøretimer" 
        elif alder >= grense1 and alder >= grense2: 
            return "Hurra, du kan ta oppkjøring!"
        else: 
            return "du må vente noen år til :)"
    except (ValueError, TypeError): 
        return "skriv inn et heltall"
bilkjøring(16, 18)

# valueerror = correct type, inappropriate value 
# typeerror = incorrect type - for example string or float instead of integer 

# oppgave 5




















