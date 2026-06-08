# Bank Account System
class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
            return
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return
        if amount > self.balance:
            print("Insufficient balance")
            return
        self.balance -= amount
        print("Withdrawn:", amount)

    def check_balance(self):
        return self.balance

    def display_account(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Current Balance:", self.balance)


account = BankAccount("Suman Behera", "SB1001", 5000)
account.display_account()
account.deposit(2000)
account.withdraw(1500)
print("Final Balance:", account.check_balance())