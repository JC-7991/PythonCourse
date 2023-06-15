class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, depAmt):
        self.balance = self.balance + depAmt