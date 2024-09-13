from bank_accounts import *

Dan = BankAccount(1000, "Dan")
Ella = BankAccount(2000, "Ella")

Dan.getBalance()
Ella.getBalance()

Ella.deposit(500)

Dan.withdraw(2000)
Dan.withdraw(500)

Dan.transfer(2000, Ella)

Dan.transfer(200, Ella)

Nelly = interestRewardAccount(1000, 'Nelly')


Nelly.getBalance()

Nelly.deposit(100)

Nelly.transfer(100, Dan)

John = SavingAccount(1000, 'John')

John.getBalance()

John.deposit(100)

John.transfer(100, Nelly)
        
