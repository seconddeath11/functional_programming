from models.person import Person


class Bus:
    def __init__(self, id: int, starting_point: str, ending_point: str, capacity: int,
                 price: int):
        self.id = id
        self.people: list[Person] = []
        self.starting_point = starting_point
        self.ending_point = ending_point
        self.capacity = capacity
        self.price = price

    def add_passenger(self, passenger: Person):
        self.people.append(passenger)

    def board_passenger(self, passenger: Person):
        if passenger.has_ticket(self.id) and passenger not in self.people:
            self.people.append(passenger)
            ticket = passenger.get_ticket(self.id)
            ticket.boarded = True
        elif passenger.has_ticket(self.id):
            print('you are already boarded')
            exit(0)
        else:
            print('you need to buy a ticket first')
            exit(0)

    def has_seats(self):
        return len(self.people) < self.capacity

    def __str__(self):
        return f"bus id: {self.id}, starting point: {self.starting_point}, ending pont: {self.ending_point}, " \
               f"capacity: {self.capacity}, price: {self.price}, boarded: {len(self.people)}"

