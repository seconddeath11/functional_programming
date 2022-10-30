def find_tickets_by_passenger(passenger_id, tickets) -> list:
    passenger_tickets = []
    for ticket in tickets:
        if ticket["person_id"] == passenger_id:
            passenger_tickets.append(ticket)
    return passenger_tickets


def find_max_ticket_id(tickets):
    return max(tickets, key=lambda x: x["id"])["id"]


def find_bus_by_id(bus_id, buses):
    for bus in buses:
        if bus["id"] == bus_id:
            return bus


def find_tickets_by_person(person_id, tickets):
    return [ticket for ticket in tickets if ticket["person_id"] == person_id]


def find_tickets_by_bus(bus_id, tickets):
    return [ticket for ticket in tickets if ticket["bus_id"] == bus_id]


def find_person_by_id(person_id, people):
    for person in people:
        if person["id"] == person_id:
            return person


def find_ticket(passenger_id, bus_id, tickets) -> dict:
    passenger_tickets = find_tickets_by_passenger(passenger_id, tickets)
    for ticket in passenger_tickets:
        if ticket["bus_id"] == bus_id:
            return ticket
