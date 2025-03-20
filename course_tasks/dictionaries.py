# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 13:22:04 2024

@author: anekl
"""

# also called associative array. One thing associated with another. 
# kobling mellom key og value. Key = indeks 

eng_to_nor = {"cat":"katt",
              "dog":"hund",
              "mouse":"mus",
              "cow":"ku"}

eng_to_nor["cat"]               # output: the belonging value. Doesn't work the other way
#eng_to_nor["katt"]             # key error 

eng_to_nor["snake"] = "slange"  # add element to dictionary 

del eng_to_nor["snake"]         # remove element from dictionary 

print(eng_to_nor)
eng_to_nor                      # list dictionary 
eng_to_nor.keys()               # list all keys
eng_to_nor.values()             # list all values 

                                # indexing and slicing on dictionaries 
list(eng_to_nor.keys())[3]      # indexing
list(eng_to_nor.keys())[3:]     # slicing 
list(eng_to_nor.keys())[2:]

eng_to_nor.items()              # list all pairs in dictionary as tuples 

kl = list(eng_to_nor.keys())
kl[3]
kl[1:]
kl[:]
kl[0:]
kl[:4]
kl[::4]


#%% Loop through all keys and values in the dictionary 

for norsk, engelsk in eng_to_nor.items():
    print(norsk, engelsk) 
    

#%%  ask if a certain key exists in the dictionary 

"snake" in eng_to_nor 
"dog" in eng_to_nor 
"hund" in eng_to_nor
    
# output = true or false 


#%% EXERCISE 

counts = {}

words = ["the", "little", "man", "sat", "on", "the", "little", "house"]
    
# alternativ 1: look before you leaf 
for word in words: 
    if word in counts:
        counts[word] +=1 
    else: 
        counts[word] = 1 
        print(counts)
    
count = {}

# alternativ 2: enklere med tilgivelse enn tillatelse 
for word in words: 
    try: 
        count[word] += 1 
    except: 
        count[word] = 1 
    
    
#%% Dictionaries in use 

# order

temps = {"Oslo":10.7,
         "Stockholm":13.5, 
         "Copenhagen":14.3, 
         "Dubai":27.0, 
         "London": 18.9,
         "Anchorage":-12}

for key in temps: 
    value = temps[key]
    print(f"The temperature in {key} is {value}C")

# sorted after key     
for key in sorted(temps): 
    value = temps[key]
    print(f"The temperature in {key} is {value}C")


#%% Polynomer 

p = {0:-1, 2:1, 7:3}  # = -1 + x**2 + 3x**7 

# alt 1 
def poly1(data,x): 
    tot = 0 

    for p in data: 
        tot += data[p]*x**p
    
    return tot

poly1(p,3)
poly1(p,50)
poly1(p,0)
poly1(p,2)

# alt 2
def poly2(data, x): 
    return sum([data[p]*x**p for p in data])

poly2(p,3)


#%% read file to dictionary 

infile = open("data\city_temperatures.txt","r")

temp = {}

data = infile.readlines()

for line in data:
    city, tempe = line.split(":")
    # remove : 
    city = city[:-1] 
    temp[city] = float(tempe)
    
for c,t in temp.items(): 
    print(c,t)
    
    
#%% read modified file (with spaces)

infile = open("city_temperatures.txt","r")

temp = {}

data = infile.readlines()

for line in data:
    city, tempe = line.split(":")
    temp[city] = float(tempe)
    
for c,t in temp.items(): 
    print(c,"-", t)

infile.close()

#%% nested dictionary 


data = {} 

infile = open("measurements.txt", "r") 

# create dict keys for features 
lines = infile.readlines() 
navn = lines[0].split() 
print("navn:", navn)

# property name as keys and new dicts as value 
for n in navn: 
    data[n] = {} 
print("data:", data)
    

for line in lines[1:]:  
    words = line.split()
    print(words)
    i = int(words[0])
    for p, v in zip(data.keys(), words[1:]):
        # p: property (column key) 
        # i: sample number (row key) 
        # v: measurement value 
        print(p, i, v) 
        if v != "NaN": 
            data[p][i] = float(v) 

print("data:", data)

# calculate average for each property 

print("calculate average:")
for p in data: 
    col_vals = data[p].values() 
    print(col_vals)
    avg = sum(col_vals)/len(col_vals)
    data[p]["avg"] = avg

print(data)


