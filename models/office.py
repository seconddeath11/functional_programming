import copy

import pandas as pd

from models.bus import board_passenger, has_seats
from models.person import has_money, deposit_wallet, pay
from utils import find_person_by_id, find_bus_by_id, find_max_ticket_id


def read_people(path: str):
    people_df = pd.read_csv(path)
    people = people_df.to_dict('records')
    return people


def read_tickets(path: str):
    tickets_df = pd.read_csv(path)
    tickets = tickets_df.to_dict('records')
    return tickets


def read_buses(path: str):
    buses_df = pd.read_csv(path)
    buses = buses_df.to_dict('records')
    return buses


def sell_ticket(person_id, bus_id, people, buses, tickets):
    new_people = copy.deepcopy(people)
    person = find_person_by_id(person_id, new_people)
    ticket_id = find_max_ticket_id(tickets) + 1
    bus = find_bus_by_id(bus_id, buses)
    if has_money(int(bus["price"]), int(person["money"])) and has_seats(bus_id, int(bus["capacity"]), tickets):
        person["money"] = pay(int(bus["price"]), int(person["money"]))
        ticket = {"id": ticket_id, "bus_id": bus_id, "person_id": person_id, "price": int(bus["price"]),
                  "boarded": False}
        new_tickets = copy.deepcopy(tickets)
        new_tickets.append(ticket)
        print('success, you now have a ticket')
        return new_people, new_tickets
    elif has_money(person, int(bus["price"])):
        print('no seats available')
    else:
        print('you don\'t have enough money, please deposit to your wallet first')


def board(person_id, bus_id, tickets):
    new_tickets = copy.deepcopy(tickets)
    new_tickets = board_passenger(person_id, bus_id, new_tickets)
    print('success, you are now boarded')
    return new_tickets


def deposit(person_id, amount, people):
    new_people = copy.deepcopy(people)
    person = find_person_by_id(person_id, new_people)
    person["money"] = deposit_wallet(amount, person["money"])
    print('success, you have made a deposit')
    return new_people


def register_person(id, name, age, people):
    person = create_person(id, name, age)
    new_people = copy.deepcopy(people)
    new_people.append(person)
    return new_people


def show_buses(buses):
    for bus in buses:
        print(bus)


def save_state(people_path, tickets_path, people, tickets):
    people_df = pd.DataFrame(people)
    people_df.to_csv(people_path, index=False)
    tickets_df = pd.DataFrame(tickets)
    tickets_df.to_csv(tickets_path, index=False)


def create_person(id, name, age):
    return {"id": id, "name": name, "age": int(age), "money": 0}
