# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 12:18:15 2024

@author: anekl
"""

# data = tall eller variabler som ikke gjør noe
# funksjoner = noe som gjør noe
# klasser = samling med variabler og funksjoner 
# klasser er en oppskrift/mal på hvordan man lager objekter 


class Y:
    
    def __init__(self, v0): 
        # klasse konstruktør (__init__). Blir automatisk kalt
        # når det lager objekter av denne klassen
        self.g = 9.81 
        self.v0 = v0 
        
    def value(self, t): 
        # metode med fritt valgt navn for å beregne 
        # verdien til kulens høyde etter tid
        return self.v0 * t - 0.5 * self.g * t**2
# Ferdig med å definere klassen y 

# Instansiere (lage) et objekt av typen Y (klassen)  
# Her blir klassen konstruktør (__init__) kalt automatisk 
y = Y(v0=3)

# Kalle y sin metode for å beregne ballens høyde etter t = 0.1
h = y.value(0.1)


ball = Y(v0 = 5)

kule = Y(v0 = 200) 

ball.value(0.1)
kule.value(0.1)

# self kan leses som "sin" - ballen sin valuemetode, kula sin valuemetode 



#%% 

class Bus: 
    def __init__ (self, passengers):
        self.passengers = []
        
    def pick_up(self, name): 
        self.passengers.append(name)
    
    def drop_off(self, name):
        self.passengers.remove(name) 
        
        
#%% 


class Cat: 
    def __init__(self, name, colour, size) :
        self.name = name
        self.colour = colour
        self.size = size
        
    def makeNoise(self):
        return "Meow!"
     
    def describeCat(self): 
        return f"{self.name} is a {self.colour} cat of {self.size} size"

Bob = Cat("Bob","Black","Medium")

Bob.name
Bob.size
Bob.colour
Bob.makeNoise()
Bob.describeCat()

kittens = [
    Cat("Sir James", "grey", "medium"),
    Cat("Miss", "black", "medium"),
    Cat("Polka", "ginger", "small"),
    Cat("Guri", "light beige", "fat"),
    Cat("Bosse", "pale", "normal"),
    Cat("Gossi", "white", "fit")
    ]


for k in kittens: 
    print(k.describeCat())
    


#%% 

class Calculator: 
    
    def __init__(self):
        self.current = 0
        
    def add(self, value):
        self.current += value 

    def subtract(self, value):
        self.current -= value 
    
    def reset(self): 
        self.current = 0 
    
    def getCurrent(self):
        return self.current

c1 = Calculator() 
c1.getCurrent()
c1.add(30)
c1.getCurrent()
c1.subtract(15)
c1.getCurrent()
c1.reset()
c1.getCurrent()
c1.add(499)
c1.getCurrent()
c1.add(50)
c1.subtract(20)
c1.getCurrent()
    

#%%
import math 

class Circle: 
    
    def __init__(self,r): 
        self.r = r 
        self.area = None
        self.circumference = None 
        
    def computeArea(self): 
        self.area = math.pi * self.r**2 
        return self.area 
    
    def computeCircumference(self): 
        self.circumference = 2 * math.pi * self.r 
        return self.circumference
    
    def printResult(self): 
        print(f"The area of the circle is {self.area:.2f}. The circumference is {self.circumference:.2f}")


sirkel = Circle(5)
sirkel.computeArea()
sirkel.computeCircumference()
sirkel.printResult()


#%% 


class Rectangle :
    
    def __init__(self,a,b): 
        self.a = a
        self.b = b 
        
    def computeArea(self): 
        self.area = self.a*self.b 
        return self.area
        
    def computeCircumference(self): 
        self.circumference = 2*self.a + 2*self.b 
        return self.area
        
    def printResult(self): 
        print(f"The area is {self.area:.2f}. The circumference is {self.circumference:.2f}")
        


rektangel = Rectangle(3, 5)
rektangel.computeArea()
rektangel.computeCircumference()
rektangel.printResult()


# bondens areal 

teiger = [Rectangle(284,499), 
          Rectangle(577,688), 
          Rectangle(707,678), 
          Rectangle(586,587), 
          Rectangle(323,567)]

totarr = 0  
for t in teiger: 
    totarr += t.computeArea()
    print(f"The area is: {totarr:.0f} m2")


#%%

import numpy as np 


def table(f, tstop, n): 
    """Make a table of t, f(t) values"""
    for t in np.linspace(0, tstop, n):
        print(f"{t:.2f} ,{f(t):.2f}")
        
ball = Y(5.0) 
kule = Y(100.0)

print("ball") 
table(ball.value, 10, 20) 

print("kule")
table(kule.value, 10, 20)


#%% 

class Person: 
    
    def __init__(self, name, mobile = None, office = None, private = None, email = None):
        self.name = name
        self.mobile = mobile 
        self.office = office
        self.private = private
        self.email = email
        
    def addMobilePhone(self, mobile):
        self.mobile = mobile
        pass
    
    def addOfficePhone(self, office): 
        self.office = office 
    
    def addPrivatePhone(self, private): 
        self.private = private 
    
    def addEmail(self,email): 
        self.email = email 
    
    def getPersonInfo(self): 
        print(self.name)
        if self.mobile is not None: 
            print(f"Mobile phone: {self.mobile}")
        if self.office is not None: 
            print(f"Office number: {self.office}")
        if self.private is not None:
            print(f"Private number: {self.private}")
        if self.email is not None: 
            print(f"Email address: {self.email}")

    def __str__(self): 
        tekst = "" 
        tekst += self.name + '\n'

        if self.mobile is not None: 
            tekst += "Mobile phone: " + self.mobile + '\n'
        if self.office is not None: 
            tekst += "Office phone: " + self.office + '\n'
        if self.private is not None:
            tekst += "Private phone: " + self.private + '\n'
        if self.email is not None: 
            tekst += "Email: " + self.email + '\n'
            
        return tekst 

Ole = Person("Ole","43124563", "23004565","91224488", "ole.henriksen@nmbu.no")

Ole.getPersonInfo()

Ane = Person("Ane", mobile = "41086199", email = "ane.student@nmbu.no")

Ane.getPersonInfo()


ansatte = [Person("Anna",email = "anna.henriksen@nmbu.no", mobile = "41984356"),
           Person("Per", email = "per.lorenzen@nmbu.no", office = "90567899")
           ]
    
for a in ansatte: 
    print(a)
    
  

    