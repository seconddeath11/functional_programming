import pandas as pd

from config.config import *
from models.bus import Bus
from models.person import Person
from models.ticket import Ticket
from models.wallet import Wallet


class Office:
    def __init__(self):
        self.people = []
        self.tickets = []
        self.buses = []
        self._read_people(PEOPLE_PATH)
        self._read_buses(BUSES_PATH)
        self._read_tickets(TICKETS_PATH)

    def _read_people(self, path: str):
        people_df = pd.read_csv(path)
        for _, person in people_df.iterrows():
            self.people.append(Person(id=person.id, name=person["name"], age=person.age, wallet=Wallet(person.money)))

    def _read_tickets(self, path: str):
        tickets_df = pd.read_csv(path)
        for _, row in tickets_df.iterrows():
            ticket = Ticket(id=row.id, person_id=row.person_id, bus_id=row.bus_id, price=row.price, boarded=bool(row.boarded))
            self.tickets.append(ticket)
            person = self.find_person_by_id(ticket.person_id)
            person.tickets.append(ticket)
            if ticket.boarded:
                bus = self.find_bus_by_id(ticket.bus_id)
                bus.add_passenger(person)


    def _read_buses(self, path: str):
        buses_df = pd.read_csv(path)
        for _, bus in buses_df.iterrows():
            self.buses.append(Bus(id=bus.id, starting_point=bus.starting_point,
                                   ending_point=bus.ending_point, capacity=bus.capacity, price=bus.price))

    def sell_ticket(self, person_id, bus_id):
        person = self.find_person_by_id(person_id)
        ticket_id = self._find_max_ticket_id() + 1
        bus = self.find_bus_by_id(bus_id)
        if person.has_money(bus.price) and bus.has_seats():
            person.pay(bus.price)
            ticket = Ticket(id=ticket_id, bus_id=bus_id, person_id=person_id, price=bus.price, boarded=False)
            person.tickets.append(ticket)
            self.tickets.append(ticket)
            bus.add_passenger(person)
            print('success, you now have a ticket')
        elif person.has_money(bus.price):
            print('no seats available')
        else:
            print('you don\'t have enough money, please deposit to your wallet first')

    def board(self, person_id, bus_id):
        bus = self.find_bus_by_id(bus_id)
        person = self.find_person_by_id(person_id)
        bus.board_passenger(person)
        print('success, you are now boarded')

    def deposit(self, person_id, amount):
        person = self.find_person_by_id(person_id)
        person.deposit(amount)
        print('success, you have made a deposit')

    def register_person(self, id, name, age):
        person = Person(id=id, name=name, age=int(age), wallet=Wallet())
        self.people.append(person)

    def find_person_by_id(self, person_id):
        for person in self.people:
            if person.id == person_id:
                return person
        print('you need to be registered first')
        exit(0)

    def _find_max_ticket_id(self):
        return max(self.tickets, key=lambda x: x.id).id

    def find_bus_by_id(self, bus_id):
        for bus in self.buses:
            if bus.id == bus_id:
                return bus

    def find_tickets_by_person(self, person_id):
        return [ticket for ticket in self.tickets if ticket.person_id == person_id]

    def show_buses(self):
        for bus in self.buses:
            print(bus)

    def save_state(self):
        people_df = pd.DataFrame([{'id': p.id, 'name': p.name, 'age': p.age, 'money': p.wallet.amount}
                                  for p in self.people])
        people_df.to_csv(PEOPLE_PATH, index=False)
        tickets_df = pd.DataFrame([{'id': t.id, 'bus_id': t.bus_id, 'person_id': t.person_id, 'price': t.price,
                                    'boarded': t.boarded} for t in self.tickets])
        tickets_df.to_csv(TICKETS_PATH, index=False)

