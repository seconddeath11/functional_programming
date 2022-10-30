from models.wallet import decrease, increase
from utils import find_tickets_by_passenger


def has_money(price, wallet) -> bool:
    return wallet >= price


def has_ticket(passenger_id, bus_id: int, tickets) -> bool:
    passenger_tickets = find_tickets_by_passenger(passenger_id, tickets)
    for ticket in passenger_tickets:
        if ticket["bus_id"] == bus_id:
            return True
    return False


def pay(price: int, wallet) -> int:
    return decrease(wallet, price)


def deposit_wallet(amount: int, wallet) -> int:
    return increase(wallet, amount)
