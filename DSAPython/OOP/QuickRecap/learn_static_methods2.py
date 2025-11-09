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
        if self._is_valid_amount(amount):
            self._balance += amount
            self.__log_transaction("deposit", amount)
        else:
            print("Deposit amount must be positive")

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5 # returns true
    
    # Protected method
    def _is_valid_amount(self, amount):
        return amount > 0
    
    # Private method
    def __log_transaction(self, transaction_type, amount):
        print(f"Logging {transaction_type} of ${amount}. \n New Balance {self._balance}")
    
account = BankAccount("Alice", 500)
account.deposit(200)

print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(10))