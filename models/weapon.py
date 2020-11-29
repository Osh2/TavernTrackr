class Weapon:
    def __init__(self, name, damage, type, magic, value, owner, id=None):
        self.name = name
        self.damage = damage
        self.type = type
        self.magic = magic
        self.value = value
        self.owner = owner
        self.id = id