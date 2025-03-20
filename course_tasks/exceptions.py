# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:00:35 2024

@author: anekl
"""

aList = [44,3,12] 
pos = 5 

try: 
    val = aList[pos] 
    print(val) 
except: 
    print(f'Need a position between 0 and {len(aList)} but got {pos}')

# if we remove try/except, you will get a general error 
# index error ix length is exceeded, type error if input is string (fx) 


#%% index error 

pos = 5 


val = aList[pos] 
print(val) 


#%% type error 

pos = "heisann"


val = aList[pos] 
print(val) 


#%% 

pos = "hei"

try: 
    val = aList[pos] 
    print(val) 
except IndexError:
    print(f'Need a position between 0 and {len(aList)} but got {pos}')
except TypeError: 
    print(f'Input must be of type integer, not type {type(pos)}')


#%% Exception in function 

def divide(x,y) :
    
    try: 
        res = x/y 
        #print(res)     #normally you don't print in functions, use return
        return res
    except ZeroDivisionError: 
        print("Warning: division by zero") 
    except TypeError: 
        print("Warning: you must provide numbers for x and y") 
    finally: 
        print("Executing some statement before leaving function")
            
divide(2,4)


#%% Break out of while loop 

while True: 
    try: 
        int(input("A number: "))
        break                       #gå ut av den indre løkka du er i nå
    except ValueError: 
        print("Not a number. Try again.")
        
        
        








