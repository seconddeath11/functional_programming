class Ticket:
    def __init__(self, id: int, bus_id: int, person_id: int, price: int, boarded: bool):
        self.person_id = person_id
        self.id = id
        self.bus_id = bus_id
        self.price = price
        self.boarded = boarded

    def __str__(self):
        return f"id: {self.id}, bus: {self.bus_id}, boarded: {self.boarded}"
