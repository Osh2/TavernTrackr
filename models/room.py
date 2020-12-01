class Room:
    def __init__(self, name, capacity, id = None ):
        self.name = name
        self.capacity = capacity 
        self.guests = []
        self.id = id 

    def check_in_guest(self, guest):
        self.guests.append(guest)

    def set_num_guests(self, num_guests):
        self.num_guests = num_guests