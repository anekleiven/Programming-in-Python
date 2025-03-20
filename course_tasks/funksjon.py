rownames_to_column()
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:13:47 2024

@author: anekl
"""

#Funksjoner og branching (forgreininger)

#Funksjon = en samling med utsagn vi kan utføre hvor og når vi måtte ønske  
#Funksjoner kan ta inputobjekter og produsere outputobjekter 
#Funksjoner hjelper oss å organisere programmer, gjøre dem mer oversiktlig, kortere, lettere å utvide 

#%%
#lage nye funksjoner 
def convCtoF(C): 
    return (9/5)*C + 32

# kaller (bruker) funksjonen 
Fval = convCtoF(20)
#variabel av typen float  

Fval  #python svarer med verdien på variabelen 

print(Fval)


#lage den motsatte funksjonen 
def convFtoC(F) :
    return (F - 32)*5/9

Cval = convFtoC(68)

Cval 

print(Cval)

#%%
deg_C = list(range(-20,41,5))
deg_F = [] 


#vanlig forløkke
for C in deg_C: 
    deg_F.append(convCtoF(C))
    
#list comprehension
deg_F2 = [convCtoF(C) for C in deg_C]


#%% 

# lokale variabler 

def sumint(start,stop): 
    s = 0          #sum variabel 
    i = start      #løkketeller = hvor mange ganger løkka kjører 
    while i <= stop:    #tester om i er mindre eller lik stopp 
        s+=i            #sum = sum + i 
        i+=1            #i = i + 1 
        print(s,i)
    return(s) 

sum_0_10 = sumint(0,10)
print(sum_0_10)


#%% 

def yfunc(t,v0):
    g = 9.81
    return v0*t - 0.5*g*t**2 

y = yfunc(0.5, 6)           #kalle funksjonen på ulike måter
y = yfunc(0.5, v0 = 6)
y = yfunc(t = 0.5, v0 = 6)
y = yfunc(t = 0.5, v0 = 6) 
y = yfunc(v0 = 6, t = 0.5)

#Funksjoner kan inneholde så mange argumenter man ønsker. 

#%% 

#Balistisk 

def yfunc(t,v0): 
    g = 9.81
    y = v0*t - 0.5*g*t**2 
    dydt = v0 - g*t  
    return y,dydt                   #position and velocity 

#unpack returned tuple 
pos, vel = yfunc(6,3)               #position and velocity 

status_ball = yfunc(0.6,50)         #returnerer en tuple, en liste som ikke kan endres
pos2 = status_ball[0]
vel2 = status_ball[1]


#%% 
#Function with three variables 


def f(x): 
    return x,x**2,x**4

t1 = f(3) 
print(type(t1)) #tuple
print(t1)

#%% Oppgave printfunksjoner 

def printA():
    print('A', end = "")            #ikke bytt linje etter denne koden 

def printB(): 
    print('B') 

def printAB(): 
    printA() 
    printB() 
    
#%% #NoneType 

def melding(course): 
    print(f"{course} is the worst!!!")      #f står for formateringsstreng  
                                            #krøllparentes: putt inn verdi 
melding('INF120')

R = melding('Fisketur')                     #R = NoneType 
print(type(R))


#%% Arguments with default values 

def someFunc(arg1,arg2,arg3=False,arg4="hei"):
    print(arg1,arg2,arg3,arg4)

someFunc("Mann","Dame")
someFunc(3,4,7)
someFunc(arg4="Hei",arg3=False,arg1 = 2,arg2 = 4)
someFunc('dette','er','din','dag')













    