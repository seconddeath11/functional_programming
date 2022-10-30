import sys

from config.config import *
from models.office import read_people, read_buses, read_tickets, register_person, board, deposit, \
    sell_ticket, save_state
from utils import find_person_by_id, find_tickets_by_person


def main(action: str):
    people = read_people(PEOPLE_PATH)
    buses = read_buses(BUSES_PATH)
    tickets = read_tickets(TICKETS_PATH)
    person_id = int(input("Enter your id: "))
    if action == "register" or find_person_by_id(person_id, people) is None:
        name = input('Enter your full name: ')
        age = input('Enter your age: ')
        people = register_person(person_id, name, int(age), people=people)
    if action == "board":
        bus_id = input('Enter bus id for boarding: ')
        tickets = board(person_id=person_id, bus_id=int(bus_id), tickets=tickets)
    if action == "deposit":
        money = input('Enter your desired deposit amount: ')
        people = deposit(person_id=person_id, amount=int(money), people=people)
    if action == "buy":
        bus_id = input('Enter desired bus id: ')
        people, tickets = sell_ticket(person_id=person_id, bus_id=int(bus_id), people=people, buses=buses, tickets=tickets)
    if action == "buses":
        for bus in buses:
            print(bus)
    if action == "person":
        print(find_person_by_id(person_id, people=people))
    if action == "tickets":
        person_tickets = find_tickets_by_person(person_id, tickets=tickets)
        for ticket in person_tickets:
            print(ticket)

    save_state(PEOPLE_PATH, TICKETS_PATH, people, tickets)


if __name__ == "__main__":
    action = sys.argv[1]
    if action not in ACTIONS:
        print('action is not supported')
        exit(0)
    main(action)
