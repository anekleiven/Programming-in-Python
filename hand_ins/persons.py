
# -*- coding: utf-8 -*-
"""Created on 26.09.24"""
__author__ = "Ane Kleiven"
__email__ = "ane.kleiven@nmbu.no"
"""                  """

#The full name list: 
    
navn = [['Tore', 'Pettersen'],['Nils', 'Olavsen'],['Aase', 'Lund'],
        ['Kristine', 'Oremo'],['Tina', 'Kittelsen'],['Per', 'Carstensen'],
        ['Lena', 'Nilsen'],['Karsten', 'Woll'],['Ine', 'Ørstad'],
        ['Ravn', 'Havnås'],['Navn', 'Navnesen'],['Kari', 'Nordmann'],
        ['Lille', 'Marius'],['Jesper', 'Danberg']]


boolean_list = []           #make an empty list for true/false values
true_names = []             #make an empty list for the names that is true 

#for loop to find true/false names based on criteria: 

for first_name,last_name in navn:          
   if (first_name.startswith("T") or len(last_name) > 6 
   or (first_name == "Navn" and last_name == "Navnesen")):
       print(True)
       boolean_list.append(True)         #add the true values to "boolean_list"
   else:
       print(False)
       boolean_list.append(False)        #add the false values to boolean_list
       
       
#for loop to add the index and true names to the empty list "true_names": 

for index, (first_name, last_name) in enumerate(navn):
    if boolean_list[index]:  
        true_names.append((index, first_name, last_name)) 
        print(f"{index+1}: {first_name:<4}  {last_name}")

