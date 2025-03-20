# -*- coding: utf-8 -*-
"""Created on 07.10.24"""

__author__ = "Ane Kleiven"
__email__ = "ane.kleiven@nmbu.no"
"""                  """

#%% function for mean value

values = [7.3743, 3.2422, 1.6541, 4.7424]           # list of x values 


def mean(values):                                   # define the mean function 
    """
    This function calculates the mean values of some list 
    """     
    N = len(values)                                 # number of elements
    return sum(values)/N

mean(values)                                        # call the function 


#%% test function for mean values

def test_mean(values):                              # define the test function 
    exact = 4.2532499999999995                      # expected mean value
    computed = mean(values)                         # calculated mean value
    
    tolerance = 1e-9                                # tolerance for floats
    msg = f'computed {computed}, expected {exact}'  # message if test is false 
    assert abs(computed - exact) < tolerance, msg   # check if value is correct 


test_mean(values)                                   # call test function 

print("Test of function for mean values has passed!")    


# %% function for standard deviation

values = [7.3743, 3.2422, 1.6541, 4.7424]           # list of x values 

import math 

def st(values):                                     # define the st function 
    """
    This function calculates the standard deviation of some list 
    """                             
    N = len(values)                                 # number om elements    
    mean_value = mean(values)                       # mean_values
    diff_sq = [(x - mean_value)**2 for x in values]    # squared differences
    variance = sum(diff_sq) / N                     # calculating variance
    return math.sqrt(variance)                      # square root of variance

st(values)                                          # call the function 


#%% test function for standard deviation 

def test_st(values):                                # define the test function 
    exact = 2.107013505533365                       # expected st.dev of values
    computed = st(values)                           # computed st.dev of values

    tolerance = 1e-9                                # tolerance for float numbers
    msg = f'computed {computed}, expected {exact}'  # message if false
    assert abs(computed - exact) < tolerance, msg   # check if diff is OK
    
test_st(values)                                     # call the function 

print("Test of function for Standard deviation has passed!") 

