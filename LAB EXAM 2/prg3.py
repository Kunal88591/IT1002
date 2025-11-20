class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def add_interest(self, rate):
        self.balance += self.balance * rate

acc = BankAccount()
acc.deposit(2000)
acc.withdraw(400)
acc.add_interest(0.05)
print(acc.balance)
