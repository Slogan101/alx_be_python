



class BankAccount:
    def __init__(self):
        self.account_balance = 0


    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance
    

    def withdraw(self, amount):
        if amount < self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    
    def display_balance(self):
        amount = self.account_balance
        print(f"Current Balance: ${amount}")
  




