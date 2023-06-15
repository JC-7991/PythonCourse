class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, depAmt):
        self.balance = self.balance + depAmt
        print(f"Added ${depAmt} to the balance.")

    def withdrawal(self, withAmt):
        if self.balance >= withAmt:
            self.balance = self.balance - withAmt
            print(f"Withdrew ${withAmt} from the balance.")
        else:
            print("Insufficient funds.")

    def __str__(self):
        return f"Owner: {self.owner}\nBalance: {self.balance}"