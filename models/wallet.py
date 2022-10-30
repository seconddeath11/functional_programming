class Wallet:
    def __init__(self, amount: int = 0):
        self.amount = amount

    def decrease(self, amount):
        self.amount -= amount

    def increase(self, amount):
        self.amount += amount

