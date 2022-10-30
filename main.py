import sys

from config.config import ACTIONS
from models.office import Office


def main(action: str):
    office = Office()
    person_id = int(input("Enter your id: "))
    if action == "register" or person_id not in [person.id for person in office.people]:
        name = input('Enter your full name: ')
        age = input('Enter your age: ')
        office.register_person(person_id, name, int(age))
    if action == "board":
        bus_id = input('Enter bus id for boarding: ')
        office.board(person_id=person_id, bus_id=int(bus_id))
    if action == "deposit":
        money = input('Enter your desired deposit amount: ')
        office.deposit(person_id=person_id, amount=int(money))
    if action == "buy":
        bus_id = input('Enter desired bus id: ')
        office.sell_ticket(person_id=person_id, bus_id=int(bus_id))
    if action == "buses":
        for bus in office.buses:
            print(bus)
    if action == "person":
        print(office.find_person_by_id(person_id))
    if action == "tickets":
        tickets = office.find_tickets_by_person(person_id)
        for ticket in tickets:
            print(ticket)

    office.save_state()


if __name__ == "__main__":
    action = sys.argv[1]
    if action not in ACTIONS:
        print('action is not supported')
        exit(0)
    main(action)
