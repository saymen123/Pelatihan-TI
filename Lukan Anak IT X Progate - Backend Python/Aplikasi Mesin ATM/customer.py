from atm_card import ATMCard

class Customer:
    def __init__(self, custPin=1234, custBalance=10000):
        self.id = id
        self.pin = custPin
        self.balance = custBalance
    
    def withdrawBalance(self, nominal):
        self.balance -= nominal
    def depositBalance(self, nominal):
        self.balance += nominal