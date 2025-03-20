# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:00:34 2024

@author: anekl
"""

"""
from math import pi 

#Lister en samling av pythonobjekter 
#Heltall, flyttall, streng etc. kan alle være i samme liste 

Liste1 = [96,"streng",97,22,pi]

Liste1.append(36)                   #sette inn flere objekter i listen
Liste1 =Liste1 + [32.1,33]          #sette inn flere objekter i listen
Liste1.insert(0, "lørdag")          #sette inn objekt på index 0, første objekt
del Liste1[2]                       #slette indeks nummer 2
len(Liste1)                         #finne lengden på listen

Liste1
Liste1[-1]                          #se siste objekt i listen, gå baklengs
Liste1.index("lørdag")              #finne posisjonen til lørdag 
"lørdag" in Liste1
                 
Kursliste = ["inf120","fys101","math121"]
infkurs, fyskurs, matkurs = Kursliste       #sette navn til objekter i liste

"""

"""
grader_C = [-20,-15,-10,-5,0,5,10,15,20,25,30,35,40]           #for-loop
for C in grader_C:
    F = (9/5*C) + 32 
    print(f"{C:5d} {F:5.1f}")
    
""" 

"""
grader_C = [-20,-15,-10,-5,0,5,10,15,20,25,30,35,40]

index = 0 

while index < len(grader_C):                                    #while-loop 
    C = grader_C[index]
    F = (9/5)*C + 32
    print(f"{C:5d} {F:5.1f}")
    index = index + 1
"""

"""
grader_C = [-20,-15,-10,-5,0,5,10,15,20,25,30,35,40]
grader_F = []                                                   #lagre liste med loop

for C in grader_C :
    F = (9/5)*C + 32
    grader_F.append(F) 

print(grader_F)
"""
"""
liste1 = [10,20,1000,-2300.4]                   #summering av lister
liste2 = [2,4,6,8]
summert_liste = [] 

for indeks in range(len(liste1)): 
    summen = liste1[indeks] + liste2[indeks] 
    summert_liste.append(summen)
    
print(summert_liste)

"""

"""
liste1 = [10,20,1000,2000]                   #summering av lister
liste2 = [2,4,6,8]                           #med while løkke 
summert_liste = [] 

indeks = 0              #indeks starter med 0

while indeks < len(liste1): 
    summert_liste.append(liste1[indeks]+liste2[indeks])
    indeks += 1 
    
print(summert_liste)
""" 

"""
#med enumerate
liste1 = [10,20,1000,2000]                   #summering av lister
liste2 = [2,4,6,8]                           
summert_liste = [] 

for indeks, element in enumerate(liste1): 
    summen = element + liste2[indeks]
    summert_liste.append(summen)

print(summert_liste)

#enumerate gir deg både posisjonen i lista og det som høres til posisjonen. 

"""

"""
grader_C = []; grader_F = [] 
n = 16 

for i in range(n): 
    C = -5 + i*0.5                  #i = økningen
    grader_C.append(C)
    grader_F.append(9/5*C + 32)
    print(grader_C[i],grader_F[i]) 
"""         

"""
#med list comprehension 

grader_c2 = []; grader_f2 = [] 
n = 16 

grader_c2 = [(-5 + i*0.5) for i in range(n)]
grader_f2 = [(9/5*C + 32) for C in grader_c2] 
print(grader_c2) 
print("\n")
print(grader_f2)

#list comprehension = en liste med en for-løkke inni seg 
"""

"""
#legge sammen lister med zip 

grader_c2 = [(-5 + i*0.5) for i in range(n)]
grader_f2 = [(9/5*C + 32) for C in grader_c2] 

for C,F in zip(grader_c2,grader_f2):
    print(C,F)
"""  

"""
                                                #med while løkke 
liste = [] 
i = 1 

while i <15: 
    liste.append(i*2 + 10)
    i += 2 
print(liste)
"""
"""
                                                #med for løkke 

liste = [] 

for i in range(1,15,2) :
    liste.append(i*2 + 10) 
print(liste)
"""

"""
                                                #med list comprehension 
#i = 1-15, øker med to for hver gang

liste = [(i*2 + 10) for i in range(1,15,2)]
print(liste)
"""

#attributer: .append(), .insert() etc. for lister 
#objekter: int, float, str, list, tuple, range, bool 
#Funksjoner: print(), len(), range(), str(), float(), int() 



