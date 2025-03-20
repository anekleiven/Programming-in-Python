# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:53:15 2024

@author: anekl
"""

#%%
# the input function 

C = input('Write degrees of Celsius: ')
Cf = float(C) 
F = 9/5 * Cf + 32 
print('Temperature in degrees Fahrenheit', F) 

#the user has to choose a value for C 


#%% 
#even numbers up to n*2 

n = int(input('n: '))
for i in range(2,2*n+1,2):
    print(i) 
    

#%% eval function 

r = eval('1+2')                 #string with mathematical function 

l = eval('[3,4,5,6]')           #string with a list 

print(l), type(l) 

s1 = "'This is text'" 
k = eval(s1)
print(k), type(k)


#%% eval with two input variables = evaluation. Returnerer en verdi. 

i1 = eval(input('Verdi 1: '))
i2 = eval(input('Verdi 2: '))

a = i1 + i2 

print(f' {type(i1)} + {type(i2)} becomes {type(a)} with value {a}')

# nb: eval funksjonen trenger noe som gir et resultat

#%% exec function = "execute"/utføre noe. Returnerer none.  
# gir flere muligheter enn om man legger inn funksjoner direkte 

statement = 'r = 1 + 1'
exec(statement)
print(r)

# for long codes, we can use multi-line strings 

someCode = """
def F(x): 
    term1 = 2 * x**4 
    term2 = x / 10 
    return term1 + term2 
""" 

exec(someCode)                  #this code makes someCode into F(x) 

F(2)



