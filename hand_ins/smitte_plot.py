# -*- coding: utf-8 -*-
"""Created on Sun Oct 27 08:01:07 2024"""
__author__ = "Ane Kleiven"
__email__ = "ane.kleiven@nmbu.no"
"""                  """
# import libraries 

import numpy as np
import matplotlib.pyplot as plt 


# open file and read s,i,r values into a nested list 

with open("data/pan.csv","r") as sir: 
    sir.readline() 
    sir_table = [] 
    for line in sir: 
        values = line.split(",")
        s, i, r = float(values[1]), float(values[2]), float(values[3])  
        sir_table.append([s, i, r])


# convert table to numpy array 

sir_array = np.array(sir_table)


# plot the values using matplotlib.pyplot 

plt.plot(sir_array[:, 0], label = "susceptible", color = "indianred") 
plt.plot(sir_array[:,1], label = "infectious", color = "darkorange")
plt.plot(sir_array[:,2], label = "recovered", color = "royalblue")

# decorate the plot 

plt.xlabel("Days")
plt.ylabel("Prevalence")
plt.title("SIR plot")
plt.legend()

plt.show()                          # show plot 

plt.savefig("SIR_plot.png")         # save plot to computer 


"""
1. Omtrent hvor stor andel av befolkningen er smittet/syk samtidig, 
   på det meste?
   40 % av befolkningen er smittet på det meste (~dag 65).

2. Etter omtrent hvor mange dager har de fleste blitt friske igjen?
   Ved dag 100 (cirka) har de fleste blitt friske igjen. 
"""
