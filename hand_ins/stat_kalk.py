# -*- coding: utf-8 -*-
"""Created on 09.10.24"""

__author__ = "Ane Kleiven"
__email__ = "ane.kleiven@nmbu.no"
"""                  """
#%% function to print the main menu 

def print_menu():
    """ Print the menu of simple statistics program"""
    print("Starting simple statistics program (SSP)") 
    print("                                  ")
    print("SSP menu:")
    print("1 = Read in values")
    print("2 = Empty value list")
    print("3 = Show mean and standard deviation")
    print("4 = List out values")
    print("5 = End program") 
    print("                                  ")


#%% function for choosing numbers between 1 and 5 

def choose_action(): 
    """Write the menu and wait for the user to choose an option""" 
    while True: 
        print_menu()
        try: 
            choice = int(input("Choose a number between 1 and 5: "))
            if 1 <= choice <= 5: 
                print (f"Your choice: {choice}")
                return choice
            else: 
                print("Invalid number. Choose again.")
        except ValueError: 
            print("Invalid input. Please choose a number between 1 and 5")


#%% function for choice 1; reading in values to list 

def read_values(values): 
    """Lets the user read in values until "Enter" is pressed"""
    values = [] 
    while True: 
        user_input = input("New value (Enter = quit): ")
        if user_input == "": 
            break 
        try: 
            value = float(user_input) 
            values.append(value) 
        except ValueError: 
            print("Invalid input. Returning to main menu.")
            break 
    print("Read values ended.")
    return(values) 


#%% function calculating mean and standard deviation from inf120stat
import inf120stat

def print_statistics(values): 
    """Calculates mean and standard deviation of the list "values", by using the 
    the functions in inf120stat"""
    try: 
        print(f"Number of values: {len(values)}")
        print(f"Mean value: {inf120stat.mean(values)}") 
        print(f"Standard deviation: {inf120stat.st(values)}")
        return inf120stat.st(values)
    except ZeroDivisionError: 
        print("List is empty. Read in values first.")



#%% putting the program together 


if __name__ == "__main__": 
    values =   [] 
    
    while True: 
        choice = choose_action()
        
        if choice == 1: 
            values = read_values(values) 
            print(f"Values read in: {values}")    
        
        elif choice == 2: 
            values.clear() 
        
        elif choice == 3: 
            print_statistics(values)
            
        elif choice == 4: 
            print(f"Values: {values}")
        
        elif choice == 5: 
            print("Ending program...")
            break 
        
        