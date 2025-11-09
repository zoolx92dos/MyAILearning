# Static Methods

# A static method belongs to the class itself rather than any
# instance of the class

# To define a static method, we can use the @staticmethod decorator

class BankAccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{self.owner}'s new balance: {self._balance}")
        else:
            print("Deposit amount must be positive")

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5 # returns true
    
account = BankAccount("Alice", 500)
account.deposit(200)

print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(10))