from typing import Any


class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, InitalAmount, AccountName):
        self.InitalAmount = InitalAmount 
        self.AccountName = AccountName
        print(f"""\nAccount '{self.AccountName}' created.\nBalance = ${self.InitalAmount : .2f}""")


    def getBalalnce(self):
        print(f"\nAccount '{self.AccountName}'\nbalance = ${self.InitalAmount: .2f}")

    def deposite(self, amount):
        self.InitalAmount += amount
        print(f"\nDeposite complete.")
        self.getBalalnce()

    def viableTrabsaction(self, amount):
        if self.InitalAmount >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.AccountName}' only has a balance of ${self.InitalAmount : .2f}")
        
    def withdraw(self, amount):
        try:
            self.viableTrabsaction(amount)
            self.InitalAmount -= amount
            print("\nWithdraw complete.")
        except BalanceException as error:
            print(f"\n Withdraw interrupted : {error}")


    def transfer(self, amount, account):
        try:
            print('\n **********\n \n Beginning Transefer...')
            self.viableTrabsaction(amount)
            self.withdraw(amount)
            account.deposite(amount)
            print("\n Trasnser Complete! \n \n ********")
        except BalanceException as error:
            print(f'\n Transefer interrupted.')


class InterestRewardsAcct(BankAccount):
    def deposite(self, amount):
        self.InitalAmount += amount*1.05
        print("\nDeposite Complete.")
        self.getBalalnce()

class SavingsAccount(InterestRewardsAcct):
    def __init__(self, InitalAmount, AccountName):
        super().__init__(InitalAmount, AccountName)
        self.fee = 5

    
    def withdraw(self, amount):
        try:
            self.viableTrabsaction(amount + self.fee)
            self.InitalAmount -= amount + self.fee
            print(f'\nWithdraw Complete.')
            self.getBalalnce()
        except BalanceException as error:
            print(f'\nWitdraw interrupted: {error}')

    
