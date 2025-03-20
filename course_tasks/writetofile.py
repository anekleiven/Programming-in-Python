# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 10:12:25 2024

@author: anekl
"""

#%% 

with open("data/tmp_table.dat") as table: data = [[float(num) for num in line.split()] for line in table]  

print(data) 


# code to write data to CSV file csv_table.txt

with open("csv_table.txt","w") as ofh: 
    #ofh output file object (file handle) 
    for row in data: 
        for col in row: 
            ofh.write(f'{col:.2f}, ')
        #write newline 
        ofh.write("\n")
#Exit open file context -> closes file automatic 



#%% 

with open("data/tmp_table.dat") as table: data = [[float(num) for num in line.split()] for line in table]  

print(data) 


# code to write data to CSV file csv_table.txt

with open("tsv_table.txt","w") as ofh: 
    #ofh output file object (file handle) 
    for row in data: 
        for col in row: 
            ofh.write(f'{col:14.8f}')
        #write newline 
        ofh.write("\n")
#Exit open file context -> closes file automatic 