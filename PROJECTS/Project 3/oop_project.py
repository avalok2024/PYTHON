from bank_account import * 

David = BankAccount(1000, "David")
Steve = BankAccount(2000, "Steve")

David.getBalalnce()
Steve.getBalalnce()

David.deposite(500)
Steve.deposite(600)

David.withdraw(10000)
Steve.withdraw(10)

David.transfer(20, Steve)
David.getBalalnce()
Steve.getBalalnce()

Jim = InterestRewardsAcct(1000, 'Jim')
Jim.getBalalnce()
Jim.deposite(100)
Jim.transfer(100, David)

Blaze = SavingsAccount(1000, "Blaze")
Blaze.getBalalnce()
Blaze.deposite(10)
Blaze.transfer(1100, David)

