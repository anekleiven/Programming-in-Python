# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 10:37:32 2024

@author: anekl
"""
# pandas is a combination of numpy and matplotlib

import pandas as pd  

datafile = "data\data.txt"
myData = pd.read_table(datafile, header = None)

rainfile = "data\rainfall.dat"
rainData = pd.read_fwf(open(rainfile), header = None, skiprows = 1, widths =  [5,5])
#widths = number of signs per column 

# other parameters in pandas: 
# header, none or line number 
# sep, separate columns 
# decimal, komma eller punktum som decimalskilletegn 


# from DataFrame to list 
rainfall_list = rainData.values.tolist() 


# from list to DataFrame 
rain_df = pd.DataFrame(rainfall_list)

#%% 
import pandas as pd

datafile = "data/data.txt"
myData = pd.read_table(datafile, header=None, sep = " ")  # Reads the data

myData.index = list(range(1, len(myData) + 1))
myData.columns = ["Sequence"]
myData.plot()
myData.plot.box()

myData.to_csv("data/data.csv")
myData.to_excel("data/data.xlsx")
