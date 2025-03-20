
# -*- coding: utf-8 -*-           
"""Created on Thu Oct 24 12:58:23 2024"""
__author__ = "Ane Kleiven"
__email__ = "ane.kleiven@nmbu.no"
"""                  """

b = 1/3             # infection rate 
k = 1/10            # recovery rate
n = 121             # number of days in simulation

# start values
s = 1.0             # susceptible individuals at day 0
i = 10 / 5e6        # infected individuals at day 0 
r = 0.0             # recovered individuals at day 0 

# function to calculate s,i,r for each day 
def updateSIR(s_y, i_y, r_y, b,k) :
    new_s = s_y - b * s_y * i_y 
    new_i = i_y + b * s_y * i_y - k * i_y
    new_r = r_y + k * i_y 
    return new_s,new_i,new_r


SIR = []            # empty list for the S,I,R values 

# simulation for 120 days 
for day in range(n):            
    SIR.append((day,s,i,r))             # add SIR values to list 
    s_y, i_y, r_y = s,i,r               # yesterdays values 
    s,i,r = updateSIR(s_y,i_y,r_y,b,k)  # update values to todays values 
    

with open("data/pan.csv", "w") as simulation:
    simulation.write("Day, s@day,i@day,r@day, \n")      # table header 
    for row in SIR[1:]:                 # skip day 0 
        simulation.write(f"{row[0]},{row[1]:.3e},{row[2]:.3e},{row[3]:.3e}\n")

