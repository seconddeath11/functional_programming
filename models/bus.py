import copy

from models.person import has_ticket
from utils import find_tickets_by_bus, find_ticket


def set_boarded(ticket_id, tickets) -> dict:
    new_tickets = copy.deepcopy(tickets)
    for ticket in new_tickets:
        if ticket["id"] == ticket_id:
            ticket["boarded"] = True
    return new_tickets


def board_passenger(passenger_id, bus_id, tickets) -> dict:
    new_tickets = copy.deepcopy(tickets)
    if has_ticket(passenger_id, bus_id, new_tickets):
        ticket = find_ticket(passenger_id, bus_id, new_tickets)
        if ticket["boarded"]:
            print('you are already boarded')
            exit(0)
        else:
            new_tickets = set_boarded(ticket["id"], new_tickets)
        return new_tickets
    else:
        print('you need to buy a ticket first')
        exit(0)


def has_seats(bus_id, capacity, tickets):
    bus_tickets = find_tickets_by_bus(bus_id, tickets)
    return len(bus_tickets) < capacity
