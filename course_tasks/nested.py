# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 08:59:06 2024

@author: anekl
"""

"""
#nøstet liste 

grader_c = list(range(-20,41,5))
grader_F = [(9/5*C + 32) for C in grader_c]
tabell =  [grader_c,grader_F]                      #tabell med to kolonner, C og F

#print(tabell)

#print(len(tabell))          # = 2 for de to listene
#print(len(tabell[0]))       # = 13 for alle elementene i grader_C

#print(tabell[0])            #hente ut tallene fra grader_c
#print(tabell[1])            #hente ut tallene fra grader_f

#print(tabell[0][6])         #hente ut tallet fra grader_c tall nr 6 


#må ha 41 for å inkludere 40 i listen
#dette er ikke en ekte liste, men et python objekt 

tabell2 = [[C,F] for C,F in zip(grader_c,grader_F)]
#print(tabell2)                                          #tabell med to rader 
print(len(tabell))
print(len(tabell2))
"""


"""
#nøstede lister 

eksliste = [[1,2,3,100],[-10,10]]

for rad in eksliste:                #for hver rad i eksliste
    for kolonne in rad:             #for hver kolonne i eksliste 
        print(kolonne)              #print kolonne 
"""

"""
#Nøstede lister. Eksamensrelevant. 

#Spiller 1: 12,16,11,12
#Spiller 2: 9 
#Spiller 3: 6,9,11,14,17,15,14,20

Scores = [[12,16,11,12],[9],[6,9,11,14,17,15,14,20]]

#Skrive ut score for hver spiller 

#Metode 1 
for index, element in enumerate(Scores):        #for en index og et element i den nøstede listen
    for subindex, subelement in enumerate(Scores[index]): 
        verdi = subelement
        print(index, verdi)

#Metode 2 
for index, element in enumerate(Scores): 
    for subindex, subelement in enumerate(element): 
        print(index, subelement)
        
#Metode 3 
for index in range(len(Scores)):                #lengden = 3, 3 sublister 
    for subindex in range(len(Scores[index])):  #lengen til index 0, 1 eller 2 (subliste 1-3) 
        verdi = Scores[index][subindex]
        print(index, verdi)
"""





