# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 18:15:22 2024

@author: anekl
"""
#%% read one line in file 
infile = open("data/data.txt","r")

line1 = infile.readline()
line2 = infile.readline()
line3 = infile.readline()
line4 = infile.readline() 
line5 = infile.readline()
line6 = infile.readline()


infile.close() 


#%% read line for line in for loop 

infile = open("data/data.txt","r")

for line in infile: 
    print(line) 
    
    
infile.close() 


#%% make a list off all elements in file 
# linjeskifttegnet er inkludert i listen 

infile = open("data/data.txt","r")
listen = infile.readlines()

print(listen)

for tall in listen: 
    print(tall)      #gir to linjeskift - ett fra list og et for hvert nye tall 
    

#%% automatic closing of file 

with open("data/data.txt","r") as infile:
    for line in infile: 
        print(line)
    
infile.closed   #check whether the file is closed or not 


#%% import values from text file and calculate mean value 

tall = []
with open("data/data.txt", "r") as liste1:  
    for line in liste1:
        n = float(line)
        tall.append(n)
        
type(tall)
type(n)

s = sum(tall)
number_in_list = len(tall)

mean = s/number_in_list
print(f"Mean value: {mean}")
print(f"Mean value: {s/number_in_list}")        #direct calculation 


#%% with list comprehension 

tall = []
with open("data/data.txt", "r") as liste1:  
    for line in liste1:
        n = float(line)
        tall = [float(line) for line in liste1]    #list comprehension 
        
type(tall)
type(n)

s = sum(tall)
number_in_list = len(tall)


#%% different methods on file object 

tall = open("data/data.txt","r")

#read entire file as text string: 
text = tall.read()   
text

#read one line from file
l1 = tall.readline()  #empty because all the lines were read in the code above

tall.close            #close the file 

tall.closed           #check if file is closed 

tall.tell             #count number of tall in list? 

#tell function counts number of bytes moved/read from file 


#EOF

