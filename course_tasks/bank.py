# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 12:41:49 2024

@author: anekl
"""
import bankaccount as ba 


class Bank: 
    
    def __init__(self):
        self._accounts = {} 
        
    def main_loop(self): 
        # a loop that will call main menu 
        # repeat until user selects 3 for exit
        choice = 0 
        while choice != 3: 
            choice = self.main_menu() 
            if choice == 1: 
                self.open_account()
            elif choice == 2: 
                self.account_menu()

    def main_menu(self): 
        # print main menu to screen
        # get menu choice from user 
        # return (int) menu choice 
        menu = """
Bank menu: 
1. Open account
2. Deposit or withdraw
3. Quit
        """
        print(menu)
        while True: 
            try: 
                # int() vil feile hvis valg ikke kan konverteres til et tall
                choice = int(input("Your choice -->"))
                if (choice > 3) or (choice < 1): 
                     raise Exception("Invalid choice. Try again.")
                # choice is OK, break quits the loop 
                break 
            except: 
                print("Insert a number between 1 and 3. Try again")
        return choice 
    
    
    def open_account(self): 
        # ask for name, account, amount
        # create new account object with given info 
        print("Open account")
        name = input("Name of account owner: ")
        # in reality, banks will automatically assign unique account numbers
        account = input("Return account number: ")
        balance = float(input("Return initial balance: "))
        acc = ba.Account(name, account, balance)
        self._accounts[account] = acc
    
    def account_menu(self): 
        # print list of accounts and let user select account to modify 
        # select to deposit, withdraw or list transactions 
        
        # add some test accounts 
        #a1 = ba.Account("Iselin", "4557", 450)
        #a2 = ba.Account("Bjørn", "3445", 200000)
        #self._accounts["4557"] = a1
        #self._accounts["3445"] = a2
        
        print("Accounts: ") 
        for acc in self._accounts.values():
            print(f"{acc.accountnumber} {acc.name}")
        
        account = input("Choose account: ")
        # get selected account object to modify 
        acc = self._accounts[account]
        
        choice = 0 
        while choice != 4: 
            menu = '''
1. Deposit 
2. Withdraw
3. Show transactions
4. Back to main menu 
''' 
            print(menu) 
            choice = int(input("Your choice: "))
            if choice == 1: 
                amount = float(input("Write amount for deposit: "))
                acc.deposit(amount)
            elif choice == 2: 
                amount = float(input("Write amount for withdrawal: "))
                acc.withdraw(amount) 
            elif choice == 3: 
                acc.printLedger() 
        # exit while loop 
    # exit account_menu 
    
    def write_accounts(self, filename):
        # go through every account object in _accounts
        # print for every transaction: 
        # account, name, ts, desc, amount 
        with open(filename, "w") as file: 
            for acc in self._accounts.values(): 
                trList = acc.toFile() 
                for tr in trList: 
                    file.write(tr + "\n")
                    
    def read_accounts(self, filename): 
        with open(filename, "r") as file: 
            for line in file: 
                account, name, ts, desc, amount = line.split(", ") 
                amount = float(amount) 
                try: 
                    # deposit or withdrawal 
                    if amount < 0: 
                        self._accounts[account].withdraw(-amount,desc,ts) 
                    else: 
                        self._accounts[account].deposit(amount, desc, ts) 
                except: 
                    # account with accountnumber does noe exist 
                    # make new account, add transaction 
                    # add account to accounts 
                    acc = ba.Account(name, account, amount)
                    self._accounts[account] = acc 
                    

Nordea = Bank() 
Nordea.read_accounts("bankdata.csv")
Nordea.main_loop()
Nordea.write_accounts("bankdata.csv")





