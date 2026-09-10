"""
Create a 'BankAccount' class with:
- Constructor that takes account_holder and balance
- deposit(amount) method
- withdraw(amount) method (check sufficient funds)
- get_balance() method
- __str__ method for nice display
 
Test it with creating an account and performing operations.

"""


class BankAccount:

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited: ${amount:.2f}')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds.')
        else:
            self.balance -= amount
            print(f'Withdrawn: ${amount:.2f}')

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f'Account holder: {self.account_holder}, Balance: ${self.balance:.2f}'


account = BankAccount('Alice', 1000)
print(account)
account.deposit(250)
account.withdraw(400)
print(f'Current balance: ${account.get_balance():.2f}')
account.withdraw(1000)
