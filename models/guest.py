class Guest:
    def __init__(self, name, type, race, room, id = None):
        self.name = name
        self.type = type 
        self.race = race
        self.room= room
        self.id = id
        self.weapons = []

    def equip_weapon(self, weapon):
        self.weapons.append(weapon)