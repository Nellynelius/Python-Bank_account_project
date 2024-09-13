class BalanceException(Exception):
     pass
class BankAccount:
    
    def __init__(self, initialAmount, accountName):
        self.balance = initialAmount
        self.name = accountName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}" )

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount  
        print("\n deposit complete.")
        self.getBalance()  

    def viableTransaction(self, amount): 
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has balance of ${self.balance:.2f}"
            )
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nwithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nwithdraw interupted: {error}")
    def transfer(self, amount, account):
        try:
            print('\n**********\n\nBeginning transfer..🚀🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\ntransfer complete: ✔✔\n\n**********")
        except BalanceException as error:
            print(f"\ntransfer interupted. ❌ {error}")  

class interestRewardAccount(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.getBalance()         
class SavingAccount(interestRewardAccount):
    def __init__(self, initialAmount, accountName):
        super().__init__(initialAmount, accountName)
        self.fee = 5
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee) 
            self.balance = self.balance - (amount +self.fee)
            print("\nwithdraw complete.")
            self.getBalance()
        except BalanceException as error :
            print(f"\nwithdraw interupted: {error} ")    
                   

        
        