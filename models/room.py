class Room:
    def __init__(self, name, capacity, id = None ):
        self.name = name
        self.capacity = capacity 
        self.guests = []
        self.id = id 