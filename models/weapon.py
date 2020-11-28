class Weapon:
    def __init__(self, name, stats, owner, id=None):
        self.name = name
        self.stats = stats
        self.owner = owner
        self.id = id