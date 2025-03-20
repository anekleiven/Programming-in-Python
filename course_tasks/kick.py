# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 13:46:46 2024

@author: anekl
"""

#Exercise 1.11 

Cd = 0.4                    #drag coeffisient 
q = 1.2                     #density of the air
a = 0.11                    #radius of the football
A = 3.14*(a)**2             #crosssectional area (normal to the velocity direction)
m = 0.43                    #mass
g = 9.81                    #Gravity 
V1 = 120/3.6                #Velocity1 of the object 
V2 = 30/3.6                 #Velocity2 of the object

Fd1 = 0.5 * Cd * q * A * (V1)**2        #Drag force with V = 120km/h
Fd2 = 0.5 * Cd * q * A * (V2)**2        #Drag force with V = 30km/h
Fg = m*g                                #Gravity force on an object 

Rounded_Fg = round(Fg,1)
Rounded_Fd1 = round(Fd1,1)
Rounded_Fd2 = round(Fd2,1)

Hardkick_drag_gravity = Fd1/Fg
Softkick_drag_gravity = Fd2/Fg
