# -*- coding: utf-8 -*-
"""Created on <21.09.2024>"""
__author__ = "Ane Kleiven"
__email__ = "ane.kleiven@nmbu.no"
"""                       """
#the name list:

navn = [['Tore', 'Pettersen'],['Nils', 'Olavsen'],['Aase', 'Lund'],
        ['Kristine', 'Oremo'],['Tina', 'Kittelsen'],['Per', 'Carstensen'],
        ['Lena', 'Nilsen'],['Karsten', 'Woll'],['Ine', 'Ørstad'],
        ['Ravn', 'Havnås'],['Navn', 'Navnesen'],['Kari', 'Nordmann'],
        ['Lille', 'Marius'],['Jesper', 'Danberg']]


#print true or false depending on statements:

boolean_list: [] 

for first_name,last_name in navn:           
   if (first_name.startswith("T") or len(last_name) > 6 
   or (first_name == "Navn" and last_name == "Navnesen")):
       print(True)
   else:
       print(False)
       


#make an empty list for the true names:

true_navn = []                                                  


#for-loop to list the true names:

for index, (first_name,last_name) in enumerate(navn):     
    if (first_name.startswith("T") or len(last_name) > 6 
    or (first_name == "Navn" and last_name == "Navnesen")):
        true_navn.append((index + 1, [first_name,last_name]))     
        
                             #enumerate function pairs the index and the value
                             #append function: adds the elements to my list              
        
        
#print results, each true name on separate lines:

for position, name in true_navn:                                
    print(f"{position}: {name[0]} {name[1]}")
