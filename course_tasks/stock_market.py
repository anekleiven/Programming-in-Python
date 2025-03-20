# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 17:00:14 2024

@author: anekl
"""

#%% 

# compare stock prices (aksjer) 
  
""" example data (google)
Date,Open,High,Low,Close,Volume,Adj Close
2008-06-02,582.50,588.04,535.10,551.00,4613000,551.00
2008-05-01,578.31,602.45,537.81,585.80,5136000,585.80
2008-04-01,447.74,584.86,441.00,574.29,6859900,574.29
2008-03-03,471.51,472.72,412.11,440.47,7501800,440.47
2008-02-01,528.67,541.04,446.85,471.18,9329400,471.18
"""

def stockread(filename) :
    with open(filename, "r") as fh: 
        data = fh.readlines() 
    # python closes the file automatic when we exit the with content 
    print(data)
    #list with the dates
    dates = []
    prices = [] 
        
    for line in data[1:]: 
        fields = line.split(",") 
        # print(fields)
        date = fields[0]
        # remove day from date 
        # 2008-06-02 
        date = date[:-3]
        price = float(fields[-1])
        print(date, price)
        dates.append(date)
        prices.append(price)
        
    # reverse for chronologic order 
    dates.reverse()
    prices.reverse() 
    return dates, prices 
        
#d,p = stockread("stockprices_Google.csv") 

#print(d[0:5], p[0:5])

dates = {} 
prices = {} 

# for each of the 3 companies 

# for sun stock prices 
sd, sp = stockread("data/stockprices_Sun.csv")
dates["Sun"] = sd
prices["Sun"] = sp 

#for google stock prices 
sd, sp = stockread("data/stockprices_Google.csv")
dates["Google"] = sd
prices["Google"] = sp 

# for microsoft stock prices 
sd, sp = stockread("data/stockprices_Microsoft.csv")
dates["Microsoft"] = sd
prices["Microsoft"] = sp 

# some checks 
print("Microsoft 5 first dates:", dates["Microsoft"][0:5])
print("Microsoft 5 first prices:", prices["Microsoft"][0:5])

# put dates and prices into one dictionary 
data = {"prices": prices, "dates": dates}


# normalize prices from Sun and Microsoft 
data["normp"] = {}
sun_first = data["prices"]["Sun"][0]
data["normp"]["Sun"] = [p/sun_first for p in data["prices"]["Sun"]]
# verify by printing the 5 first normalized values 
print(data["normp"]["Sun"][0:5])

microsoft_first = data["prices"]["Microsoft"][0]
data["normp"]["Microsoft"] = [p/microsoft_first for p in data["prices"]["Microsoft"]]
print(data["normp"]["Microsoft"][0:5])


# normalize the prices from google 

# find the index number for january 2005 in dates 
jan05index = data["dates"]["Sun"].index("2005-01")
print("jan05index:", jan05index)

pj05_sun = data["prices"]["Sun"][204]
print("pj05_sun:", pj05_sun)

pj05_microsoft = data["prices"]["Microsoft"][204]
print("pj05_microsoft:", pj05_microsoft)

google_norm_factor = data["prices"]["Google"][0] / max(pj05_microsoft,pj05_sun)
print(google_norm_factor)

# normalize google prices 
data["normp"]["Google"] = [p/google_norm_factor for p in data["prices"]["Google"]]
print("First google price:", data["normp"]["Google"][0:5])

# x axis values for the 3 companies 
x = {} 
x['Sun'] = range(len(data['normp']['Sun']))
x['Microsoft'] = range(len(data['normp']['Microsoft']))
x['Google'] = range(jan05index, jan05index+len(data['normp']['Google']))

# %%
# Plot of normalized prices

import matplotlib.pyplot as plt

plt.plot(x['Sun'], data['normp']['Sun'], 'r-')
plt.plot(x['Microsoft'], data['normp']['Microsoft'], 'b-')
plt.plot(x['Google'], data['normp']['Google'], 'y-')
plt.legend(['Sun', 'Microsoft', 'Google'])
# %%
# Plot of not normalized prices
plt.plot(x['Sun'], data['prices']['Sun'], 'r-')
plt.plot(x['Microsoft'], data['prices']['Microsoft'], 'b-')
plt.plot(x['Google'], data['prices']['Google'], 'y-')
plt.legend(['Sun', 'Microsoft', 'Google'])













