 class FinanceTracker:
    def __init__(self):
        self.balance = 0
    
    def add_income(self, amount):
        self.balance += amount
    
    def add_expense(self, amount):
        self.balance -= amount
    
    def get_balance(self):
        return self.balance
