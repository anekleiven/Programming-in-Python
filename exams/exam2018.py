# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 10:08:47 2024

@author: anekl
"""

#%% 

# Spørsmål 1 

print("Cartoon".replace("o", "a"))
# Cartaan

print(int(10.0/int("2")))
# 5 

print("*".join(["student","at","NMBU".lower()]))
# student*at*nmbu 

"Berlin: 18.4 C at 4 pm".split() 
#["Berlin:", "18.4", "C", "at", "4", "pm"]

print("The person is {0:.2f} m tall, weighs {2} kg and has shoe size {1}".format(1.5999, 40, 45))
# The person is 1.60, weighs 45 kg and has shoe size 40

"Glasgow: 22.2 C at 4 pm".split(":")[1].split()[0]
# 22.2 

"Oslo: 22.3 C at 6 pm".split(".")[0].split()[1]


#%% 


# Oppgave 2 


a = 7
b = -3 

a > 0 and b < 0 
# True

b > 0 or a < 0 
# False

a != 3 and b <=-1 
# True  

a > 1 or not (b != 1) 
# True 

not (a < 0 and not (b >= -3)) 
# True


#%% 

# Oppgave 3 
comb = [] 
colours = ["green", "red", "blue"]
numbers = [7,8,9]

for colour in colours: 
    for number in numbers: 
        comb.append(colour + str(number))

print(comb)
 

#%% 

# Oppgave 4 

fridager = {"17.mai" : "Nasjonaldagen", 
            "24.desember" : "Julaften", 
            "25.desember" : "første juledag",
            "26.desember" : "andre juledag",
            "31.desember" : "Nyttårsaften",
            "1.januar" : "første nyttårsdag",
            "1.mai" : "Arbeidernes dag"}

def helligdager():
    dato = input("Angi dato: ") 
    if dato in fridager: 
        print(f"Dette er {fridager[dato]}") 
    else: 
        print("Denne fridagen finnes ikke i vår database")



helligdager()


#%% 

# Oppgave 5: try-except 


data = [2, "NaN", 5, 9, "NaN", "NaN", 3]

def integer_adder(liste): 
    result = 0 
    for number in liste: 
        try: 
            number = int(number) 
            result += number ** 2 
        except (ValueError, TypeError): 
            pass 
    return result 

test = [2,"NaN", 3,4]
integer_adder(test)
integer_adder(data)

#%% 

# Oppgave 6 

group_1 = ["Italy", "France", "Germany", "UK", "Spain"]
group_2 = ["Ireland", "Norway", "Norway", "Ireland", "Italy"] 
group_3 = ["Ireland", "Italy", "Norway", "Portugal", "Portugal"]
group_4 = ["Denmark", "Belgium", "Austria", "Portugal", "UK"]

set(group_1) 
# {"Italy", "France", "Germany", "UK", "Spain"}

set(group_2) - set(group_1) 
# {"Ireland", "Norway"}

set(group_3) & set(group_4) 
# {"Portugal"}

set(group_2) | set(group_3) 
# {"Ireland","Norway", "Italy","Portugal"}


#%% 

# Oppgave 7: funksjoner

import math 

originalvalues = [4.5, 3.3, 9.2]
predictedvalues = [4.5, 3.7, 9.6] 
N = len(predictedvalues)

def calc_rmsep(originalvalues, predictedvalues): 
    squared_diff = sum((o-p) ** 2 for 0)
    RMSEP = math.sqrt(1/N * sum(originalvalues - predictedvalues)**2)
    return RMSEP 

calc_rmsep(originalvalues, predictedvalues)

#%% 

# oppgave 1 

print('Cartoon'.replace('o', 'a')) 
#Cartaan

print(int(10.0 / int('2')))
# 5 

print('*'.join(['student', 'at', 'NMBU'.lower()]))
#student*at*nmbu

'Berlin: 18.4 C at 4 pm'.split()
#['Berlin:', '18.4', 'C', 'at', '4', 'pm']

print('The person is {0:.2f} m tall, weighs {2} kg and has shoe size {1}.'.format(1.5999, 40, 45))
# The person is 1,60 m tall, weighs 45 kg and has shoe size 40

f'Glasgow: 22.2 C at 4 pm'.split(':')[1].split()[0]
# 22.2

# oppgave 2 
a = 7
b = -3 

a > 0 and b < 0 
# True 

b > 0 or a < 0 
# False 

a != 3 and b <= - 1
# True 

a > 1 or not(b != 1) 
# True
    
not(a < 0 and not(b >= -3))
# True


# oppgave 3 


colours = ['green', 'red', 'blue']; numbers = [7, 8, 9]

for c in colours: 
    for n in numbers: 
        print(c + str(n))
        

fridager = {"17. mai" : "nasjonaldagen",
            "24. desember" : "julaften", 
            "31. desember" : "nyttårsaften"} 

dato = input("Angi dato: ")
if dato in fridager: 
    print(f"Dette er {fridager[dato]}")
if dato not in fridager: 
    print("Denne datoen finnes ikke i vår database..")









































