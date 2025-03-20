# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 07:07:05 2024

@author: anekl
"""

from datetime import datetime as dt 

def isots(): 
    #return timestamp with iso format "2024-11-29T08:47:03" 
    return dt.now().isoformat(timespec = "seconds")

class AccountOld: 
    
    def __init__(self, name, konto, initbalance):  
        self.name = name 
        self.accountnumber = konto
        self.balance = initbalance
        
    def deposit(self, amount): 
        self.balance += amount 
    
    
    def withdraw(self, amount) :
        self.balance -= amount 
        
    def getAccountinfo(self): 
        print(f"Owner: {self.name}, Acc.no: {self.accountnumber}, Balance: {self.balance}")

class Account: 
    
    def __init__ (self, name, konto, initbalance, ts = isots()):
        self.name = name 
        self.accountnumber = konto
        self._ledger = [] 
        # timestamp, desc, amount 
        first = (ts, "Opening balance", initbalance)
        self._ledger.append(first)
        
    def deposit(self, amount, desc = "Deposit", ts = isots()):
        self._ledger.append((ts, desc, amount))
    
    def withdraw(self, amount, desc = "Withdraw", ts = isots()):
        self._ledger.append((ts, desc, -amount)) 
        
    def getAccountinfo(self): 
        balance = self.getBalance()
        print(f"Owner: {self.name}, Acc.no: {self.accountnumber}, Balance: {balance}")
        
    def getBalance(self): 
        # sum amounts in the ledger
        return sum([t[2] for t in self._ledger])
    
    def printLedger(self): 
        for t in self._ledger: 
            print(t)
            
    def toFile(self): 
        # go through the list of transactions 
        # generate a string with: account, name, ts, desc, balance 
        # for every transaction 
        lines = [] 
        for tr in self._ledger: 
            lines.append(f"{self.accountnumber}, {self.name}, {tr[0]}, {tr[1]}, {tr[2]}")
        return lines 

def test_account(): 
    "Function to test bank account class"
    
    Account1 = Account("Ane","45670538",3400)
    Account1.deposit(400) 
    Account1.withdraw(100)
    assert Account1.getBalance() == 3700, "Balance mismatch"
    return Account1

    
import time 
import random as rd 

def add_transaction(acc, n = 10) :
    # makes a list with n random time stamps in the interval
    # 5 years back and until today 
    # utn represents the number of seconds since the first of january 1970
    utn = int(time.time()) 
    tsfirst = utn - (5 * 365 * 24 * 60 * 60)
    srange = [rd.randint(tsfirst, utn) for _ in range(n)] 
    tsrange = [dt.fromtimestamp(ut).isoformat(timespec = "seconds") for ut in srange] 
    
    print(tsrange)
    
    # generate normal distributed amounts 
    # mean = 100, st.dev = 1000 
    amount = [rd.gauss(100,1000) for _ in range(n)]
    print(amount)   
    
    
    for ts, am in zip(tsrange, amount): 
        am = round(am, 2) 
        if am > 0: 
            acc.deposit(am, "Deposit", ts) 
        else: 
            acc.withdraw(abs(am), "Withdraw", ts)

    

if __name__ == "__main__": 
    #if this test is run directly, not imported 
    Account1 = test_account()
    add_transaction(Account1)


Account2 = Account("Test", "342045", 1000)
Account2.deposit(1000)
Account2.withdraw(200)
Account2.deposit(30000, desc = "lønn") 
Account2.getAccountinfo()
Account2.printLedger()
Account2.getBalance()




