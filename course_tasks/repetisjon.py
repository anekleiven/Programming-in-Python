# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 09:39:54 2024

@author: anekl
"""

# int(), float(), divmod(), pow() 
# objekt, funksjon 
# kodefeil 
# arrays, indeksering og slicing
# fillesing, hvordan lese disse dataene
# logikk, evaluering av logiske uttrykk - sammensatte 
# klassebeskrivelse
# plotting 
# dictionaries 
# try except 

# Matteoperasjoner 

a = 5
b = 3 

a+b 
a-b 
a*b 
a/b
a//b
a%b 

f"{59.5568498:.2f}"
f"{0:.2f}".format(59.5568498)

pow(2,5,2)


a = [4,5,6,7] 
b = [4,7,8,9] 
a+b 
# [4,5,6,7,4,7,8,9] 

a.insert(0, 8)
del(a[0])
len(a)
b.insert(3,5)
b
a.index(4) # finne ut hvilken index som inneholder tallet 4 
a.index(4,0,5) # let etter 4 mellom index 0 og 3 
a.append(4)
a.count(4)

c = list(range(2,11,4))
d = list(range(3))

a
test = enumerate(a) 
print(list(test))



# list comprehensions 


number = [1,2,3,4,5] 

# new_list = [new_item for item in list] 

new_number = [num*2 for num in number if num > 2]


# join function 

words = ["Hey", "my", "name", "is", "ane"]
sentence = "_".join(words)



#%%


import matplotlib.pyplot as plt

# Create a 1x2 grid of subplots
plt.subplot(2, 1, 1)  # First subplot (1 row, 2 columns, position 1)
plt.plot([0, 1], [0, 1])
plt.title("Plot 1")

plt.subplot(2, 1, 2)  # Second subplot (1 row, 2 columns, position 2)
plt.plot([0, 1], [1, 0])
plt.title("Plot 2")

plt.show()


fig, axes = plt.subplots(2, 2)  # 2x2 grid of subplots
axes[0, 0].plot([0, 1], [0, 1])  # First subplot
axes[0, 1].plot([0, 1], [1, 0])  # Second subplot
axes[1, 0].plot([0, 1], [0, 0])  # Third subplot
axes[1, 1].plot([0, 1], [1, 1])  # Fourth subplot
plt.show()


#%% 

#dict 

student = {"name" : "Ane", 
           "age" : 28, 
           "school" : "NMBU", 
           "subjects" : ["proteinchemistry", "functional genomics", "programming in python"]}

student.keys()
student.values() 
student["name"]
student["subjects"]
del student["age"]
student.keys()
student.values()
student.update({"age" : 28})
student.items()
"age" in student 

hilsen = "\n"
hilsen[8:]
hilsen.lstrip("h")

hilsen.isdigit()
hilsen.endswith("00")
hilsen.isspace()


#%% 

import random as rd

print(rd.random())
liste = [1,2,3,5,6,"hei","ball", "hatt", "9,44"]
Setning = "Hei jeg heter bjarne" 
rd.choice(liste)

test = ["banan", "ball", "lang", "kort", "nisse", "jul"]
rd.shuffle(test)
print(test)

rd.shuffle(liste)
print(liste)

test.pop()
test.pop(1)
test

#%% 

a = [1,2,3,7,4,2,5,6,8]
b = [4,5,6,3,5,6,7,42,1,4,6,7]

c = zip(a,b)
print(tuple(c))
sorted(a)
b.sort()
b.sort(reverse = True)


#%% 
import numpy as np 

arr = np.array([[1,2,3,4],[1,42,3,5],[3,4,5,7]])
arr[1,1]
arr[1,0:]
arr[2,-1]
arr[-1,-1]
arr[0,3]
arr[0,::2]
arr[0,::]

rekke = np.linspace(0,30)
nytest = np.zeros(3)

arr[0:3:1]
arr[0:3:1,::]
# arr[start index rad: stopp index rad : step index rad] 
# samme som: arr[0:3:1,]

np.where(arr == 2)

arr[:,1]

np.shape(arr)
horisontal = np.hstack(arr)
vertikal = np.vstack(horisontal)

isinstance("Hello", str)
isinstance(5, float)
