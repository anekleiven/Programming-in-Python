# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 12:30:25 2024

@author: anekl
"""

#%%


import numpy as np 


arr_a = [[1,3,4,5],[1,4,6,7]]
arr_b = np.array(arr_a)
# take home message: here a is a list, b is a numpy array - not a "carbon copy" 

# copy without the same object 
c = arr_b.copy()
c[0,2] = 99
arr_b[0,2] = 55     # 55 will only be changed in b 



#%% two dimensional arrays

Array = np.zeros([3,4])             # array with zeros. 3 rows and 4 columns
Array[0,0] = -1
Array[1,0] = 0
Array[2,0] = 3
Array[1,1] = 6
Array[2,2] = 5
Array[0,1] = 8 


Array[0][1] = 55                    # same as array[0,1]


#%% Nested list to array 


grader_c = [-30 + i*10 for i in range(4)]
grader_f = [9/5*C + 32 for C in grader_c]

tabell = [[C,F] for C,F in zip(grader_c,grader_f)]


# convert to numpy array 

tabell2 = np.array(tabell)

# shape of [0] = number of rows, [1] = number of columns
for i in range(tabell2.shape[0]):           
    for j in range(tabell2.shape[1]): 
        print(f"tabell2[{i},{j}] = {tabell2[i,j]}")


# same output with np.ndenumerate
for indeks, element in np.ndenumerate(tabell2): 
    print(f"tabell2[{indeks[0]},{indeks[1]}] = {element}")
    

rader, kolonner = np.shape(tabell2) 
print(rader) 
print(kolonner)


ny_tabell = np.zeros(np.shape(tabell2))


#%% 

import numpy as np

en_liste = [[1,2,4,5],[5,4,6,7]]

horisontal = np.hstack(en_liste)
vertikal = np.vstack(en_liste)


en_array = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
en_kopi = np.copy(en_array)

bred_array = np.hstack([en_array,en_kopi])
høy_array = np.vstack([en_array,en_kopi])


isinstance(en_array, np.ndarray)          # sjekker om en_array er en numpy array
isinstance(en_liste, np.ndarray)


#%%


def is_np_array(x): 
    if isinstance(x, np.ndarray):
        print(x.shape)
        return True
    else: 
        print("dette er ikke en numpy array")

is_np_array(en_liste)
is_np_array(en_array)


#%% 

array_a = np.array(range(1,501,1))
array_b = np.array(range(501,1001,1))

# eventuelt: 
# array_a = np.linspace(1,500,500)
# array_b = np.linspace(501,1000,500)
# array_a = np.arange(501,1001)

def add_arrays(arr1,arr2): 
    for i in range(len(array_a)): 
        tall = arr1[i] + arr2[i]
        arr1[i] = tall 
    return arr1
    

add_arrays(array_a, array_b)


#%% funksjon for å definere en array eller et enkelttall 

def f(x): 
    if isinstance(x, (float,int)):
        return 2 
    elif isinstance(x, np.ndarray):
        return np.zeros(np.shape(x), x.dtype) + 2 
    else: 
        raise TypeError("x må være int, float eller array, ikke {x.type}")
        
f(array_a)


#%% time

import time 

stor_array = 10**7
arr1 = np.zeros(stor_array) + 2 
arr2 = np.zeros(stor_array) + 2

tidspunkt1 = time.time()
for i in range(len(arr1)): 
   tall = arr1[i] + arr2[i]
   arr1[i] = tall 

slutt1 = time.time()

tiden1 = slutt1-tidspunkt1
print("bruke loop tid:", slutt1-tidspunkt1) 

tidspunkt2 = time.time() 
arr1+=arr2

slutt2 = time.time() 
tiden2 = slutt2 - tidspunkt2

print("bruke vektorisert tid", slutt2-tidspunkt2)

print(f"vektorisert er {tiden1/tiden2} ganger raskere")


#%% slicing and indexing 

array_t = np.linspace(1,8,8)

b = [2,3,4]

array_t[b]          #index array with another array - exam question 

array_t[2:7:3]

array_t[2:4]
array_t[:4]


# this is not allowed for lists! only for arrays. EXAM
array_t[array_t > 2]
array_t[array_t < 2]
array_t[array_t < 0]

array_t[array_t < 2] = array_t.max()        #changes the first number into the highest value in the array

np.where(array_t == 7)          #what index is equal to 7 


#%% slice av to-dimensjonale arrays

# henter ut andre kolonne

en_array[0:en_array.shape[0],1]
en_array[0:,1]
en_array[:,1]

# : = all rows, 1 = column 2 (indexing starts at 0)
# 0:en_array.shape[0] = alle rader fra 0 til totalt ant. rader av en_array = alle rader


#%% slice with bigger array 

t = np.linspace(1,48,48).reshape(6,8)

t[1:-1:2,2:]

# gi meg rad 1 til og med nest siste rad, hopp over hver andre rad 
# kolonne 2 og bortover 

d = np.linspace(1,36,36).reshape(6,6)

d[0,3:5]

# gi meg rad 0 (indexing fordi det er uten kolon), kolonne 3-5 (slicing) = TALL 4 OG 5

d[4:,4:]
d[4:6,4:6]
d[-2:,-2:]

d[0:,2:3]
d[:,2:3]
d[0:,-4]
d[:,2]

d[2::,2]            #fra rad 2, kolonne 2
d[2::2,2]           #fra rad 2, kolonne 2. Hopp over annenhver 
d[2::2,::2]         #rad 2,4 (annenhver). fra kolonne 0, annenhver kolonne


#%% Plot arrays 

from scipy import misc 
import matplotlib.pyplot as plt
frame = misc.face(gray = True)
frame = 1*frame
plt.imshow(frame, cmap="gray")

import numpy as np

type(frame)
frame.shape

# min og maks value. lys eller mørk piksel. 
frame.max()
frame.min()

# høyre øye 
plt.imshow(frame[300:360,680:750], cmap="gray")


            