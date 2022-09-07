class car():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def open_seats(self):
        return self.capacity - len(self.passengers)

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        else:
            self.passengers.append(name)
            return True

Saigon_Dalat = car(7)
family = ["Archer", "Danielle", "Ashley", "Nana", "Papa", "Bee", "Tuan", "Hon", "Thanh", "Bo", "Phuc An"]

for person in family:
    success = Saigon_Dalat.add_passenger(person)
    if not success:
        print(f"There is not enough seat for {person}")
    else:
        print(f"Added {person} to our car successfully!")

print("These are people already in car: ")
for person in Saigon_Dalat.passengers:
    print(person)