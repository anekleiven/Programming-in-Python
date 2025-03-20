# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 05:58:46 2024

@author: anekl
"""

Liste = [1,5,7,8,0,4,3,2,10,14,13]

#indeks gir deg deler av listen basert på indekstall (fra 0-slutt og -1-slutt) 


Liste[:2]               #indeks 0 og 1 
Liste[2:]               #indeks 2 til slutt 
Liste[2:4]              #indeks 2 og 3 
Liste[-2:]              #baklengs. teller fra indeks -2: 14 og 13
Liste[-1:]              #indeks bakerste tall 
Liste[0]                #første tall i listen 
Liste[:-2]              #teller fra indeks -3 og opp
Liste[:4]               #fra indeks fire og baklengs (uten indeks 4) 

#slice deler listen basert på mellomrom 

Liste[slice(4)]         #gir de fire første verdiene - til indeks 4 
Liste[slice(6,8)]       #gir tallverdiene som ligger mellom mellomrom 6 og 8 = 2 tall 
Liste[slice(-3)]        #gir tallverdiene som ligger før mellomrom -3 bakfra 
