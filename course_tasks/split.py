# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 18:55:40 2024

@author: anekl
"""
with open("data/data.txt", "r") as tall: 
    text = tall.read() 

#first 2 numbers 
nums = text.split("\n", maxsplit = 2)
print(nums)


#%% split function 

quote = """Hei du er en ost, 
og jeg er en skinke"""

words_by_space = quote.split(",")    #split by comma
words_by_space = quote.split()       #split by single words 

words_by_space[4]

#max antall split, resten i egen streng
words_by_space = quote.split(" ", maxsplit=2)
words_by_space[2]


#split på linjeskift: 
    
words_by_space = quote.split("\n")
words_by_space[0]


#%% read rainfall file 

#make a function to interpret one type of files 
#e.g. london, rome etc. 

def extract_data(filename):
    
    with open(filename, "r") as fh: 
        fh.readline()                       #throw away the first line
        num = [] 
        #read each line and convert to numbers
        for line in fh: 
            words = line.split()
            n = float(words[1])
            num.append(n)
    
    return num


values = extract_data("data/rainfall.dat")
import matplotlib.pyplot as plt 
#Month number
month_indices = range(1,13)         #line 1 to 12 contains the 12 months
plt.plot(month_indices, values[:-1],["b-"])

#b- = blue colour and - for line 




