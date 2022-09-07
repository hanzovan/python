class Room():
    def __init__(self, capacity):
        self.capacity = capacity
        self.mates = []

    def open_space(self):
        return self.capacity - len(self.mates)
    
    def add_mate(self, name):
        if not self.open_space():
            return False
        else: 
            self.mates.append(name)
            return True


room = Room(2)
clients = ["Danielle", "Bee", "Ashley", "Archer"]

for person in clients:
    success = room.add_mate(person)
    if success:
        print(f"Added {person} to room successfully")
    else:
        print(f"There is not enough space for {person}")

print("These are people in room")
for person in room.mates:
    print(person)