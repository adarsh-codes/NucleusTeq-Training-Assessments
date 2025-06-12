class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited Rs.{amount}. New balance: Rs.{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew Rs.{amount}. New balance: Rs.{self.balance}")

    def display(self):
        print(f"Owner: {self.owner}, Balance: Rs.{self.balance}")

my_account = BankAccount("Adarsh",10000)

my_account.display()
my_account.deposit(2000)
my_account.display()