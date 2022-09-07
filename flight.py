class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def open_seats(self):
        return self.capacity - len(self.passengers)

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

flight = Flight(3)
people = ["Harry", "Ron", "Hermione", "Ginny", "Draco"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully")
    else:
        print(f"There is not enough seat for {person}")

print("Passengers in this flight are: ")
for person in flight.passengers:
    print(person)