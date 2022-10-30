from models.ticket import Ticket
from models.wallet import Wallet


class Person:
    def __init__(self, id: int, name: str, age: int, wallet: Wallet):
        self.id = id
        self.name = name
        self.wallet = wallet
        self.age = age
        self.tickets: list[Ticket] = []

    def has_money(self, price):
        return self.wallet.amount >= price

    def has_ticket(self, bus_id: int):
        for ticket in self.tickets:
            if ticket.bus_id == bus_id:
                return True
        return False

    def pay(self, price: int):
        self.wallet.decrease(price)

    def deposit(self, amount: int):
        self.wallet.increase(amount)

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, age: {self.age}, money: {self.wallet.amount}"

    def get_ticket(self, bus_id):
        for ticket in self.tickets:
            if ticket.bus_id == bus_id:
                return ticket
