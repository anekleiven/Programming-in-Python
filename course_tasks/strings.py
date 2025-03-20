# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 07:30:23 2024

@author: anekl
"""

# strings er konstante objekter som ikke kan endres (som tuples) 

string = 'Berlin: 18.4 C klokken 16'
type(string)
len(string)
string[1:]

string.find("Berlin")
string.find(":")
string.upper()
string.lower()
string.find("18.4")         # gir oss indexen der ordet vi søker på starter 
string.find("5")            # output -1, 5 finnes ikke i strengen
string.find("4")            # nb: gir bare det første 4-tallet i strengen 

"Berlin" in string          # true or false 

string.endswith("16")
string.endswith("6")
string.startswith("B")
string.startswith("Berlin")

#%%
# finne tall som kommer flere ganger i en streng 

new_string = "Hallo hello hellow yellow gull"

index = 0 
funnet = [] 

while index < len(new_string): 
    index = new_string.find("ll", index)
    
    if index == -1: 
        break 
    funnet.append(index)
    print(f"Fant dobbel l ved index {index}")
    index += 2

#%% 
Berlin = 'Berlin: 18.4 C klokken 16'
Berlin.replace("Berlin", "Oslo")
Berlin.replace(Berlin[:Berlin.find(":")], "Paris")


#%% Separate strings into substrings 

Berlin.split()
Berlin.split(":")
Berlin.split(":")[1].split()[1]            # think step by step 


#%%

test_string = "First line \nSecond line\nThird line"
print(test_string)

test_string.split("\n")     # split by new line 
test_string.splitlines()    # same output 


#%% 

text = "                         string med mange                mellomrom"
text.strip()                # fjerner mellomrom 
text.lstrip()               # fjerner mellomrom på venstre side 
text.rstrip()               # fjerner mellomrom på høyre side

#%% 

NZ_byer = ["Auckland", "Wellington", "Hobbitun", "Mordor"]
"; ".join(NZ_byer).split("; ")      # join and split are opposite functions 


#%% 

line = "This is a line of words separated by space" 

words = line.split()

line2 = " ".join(words[2:])

line
line2




