# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 12:58:23 2024

@author: anekl
"""

#%% first matplot

import numpy as np

# import pyplot, submodule from matplotlib
import matplotlib.pyplot as plt 


x = np.linspace(0,3,20) 
y = np.linspace(0,9,20) 

plt.plot(x,y) 
plt.plot(x,y,"o") # to make pointed line


#%% 

import numpy as np

# import pyplot, submodule from matplotlib
import matplotlib.pyplot as plt 

def f1(t): 
    return t**2 * np.exp(-t**2) 

def f2(t, func): 
    return t**2 * func(t) 

t = np.linspace(0,3,50) 
y1 = f1(t) 
y2 = f2(t,f1)

plt.plot(t,y1, "r-")            # red line
plt.plot(t,y2, "bo")            # blue pointed line

plt.xlabel("t")
plt.ylabel("y") 

plt.legend(["t**2 * exp(-t**2)", "t**2 * f1(t)"])
plt.title("plotting two curves in the same plot")


plt.savefig("kurve2.png")

plt.show()



#%% to plots i samme figur


import numpy as np 
import matplotlib.pyplot as plt 

x1 = np.linspace(0.0,5.0)  # default n (=50) 
x2 = np.linspace(0.0,2.0) 

y1 = np.cos(2* np.pi * x1) * np.exp(-x1) 
y2 = np.cos(2* np.pi * x2) 

# number of columns, rows and index
plt.subplot(2,1,1)

plt.plot(x1,y1,"ko-")
plt.title("A tale of 2 subplots")
plt.ylabel("Damped oscilattion") 

plt.subplot(2,1,2) 
plt.plot(x2,y2,"r.-") 
plt.xlabel("time (s)") 
plt.ylabel("Undamped")

plt.savefig("test.eps") 
plt.savefig("test.png") 
plt.savefig("test.jpg") 

plt.show()


 

plt.show()



#%% plot with to y-axes 

import numpy as np 
def f1(t): 
    return t**2 * np.exp(-t**2) 

def f2(t, func): 
    return t**2 * func(t) 


t = np.linspace(0,3,50) 

y1 = f1(t) 
y2 = f2(t,f1)

fig, ax1 = plt.subplots()
ax1.plot(t,y1,"b.-")
ax1.set_label("tid")
ax1.set_ylabel("temp", color = "blue") 

ax2 = ax1.twinx() 
ax2.plot(t,y2,"m")
ax2.set_ylabel("regn", color = "magenta")







